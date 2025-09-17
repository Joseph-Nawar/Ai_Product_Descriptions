from typing import Dict, Any
from fastapi import Depends
from sqlalchemy.orm import Session

from src.auth.firebase import get_current_user
from app.db.session import get_db
from app.repos import user_repo


async def get_authed_user_db(
    claims: Dict[str, Any] = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Verify Firebase token, ensure a User row exists, and provide both claims and ORM user."""
    uid = claims.get("uid")
    email = claims.get("email")
    user = user_repo.get_or_create_user(db, uid, email=email)
    return {"claims": claims, "user": user}
