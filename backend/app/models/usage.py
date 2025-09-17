from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func, Integer, UniqueConstraint

from app.db.base import Base


class Usage(Base):
    __tablename__ = "usage"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, index=True)
    key: Mapped[str] = mapped_column(String)  # e.g., rows_processed_month
    value: Mapped[int] = mapped_column(Integer, default=0)
    period: Mapped[str] = mapped_column(String)  # e.g., 2025-09
    created_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    __table_args__ = (
        UniqueConstraint("user_id", "key", "period", name="uq_usage_user_key_period"),
    )
