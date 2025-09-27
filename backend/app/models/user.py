from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True)  # firebase UID
    email: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    firebase_uid: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    subscription_plan_id: Mapped[str] = mapped_column(String, nullable=False, default='free')
    credits_remaining: Mapped[int] = mapped_column(nullable=False, default=0)
    credits_used: Mapped[int] = mapped_column(nullable=False, default=0)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
