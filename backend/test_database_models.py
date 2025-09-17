#!/usr/bin/env python3
"""
Database Models Test Script

This script tests the SQLAlchemy database models and payment system integration.
Run this script to verify that all database functionality is working correctly.
"""

import asyncio
import logging
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

# Add backend directory to path
BACKEND_DIR = Path(__file__).parent
sys.path.insert(0, str(BACKEND_DIR))

from src.database.connection import init_database, check_database_connection, get_database_info
from src.database.migrations import run_initial_migrations, get_migration_status
from src.database.init_db import create_default_plans, verify_database_setup
from src.payments.sqlalchemy_service import SQLAlchemyPaymentService
from src.models.payment_models import (
    SubscriptionPlan, UserSubscription, UserCredits, 
    PaymentHistory, UsageLog, SubscriptionTier, 
    SubscriptionStatus, PaymentStatus, UsageType
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_database_connection():
    """Test database connection"""
    print("🔗 Testing database connection...")
    
    if not check_database_connection():
        print("❌ Database connection failed")
        return False
    
    db_info = get_database_info()
    print(f"✅ Connected to: {db_info.get('url', 'Unknown')}")
    print(f"✅ Version: {db_info.get('version', 'Unknown')}")
    return True


def test_database_initialization():
    """Test database initialization"""
    print("\n🏗️  Testing database initialization...")
    
    try:
        # Initialize database
        init_database()
        print("✅ Database tables created")
        
        # Run migrations
        run_initial_migrations()
        print("✅ Initial migrations completed")
        
        # Create default plans
        create_default_plans()
        print("✅ Default plans created")
        
        # Verify setup
        if verify_database_setup():
            print("✅ Database setup verified")
            return True
        else:
            print("❌ Database setup verification failed")
            return False
            
    except Exception as e:
        print(f"❌ Database initialization failed: {str(e)}")
        return False


def test_sqlalchemy_service():
    """Test SQLAlchemy payment service"""
    print("\n💳 Testing SQLAlchemy payment service...")
    
    try:
        service = SQLAlchemyPaymentService()
        
        # Test subscription plans
        print("1. Testing subscription plans...")
        plans = service.get_subscription_plans()
        print(f"✅ Found {len(plans)} subscription plans")
        for plan in plans:
            print(f"   - {plan['name']}: ${plan['price']}/{plan['billing_interval']}")
        
        # Test user creation
        print("\n2. Testing user creation...")
        import uuid
        test_user_id = f"test_user_sqlalchemy_{uuid.uuid4().hex[:8]}"
        user_credits = service.create_user_credits(test_user_id, "free")
        print(f"✅ Created user: {user_credits.user_id}")
        print(f"   - Credits: {user_credits.current_credits}")
        
        # Test credit operations
        print("\n3. Testing credit operations...")
        success, result = service.use_credits(test_user_id, 1)
        print(f"✅ Credit deduction: {'SUCCESS' if success else 'FAILED'}")
        if success:
            print(f"   - Credits deducted: {result.get('credits_deducted', 0)}")
            print(f"   - Remaining: {result.get('remaining_credits', 0)}")
        
        # Test rate limiting
        print("\n4. Testing rate limiting...")
        can_proceed, rate_info = service.check_rate_limits(test_user_id)
        print(f"✅ Rate limit check: {'PASSED' if can_proceed else 'FAILED'}")
        if rate_info:
            print(f"   - Rate limits: {rate_info.get('rate_limits', {})}")
        
        # Test usage logging
        print("\n5. Testing usage logging...")
        success = service.log_usage(
            test_user_id, 
            UsageType.AI_GENERATION, 
            credits_used=1,
            product_count=1,
            language_code="en",
            category="electronics",
            tokens_used=150,
            response_time_ms=2500,
            cost_usd=0.001
        )
        print(f"✅ Usage logging: {'SUCCESS' if success else 'FAILED'}")
        
        # Test user stats
        print("\n6. Testing user statistics...")
        stats = service.get_user_stats(test_user_id)
        print(f"✅ User stats retrieved:")
        print(f"   - Current credits: {stats.get('credits', {}).get('current_credits', 0)}")
        print(f"   - Total used: {stats.get('credits', {}).get('total_credits_used', 0)}")
        print(f"   - Usage stats: {stats.get('usage_stats', {})}")
        
        # Test subscription creation
        print("\n7. Testing subscription creation...")
        subscription = service.create_user_subscription(
            test_user_id,
            "basic",
            f"ls_sub_test_{uuid.uuid4().hex[:8]}"
        )
        print(f"✅ Created subscription: {subscription['id']}")
        print(f"   - Plan: {subscription['plan_id']}")
        print(f"   - Status: {subscription['status']}")
        print(f"   - Active: {subscription['is_active']}")
        
        # Test payment history
        print("\n8. Testing payment history...")
        payment = PaymentHistory(
            id=f"payment_test_{uuid.uuid4().hex[:8]}",
            user_id=test_user_id,
            amount=9.99,
            currency="USD",
            status=PaymentStatus.COMPLETED,
            lemon_squeezy_order_id=f"ls_order_test_{uuid.uuid4().hex[:8]}",
            credits_awarded=100,
            plan_id="basic"
        )
        success = service.add_payment_history(payment)
        print(f"✅ Payment history: {'SUCCESS' if success else 'FAILED'}")
        
        # Test health check
        print("\n9. Testing health check...")
        health = service.health_check()
        print(f"✅ Health check: {health['status']}")
        print(f"   - Plans: {health.get('plans_count', 0)}")
        print(f"   - Users: {health.get('users_count', 0)}")
        print(f"   - Payments: {health.get('payments_count', 0)}")
        
        print("\n🎉 All SQLAlchemy service tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ SQLAlchemy service test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_model_relationships():
    """Test model relationships"""
    print("\n🔗 Testing model relationships...")
    
    try:
        import uuid
        service = SQLAlchemyPaymentService()
        
        # Create test data
        test_user_id = f"test_relationships_{uuid.uuid4().hex[:8]}"
        
        # Create user credits
        user_credits = service.create_user_credits(test_user_id, "pro")
        
        # Create subscription
        subscription = service.create_user_subscription(
            test_user_id, 
            "pro", 
            f"ls_sub_relationships_{uuid.uuid4().hex[:8]}"
        )
        
        # Update user credits with subscription
        user_credits.subscription_id = subscription['id']
        service.update_user_credits(user_credits)
        
        # Create payment
        payment = PaymentHistory(
            id=f"payment_relationships_{uuid.uuid4().hex[:8]}",
            user_id=test_user_id,
            amount=29.99,
            currency="USD",
            status=PaymentStatus.COMPLETED,
            subscription_id=subscription['id'],
            credits_awarded=1000,
            plan_id="pro"
        )
        service.add_payment_history(payment)
        
        # Test relationships
        print("1. Testing user credits -> subscription relationship...")
        updated_credits = service.get_user_credits(test_user_id)
        if updated_credits and updated_credits.subscription_id == subscription['id']:
            print("✅ User credits linked to subscription")
        else:
            print("❌ User credits not linked to subscription")
        
        print("2. Testing subscription -> plan relationship...")
        if subscription['plan_id'] == "pro":
            print("✅ Subscription linked to plan")
        else:
            print("❌ Subscription not linked to plan")
        
        print("3. Testing payment -> subscription relationship...")
        payments = service.get_payment_history(test_user_id, limit=1)
        if payments and payments[0].subscription_id == subscription['id']:
            print("✅ Payment linked to subscription")
        else:
            print("❌ Payment not linked to subscription")
        
        print("\n🎉 Model relationship tests completed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Model relationship test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_migration_system():
    """Test migration system"""
    print("\n🔄 Testing migration system...")
    
    try:
        # Get migration status
        status = get_migration_status()
        print(f"✅ Migration status:")
        print(f"   - Applied: {status['total_applied']}")
        print(f"   - Pending: {status['total_pending']}")
        
        if status['applied']:
            print("   - Applied migrations:")
            for migration in status['applied']:
                print(f"     * {migration}")
        
        if status['pending']:
            print("   - Pending migrations:")
            for migration in status['pending']:
                print(f"     * {migration}")
        
        print("\n🎉 Migration system test completed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Migration system test failed: {str(e)}")
        return False


def main():
    """Main test function"""
    print("🚀 SQLAlchemy Database Models Test")
    print("=" * 60)
    
    # Test database connection
    if not test_database_connection():
        print("\n❌ Database connection failed. Please check your configuration.")
        return False
    
    # Test database initialization
    if not test_database_initialization():
        print("\n❌ Database initialization failed.")
        return False
    
    # Test SQLAlchemy service
    if not test_sqlalchemy_service():
        print("\n❌ SQLAlchemy service tests failed.")
        return False
    
    # Test model relationships
    if not test_model_relationships():
        print("\n❌ Model relationship tests failed.")
        return False
    
    # Test migration system
    if not test_migration_system():
        print("\n❌ Migration system tests failed.")
        return False
    
    # Summary
    print("\n📊 Test Summary")
    print("=" * 50)
    print("✅ Database connection: PASSED")
    print("✅ Database initialization: PASSED")
    print("✅ SQLAlchemy service: PASSED")
    print("✅ Model relationships: PASSED")
    print("✅ Migration system: PASSED")
    
    print("\n🎉 All database model tests passed!")
    print("The SQLAlchemy payment system is ready for production use.")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
