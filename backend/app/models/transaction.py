from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func, Numeric

from app.db.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String, index=True)
    provider: Mapped[str] = mapped_column(String, default="lemon_squeezy")
    provider_ref: Mapped[str] = mapped_column(String, index=True)  # order/sub ID
    amount: Mapped[object] = mapped_column(Numeric(10, 2))
    currency: Mapped[str] = mapped_column(String(10))
    created_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
