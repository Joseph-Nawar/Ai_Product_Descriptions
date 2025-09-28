import os
from datetime import datetime, timezone
from typing import Dict, Any

from sqlalchemy.orm import Session

from app.models.subscription import SubscriptionStatus
from app.repos import user_repo, subscription_repo, transaction_repo, webhook_repo


class BillingService:
    def __init__(self, db: Session):
        self.db = db
        # Map variant IDs to plan names (from environment variables)
        self.variant_to_plan = {
            os.getenv("LEMON_SQUEEZY_VARIANT_ID_PRO", "1013286"): "pro",
            os.getenv("LEMON_SQUEEZY_VARIANT_ID_ENTERPRISE", "1013276"): "enterprise", 
            os.getenv("LEMON_SQUEEZY_VARIANT_ID_YEARLY", "1013282"): "pro-yearly"
        }

    def handle_webhook(self, event_id: str, event: Dict[str, Any]) -> None:
        # idempotency
        if not webhook_repo.record_event(self.db, event_id):
            return

        meta = event.get("meta", {})
        etype = meta.get("event_name", "")
        data = event.get("data", {})
        attrs = data.get("attributes", {})

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

        if etype in {"subscription_created", "subscription_updated", "subscription_resumed", "subscription_unpaused", "subscription_plan_changed"}:
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
            
            subscription_repo.upsert_subscription(
                self.db,
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
    
    def _map_variant_id_to_plan(self, variant_id: str) -> str:
        """Map Lemon Squeezy variant_id to internal plan name"""
        # Convert variant_id to string to ensure consistent comparison
        variant_id_str = str(variant_id)
        print(f"🔧 Mapping variant_id: {variant_id_str} (type: {type(variant_id)})")
        print(f"🔧 Available mappings: {self.variant_to_plan}")
        
        plan = self.variant_to_plan.get(variant_id_str, "free")
        print(f"🔧 Mapped to plan: {plan}")
        return plan
