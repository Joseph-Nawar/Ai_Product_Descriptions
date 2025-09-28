#!/usr/bin/env python3
"""
Test script to verify the credits endpoint is working
"""
import requests
import json
import sys
import os

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_credits_endpoint():
    """Test the credits endpoint without authentication"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing credits endpoint...")
    
    # Test the endpoint without auth (should return 401)
    try:
        response = requests.get(f"{base_url}/api/payment/user/credits")
        print(f"📊 Status Code: {response.status_code}")
        print(f"📊 Response: {response.text}")
        
        if response.status_code == 401:
            print("✅ Endpoint is working - correctly returns 401 for unauthenticated requests")
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend. Is it running?")
        return False
    except Exception as e:
        print(f"❌ Error testing endpoint: {str(e)}")
        return False
    
    return True

def test_health_endpoint():
    """Test the health endpoint"""
    base_url = "http://localhost:8000"
    
    print("\n🧪 Testing health endpoint...")
    
    try:
        response = requests.get(f"{base_url}/api/health")
        print(f"📊 Status Code: {response.status_code}")
        print(f"📊 Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ Health endpoint is working")
            return True
        else:
            print(f"❌ Health endpoint returned status: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend. Is it running?")
        return False
    except Exception as e:
        print(f"❌ Error testing health endpoint: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Starting backend endpoint tests...")
    
    health_ok = test_health_endpoint()
    credits_ok = test_credits_endpoint()
    
    if health_ok and credits_ok:
        print("\n✅ All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)
