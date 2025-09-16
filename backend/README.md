# Backend - AI Product Descriptions

This directory contains the backend services for the AI Product Descriptions application.

## Structure

- `src/` - Main backend code (APIs, automation, scripts)
- `models/` - Saved AI/ML models or prompt templates
- `utils/` - Helper functions (data cleaning, APIs, etc.)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

3. Run the development server:
   ```bash
   uvicorn src.main:app --reload
   ```

## Authentication

This backend uses Firebase Admin SDK for JWT token verification:

- All API requests should include `Authorization: Bearer <firebase_id_token>` header
- Test auth with `GET /auth/me` endpoint
- Environment requires Firebase service account credentials

### Firebase Admin Setup

1. In Firebase Console → Project Settings → Service Accounts
2. Generate new private key (downloads JSON file)
3. Base64-encode the entire JSON:
   - **Windows PowerShell**: `[Convert]::ToBase64String([IO.File]::ReadAllBytes("serviceAccount.json"))`
   - **macOS/Linux**: `base64 -w 0 serviceAccount.json`
4. Add to `.env`:
   ```bash
   FIREBASE_PROJECT_ID=your-project-id
   FIREBASE_SERVICE_ACCOUNT_BASE64=base64_encoded_service_account_json
   ```

## API Endpoints

- `POST /api/generate-description` - Generate product description
- `GET /api/health` - Health check endpoint
- `GET /auth/me` - Returns Firebase user claims (requires auth)

## Development

- Use `black` for code formatting
- Use `flake8` for linting
- Run tests with `pytest`
