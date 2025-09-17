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
) -> Subscription:
    sub = get_by_user(db, user_id)
    if sub is None:
        sub = Subscription(
            user_id=user_id,
            plan=plan,
            status=status,
            current_period_end=current_period_end,
        )
        db.add(sub)
        db.flush()
        return sub
    sub.plan = plan
    sub.status = status
    sub.current_period_end = current_period_end
    db.flush()
    return sub


def set_status(db: Session, sub_id: int, status: SubscriptionStatus) -> None:
    sub = db.get(Subscription, sub_id)
    if sub:
        sub.status = status
        db.flush()
