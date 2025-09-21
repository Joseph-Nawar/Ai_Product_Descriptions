from typing import Optional
from sqlalchemy.orm import Session

from app.models.subscription import Subscription, SubscriptionStatus


def get_by_user(db: Session, user_id: str) -> Optional[Subscription]:
    return (
        db.query(Subscription)
        .filter(Subscription.user_id == user_id)
        .order_by(Subscription.id.desc())
        .first()
    )


def upsert_subscription(
    db: Session,
    *,
    user_id: str,
    plan: str,
    status: SubscriptionStatus,
    current_period_end,
    customer_id: str = None,
) -> Subscription:
    sub = get_by_user(db, user_id)
    if sub is None:
        sub = Subscription(
            user_id=user_id,
            plan=plan,
            status=status,
            current_period_end=current_period_end,
            lemon_squeezy_customer_id=customer_id,
        )
        db.add(sub)
        db.flush()
        return sub
    sub.plan = plan
    sub.status = status
    sub.current_period_end = current_period_end
    if customer_id:
        sub.lemon_squeezy_customer_id = customer_id
    db.flush()
    return sub


def set_status(db: Session, sub_id: int, status: SubscriptionStatus) -> None:
    sub = db.get(Subscription, sub_id)
    if sub:
        sub.status = status
        db.flush()


def get_customer_id_by_user(db: Session, user_id: str) -> Optional[str]:
    """Get the Lemon Squeezy customer ID for a user"""
    sub = get_by_user(db, user_id)
    return sub.lemon_squeezy_customer_id if sub else None


def update_customer_id(db: Session, user_id: str, customer_id: str) -> None:
    """Update the Lemon Squeezy customer ID for a user"""
    sub = get_by_user(db, user_id)
    if sub:
        sub.lemon_squeezy_customer_id = customer_id
        db.flush()