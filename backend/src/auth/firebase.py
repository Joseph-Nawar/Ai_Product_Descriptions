# backend/src/auth/firebase.py
import os
import json
import base64
import firebase_admin
from firebase_admin import auth, credentials
from fastapi import HTTPException, Request

def _init_firebase_admin():
    if firebase_admin._apps:
        return
    sa_b64 = os.getenv("FIREBASE_SERVICE_ACCOUNT_BASE64")
    project_id = os.getenv("FIREBASE_PROJECT_ID")
    if sa_b64:
        info = json.loads(base64.b64decode(sa_b64))
        cred = credentials.Certificate(info)
        firebase_admin.initialize_app(cred, {'projectId': project_id} if project_id else None)
    else:
        # ADC fallback (works on many platforms if GOOGLE_APPLICATION_CREDENTIALS is set)
        firebase_admin.initialize_app()

_init_firebase_admin()

async def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization", "")
    parts = auth_header.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Missing bearer token")
    id_token = parts[1]
    try:
        decoded = auth.verify_id_token(id_token)
        return decoded
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid auth token")
