# AI Product Descriptions - Setup Instructions

## Issues Fixed

The connection error you were experiencing has been resolved. Here are the issues that were found and fixed:

### 1. **Port Mismatch** ✅ FIXED
- **Problem**: Frontend was trying to connect to port `8001`, but backend runs on port `8000`
- **Solution**: Updated `frontend/src/api/client.ts` to use port `8000`

### 2. **Missing Dependencies** ✅ FIXED
- **Problem**: Backend was missing FastAPI and uvicorn dependencies
- **Solution**: Added `fastapi>=0.104.0` and `uvicorn>=0.24.0` to `backend/requirements.txt`

### 3. **API Endpoint Mismatch** ✅ FIXED
- **Problem**: Frontend was calling `/generate` but backend had `/api/generate-batch`
- **Solution**: Updated frontend to call `/api/generate-batch` and added JSON array support

### 4. **Missing Environment Files** ✅ FIXED
- **Problem**: No `.env` files existed to configure the connection
- **Solution**: Created PowerShell scripts that will create the necessary `.env` files

## How to Run the Application

### Option 1: Use the PowerShell Scripts (Recommended)

1. **Start the Backend Server**:
   ```powershell
   .\start_backend.ps1
   ```
   This script will:
   - Create a virtual environment
   - Install dependencies
   - Create a `.env` file
   - Start the server on `http://localhost:8000`

2. **Start the Frontend Server** (in a new terminal):
   ```powershell
   .\start_frontend.ps1
   ```
   This script will:
   - Install npm dependencies
   - Create a `.env` file
   - Start the development server on `http://localhost:5173`

### Option 2: Manual Setup

#### Backend Setup:
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Create .env file with your API key
echo "GEMINI_API_KEY=your_api_key_here" > .env
echo "DRY_RUN=true" >> .env

# Start server
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup:
```powershell
cd frontend
npm install

# Create .env file
echo "VITE_API_BASE_URL=http://localhost:8000" > .env
echo "VITE_USE_MOCK=false" >> .env

# Start development server
npm run dev
```

## Configuration

### Backend Configuration (backend/.env):
```env
GEMINI_API_KEY=your_gemini_api_key_here
DRY_RUN=true
GEMINI_MODEL=gemini-1.5-flash
TEMPERATURE=0.2
```

### Frontend Configuration (frontend/.env):
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_USE_MOCK=false
```

## API Endpoints

The backend now provides these endpoints:

- `GET /api/health` - Health check
- `POST /api/generate-description` - Generate single description
- `POST /api/generate-batch` - Generate descriptions from JSON array
- `POST /api/generate-batch-csv` - Generate descriptions from CSV file
- `GET /api/usage-stats` - Get usage statistics
- `GET /batch/{batch_id}` - Fetch batch by ID (placeholder)
- `GET /download/{batch_id}` - Download batch as ZIP (placeholder)

## Testing the Fix

1. Start both servers using the PowerShell scripts
2. Open `http://localhost:5173` in your browser
3. Upload a CSV file or add products manually
4. Click "Generate Description" - it should now work without connection errors

## Troubleshooting

If you still get connection errors:

1. **Check if backend is running**: Visit `http://localhost:8000/api/health`
2. **Check if frontend is running**: Visit `http://localhost:5173`
3. **Check the browser console** for any error messages
4. **Verify the .env files** were created correctly

## Next Steps

1. **Get a Gemini API Key**: Sign up at [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Update the .env file**: Replace `your_gemini_api_key_here` with your actual API key
3. **Set DRY_RUN=false**: Once you have a real API key, set this to `false` to enable actual AI generation

The application should now work correctly without the connection refused error!



