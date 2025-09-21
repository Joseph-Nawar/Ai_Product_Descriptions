from datetime import datetime, timezone
from typing import Dict, Any

from sqlalchemy.orm import Session

from app.models.subscription import SubscriptionStatus
from app.repos import user_repo, subscription_repo, transaction_repo, webhook_repo


class BillingService:
    def __init__(self, db: Session):
        self.db = db

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

        if etype in {"subscription_created", "subscription_updated"}:
            plan = str(custom.get("plan_id") or attrs.get("variant_id") or "")
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
        elif etype in {"subscription_cancelled", "subscription_expired"}:
            sub = subscription_repo.get_by_user(self.db, user_id)
            if sub:
                subscription_repo.set_status(self.db, sub.id, SubscriptionStatus.canceled)
        elif etype in {"order_created", "order_refunded", "payment_success", "payment_refunded"}:
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
