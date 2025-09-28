import os
from datetime import datetime, timezone
from typing import Dict, Any

from sqlalchemy.orm import Session

from app.models.subscription import SubscriptionStatus
from app.repos import user_repo, subscription_repo, transaction_repo, webhook_repo
from src.payments.sqlalchemy_service import SQLAlchemyPaymentService


class BillingService:
    def __init__(self, db: Session):
        self.db = db
        # Map variant IDs to plan names (from environment variables)
        self.variant_to_plan = {
            os.getenv("LEMON_SQUEEZY_VARIANT_ID_PRO", "1013286"): "pro",
            os.getenv("LEMON_SQUEEZY_VARIANT_ID_ENTERPRISE", "1013276"): "enterprise", 
            os.getenv("LEMON_SQUEEZY_VARIANT_ID_YEARLY", "1013282"): "pro-yearly"
        }
        # Initialize SQLAlchemy service for UserSubscription updates
        self.sqlalchemy_service = SQLAlchemyPaymentService()

    def handle_webhook(self, event_id: str, event: Dict[str, Any]) -> None:
        print(f"🎯 BillingService: Processing webhook event_id={event_id}")
        print(f"🎯 BillingService: Event data: {event}")
        
        # Check if event was already processed, but don't skip if subscription doesn't exist
        try:
            webhook_repo.record_event(self.db, event_id)
            print(f"🎯 BillingService: Event {event_id} is new, processing...")
        except Exception as e:
            print(f"🎯 BillingService: Event {event_id} already exists in database")
            # Check if user actually has a subscription - if not, process anyway
            meta = event.get("meta", {})
            custom_data = meta.get("custom_data", {})
            user_id = custom_data.get("user_id")
            
            if user_id:
                existing_sub = subscription_repo.get_by_user(self.db, user_id)
                if existing_sub and existing_sub.plan != "free":
                    print(f"🎯 BillingService: User {user_id} already has subscription {existing_sub.plan}, skipping")
                    return
                else:
                    print(f"🎯 BillingService: User {user_id} has no subscription or is on free plan, processing anyway...")
            else:
                print(f"🎯 BillingService: No user_id found, skipping")
                return

        meta = event.get("meta", {})
        etype = meta.get("event_name", "")
        data = event.get("data", {})
        attrs = data.get("attributes", {})
        
        print(f"🎯 BillingService: Event type: {etype}")
        print(f"🎯 BillingService: Attributes: {attrs}")

        # identify user from custom metadata or email
        user_id = None
        checkout_data = attrs.get("checkout_data", {})
        custom = checkout_data.get("custom", {})
        user_id = custom.get("user_id")
        if not user_id:
            email = attrs.get("user_email") or attrs.get("email")
            if email and "@" in email:
                user_id = email.split("@")[0]

        if not user_id:
            return

        # ensure user exists
        email = attrs.get("user_email") or attrs.get("email")
        user_repo.get_or_create_user(self.db, user_id, email=email)

        print(f"🎯 BillingService: Checking event type '{etype}' against subscription events")
        
        # Check if this is a subscription-related event or if it contains subscription data
        is_subscription_event = etype in {
            "subscription_created", "subscription_updated", "subscription_resumed", 
            "subscription_unpaused", "subscription_plan_changed", "order_created", 
            "order_updated", "subscription_payment_success", "subscription_payment_recovered"
        }
        
        # Also check if the event contains subscription data even if event type doesn't match
        has_subscription_data = (
            attrs.get("variant_id") is not None or 
            attrs.get("checkout_data", {}).get("custom", {}).get("user_id") is not None
        )
        
        print(f"🎯 BillingService: is_subscription_event={is_subscription_event}, has_subscription_data={has_subscription_data}")
        
        if is_subscription_event or has_subscription_data:
            # Get plan from custom data first, then map variant_id to plan name
            plan = custom.get("plan_id")
            if not plan:
                variant_id = attrs.get("variant_id")
                if variant_id:
                    # Map variant_id to plan name
                    plan = self._map_variant_id_to_plan(variant_id)
                    print(f"🔧 Mapped variant_id {variant_id} to plan: {plan}")
                else:
                    print(f"⚠️  No variant_id found in webhook data")
            else:
                print(f"✅ Using plan from custom data: {plan}")
            
            if not plan:
                plan = "free"  # Default to free plan if no plan found
                print(f"⚠️  Defaulting to free plan")
            
            status_map = {
                "active": SubscriptionStatus.active,
                "on_trial": SubscriptionStatus.trialing,
                "past_due": SubscriptionStatus.past_due,
                "cancelled": SubscriptionStatus.canceled,
                "expired": SubscriptionStatus.expired,
            }
            ls_status = attrs.get("status", "active")
            status = status_map.get(ls_status, SubscriptionStatus.active)
            period_end = attrs.get("renews_at") or attrs.get("ends_at")
            if isinstance(period_end, str):
                try:
                    period_end = datetime.fromisoformat(period_end.replace("Z", "+00:00"))
                except Exception:
                    period_end = None
            
            # Get customer ID from webhook data
            customer_id = attrs.get("customer_id") or attrs.get("user_email")
            
            # Update both subscription tables for consistency
            self._update_subscription_tables(
                user_id=user_id,
                plan=plan,
                status=status,
                current_period_end=period_end,
                customer_id=customer_id,
            )
            
            print(f"✅ Updated subscription for user {user_id}: plan={plan}, status={status}")
            
            # Commit the transaction to ensure subscription update is persisted
            self.db.commit()
            print(f"✅ Committed subscription update to database")
        elif etype in {"subscription_cancelled", "subscription_expired"}:
            sub = subscription_repo.get_by_user(self.db, user_id)
            if sub:
                subscription_repo.set_status(self.db, sub.id, SubscriptionStatus.canceled)
        elif etype in {"subscription_paused"}:
            sub = subscription_repo.get_by_user(self.db, user_id)
            if sub:
                subscription_repo.set_status(self.db, sub.id, SubscriptionStatus.paused)
        elif etype in {"subscription_payment_failed"}:
            # Handle failed payment - could pause subscription or send notification
            print(f"🎯 BillingService: Subscription payment failed for user {user_id}")
        elif etype in {"subscription_payment_success", "subscription_payment_recovered"}:
            # Handle successful payment - ensure subscription is active
            # For payment success events, we need to get the plan from the subscription data
            # Check if this event contains subscription information
            if has_subscription_data:
                # Get plan from variant_id if available
                variant_id = attrs.get("variant_id")
                if variant_id:
                    plan = self._map_variant_id_to_plan(variant_id)
                    print(f"🔧 Payment success: Mapped variant_id {variant_id} to plan: {plan}")
                else:
                    # Try to get plan from existing subscription
                    sub = subscription_repo.get_by_user(self.db, user_id)
                    if sub and sub.plan != "free":
                        plan = sub.plan
                        print(f"🔧 Payment success: Using existing plan {plan}")
                    else:
                        plan = "free"
                        print(f"⚠️  Payment success: No variant_id or existing plan, defaulting to free")
                
                # Update subscription with correct plan
                self._update_subscription_tables(
                    user_id=user_id,
                    plan=plan,
                    status=SubscriptionStatus.active,
                    current_period_end=attrs.get("renews_at") or attrs.get("ends_at"),
                    customer_id=attrs.get("customer_id") or attrs.get("user_email"),
                )
                print(f"✅ Updated subscription for user {user_id}: plan={plan}, status=active")
                self.db.commit()
            else:
                # Fallback: just ensure existing subscription is active
                sub = subscription_repo.get_by_user(self.db, user_id)
                if sub:
                    subscription_repo.set_status(self.db, sub.id, SubscriptionStatus.active)
        elif etype in {"subscription_payment_refunded"}:
            # Handle refunded payment - could downgrade subscription
            print(f"🎯 BillingService: Subscription payment refunded for user {user_id}")
        elif etype in {"payment_success", "payment_refunded"}:
            print(f"🎯 BillingService handling {etype} event for user {user_id}")
            amount_cents = attrs.get("total") or attrs.get("amount") or 0
            amount = (amount_cents or 0) / 100
            currency = (attrs.get("currency") or "USD").upper()
            provider_ref = data.get("id") or attrs.get("order_id") or meta.get("event_id")
            
            if provider_ref and amount:
                transaction_repo.record_payment(
                    self.db,
                    user_id=user_id,
                    provider_ref=str(provider_ref),
                    amount=amount,
                    currency=currency,
                )
        else:
            print(f"🎯 BillingService: Unhandled event type '{etype}' for user {user_id}")
            print(f"🎯 BillingService: Event data: {event}")
    
    def _map_variant_id_to_plan(self, variant_id: str) -> str:
        """Map Lemon Squeezy variant_id to internal plan name"""
        # Convert variant_id to string to ensure consistent comparison
        variant_id_str = str(variant_id)
        print(f"🔧 Mapping variant_id: {variant_id_str} (type: {type(variant_id)})")
        print(f"🔧 Available mappings: {self.variant_to_plan}")
        
        plan = self.variant_to_plan.get(variant_id_str, "free")
        print(f"🔧 Mapped to plan: {plan}")
        return plan
    
    def _update_subscription_tables(self, user_id: str, plan: str, status, current_period_end, customer_id: str = None):
        """Update both Subscription and UserSubscription tables for consistency"""
        try:
            # Update the main Subscription table (used by billing service)
            subscription_repo.upsert_subscription(
                self.db,
                user_id=user_id,
                plan=plan,
                status=status,
                current_period_end=current_period_end,
                customer_id=customer_id,
            )
            print(f"✅ Updated Subscription table for user {user_id}: plan={plan}")
            
            # Update the UserSubscription table (used by payment endpoints)
            # Map plan names to plan IDs
            plan_id_mapping = {
                "free": "free",
                "pro": "pro", 
                "enterprise": "enterprise",
                "pro-yearly": "pro-yearly"
            }
            plan_id = plan_id_mapping.get(plan, "free")
            
            # Update or create UserSubscription
            existing_sub = self.sqlalchemy_service.get_user_subscription(user_id, self.db)
            if existing_sub:
                # Update existing subscription
                existing_sub.plan_id = plan_id
                # Map status to UserSubscription status values
                status_mapping = {
                    "active": "active",
                    "past_due": "inactive", 
                    "canceled": "cancelled",
                    "expired": "expired",
                    "trialing": "trial",
                    "inactive": "inactive",
                    "paused": "paused"
                }
                mapped_status = status_mapping.get(
                    status.value if hasattr(status, 'value') else str(status), 
                    "active"
                )
                existing_sub.status = mapped_status
                if current_period_end:
                    existing_sub.current_period_end = current_period_end
                if customer_id:
                    existing_sub.lemon_squeezy_customer_id = customer_id
                self.db.flush()
                print(f"✅ Updated UserSubscription table for user {user_id}: plan_id={plan_id}, status={mapped_status}")
            else:
                # Create new subscription
                from datetime import datetime, timezone, timedelta
                now = datetime.now(timezone.utc)
                period_end = current_period_end or (now + timedelta(days=30))
                
                self.sqlalchemy_service.create_user_subscription(
                    self.db,
                    user_id=user_id,
                    plan_id=plan_id,
                    lemon_squeezy_subscription_id=None
                )
                print(f"✅ Created new UserSubscription for user {user_id}: plan_id={plan_id}")
                
        except Exception as e:
            print(f"❌ Error updating subscription tables for user {user_id}: {str(e)}")
            raise
