# PowerShell script to start the backend server
Write-Host "Starting AI Product Descriptions Backend Server..." -ForegroundColor Green

# Check if we're in the right directory
if (-not (Test-Path "backend\src\main.py")) {
    Write-Host "Error: Please run this script from the project root directory" -ForegroundColor Red
    exit 1
}

# Navigate to backend directory
Set-Location backend

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Install dependencies (including firebase_admin)
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Install firebase_admin if not already installed
Write-Host "Checking for firebase_admin..." -ForegroundColor Yellow
$firebaseInstalled = pip list | Select-String "firebase-admin"
if (-not $firebaseInstalled) {
    Write-Host "Installing firebase_admin..." -ForegroundColor Yellow
    pip install firebase-admin
}

# Create .env file if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "Creating .env file..." -ForegroundColor Yellow
    @"
# AI Product Descriptions Backend Configuration
# Copy this file and add your actual API keys

# Google Gemini API Key (required for AI generation)
GEMINI_API_KEY=your_gemini_api_key_here

# Firebase Admin SDK Configuration (for authentication)
FIREBASE_PROJECT_ID=your_firebase_project_id_here
FIREBASE_PRIVATE_KEY=your_firebase_private_key_here
FIREBASE_CLIENT_EMAIL=your_firebase_client_email_here

# Optional: Set to "true" to enable dry-run mode (no actual API calls)
DRY_RUN=true

# Optional: Model configuration
GEMINI_MODEL=gemini-1.5-flash
TEMPERATURE=0.2
"@ | Out-File -FilePath ".env" -Encoding UTF8
    Write-Host "Created .env file. Please edit it with your API keys." -ForegroundColor Cyan
}

# Start the server
Write-Host "Starting server on http://localhost:8000..." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000