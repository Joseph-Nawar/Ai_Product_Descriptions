# PowerShell script to fix missing dependencies
Write-Host "🔧 Fixing missing dependencies..." -ForegroundColor Green

# Navigate to backend directory
Set-Location backend

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Install the missing google-generativeai package
Write-Host "Installing google-generativeai..." -ForegroundColor Yellow
pip install google-generativeai

# Verify installation
Write-Host "Verifying installation..." -ForegroundColor Yellow
$genaiInstalled = pip list | Select-String "google-generativeai"
if ($genaiInstalled) {
    Write-Host "✅ google-generativeai installed successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to install google-generativeai" -ForegroundColor Red
}

# Also install any other potentially missing packages
Write-Host "Installing other critical packages..." -ForegroundColor Yellow
pip install fastapi uvicorn python-multipart python-dotenv pandas

Write-Host "🎉 Dependency fix completed!" -ForegroundColor Green
Write-Host "Now try running: .\start_backend.ps1" -ForegroundColor Cyan
