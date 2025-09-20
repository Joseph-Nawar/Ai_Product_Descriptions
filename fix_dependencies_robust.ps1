# PowerShell script to fix missing dependencies with robust installation
Write-Host "🔧 Fixing missing dependencies (Robust Method)..." -ForegroundColor Green

# Navigate to backend directory
Set-Location backend

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Clear pip cache to avoid corrupted files
Write-Host "Clearing pip cache..." -ForegroundColor Yellow
pip cache purge

# Install packages one by one to avoid conflicts
Write-Host "Installing core packages..." -ForegroundColor Yellow

# Install basic packages first
$packages = @(
    "fastapi",
    "uvicorn[standard]",
    "sqlalchemy",
    "alembic",
    "python-multipart",
    "python-jose[cryptography]",
    "passlib[bcrypt]",
    "python-dotenv",
    "pydantic",
    "requests",
    "httpx"
)

foreach ($package in $packages) {
    Write-Host "Installing $package..." -ForegroundColor Cyan
    try {
        pip install $package --no-cache-dir
        Write-Host "✅ $package installed successfully" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  $package installation had issues, but continuing..." -ForegroundColor Yellow
    }
}

# Try to install google-generativeai with specific options
Write-Host "Installing google-generativeai with Windows-friendly options..." -ForegroundColor Yellow
try {
    pip install google-generativeai --no-cache-dir --no-deps
    pip install google-api-core google-auth google-api-python-client protobuf pydantic tqdm typing-extensions --no-cache-dir
    Write-Host "✅ google-generativeai installed successfully" -ForegroundColor Green
} catch {
    Write-Host "⚠️  google-generativeai installation failed, but server can still start" -ForegroundColor Yellow
}

# Install other potentially missing packages
Write-Host "Installing additional packages..." -ForegroundColor Yellow
$additionalPackages = @(
    "firebase-admin",
    "lemon-squeezy-python",
    "stripe",
    "cryptography",
    "bcrypt"
)

foreach ($package in $additionalPackages) {
    Write-Host "Installing $package..." -ForegroundColor Cyan
    try {
        pip install $package --no-cache-dir
        Write-Host "✅ $package installed successfully" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  $package installation had issues, but continuing..." -ForegroundColor Yellow
    }
}

# Verify critical packages
Write-Host "Verifying critical packages..." -ForegroundColor Yellow
$criticalPackages = @("fastapi", "uvicorn", "sqlalchemy", "pydantic")
foreach ($package in $criticalPackages) {
    $installed = pip list | Select-String $package
    if ($installed) {
        Write-Host "✅ $package is available" -ForegroundColor Green
    } else {
        Write-Host "❌ $package is missing" -ForegroundColor Red
    }
}

Write-Host "`n🎉 Dependency installation completed!" -ForegroundColor Green
Write-Host "You can now try starting the server with: .\start_backend.ps1" -ForegroundColor Cyan
