from typing import Dict, Any
from fastapi import Depends
from sqlalchemy.orm import Session

from src.auth.firebase import get_current_user
from src.database.deps import get_db
from app.repos import user_repo


async def get_authed_user_db(
    claims: Dict[str, Any] = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Verify Firebase token, ensure a User row exists, and provide both claims and ORM user."""
    import logging
    logger = logging.getLogger(__name__)
    
    logger.info(f"🔍 get_authed_user_db called - claims: {claims}")
    uid = claims.get("uid")
    email = claims.get("email")
    logger.info(f"🔍 UID: {uid}, Email: {email}")
    
    try:
        # Remove database connection test to avoid session state issues
        logger.info(f"🔍 Creating/retrieving user...")
        user = user_repo.get_or_create_user(db, uid, email=email)
        logger.info(f"🔍 User created/retrieved: {user}")
        return {"claims": claims, "user": user}
    except Exception as e:
        logger.error(f"❌ Error in get_authed_user_db: {str(e)}")
        import traceback
        logger.error(f"❌ Full traceback: {traceback.format_exc()}")
        raise
