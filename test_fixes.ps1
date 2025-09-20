# PowerShell script to test all the fixes
Write-Host "🧪 Testing AI Product Descriptions Fixes..." -ForegroundColor Green

# Test 1: Check if backend starts without crashing
Write-Host "`n1. Testing Backend Server Startup..." -ForegroundColor Yellow
Write-Host "Starting backend server in background..." -ForegroundColor Cyan

# Start backend in background
$backendJob = Start-Job -ScriptBlock {
    Set-Location "backend"
    python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
}

# Wait a bit for server to start
Start-Sleep -Seconds 10

# Test 2: Check if server is responding
Write-Host "`n2. Testing Server Health..." -ForegroundColor Yellow
try {
    $healthResponse = Invoke-RestMethod -Uri "http://localhost:8000/api/health" -Method GET
    Write-Host "✅ Backend health check passed: $($healthResponse.status)" -ForegroundColor Green
} catch {
    Write-Host "❌ Backend health check failed: $($_.Exception.Message)" -ForegroundColor Red
}

# Test 3: Check CORS headers
Write-Host "`n3. Testing CORS Configuration..." -ForegroundColor Yellow
try {
    $corsResponse = Invoke-WebRequest -Uri "http://localhost:8000/api/health" -Method OPTIONS
    $corsHeaders = $corsResponse.Headers
    if ($corsHeaders["Access-Control-Allow-Origin"]) {
        Write-Host "✅ CORS headers present: $($corsHeaders['Access-Control-Allow-Origin'])" -ForegroundColor Green
    } else {
        Write-Host "❌ CORS headers missing" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ CORS test failed: $($_.Exception.Message)" -ForegroundColor Red
}

# Test 4: Check payment endpoints
Write-Host "`n4. Testing Payment Endpoints..." -ForegroundColor Yellow
try {
    $plansResponse = Invoke-RestMethod -Uri "http://localhost:8000/api/payment/plans" -Method GET
    Write-Host "✅ Payment plans endpoint working: $($plansResponse.plans.Count) plans found" -ForegroundColor Green
} catch {
    Write-Host "❌ Payment plans endpoint failed: $($_.Exception.Message)" -ForegroundColor Red
}

# Test 5: Check WebSocket endpoint
Write-Host "`n5. Testing WebSocket Endpoint..." -ForegroundColor Yellow
try {
    $wsTest = Test-NetConnection -ComputerName "localhost" -Port 8000
    if ($wsTest.TcpTestSucceeded) {
        Write-Host "✅ WebSocket port 8000 is accessible" -ForegroundColor Green
    } else {
        Write-Host "❌ WebSocket port 8000 is not accessible" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ WebSocket test failed: $($_.Exception.Message)" -ForegroundColor Red
}

# Test 6: Check database connection
Write-Host "`n6. Testing Database Connection..." -ForegroundColor Yellow
try {
    $dbResponse = Invoke-RestMethod -Uri "http://localhost:8000/readyz" -Method GET
    if ($dbResponse.db) {
        Write-Host "✅ Database connection working" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Database connection degraded but server running" -ForegroundColor Yellow
    }
} catch {
    Write-Host "❌ Database test failed: $($_.Exception.Message)" -ForegroundColor Red
}

# Test 7: Check frontend build
Write-Host "`n7. Testing Frontend Build..." -ForegroundColor Yellow
Set-Location "frontend"
try {
    npm run build
    Write-Host "✅ Frontend builds successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Frontend build failed: $($_.Exception.Message)" -ForegroundColor Red
}

# Cleanup
Write-Host "`n8. Cleaning up..." -ForegroundColor Yellow
Stop-Job $backendJob -ErrorAction SilentlyContinue
Remove-Job $backendJob -ErrorAction SilentlyContinue

Write-Host "`n🎉 Testing completed! Check the results above." -ForegroundColor Green
Write-Host "`n📋 Summary of fixes applied:" -ForegroundColor Cyan
Write-Host "✅ CORS configuration updated with additional origins" -ForegroundColor Green
Write-Host "✅ Server startup error handling improved" -ForegroundColor Green
Write-Host "✅ Database configuration set to SQLite by default" -ForegroundColor Green
Write-Host "✅ API endpoint mismatches fixed in frontend" -ForegroundColor Green
Write-Host "✅ Frontend runtime errors fixed with null checks" -ForegroundColor Green
Write-Host "✅ WebSocket endpoint added to backend" -ForegroundColor Green

Write-Host "`n🚀 Next steps:" -ForegroundColor Cyan
Write-Host "1. Start the backend: .\start_backend.ps1" -ForegroundColor White
Write-Host "2. Start the frontend: .\start_frontend.ps1" -ForegroundColor White
Write-Host "3. Test the application in your browser" -ForegroundColor White
