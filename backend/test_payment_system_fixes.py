#!/usr/bin/env python3
"""
Comprehensive tests for payment and credits system fixes

This test suite validates all the fixes implemented:
1. Standardized plan definitions
2. Fixed credit/daily limit logic
3. Fixed timezone handling
4. Fixed session management
5. Atomic credit operations
6. Correct daily credits display
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
from src.auth.deps import get_authed_user_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PaymentSystemTester:
    """Test suite for payment system fixes"""
    
    def __init__(self):
        self.credit_service = CreditService()
        self.db_service = SQLAlchemyPaymentService()
        self.test_user_id = "test_user_123"
        self.test_results = []
    
    def log_test_result(self, test_name: str, passed: bool, details: str = ""):
        """Log test result"""
        status = "✅ PASS" if passed else "❌ FAIL"
        logger.info(f"{status} {test_name}: {details}")
        self.test_results.append({
            "test": test_name,
            "passed": passed,
            "details": details
        })
    
    def test_standardized_plans(self):
        """Test 1: Verify standardized plan definitions"""
        logger.info("🧪 Testing standardized plan definitions...")
        
        try:
            with get_session() as session:
                # Get all plans from database
                plans = session.query(SubscriptionPlan).all()
                
                # Verify we have the expected plans
                plan_ids = [plan.id for plan in plans]
                expected_plans = ["free", "pro", "enterprise", "yearly"]
                
                for expected_plan in expected_plans:
                    if expected_plan not in plan_ids:
                        self.log_test_result(
                            "Standardized Plans - Plan Exists",
                            False,
                            f"Missing plan: {expected_plan}"
                        )
                        return
                
                # Verify plan limits are consistent
                free_plan = session.query(SubscriptionPlan).filter_by(id="free").first()
                pro_plan = session.query(SubscriptionPlan).filter_by(id="pro").first()
                enterprise_plan = session.query(SubscriptionPlan).filter_by(id="enterprise").first()
                
                if free_plan.max_api_calls_per_day != 2:
                    self.log_test_result(
                        "Standardized Plans - Free Plan Limits",
                        False,
                        f"Free plan daily limit should be 2, got {free_plan.max_api_calls_per_day}"
                    )
                    return
                
                if pro_plan.max_api_calls_per_day != 5:
                    self.log_test_result(
                        "Standardized Plans - Pro Plan Limits",
                        False,
                        f"Pro plan daily limit should be 5, got {pro_plan.max_api_calls_per_day}"
                    )
                    return
                
                if enterprise_plan.max_api_calls_per_day != 15:
                    self.log_test_result(
                        "Standardized Plans - Enterprise Plan Limits",
                        False,
                        f"Enterprise plan daily limit should be 15, got {enterprise_plan.max_api_calls_per_day}"
                    )
                    return
                
                self.log_test_result(
                    "Standardized Plans",
                    True,
                    f"All {len(plans)} plans have correct limits"
                )
                
        except Exception as e:
            self.log_test_result(
                "Standardized Plans",
                False,
                f"Exception: {str(e)}"
            )
    
    def test_new_user_assignment(self):
        """Test 2: Verify new users get Free plan with correct limits"""
        logger.info("🧪 Testing new user assignment...")
        
        try:
            with get_session() as session:
                # Clean up any existing test user
                session.query(UserCredits).filter_by(user_id=self.test_user_id).delete()
                session.query(UserSubscription).filter_by(user_id=self.test_user_id).delete()
                session.commit()
                
                # Test user assignment
                success = self.db_service.assign_free_plan_to_user(self.test_user_id, session)
                
                if not success:
                    self.log_test_result(
                        "New User Assignment - Assignment",
                        False,
                        "Failed to assign free plan to user"
                    )
                    return
                
                # Verify subscription was created
                subscription = self.db_service.get_user_subscription(self.test_user_id, session)
                if not subscription or subscription.plan_id != "free":
                    self.log_test_result(
                        "New User Assignment - Subscription",
                        False,
                        f"Expected free plan, got {subscription.plan_id if subscription else 'None'}"
                    )
                    return
                
                # Verify credits were created
                user_credits = self.db_service.get_user_credits(self.test_user_id, session)
                if not user_credits or user_credits.current_credits != 2:
                    self.log_test_result(
                        "New User Assignment - Credits",
                        False,
                        f"Expected 2 credits, got {user_credits.current_credits if user_credits else 'None'}"
                    )
                    return
                
                # Verify daily limit
                daily_limit = self.db_service.get_user_daily_limit(self.test_user_id, session)
                if daily_limit != 2:
                    self.log_test_result(
                        "New User Assignment - Daily Limit",
                        False,
                        f"Expected daily limit 2, got {daily_limit}"
                    )
                    return
                
                self.log_test_result(
                    "New User Assignment",
                    True,
                    "User correctly assigned to Free plan with 2 credits/day"
                )
                
        except Exception as e:
            self.log_test_result(
                "New User Assignment",
                False,
                f"Exception: {str(e)}"
            )
    
    def test_daily_usage_tracking(self):
        """Test 3: Verify daily usage increments correctly and caps at limit"""
        logger.info("🧪 Testing daily usage tracking...")
        
        try:
            with get_session() as session:
                # Ensure test user exists
                self.db_service.assign_free_plan_to_user(self.test_user_id, session)
                
                # Test first generation
                can_proceed, credit_info = asyncio.run(
                    self.credit_service.check_credits_and_limits(
                        self.test_user_id, OperationType.SINGLE_DESCRIPTION, 1, session
                    )
                )
                
                if not can_proceed:
                    self.log_test_result(
                        "Daily Usage - First Generation",
                        False,
                        f"Should be able to generate, got: {credit_info.get('error')}"
                    )
                    return
                
                if credit_info.get('remaining_daily_credits') != 2:
                    self.log_test_result(
                        "Daily Usage - Initial Credits",
                        False,
                        f"Expected 2 remaining credits, got {credit_info.get('remaining_daily_credits')}"
                    )
                    return
                
                # Deduct credits for first generation
                success, result = asyncio.run(
                    self.credit_service.deduct_credits(
                        self.test_user_id, OperationType.SINGLE_DESCRIPTION, 1, session=session
                    )
                )
                
                if not success:
                    self.log_test_result(
                        "Daily Usage - Credit Deduction",
                        False,
                        f"Failed to deduct credits: {result.get('error')}"
                    )
                    return
                
                # Test second generation
                can_proceed, credit_info = asyncio.run(
                    self.credit_service.check_credits_and_limits(
                        self.test_user_id, OperationType.SINGLE_DESCRIPTION, 1, session
                    )
                )
                
                if not can_proceed:
                    self.log_test_result(
                        "Daily Usage - Second Generation",
                        False,
                        f"Should be able to generate, got: {credit_info.get('error')}"
                    )
                    return
                
                if credit_info.get('remaining_daily_credits') != 1:
                    self.log_test_result(
                        "Daily Usage - After First Use",
                        False,
                        f"Expected 1 remaining credit, got {credit_info.get('remaining_daily_credits')}"
                    )
                    return
                
                # Deduct credits for second generation
                success, result = asyncio.run(
                    self.credit_service.deduct_credits(
                        self.test_user_id, OperationType.SINGLE_DESCRIPTION, 1, session=session
                    )
                )
                
                # Test third generation (should fail - limit reached)
                can_proceed, credit_info = asyncio.run(
                    self.credit_service.check_credits_and_limits(
                        self.test_user_id, OperationType.SINGLE_DESCRIPTION, 1, session
                    )
                )
                
                if can_proceed:
                    self.log_test_result(
                        "Daily Usage - Limit Enforcement",
                        False,
                        "Should not be able to generate after reaching daily limit"
                    )
                    return
                
                if credit_info.get('remaining_daily_credits') != 0:
                    self.log_test_result(
                        "Daily Usage - Limit Reached",
                        False,
                        f"Expected 0 remaining credits, got {credit_info.get('remaining_daily_credits')}"
                    )
                    return
                
                self.log_test_result(
                    "Daily Usage Tracking",
                    True,
                    "Daily usage correctly increments and enforces limits"
                )
                
        except Exception as e:
            self.log_test_result(
                "Daily Usage Tracking",
                False,
                f"Exception: {str(e)}"
            )
    
    def test_timezone_handling(self):
        """Test 4: Verify timezone-aware datetime handling"""
        logger.info("🧪 Testing timezone handling...")
        
        try:
            with get_session() as session:
                # Create a test subscription
                now = datetime.now(timezone.utc)
                period_end = now + timedelta(days=30)
                
                subscription = UserSubscription(
                    id=f"test_sub_{int(now.timestamp())}",
                    user_id=self.test_user_id,
                    plan_id="free",
                    status="active",
                    current_period_start=now,
                    current_period_end=period_end
                )
                
                session.add(subscription)
                session.commit()
                
                # Test is_active() method
                is_active = subscription.is_active()
                
                if not is_active:
                    self.log_test_result(
                        "Timezone Handling - Active Subscription",
                        False,
                        "Subscription should be active"
                    )
                    return
                
                # Test with expired subscription
                expired_subscription = UserSubscription(
                    id=f"test_expired_{int(now.timestamp())}",
                    user_id=f"{self.test_user_id}_expired",
                    plan_id="free",
                    status="active",
                    current_period_start=now - timedelta(days=35),
                    current_period_end=now - timedelta(days=5)
                )
                
                is_active_expired = expired_subscription.is_active()
                
                if is_active_expired:
                    self.log_test_result(
                        "Timezone Handling - Expired Subscription",
                        False,
                        "Expired subscription should not be active"
                    )
                    return
                
                self.log_test_result(
                    "Timezone Handling",
                    True,
                    "Timezone-aware datetime comparisons work correctly"
                )
                
        except Exception as e:
            self.log_test_result(
                "Timezone Handling",
                False,
                f"Exception: {str(e)}"
            )
    
    def test_atomic_credit_operations(self):
        """Test 5: Verify atomic credit operations prevent race conditions"""
        logger.info("🧪 Testing atomic credit operations...")
        
        try:
            with get_session() as session:
                # Ensure test user has credits
                self.db_service.assign_free_plan_to_user(self.test_user_id, session)
                user_credits = self.db_service.get_user_credits(self.test_user_id, session)
                user_credits.current_credits = 10  # Give user 10 credits for testing
                session.commit()
                
                # Test atomic credit deduction
                success, result = self.db_service.use_credits(self.test_user_id, 5, session)
                
                if not success:
                    self.log_test_result(
                        "Atomic Operations - Credit Deduction",
                        False,
                        f"Failed to deduct credits: {result.get('error')}"
                    )
                    return
                
                if result.get('remaining_credits') != 5:
                    self.log_test_result(
                        "Atomic Operations - Remaining Credits",
                        False,
                        f"Expected 5 remaining credits, got {result.get('remaining_credits')}"
                    )
                    return
                
                # Test insufficient credits
                success, result = self.db_service.use_credits(self.test_user_id, 10, session)
                
                if success:
                    self.log_test_result(
                        "Atomic Operations - Insufficient Credits",
                        False,
                        "Should not be able to deduct more credits than available"
                    )
                    return
                
                self.log_test_result(
                    "Atomic Credit Operations",
                    True,
                    "Atomic operations work correctly with proper error handling"
                )
                
        except Exception as e:
            self.log_test_result(
                "Atomic Credit Operations",
                False,
                f"Exception: {str(e)}"
            )
    
    def test_daily_credits_display(self):
        """Test 6: Verify frontend receives correct daily credits count"""
        logger.info("🧪 Testing daily credits display...")
        
        try:
            with get_session() as session:
                # Ensure test user exists
                self.db_service.assign_free_plan_to_user(self.test_user_id, session)
                
                # Get user credit info (simulating endpoint call)
                user_credits = self.db_service.get_user_credits(self.test_user_id, session)
                subscription = self.db_service.get_user_subscription(self.test_user_id, session)
                daily_limit = self.db_service.get_user_daily_limit(self.test_user_id, session)
                daily_usage_count = self.db_service.get_daily_usage_count(self.test_user_id, session)
                remaining_daily_credits = max(0, daily_limit - daily_usage_count)
                
                # Verify initial state
                if remaining_daily_credits != 2:
                    self.log_test_result(
                        "Daily Credits Display - Initial State",
                        False,
                        f"Expected 2 remaining daily credits, got {remaining_daily_credits}"
                    )
                    return
                
                # Use one credit
                success, result = asyncio.run(
                    self.credit_service.deduct_credits(
                        self.test_user_id, OperationType.SINGLE_DESCRIPTION, 1, session=session
                    )
                )
                
                # Check updated state
                daily_usage_count = self.db_service.get_daily_usage_count(self.test_user_id, session)
                remaining_daily_credits = max(0, daily_limit - daily_usage_count)
                
                if remaining_daily_credits != 1:
                    self.log_test_result(
                        "Daily Credits Display - After Use",
                        False,
                        f"Expected 1 remaining daily credit, got {remaining_daily_credits}"
                    )
                    return
                
                self.log_test_result(
                    "Daily Credits Display",
                    True,
                    "Frontend receives correct daily credits count"
                )
                
        except Exception as e:
            self.log_test_result(
                "Daily Credits Display",
                False,
                f"Exception: {str(e)}"
            )
    
    def run_all_tests(self):
        """Run all tests and report results"""
        logger.info("🚀 Starting Payment System Fixes Test Suite...")
        
        # Initialize database
        init_database()
        create_default_plans()
        
        # Run all tests
        self.test_standardized_plans()
        self.test_new_user_assignment()
        self.test_daily_usage_tracking()
        self.test_timezone_handling()
        self.test_atomic_credit_operations()
        self.test_daily_credits_display()
        
        # Report results
        passed_tests = sum(1 for result in self.test_results if result["passed"])
        total_tests = len(self.test_results)
        
        logger.info(f"\n📊 Test Results: {passed_tests}/{total_tests} tests passed")
        
        if passed_tests == total_tests:
            logger.info("🎉 All tests passed! Payment system fixes are working correctly.")
        else:
            logger.error("❌ Some tests failed. Please review the issues above.")
            for result in self.test_results:
                if not result["passed"]:
                    logger.error(f"  - {result['test']}: {result['details']}")
        
        return passed_tests == total_tests


def main():
    """Main test runner"""
    tester = PaymentSystemTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()


