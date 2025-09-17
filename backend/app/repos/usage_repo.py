from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.usage import Usage


def increment(db: Session, user_id: str, key: str, amount: int, period: str) -> Usage:
    row = (
        db.execute(
            select(Usage).where(
                Usage.user_id == user_id, Usage.key == key, Usage.period == period
            )
        )
        .scalars()
        .first()
    )
    if row is None:
        row = Usage(user_id=user_id, key=key, value=amount, period=period)
        db.add(row)
        db.flush()
        return row
    row.value += amount
    db.flush()
    return row
