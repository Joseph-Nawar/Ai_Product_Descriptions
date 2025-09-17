from sqlalchemy.orm import Session

from app.models.subscription import SubscriptionStatus
from app.repos import subscription_repo


class EntitlementService:
    def __init__(self, db: Session):
        self.db = db

    def has_access(self, user_id: str) -> bool:
        sub = subscription_repo.get_by_user(self.db, user_id)
        if not sub:
            return False
        return sub.status in {SubscriptionStatus.active, SubscriptionStatus.trialing}
