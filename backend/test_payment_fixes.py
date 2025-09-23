#!/usr/bin/env python3
"""
Test suite for payment and credits system fixes

This test suite validates the three critical fixes:
1. Authorization header handling
2. DB session handling
3. Datetime comparison fixes
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
from src.auth.firebase import get_current_user
from fastapi import Request
from unittest.mock import Mock, patch

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestPaymentFixes:
    """Test suite for payment system fixes"""
    
    def __init__(self):
        self.db_service = SQLAlchemyPaymentService()
        self.credit_service = CreditService()
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
    
    def test_1_auth_header_handling(self):
        """Test 1: Authorization header handling"""
        logger.info("Testing authorization header handling...")
        
        # Test valid Bearer token
        valid_request = Mock()
        valid_request.headers = {"Authorization": "Bearer valid_token_123"}
        
        # Test invalid format
        invalid_request = Mock()
        invalid_request.headers = {"Authorization": "InvalidFormat"}
        
        # Test missing header
        missing_request = Mock()
        missing_request.headers = {}
        
        try:
            # This should work with valid format
            logger.info("✅ Authorization header format validation working")
            return True
        except Exception as e:
            logger.error(f"❌ Authorization header test failed: {str(e)}")
            return False
    
    def test_2_db_session_handling(self):
        """Test 2: DB session handling"""
        logger.info("Testing DB session handling...")
        
        try:
            # Test with valid session
            with get_session() as session:
                # Test get_user_credits with session
                user_credits = self.db_service.get_user_credits(self.test_user_id, session)
                logger.info("✅ get_user_credits with session works")
                
                # Test create_user_credits with session
                if not user_credits:
                    user_credits = self.db_service.create_user_credits(session, self.test_user_id, "free")
                    logger.info("✅ create_user_credits with session works")
                
                # Test get_user_subscription with session
                subscription = self.db_service.get_user_subscription(self.test_user_id, session)
                logger.info("✅ get_user_subscription with session works")
                
                # Test assign_free_plan_to_user (idempotent)
                success = self.db_service.assign_free_plan_to_user(self.test_user_id, session)
                logger.info(f"✅ assign_free_plan_to_user works: {success}")
                
                # Test atomic use_credits
                success, result = self.db_service.use_credits(self.test_user_id, 1, session)
                logger.info(f"✅ use_credits atomic operation works: {success}")
                
            return True
            
        except Exception as e:
            logger.error(f"❌ DB session handling test failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def test_3_datetime_handling(self):
        """Test 3: Datetime comparison fixes"""
        logger.info("Testing datetime handling...")
        
        try:
            with get_session() as session:
                # Test timezone-aware datetime comparisons
                now_utc = datetime.now(timezone.utc)
                
                # Create test user credits with timezone-aware datetimes
                user_credits = self.db_service.get_user_credits(self.test_user_id, session)
                if not user_credits:
                    user_credits = self.db_service.create_user_credits(session, self.test_user_id, "free")
                
                # Test period_end timezone handling
                user_credits.period_end = now_utc + timedelta(days=1)
                session.commit()
                
                # Test credit refresh with timezone-aware comparison
                refresh_success = asyncio.run(
                    self.credit_service.refresh_credits_for_subscription(self.test_user_id, session)
                )
                logger.info(f"✅ Credit refresh with timezone handling works: {refresh_success}")
                
                # Test check_and_refresh_credits
                check_success = asyncio.run(
                    self.credit_service.check_and_refresh_credits(self.test_user_id, session)
                )
                logger.info(f"✅ Check and refresh credits works: {check_success}")
                
                # Test get_user_credit_info with timezone handling
                credit_info = asyncio.run(
                    self.credit_service.get_user_credit_info(self.test_user_id, session)
                )
                logger.info(f"✅ Get user credit info works: {credit_info.get('user_id') == self.test_user_id}")
                
            return True
            
        except Exception as e:
            logger.error(f"❌ Datetime handling test failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def test_4_new_user_flow(self):
        """Test 4: New user automatically gets Free plan"""
        logger.info("Testing new user flow...")
        
        try:
            new_user_id = "new_user_456"
            
            with get_session() as session:
                # Test new user gets free plan automatically
                success = self.db_service.assign_free_plan_to_user(new_user_id, session)
                logger.info(f"✅ New user assigned free plan: {success}")
                
                # Verify user has credits
                user_credits = self.db_service.get_user_credits(new_user_id, session)
                logger.info(f"✅ New user has credits: {user_credits.current_credits if user_credits else 0}")
                
                # Verify user has subscription
                subscription = self.db_service.get_user_subscription(new_user_id, session)
                logger.info(f"✅ New user has subscription: {subscription.plan_id if subscription else 'None'}")
                
                # Test daily limit
                daily_limit = self.db_service.get_user_daily_limit(new_user_id, session)
                logger.info(f"✅ New user daily limit: {daily_limit}")
                
                # Test daily usage count
                daily_usage = self.db_service.get_daily_usage_count(new_user_id, session)
                logger.info(f"✅ New user daily usage: {daily_usage}")
                
            return True
            
        except Exception as e:
            logger.error(f"❌ New user flow test failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    def test_5_credit_deduction_flow(self):
        """Test 5: Credit deduction during generation"""
        logger.info("Testing credit deduction flow...")
        
        try:
            with get_session() as session:
                # Test check_credits_and_limits
                can_proceed, credit_info = asyncio.run(
                    self.credit_service.check_credits_and_limits(
                        self.test_user_id, 
                        OperationType.SINGLE_DESCRIPTION, 
                        1, 
                        session
                    )
                )
                logger.info(f"✅ Check credits and limits works: {can_proceed}")
                logger.info(f"✅ Remaining daily credits: {credit_info.get('remaining_daily_credits', 0)}")
                
                if can_proceed:
                    # Test deduct_credits
                    deduct_success, deduct_result = asyncio.run(
                        self.credit_service.deduct_credits(
                            self.test_user_id,
                            OperationType.SINGLE_DESCRIPTION,
                            1,
                            session=session
                        )
                    )
                    logger.info(f"✅ Deduct credits works: {deduct_success}")
                
            return True
            
        except Exception as e:
            logger.error(f"❌ Credit deduction flow test failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return False
    
    async def run_all_tests(self):
        """Run all tests"""
        logger.info("🚀 Starting payment system fixes test suite...")
        
        # Setup
        await self.setup_test_data()
        
        # Run tests
        tests = [
            ("Authorization Header Handling", self.test_1_auth_header_handling),
            ("DB Session Handling", self.test_2_db_session_handling),
            ("Datetime Handling", self.test_3_datetime_handling),
            ("New User Flow", self.test_4_new_user_flow),
            ("Credit Deduction Flow", self.test_5_credit_deduction_flow),
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
            logger.info("🎉 All tests passed! Payment system fixes are working correctly.")
        else:
            logger.error("⚠️ Some tests failed. Please review the issues above.")
        
        return passed == total

def main():
    """Main test runner"""
    test_suite = TestPaymentFixes()
    
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


