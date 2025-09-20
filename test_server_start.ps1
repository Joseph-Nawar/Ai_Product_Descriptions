# PowerShell script to test if server can start
Write-Host "🧪 Testing server startup..." -ForegroundColor Green

# Navigate to backend directory
Set-Location backend

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Try to import the main module to check for errors
Write-Host "Testing Python imports..." -ForegroundColor Yellow
python -c "
try:
    import sys
    sys.path.insert(0, '.')
    from src.main import app
    print('✅ Server module imported successfully')
    print('✅ FastAPI app created successfully')
except Exception as e:
    print(f'❌ Import failed: {str(e)}')
    import traceback
    traceback.print_exc()
"

Write-Host "`n🎉 Test completed!" -ForegroundColor Green
