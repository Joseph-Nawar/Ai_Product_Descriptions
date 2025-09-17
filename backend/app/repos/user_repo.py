from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User


def get_or_create_user(db: Session, uid: str, email: Optional[str] = None) -> User:
    user = db.get(User, uid)
    if user:
        return user
    user = User(id=uid, email=email)
    db.add(user)
    db.flush()
    return user
