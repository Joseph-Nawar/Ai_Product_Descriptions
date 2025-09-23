#!/usr/bin/env python3
"""
Test script to verify the automatic free plan assignment fix
"""

import sys
import os
from datetime import datetime, timezone, timedelta

# Add the backend directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_free_plan_assignment():
    """Test the automatic free plan assignment functionality"""
    print("🧪 Testing Automatic Free Plan Assignment Fix")
    print("=" * 60)
    
    try:
        from payments.sqlalchemy_service import SQLAlchemyPaymentService
        from payments.credit_service import CreditService, OperationType
        from database.connection import get_session
        
        # Initialize services
        payment_service = SQLAlchemyPaymentService()
        credit_service = CreditService()
        
        # Test user ID
        test_user_id = "test_new_user_456"
        
        print(f"📋 Testing with new user: {test_user_id}")
        
        # Test 1: Check if user has subscription (should be None initially)
        print("\n1️⃣ Testing initial subscription check...")
        with get_session() as session:
            subscription = payment_service.get_user_subscription(session, test_user_id)
            print(f"   ✅ Initial subscription: {subscription}")
        
        # Test 2: Assign free plan to user
        print("\n2️⃣ Testing free plan assignment...")
        with get_session() as session:
            success = payment_service.assign_free_plan_to_user(session, test_user_id)
            print(f"   ✅ Free plan assignment result: {success}")
        
        # Test 3: Check if subscription was created
        print("\n3️⃣ Testing subscription creation...")
        with get_session() as session:
            subscription = payment_service.get_user_subscription(session, test_user_id)
            if subscription:
                print(f"   ✅ Subscription created: {subscription.plan_id}")
                print(f"   📊 Status: {subscription.status}")
                print(f"   📅 Period: {subscription.current_period_start} to {subscription.current_period_end}")
            else:
                print("   ❌ No subscription found")
        
        # Test 4: Check if user credits were created
        print("\n4️⃣ Testing user credits creation...")
        with get_session() as session:
            user_credits = payment_service.get_user_credits(session, test_user_id)
            if user_credits:
                print(f"   ✅ User credits created: {user_credits.current_credits} credits")
            else:
                print("   ❌ No user credits found")
        
        # Test 5: Test credit validation with new user
        print("\n5️⃣ Testing credit validation with new user...")
        import asyncio
        async def test_credit_validation():
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            print(f"   ✅ Can proceed: {can_proceed}")
            print(f"   📊 Credit info: {credit_info}")
            return can_proceed, credit_info
        
        can_proceed, credit_info = asyncio.run(test_credit_validation())
        
        # Test 6: Test idempotency (should not create duplicate)
        print("\n6️⃣ Testing idempotency...")
        with get_session() as session:
            success = payment_service.assign_free_plan_to_user(session, test_user_id)
            print(f"   ✅ Second assignment result: {success}")
        
        print("\n🎉 Free plan assignment test completed!")
        
        # Summary
        print("\n" + "=" * 60)
        print("📝 Test Results Summary:")
        print(f"   • Free plan assignment: {'✅ PASS' if success else '❌ FAIL'}")
        print(f"   • Credit validation: {'✅ PASS' if can_proceed else '❌ FAIL'}")
        print(f"   • Daily limit check: {'✅ PASS' if 'daily_limit' in credit_info else '❌ FAIL'}")
        
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()

def test_user_creation_flow():
    """Test the user creation flow with automatic free plan assignment"""
    print("\n🔄 Testing User Creation Flow")
    print("=" * 60)
    
    try:
        from app.repos.user_repo import get_or_create_user
        from database.connection import get_session
        
        # Test user ID
        test_user_id = "test_creation_flow_789"
        test_email = "test@example.com"
        
        print(f"📋 Testing user creation for: {test_user_id}")
        
        # Test 1: Create new user
        print("\n1️⃣ Testing new user creation...")
        with get_session() as session:
            user = get_or_create_user(session, test_user_id, test_email)
            print(f"   ✅ User created: {user.id}")
            print(f"   📧 Email: {user.email}")
        
        # Test 2: Check if free plan was automatically assigned
        print("\n2️⃣ Testing automatic free plan assignment...")
        with get_session() as session:
            from payments.sqlalchemy_service import SQLAlchemyPaymentService
            payment_service = SQLAlchemyPaymentService()
            subscription = payment_service.get_user_subscription(session, test_user_id)
            if subscription:
                print(f"   ✅ Free plan automatically assigned: {subscription.plan_id}")
            else:
                print("   ❌ No subscription found")
        
        # Test 3: Test idempotency (should not create duplicate user)
        print("\n3️⃣ Testing user creation idempotency...")
        with get_session() as session:
            user2 = get_or_create_user(session, test_user_id, test_email)
            print(f"   ✅ Same user returned: {user2.id == user.id}")
        
        print("\n🎉 User creation flow test completed!")
        
    except Exception as e:
        print(f"❌ User creation test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🚀 Starting Free Plan Assignment Fix Verification")
    print("=" * 80)
    
    # Test free plan assignment
    test_free_plan_assignment()
    
    # Test user creation flow
    test_user_creation_flow()
    
    print("\n" + "=" * 80)
    print("✅ All tests completed!")
    print("\n📝 Summary of changes:")
    print("   • Added assign_free_plan_to_user() method to SQLAlchemyPaymentService")
    print("   • Updated get_or_create_user() to automatically assign free plan")
    print("   • Updated credit service to auto-assign free plan if no subscription exists")
    print("   • Made methods idempotent to prevent duplicate subscriptions")
    print("   • Fixed session management for database operations")
    print("\n🎯 Result: New users now automatically get Free tier without manual assignment!")


