from decimal import Decimal
from typing import Optional
from sqlalchemy.orm import Session

from app.models.transaction import Transaction


def record_payment(
    db: Session,
    *,
    user_id: str,
    provider_ref: str,
    amount: Decimal | float,
    currency: str,
) -> Transaction:
    tx = Transaction(
        user_id=user_id,
        provider_ref=provider_ref,
        amount=Decimal(str(amount)),
        currency=currency,
    )
    db.add(tx)
    db.flush()
    return tx
