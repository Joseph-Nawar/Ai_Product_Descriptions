#!/usr/bin/env python3
"""
Minimal test to verify the router import works without environment dependencies
"""

import sys
from pathlib import Path

# Add the backend src directory to the path
backend_src = Path(__file__).parent / "src"
sys.path.insert(0, str(backend_src))

def test_router_import():
    """Test that the router can be imported without environment dependencies"""
    print("🧪 Testing Router Import (Minimal Test)...")
    print("=" * 50)
    
    try:
        # Test 1: Import the router directly
        print("1. Testing direct router import...")
        from src.payments.endpoints import router
        print("   ✅ Router imported successfully")
        print(f"   📋 Router prefix: {router.prefix}")
        print(f"   📋 Router tags: {router.tags}")
        
        # Test 2: Check router routes
        print("\n2. Testing router routes...")
        routes = []
        for route in router.routes:
            if hasattr(route, 'path') and hasattr(route, 'methods'):
                routes.append({
                    'path': route.path,
                    'methods': list(route.methods)
                })
        
        print(f"   📋 Found {len(routes)} routes:")
        for route_info in routes:
            path = route_info['path']
            methods = route_info['methods']
            print(f"      ✅ {methods} {path}")
        
        # Test 3: Check for critical endpoints
        print("\n3. Testing critical endpoints...")
        critical_endpoints = ["/checkout", "/plans", "/webhook", "/health"]
        missing_endpoints = []
        
        for endpoint in critical_endpoints:
            found = any(endpoint in route['path'] for route in routes)
            if found:
                print(f"   ✅ Critical endpoint {endpoint} found")
            else:
                print(f"   ❌ Critical endpoint {endpoint} MISSING")
                missing_endpoints.append(endpoint)
        
        return len(missing_endpoints) == 0
        
    except ImportError as e:
        print(f"   ❌ Import failed: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 MINIMAL ROUTER IMPORT TEST")
    print("=" * 50)
    print("Testing if the endpoints.py router can be imported")
    print("(This test doesn't require environment variables)")
    print()
    
    # Test router import
    router_ok = test_router_import()
    
    # Summary
    print(f"\n📊 Test Results Summary")
    print("=" * 30)
    print(f"Router Import: {'✅ PASS' if router_ok else '❌ FAIL'}")
    
    if router_ok:
        print(f"\n🎉 ROUTER IMPORT TEST PASSED!")
        print(f"The endpoints.py file has been successfully restored.")
        print(f"The router can be imported without ImportError.")
        print(f"\nNext steps:")
        print(f"1. Set up environment variables in .env file")
        print(f"2. Start the backend with: python -m uvicorn src.main:app --reload")
    else:
        print(f"\n⚠️  ROUTER IMPORT TEST FAILED!")
        print(f"The endpoints.py file still has issues.")

if __name__ == "__main__":
    main()
