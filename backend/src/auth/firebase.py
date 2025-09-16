# backend/src/auth/firebase.py
import os
import json
import base64
import logging
import firebase_admin
from firebase_admin import auth, credentials
from fastapi import HTTPException, Request

logging.info("🔥 Firebase auth module imported")

def _init_firebase_admin():
    if firebase_admin._apps:
        logging.info("Firebase Admin SDK already initialized")
        print("Firebase Admin SDK already initialized")
        return
    
    sa_b64 = os.getenv("FIREBASE_SERVICE_ACCOUNT_BASE64")
    project_id = os.getenv("FIREBASE_PROJECT_ID")
    
    logging.info(f"Firebase config - Project ID: {project_id}")
    logging.info(f"Firebase config - Service Account: {'SET' if sa_b64 else 'NOT SET'}")
    
    if sa_b64:
        try:
            info = json.loads(base64.b64decode(sa_b64))
            cred = credentials.Certificate(info)
            firebase_admin.initialize_app(cred, {'projectId': project_id} if project_id else None)
            logging.info("✅ Firebase Admin SDK initialized successfully")
        except Exception as e:
            logging.error(f"❌ Failed to initialize Firebase Admin SDK: {str(e)}")
            logging.error(f"❌ Error type: {type(e).__name__}")
            import traceback
            logging.error(f"❌ Full traceback: {traceback.format_exc()}")
            raise
    else:
        logging.warning("⚠️ No Firebase service account found, trying ADC fallback")
        try:
            firebase_admin.initialize_app()
            logging.info("✅ Firebase Admin SDK initialized with ADC")
        except Exception as e:
            logging.error(f"❌ Failed to initialize Firebase Admin SDK with ADC: {str(e)}")
            logging.error(f"❌ Error type: {type(e).__name__}")
            import traceback
            logging.error(f"❌ Full traceback: {traceback.format_exc()}")
            raise

logging.info("🔥 About to initialize Firebase Admin SDK")
_init_firebase_admin()
logging.info("🔥 Firebase Admin SDK initialization completed")

async def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization", "")
    logging.info(f"Auth header received: {auth_header[:20]}..." if auth_header else "No auth header")
    
    parts = auth_header.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        logging.warning("Invalid auth header format")
        raise HTTPException(status_code=401, detail="Missing bearer token")
    
    id_token = parts[1]
    logging.info(f"Verifying token: {id_token[:20]}...")
    
    try:
        decoded = auth.verify_id_token(id_token)
        logging.info(f"✅ Token verified for user: {decoded.get('email', 'unknown')}")
        return decoded
    except Exception as e:
        logging.error(f"❌ Token verification failed: {str(e)}")
        raise HTTPException(status_code=401, detail=f"Invalid auth token: {str(e)}")