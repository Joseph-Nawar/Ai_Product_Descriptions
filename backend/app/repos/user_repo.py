from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User


def get_or_create_user(db: Session, uid: str, email: Optional[str] = None) -> User:
    # First try to get user by ID
    user = db.get(User, uid)
    if user:
        return user
    
    # If not found by ID, try to get by email
    if email:
        user = db.query(User).filter(User.email == email).first()
        if user:
            # Update the user's ID to match the new UID if it's different
            if user.id != uid:
                print(f"🔄 Updating user ID from {user.id} to {uid} for email {email}")
                user.id = uid
                user.firebase_uid = uid
                db.flush()
            return user
    
    # Create new user if doesn't exist
    try:
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
    except Exception as e:
        if "duplicate key value violates unique constraint" in str(e):
            # User already exists, try to get them by email
            print(f"🔄 User creation failed due to duplicate, trying to get by email: {email}")
            if email:
                user = db.query(User).filter(User.email == email).first()
                if user:
                    # Update the user's ID to match the new UID if it's different
                    if user.id != uid:
                        print(f"🔄 Updating user ID from {user.id} to {uid} for email {email}")
                        user.id = uid
                        user.firebase_uid = uid
                        db.flush()
                    return user
        raise e
