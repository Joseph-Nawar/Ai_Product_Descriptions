#!/usr/bin/env python3
"""
Simple test script to verify backend functionality
"""
import sys
import os
from pathlib import Path

# Add backend directory to path
BACKEND_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BACKEND_DIR))

try:
    from src.main import app
    print("✅ Backend imports successful!")
    print("✅ FastAPI app created successfully!")
    
    # Test if we can access the app
    print(f"✅ App title: {app.title}")
    print(f"✅ App version: {app.version}")
    
    # List available routes
    routes = []
    for route in app.routes:
        if hasattr(route, 'path') and hasattr(route, 'methods'):
            routes.append(f"{route.methods} {route.path}")
    
    print(f"✅ Available routes:")
    for route in routes:
        print(f"   {route}")
    
    print("\n🎉 Backend is ready to run!")
    print("To start the server, run:")
    print("   python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()



