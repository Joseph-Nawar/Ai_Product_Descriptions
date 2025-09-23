#!/usr/bin/env python3
"""
Test suite for backend fixes

This test suite validates the two critical fixes:
1. SQLAlchemy Session misuse in queries
2. Missing DB injection in endpoints
"""

import asyncio
import logging
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add backend directory to path
BACKEND_DIR = Path(__file__).parent
sys.path.insert(0, str(BACKEND_DIR))

from src.database.connection import get_session, init_database
from src.database.init_db import create_default_plans
from src.models.payment_models import SubscriptionPlan, UserCredits, UserSubscription, UsageLog
from src.payments.credit_service import CreditService, OperationType
from src.payments.sqlalchemy_service import SQLAlchemyPaymentService
from src.payments.lemon_squeezy import LemonSqueezyService
from src.payments.secure_operations import SecurePaymentOperations

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestBackendFixes:
    """Test suite for backend fixes"""
    
    def __init__(self):
        self.db_service = SQLAlchemyPaymentService()
        self.credit_service = CreditService()
        self.lemon_squeezy = LemonSqueezyService()
        self.secure_ops = SecurePaymentOperations()
        self.test_user_id = "test_user_123"
        self.test_email = "test@example.com"
        
    async def setup_test_data(self):
        """Set up test data"""
        logger.info("Setting up test data...")
        
        # Initialize database
        init_database()
        
        # Create default plans
        create_default_plans()
        
        logger.info("Test data setup complete")
    
    def test_1_session_parameter_order(self):
        """Test 1: SQLAlchemy Session parameter order fixes"""
        logger.info("Testing SQLAlchemy Session parameter order fixes...")
        
        try:
            with get_session() as session:
                # Test get_user_credits with correct parameter order
                user_credits = self.db_service.get_user_credits(self.test_user_id, session)
                logger.info("✅ get_user_credits with correct parameter order works")
                
                # Test lemon_squeezy.get_user_credits with correct parameter order
                user_credits_ls = asyncio.run(self.lemon_squeezy.get_user_credits(self.test_user_id, session))
                logger.info("✅ lemon_squeezy.get_user_credits with correct parameter order works")
                
                # Test secure_operations._get_user_credits with correct parameter order
                user_credits_so = asyncio.run(self.secure_ops._get_user_credits(self.test_user_id, session))
                logger.info("✅ secure_operations._get_user_credits with correct parameter order works")
                
            return True
            
        except Exception as e:
            logger.error(f"❌ Session parameter order test failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def test_2_db_session_injection(self):
        """Test 2: DB session injection in endpoints"""
        logger.info("Testing DB session injection in endpoints...")
        
        try:
            with get_session() as session:
                # Test that all credit service methods work with session parameter
                can_proceed, credit_info = asyncio.run(
                    self.credit_service.check_credits_and_limits(
                        self.test_user_id, 
                        OperationType.SINGLE_DESCRIPTION, 
                        1, 
                        session=session
                    )
                )
                logger.info(f"✅ check_credits_and_limits with session works: {can_proceed}")
                
                # Test deduct_credits with session parameter
                deduct_success, deduct_result = asyncio.run(
                    self.credit_service.deduct_credits(
                        self.test_user_id,
                        OperationType.SINGLE_DESCRIPTION,
                        1,
                        session=session
                    )
                )
                logger.info(f"✅ deduct_credits with session works: {deduct_success}")
                
                # Test check_and_refresh_credits with session parameter
                refresh_success = asyncio.run(
                    self.credit_service.check_and_refresh_credits(self.test_user_id, session)
                )
                logger.info(f"✅ check_and_refresh_credits with session works: {refresh_success}")
                
            return True
            
        except Exception as e:
            logger.error(f"❌ DB session injection test failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def test_3_user_credits_flow(self):
        """Test 3: Complete user credits flow"""
        logger.info("Testing complete user credits flow...")
        
        try:
            with get_session() as session:
                # Test new user gets free plan
                success = self.db_service.assign_free_plan_to_user(self.test_user_id, session)
                logger.info(f"✅ New user assigned free plan: {success}")
                
                # Test get user credits
                user_credits = self.db_service.get_user_credits(self.test_user_id, session)
                logger.info(f"✅ User credits retrieved: {user_credits.current_credits if user_credits else 0}")
                
                # Test get user subscription
                subscription = self.db_service.get_user_subscription(self.test_user_id, session)
                logger.info(f"✅ User subscription retrieved: {subscription.plan_id if subscription else 'None'}")
                
                # Test daily limit
                daily_limit = self.db_service.get_user_daily_limit(self.test_user_id, session)
                logger.info(f"✅ Daily limit retrieved: {daily_limit}")
                
                # Test daily usage count
                daily_usage = self.db_service.get_daily_usage_count(self.test_user_id, session)
                logger.info(f"✅ Daily usage count retrieved: {daily_usage}")
                
            return True
            
        except Exception as e:
            logger.error(f"❌ User credits flow test failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def test_4_credit_operations(self):
        """Test 4: Credit operations with proper session handling"""
        logger.info("Testing credit operations with proper session handling...")
        
        try:
            with get_session() as session:
                # Test use_credits atomic operation
                success, result = self.db_service.use_credits(self.test_user_id, 1, session)
                logger.info(f"✅ use_credits atomic operation works: {success}")
                
                # Test add_credits
                add_success = self.db_service.add_credits(session, self.test_user_id, 5, "test")
                logger.info(f"✅ add_credits works: {add_success}")
                
                # Test update_user_credits
                if user_credits := self.db_service.get_user_credits(self.test_user_id, session):
                    update_success = self.db_service.update_user_credits(session, user_credits)
                    logger.info(f"✅ update_user_credits works: {update_success}")
                
            return True
            
        except Exception as e:
            logger.error(f"❌ Credit operations test failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def test_5_endpoint_simulation(self):
        """Test 5: Simulate endpoint calls with proper DB injection"""
        logger.info("Testing endpoint simulation with proper DB injection...")
        
        try:
            with get_session() as session:
                # Simulate generate_description endpoint flow
                user_id = self.test_user_id
                
                # Check and refresh credits
                refresh_success = asyncio.run(
                    self.credit_service.check_and_refresh_credits(user_id, session)
                )
                logger.info(f"✅ Credit refresh simulation works: {refresh_success}")
                
                # Check credits and limits
                can_proceed, credit_info = asyncio.run(
                    self.credit_service.check_credits_and_limits(
                        user_id, 
                        OperationType.SINGLE_DESCRIPTION, 
                        1, 
                        session=session
                    )
                )
                logger.info(f"✅ Credit check simulation works: {can_proceed}")
                
                if can_proceed:
                    # Deduct credits
                    deduct_success, deduct_result = asyncio.run(
                        self.credit_service.deduct_credits(
                            user_id,
                            OperationType.SINGLE_DESCRIPTION,
                            1,
                            session=session
                        )
                    )
                    logger.info(f"✅ Credit deduction simulation works: {deduct_success}")
                
            return True
            
        except Exception as e:
            logger.error(f"❌ Endpoint simulation test failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    async def run_all_tests(self):
        """Run all tests"""
        logger.info("🚀 Starting backend fixes test suite...")
        
        # Setup
        await self.setup_test_data()
        
        # Run tests
        tests = [
            ("Session Parameter Order", self.test_1_session_parameter_order),
            ("DB Session Injection", self.test_2_db_session_injection),
            ("User Credits Flow", self.test_3_user_credits_flow),
            ("Credit Operations", self.test_4_credit_operations),
            ("Endpoint Simulation", self.test_5_endpoint_simulation),
        ]
        
        results = []
        for test_name, test_func in tests:
            logger.info(f"\n{'='*50}")
            logger.info(f"Running: {test_name}")
            logger.info(f"{'='*50}")
            
            try:
                if asyncio.iscoroutinefunction(test_func):
                    result = await test_func()
                else:
                    result = test_func()
                results.append((test_name, result))
                
                if result:
                    logger.info(f"✅ {test_name}: PASSED")
                else:
                    logger.error(f"❌ {test_name}: FAILED")
                    
            except Exception as e:
                logger.error(f"❌ {test_name}: ERROR - {str(e)}")
                results.append((test_name, False))
        
        # Summary
        logger.info(f"\n{'='*50}")
        logger.info("TEST SUMMARY")
        logger.info(f"{'='*50}")
        
        passed = sum(1 for _, result in results if result)
        total = len(results)
        
        for test_name, result in results:
            status = "✅ PASSED" if result else "❌ FAILED"
            logger.info(f"{test_name}: {status}")
        
        logger.info(f"\nOverall: {passed}/{total} tests passed")
        
        if passed == total:
            logger.info("🎉 All tests passed! Backend fixes are working correctly.")
        else:
            logger.error("⚠️ Some tests failed. Please review the issues above.")
        
        return passed == total

def main():
    """Main test runner"""
    test_suite = TestBackendFixes()
    
    try:
        success = asyncio.run(test_suite.run_all_tests())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        logger.info("Test suite interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Test suite failed with error: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()


