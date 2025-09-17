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

# Install firebase if not already installed
Write-Host "Checking for firebase..." -ForegroundColor Yellow
$firebaseInstalled = npm list firebase 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Installing firebase..." -ForegroundColor Yellow
    npm install firebase
}

# Create .env file if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "Creating .env file..." -ForegroundColor Yellow
    @"
VITE_API_BASE_URL=http://localhost:8000
VITE_USE_MOCK=false

# Firebase Configuration (replace with your actual Firebase config)
VITE_FIREBASE_API_KEY=your_firebase_api_key_here
VITE_FIREBASE_AUTH_DOMAIN=your_project_id.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your_firebase_project_id_here
VITE_FIREBASE_STORAGE_BUCKET=your_project_id.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id_here
VITE_FIREBASE_APP_ID=your_firebase_app_id_here
VITE_FIREBASE_MEASUREMENT_ID=your_measurement_id_here
"@ | Out-File -FilePath ".env" -Encoding UTF8
    Write-Host "Created .env file with backend connection and Firebase settings." -ForegroundColor Cyan
}

# Create vite-env.d.ts file for TypeScript support
if (-not (Test-Path "src\vite-env.d.ts")) {
    Write-Host "Creating TypeScript environment definitions..." -ForegroundColor Yellow
    @"
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_BASE_URL: string
  readonly VITE_USE_MOCK: string
  readonly VITE_FIREBASE_API_KEY: string
  readonly VITE_FIREBASE_AUTH_DOMAIN: string
  readonly VITE_FIREBASE_PROJECT_ID: string
  readonly VITE_FIREBASE_STORAGE_BUCKET: string
  readonly VITE_FIREBASE_MESSAGING_SENDER_ID: string
  readonly VITE_FIREBASE_APP_ID: string
  readonly VITE_FIREBASE_MEASUREMENT_ID: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
"@ | Out-File -FilePath "src\vite-env.d.ts" -Encoding UTF8
}

# Start the development server
Write-Host "Starting frontend server on http://localhost:5173..." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
npm run dev