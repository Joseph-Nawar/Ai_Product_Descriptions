#!/usr/bin/env python3
"""
Emergency test script to verify backend startup after endpoints.py fix
"""

import sys
import os
from pathlib import Path

# Add the backend src directory to the path
backend_src = Path(__file__).parent / "src"
sys.path.insert(0, str(backend_src))

def test_imports():
    """Test that all critical imports work"""
    print("🧪 Testing Critical Imports...")
    print("=" * 40)
    
    try:
        # Test 1: Import the router
        print("1. Testing router import...")
        from src.payments.endpoints import router
        print("   ✅ Router imported successfully")
        print(f"   📋 Router prefix: {router.prefix}")
        print(f"   📋 Router tags: {router.tags}")
        
        # Test 2: Import main app
        print("\n2. Testing main app import...")
        from src.main import app
        print("   ✅ Main app imported successfully")
        
        # Test 3: Check if router is included in app
        print("\n3. Testing router inclusion...")
        routes = [route.path for route in app.routes]
        payment_routes = [route for route in routes if "/api/payment" in route]
        print(f"   📋 Found {len(payment_routes)} payment routes:")
        for route in payment_routes[:5]:  # Show first 5
            print(f"      - {route}")
        
        return True
        
    except ImportError as e:
        print(f"   ❌ Import failed: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
        return False

def test_router_endpoints():
    """Test that router has the expected endpoints"""
    print("\n🔧 Testing Router Endpoints...")
    print("=" * 40)
    
    try:
        from src.payments.endpoints import router
        
        # Get all routes from the router
        routes = []
        for route in router.routes:
            if hasattr(route, 'path') and hasattr(route, 'methods'):
                routes.append({
                    'path': route.path,
                    'methods': list(route.methods)
                })
        
        print(f"📋 Found {len(routes)} routes in payment router:")
        
        expected_routes = [
            "/plans",
            "/checkout", 
            "/webhook",
            "/user/credits",
            "/health"
        ]
        
        for route_info in routes:
            path = route_info['path']
            methods = route_info['methods']
            print(f"   ✅ {methods} {path}")
        
        # Check for critical endpoints
        critical_endpoints = ["/checkout", "/plans"]
        missing_endpoints = []
        
        for endpoint in critical_endpoints:
            found = any(endpoint in route['path'] for route in routes)
            if found:
                print(f"   ✅ Critical endpoint {endpoint} found")
            else:
                print(f"   ❌ Critical endpoint {endpoint} MISSING")
                missing_endpoints.append(endpoint)
        
        return len(missing_endpoints) == 0
        
    except Exception as e:
        print(f"   ❌ Error testing endpoints: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 EMERGENCY BACKEND STARTUP TEST")
    print("=" * 50)
    print("Testing if the endpoints.py fix resolved the ImportError")
    print()
    
    # Test 1: Imports
    imports_ok = test_imports()
    
    # Test 2: Router endpoints
    endpoints_ok = test_router_endpoints()
    
    # Summary
    print(f"\n📊 Test Results Summary")
    print("=" * 30)
    print(f"Imports:     {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"Endpoints:   {'✅ PASS' if endpoints_ok else '❌ FAIL'}")
    
    if imports_ok and endpoints_ok:
        print(f"\n🎉 BACKEND STARTUP TEST PASSED!")
        print(f"The endpoints.py file has been successfully restored.")
        print(f"You should now be able to start the backend with:")
        print(f"   cd backend")
        print(f"   python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000")
    else:
        print(f"\n⚠️  BACKEND STARTUP TEST FAILED!")
        print(f"Please check the errors above and fix them before starting the backend.")

if __name__ == "__main__":
    main()
