from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True)  # firebase UID
    email: Mapped[str | None] = mapped_column(String, index=True, nullable=True)
    created_at: Mapped[object] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
