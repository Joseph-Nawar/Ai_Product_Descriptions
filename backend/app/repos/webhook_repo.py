from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.webhook_event import WebhookEvent


def record_event(db: Session, event_id: str) -> bool:
    """Insert webhook event id; return False if already processed."""
    try:
        evt = WebhookEvent(event_id=event_id)
        db.add(evt)
        db.flush()
        return True
    except IntegrityError:
        db.rollback()
        return False
