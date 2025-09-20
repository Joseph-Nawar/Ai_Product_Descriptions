# PowerShell script to start backend with minimal dependencies
Write-Host "🚀 Starting AI Product Descriptions Backend (Minimal Mode)..." -ForegroundColor Green

# Navigate to backend directory
Set-Location backend

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Install minimal requirements first
Write-Host "Installing minimal requirements..." -ForegroundColor Yellow
pip install -r requirements_minimal.txt

# Try to install optional packages (don't fail if they don't work)
Write-Host "Installing optional packages..." -ForegroundColor Yellow
try {
    pip install google-generativeai --no-cache-dir
    Write-Host "✅ AI packages installed" -ForegroundColor Green
} catch {
    Write-Host "⚠️  AI packages not available - server will run in limited mode" -ForegroundColor Yellow
}

try {
    pip install firebase-admin --no-cache-dir
    Write-Host "✅ Firebase packages installed" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Firebase packages not available - auth will be limited" -ForegroundColor Yellow
}

try {
    pip install lemon-squeezy-python --no-cache-dir
    Write-Host "✅ Payment packages installed" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Payment packages not available - payments will be limited" -ForegroundColor Yellow
}

# Start the server
Write-Host "Starting FastAPI server..." -ForegroundColor Yellow
Write-Host "Server will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "API docs will be available at: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow

python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
