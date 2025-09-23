#!/usr/bin/env python3
"""
Test script to verify the Lemon Squeezy parameter mismatch fix
"""

import asyncio
import os
import sys
import json
from pathlib import Path

# Add the backend src directory to the path
backend_src = Path(__file__).parent / "src"
sys.path.insert(0, str(backend_src))

from payments.lemon_squeezy import LemonSqueezyService

async def test_checkout_session_creation():
    """Test the create_checkout_session method with variant_id parameter"""
    
    print("🧪 Testing Lemon Squeezy Parameter Mismatch Fix")
    print("=" * 50)
    
    # Initialize the service
    try:
        service = LemonSqueezyService()
        print("✅ LemonSqueezyService initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize LemonSqueezyService: {e}")
        return False
    
    # Test data
    test_user_id = "test_user_123"
    test_email = "test@example.com"
    test_variant_id = "1009476"  # Pro plan variant ID from .env
    test_success_url = "https://app.com/success"
    test_cancel_url = "https://app.com/cancel"
    
    print(f"\n📋 Test Parameters:")
    print(f"   User ID: {test_user_id}")
    print(f"   Email: {test_email}")
    print(f"   Variant ID: {test_variant_id}")
    print(f"   Success URL: {test_success_url}")
    print(f"   Cancel URL: {test_cancel_url}")
    
    # Test the method signature
    try:
        print(f"\n🔧 Testing method signature...")
        
        # This should work with the new variant_id parameter
        result = await service.create_checkout_session(
            user_id=test_user_id,
            user_email=test_email,
            variant_id=test_variant_id,  # ✅ Using variant_id directly
            success_url=test_success_url,
            cancel_url=test_cancel_url
        )
        
        print("✅ Method signature test passed")
        print(f"📊 Result: {json.dumps(result, indent=2)}")
        
        if result.get("success") and result.get("checkout_url"):
            print("🎉 SUCCESS: Checkout session created successfully!")
            print(f"🔗 Checkout URL: {result['checkout_url']}")
            return True
        else:
            print("⚠️  Checkout session created but no URL returned")
            return False
            
    except ValueError as e:
        if "Invalid variant ID format" in str(e):
            print(f"❌ Variant ID validation failed: {e}")
            return False
        else:
            print(f"❌ Validation error: {e}")
            return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

async def test_environment_configuration():
    """Test that all required environment variables are set"""
    
    print(f"\n🔧 Testing Environment Configuration")
    print("=" * 50)
    
    required_vars = [
        "LEMON_SQUEEZY_API_KEY",
        "LEMON_SQUEEZY_STORE_ID", 
        "LEMON_SQUEEZY_VARIANT_ID_PRO",
        "LEMON_SQUEEZY_VARIANT_ID_ENTERPRISE",
        "LEMON_SQUEEZY_VARIANT_ID_YEARLY"
    ]
    
    all_present = True
    
    for var in required_vars:
        value = os.getenv(var)
        if value:
            # Mask sensitive values
            if "API_KEY" in var:
                display_value = f"{value[:10]}..." if len(value) > 10 else "***"
            else:
                display_value = value
            print(f"✅ {var}: {display_value}")
        else:
            print(f"❌ {var}: NOT SET")
            all_present = False
    
    return all_present

async def main():
    """Main test function"""
    
    print("🚀 Lemon Squeezy Parameter Mismatch Fix - Test Suite")
    print("=" * 60)
    
    # Test 1: Environment Configuration
    env_ok = await test_environment_configuration()
    
    if not env_ok:
        print("\n❌ Environment configuration test failed")
        print("Please ensure all required environment variables are set in .env")
        return
    
    # Test 2: Checkout Session Creation
    checkout_ok = await test_checkout_session_creation()
    
    # Summary
    print(f"\n📊 Test Results Summary")
    print("=" * 30)
    print(f"Environment Config: {'✅ PASS' if env_ok else '❌ FAIL'}")
    print(f"Checkout Creation:  {'✅ PASS' if checkout_ok else '❌ FAIL'}")
    
    if env_ok and checkout_ok:
        print(f"\n🎉 ALL TESTS PASSED!")
        print(f"The parameter mismatch fix is working correctly.")
        print(f"You should no longer see 'Missing required field: amount' errors.")
    else:
        print(f"\n⚠️  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    asyncio.run(main())
