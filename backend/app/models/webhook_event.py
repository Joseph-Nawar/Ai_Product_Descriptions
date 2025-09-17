from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func, UniqueConstraint

from app.db.base import Base


class WebhookEvent(Base):
    __tablename__ = "webhook_events"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    event_id: Mapped[str] = mapped_column(String)
    created_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    __table_args__ = (UniqueConstraint("event_id", name="uq_webhook_event_event_id"),)
