from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User


def get_or_create_user(db: Session, uid: str, email: Optional[str] = None) -> User:
    user = db.get(User, uid)
    if user:
        return user
    
    # Create new user
    user = User(id=uid, email=email, firebase_uid=uid)
    db.add(user)
    db.flush()
    
    # Automatically assign free plan to new user
    try:
        from src.payments.sqlalchemy_service import SQLAlchemyPaymentService
        payment_service = SQLAlchemyPaymentService()
        payment_service.assign_free_plan_to_user(db, uid)
    except Exception as e:
        # Log error but don't fail user creation
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to assign free plan to new user {uid}: {str(e)}")
    
    return user
