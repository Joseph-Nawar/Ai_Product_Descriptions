# Database Setup Script for AI Product Descriptions
# This script helps you set up the database for production

Write-Host "🚀 AI Product Descriptions - Database Setup" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Green

# Check if we're in the right directory
if (-not (Test-Path "backend")) {
    Write-Host "❌ Error: Please run this script from the project root directory" -ForegroundColor Red
    exit 1
}

Write-Host "📋 Database Setup Options:" -ForegroundColor Yellow
Write-Host "1. SQLite (Development - Default, no setup required)"
Write-Host "2. PostgreSQL (Production recommended)"
Write-Host ""

$choice = Read-Host "Select option (1 or 2)"

if ($choice -eq "1") {
    Write-Host "✅ SQLite selected - No additional setup required!" -ForegroundColor Green
    Write-Host "The application will create the database automatically on first run." -ForegroundColor Cyan
} elseif ($choice -eq "2") {
    Write-Host "🐘 PostgreSQL Setup Selected" -ForegroundColor Green
    Write-Host ""
    
    # Check if PostgreSQL is installed
    try {
        $pgVersion = psql --version 2>$null
        if ($pgVersion) {
            Write-Host "✅ PostgreSQL is installed: $pgVersion" -ForegroundColor Green
        } else {
            Write-Host "❌ PostgreSQL not found. Please install PostgreSQL first:" -ForegroundColor Red
            Write-Host "   - Download from: https://www.postgresql.org/download/windows/" -ForegroundColor Yellow
            Write-Host "   - Or use Chocolatey: choco install postgresql" -ForegroundColor Yellow
            exit 1
        }
    } catch {
        Write-Host "❌ PostgreSQL not found. Please install PostgreSQL first." -ForegroundColor Red
        exit 1
    }
    
    Write-Host ""
    Write-Host "📝 Please provide PostgreSQL connection details:" -ForegroundColor Yellow
    
    $dbHost = Read-Host "Database Host (default: localhost)"
    if ([string]::IsNullOrEmpty($dbHost)) { $dbHost = "localhost" }
    
    $dbPort = Read-Host "Database Port (default: 5432)"
    if ([string]::IsNullOrEmpty($dbPort)) { $dbPort = "5432" }
    
    $dbName = Read-Host "Database Name (default: ai_descriptions)"
    if ([string]::IsNullOrEmpty($dbName)) { $dbName = "ai_descriptions" }
    
    $dbUser = Read-Host "Database User (default: postgres)"
    if ([string]::IsNullOrEmpty($dbUser)) { $dbUser = "postgres" }
    
    $dbPassword = Read-Host "Database Password" -AsSecureString
    $dbPasswordPlain = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($dbPassword))
    
    Write-Host ""
    Write-Host "🔧 Creating database and user..." -ForegroundColor Yellow
    
    # Create database and user
    $createDbScript = @"
CREATE DATABASE $dbName;
CREATE USER ai_user WITH PASSWORD '$dbPasswordPlain';
GRANT ALL PRIVILEGES ON DATABASE $dbName TO ai_user;
"@
    
    try {
        # Execute SQL commands
        $createDbScript | psql -h $dbHost -p $dbPort -U $dbUser -d postgres
        Write-Host "✅ Database and user created successfully!" -ForegroundColor Green
    } catch {
        Write-Host "❌ Error creating database. Please check your PostgreSQL connection." -ForegroundColor Red
        Write-Host "You may need to create the database manually:" -ForegroundColor Yellow
        Write-Host "   psql -U $dbUser -d postgres" -ForegroundColor Cyan
        Write-Host "   CREATE DATABASE $dbName;" -ForegroundColor Cyan
        Write-Host "   CREATE USER ai_user WITH PASSWORD '$dbPasswordPlain';" -ForegroundColor Cyan
        Write-Host "   GRANT ALL PRIVILEGES ON DATABASE $dbName TO ai_user;" -ForegroundColor Cyan
    }
    
    # Update .env file
    $envFile = "backend\.env"
    if (Test-Path $envFile) {
        Write-Host ""
        Write-Host "📝 Updating backend/.env file..." -ForegroundColor Yellow
        
        # Read current .env content
        $envContent = Get-Content $envFile -Raw
        
        # Update DATABASE_URL
        $newDatabaseUrl = "postgresql+psycopg://ai_user:$dbPasswordPlain@$dbHost`:$dbPort/$dbName"
        $envContent = $envContent -replace "DATABASE_URL=.*", "DATABASE_URL=$newDatabaseUrl"
        
        # Write back to file
        Set-Content $envFile $envContent
        Write-Host "✅ Database URL updated in backend/.env" -ForegroundColor Green
    }
} else {
    Write-Host "❌ Invalid choice. Please select 1 or 2." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🔄 Running database migrations..." -ForegroundColor Yellow

# Change to backend directory and run migrations
Set-Location backend

try {
    # Check if virtual environment exists
    if (Test-Path "venv\Scripts\Activate.ps1") {
        Write-Host "📦 Activating virtual environment..." -ForegroundColor Cyan
        & "venv\Scripts\Activate.ps1"
    }
    
    # Run migrations
    Write-Host "🚀 Running Alembic migrations..." -ForegroundColor Cyan
    python -m alembic upgrade head
    
    Write-Host "✅ Database migrations completed successfully!" -ForegroundColor Green
} catch {
    Write-Host "❌ Error running migrations. Please check your database connection and try again." -ForegroundColor Red
    Write-Host "You can run migrations manually with:" -ForegroundColor Yellow
    Write-Host "   cd backend" -ForegroundColor Cyan
    Write-Host "   python -m alembic upgrade head" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "🧪 Testing database connection..." -ForegroundColor Yellow

try {
    python test_database_models.py
    Write-Host "✅ Database tests passed!" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Database tests failed. Please check your configuration." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🎉 Database setup completed!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Complete Lemon Squeezy store setup (see PRODUCTION_SETUP_GUIDE.md)" -ForegroundColor Cyan
Write-Host "2. Deploy your application" -ForegroundColor Cyan
Write-Host "3. Configure webhooks after deployment" -ForegroundColor Cyan
Write-Host ""
Write-Host "For detailed instructions, see: PRODUCTION_SETUP_GUIDE.md" -ForegroundColor Cyan

