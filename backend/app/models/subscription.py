from enum import Enum as PyEnum
from typing import Optional

from sqlalchemy import String, DateTime, func, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class SubscriptionStatus(PyEnum):
    active = "active"
    past_due = "past_due"
    canceled = "canceled"
    expired = "expired"
    trialing = "trialing"
    inactive = "inactive"


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), index=True)
    provider: Mapped[str] = mapped_column(String, default="lemon_squeezy")
    plan: Mapped[str] = mapped_column(String)  # variant_id or monthly/yearly label
    status: Mapped[SubscriptionStatus] = mapped_column(
        Enum(SubscriptionStatus), index=True
    )
    current_period_end: Mapped[Optional[object]] = mapped_column(
        DateTime(timezone=True)
    )
    # Lemon Squeezy integration
    lemon_squeezy_customer_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    lemon_squeezy_subscription_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    created_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )
