from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.repos import user_repo, subscription_repo, webhook_repo
from app.models.subscription import SubscriptionStatus


def test_subscription_crud_and_webhook_unique(tmp_path):
    engine = create_engine("sqlite+pysqlite:///:memory:", future=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, future=True)
    with Session() as db:
        # user
        user = user_repo.get_or_create_user(db, "u1", email="u1@example.com")
        assert user.id == "u1"

        # upsert subscription
        sub = subscription_repo.upsert_subscription(
            db,
            user_id="u1",
            plan="monthly",
            status=SubscriptionStatus.active,
            current_period_end=None,
        )
        assert sub.id is not None

        # set status
        subscription_repo.set_status(db, sub.id, SubscriptionStatus.canceled)
        db.refresh(sub)
        assert sub.status == SubscriptionStatus.canceled

        # webhook idempotency
        ok1 = webhook_repo.record_event(db, "evt_1")
        ok2 = webhook_repo.record_event(db, "evt_1")
        assert ok1 is True and ok2 is False

    Base.metadata.drop_all(engine)
