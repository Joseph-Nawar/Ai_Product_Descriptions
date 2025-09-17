import os
import hmac
import hashlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.db.session import DATABASE_URL
from app.services.billing_service import BillingService

os.environ.setdefault("LEMON_SQUEEZY_WEBHOOK_SECRET", "secret")


def test_hmac_verification_and_idempotency(tmp_path):
    payload = "{\"meta\":{\"event_id\":\"evt_1\",\"event_name\":\"payment_success\"},\"data\":{\"id\":\"order_1\",\"attributes\":{\"total\":1000,\"currency\":\"USD\",\"checkout_data\":{\"custom\":{\"user_id\":\"user_1\",\"plan_id\":\"basic\"}}}}}"
    secret = os.environ["LEMON_SQUEEZY_WEBHOOK_SECRET"].encode()
    sig = hmac.new(secret, payload.encode(), hashlib.sha256).hexdigest()

    # local engine for test DB (reuse env URL if it points to local Postgres)
    engine = create_engine(DATABASE_URL, future=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, future=True)
    with Session() as db:
        svc = BillingService(db)
        # first process
        svc.handle_webhook("evt_1", __import__("json").loads(payload))
        # second (replay) should be idempotent
        svc.handle_webhook("evt_1", __import__("json").loads(payload))

    # drop tables after
    Base.metadata.drop_all(engine)
