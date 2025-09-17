import os
import types
import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("FIREBASE_SERVICE_ACCOUNT_BASE64", "e30=")  # {}

from src.main import app


# Add a tiny protected route for testing
@app.get("/api/protected/ping")
def protected_ping(user = types.SimpleNamespace()):
    return {"ok": True}


@pytest.fixture
def client():
    return TestClient(app)


def test_no_token_unauthorized(client):
    r = client.get("/api/protected/ping")
    assert r.status_code == 401


def test_invalid_token_unauthorized(client, monkeypatch):
    # Force token verification to raise
    from src.auth import firebase as fb

    async def fake_get_current_user(request):
        raise Exception("bad token")

    monkeypatch.setattr(fb, "get_current_user", fake_get_current_user)
    r = client.get("/api/protected/ping", headers={"Authorization": "Bearer bad"})
    assert r.status_code == 401


def test_valid_token_allows(client, monkeypatch):
    from src.auth import firebase as fb

    async def fake_get_current_user(request):
        return {"uid": "u1", "email": "u1@example.com"}

    monkeypatch.setattr(fb, "get_current_user", fake_get_current_user)
    r = client.get("/api/protected/ping", headers={"Authorization": "Bearer good"})
    assert r.status_code == 200
    assert r.json()["ok"] is True
