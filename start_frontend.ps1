# PowerShell script to start the frontend server
Write-Host "Starting AI Product Descriptions Frontend Server..." -ForegroundColor Green

# Check if we're in the right directory
if (-not (Test-Path "frontend\package.json")) {
    Write-Host "Error: Please run this script from the project root directory" -ForegroundColor Red
    exit 1
}

# Navigate to frontend directory
Set-Location frontend

# Check if node_modules exists
if (-not (Test-Path "node_modules")) {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    npm install
}

# Create .env file if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "Creating .env file..." -ForegroundColor Yellow
    @"
VITE_API_BASE_URL=http://localhost:8000
VITE_USE_MOCK=false
"@ | Out-File -FilePath ".env" -Encoding UTF8
    Write-Host "Created .env file with backend connection settings." -ForegroundColor Cyan
}

# Start the development server
Write-Host "Starting frontend server on http://localhost:5173..." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
npm run dev



