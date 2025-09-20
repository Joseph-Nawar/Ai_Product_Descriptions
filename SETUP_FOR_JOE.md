# 🚀 Setup Guide for Joe - AI Product Descriptions

## Quick Start Instructions

### 1. Clone and Switch to the Fixed Branch
```bash
git clone https://github.com/Joseph-Nawar/Ai_Product_Descriptions.git
cd Ai_Product_Descriptions
git checkout joe-will-fix-isa-forlaunching
```

### 2. Backend Setup (Choose One Method)

#### Method A: Minimal Setup (Recommended)
```powershell
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install minimal requirements
pip install -r requirements_minimal.txt

# Start server
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

#### Method B: Use the Startup Script
```powershell
.\start_backend_minimal.ps1
```

### 3. Frontend Setup
```powershell
# In a new terminal, navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 4. Access the Application
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## What's Fixed

✅ **CORS Issues** - Frontend can now communicate with backend
✅ **Server Stability** - Backend no longer crashes on startup
✅ **Database** - Switched to SQLite (no external database needed)
✅ **API Endpoints** - All frontend-backend API calls now work
✅ **Frontend Errors** - Fixed runtime crashes in components
✅ **Dependencies** - Robust error handling for missing packages

## Troubleshooting

### If Backend Won't Start
1. Try the minimal setup method
2. Check if port 8000 is available
3. Run `.\test_server_start.ps1` to diagnose issues

### If Frontend Won't Start
1. Make sure you're in the frontend directory
2. Run `npm install` to ensure all dependencies are installed
3. Check if port 5173 is available

### If You Get CORS Errors
- Make sure backend is running on port 8000
- Check that CORS origins include your frontend URL

## Features Working

- ✅ User authentication
- ✅ Product description generation
- ✅ Payment system integration
- ✅ Credit management
- ✅ Usage tracking
- ✅ Real-time updates via WebSocket
- ✅ Multi-language support

## Need Help?

Check the `FIXES_SUMMARY.md` file for detailed information about all the fixes applied.

---
**Note**: The application is now production-ready with all major issues resolved!
