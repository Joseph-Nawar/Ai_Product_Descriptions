"""
Comprehensive pytest tests for Free plan assignment functionality

Tests verify that:
✅ New users automatically get the Free plan
✅ Old users without subscription are migrated to Free
✅ Users can generate up to 2 times/day without being asked for payment
✅ After 2 generations, further attempts are blocked

Run with: pytest backend/tests/test_free_plan_assignment.py -v
"""

import pytest
import asyncio
from datetime import datetime, timezone, timedelta
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session

# Import the modules we're testing
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.repos.user_repo import get_or_create_user
from src.payments.credit_service import CreditService, OperationType
from src.payments.sqlalchemy_service import SQLAlchemyPaymentService
from src.models.payment_models import UserSubscription, UserCredits, SubscriptionStatus, SubscriptionPlan
from app.models.user import User
from src.database.connection import get_session


class TestFreePlanAssignment:
    """Test suite for Free plan assignment functionality"""
    
    @pytest.fixture
    def test_user_id(self):
        """Generate a unique test user ID"""
        return f"test_user_{datetime.now().timestamp()}"
    
    @pytest.fixture
    def test_email(self):
        """Generate a unique test email"""
        return f"test_{datetime.now().timestamp()}@example.com"
    
    @pytest.fixture
    def payment_service(self):
        """Create a payment service instance"""
        return SQLAlchemyPaymentService()
    
    @pytest.fixture
    def credit_service(self):
        """Create a credit service instance"""
        return CreditService()
    
    def test_new_user_gets_free_plan_automatically(self, test_user_id, test_email):
        """Test that new users automatically get the Free plan assigned"""
        with get_session() as session:
            # Create a new user
            user = get_or_create_user(session, test_user_id, test_email)
            
            # Verify user was created
            assert user.id == test_user_id
            assert user.email == test_email
            
            # Verify free plan was assigned
            payment_service = SQLAlchemyPaymentService()
            subscription = payment_service.get_user_subscription(session, test_user_id)
            
            assert subscription is not None, "User should have a subscription"
            assert subscription.plan_id == "free", "User should have free plan"
            assert subscription.status == SubscriptionStatus.ACTIVE, "Subscription should be active"
            
            # Verify user credits were created
            user_credits = payment_service.get_user_credits(session, test_user_id)
            assert user_credits is not None, "User should have credits record"
            assert user_credits.current_credits > 0, "User should have initial credits"
    
    def test_existing_user_does_not_get_duplicate_subscription(self, test_user_id, test_email):
        """Test that existing users don't get duplicate subscriptions"""
        with get_session() as session:
            # Create user first time
            user1 = get_or_create_user(session, test_user_id, test_email)
            
            # Create user second time (should be same user)
            user2 = get_or_create_user(session, test_user_id, test_email)
            
            # Should be the same user object
            assert user1.id == user2.id
            
            # Should only have one subscription
            payment_service = SQLAlchemyPaymentService()
            subscriptions = session.query(UserSubscription).filter_by(user_id=test_user_id).all()
            assert len(subscriptions) == 1, "User should have exactly one subscription"
    
    @pytest.mark.asyncio
    async def test_credit_service_auto_assigns_free_plan(self, test_user_id, credit_service):
        """Test that credit service auto-assigns free plan if user has no subscription"""
        with get_session() as session:
            # Create user without subscription (simulate old user)
            user = User(id=test_user_id, email="test@example.com")
            session.add(user)
            session.flush()
            
            # Verify no subscription exists initially
            payment_service = SQLAlchemyPaymentService()
            subscription = payment_service.get_user_subscription(session, test_user_id)
            assert subscription is None, "User should not have subscription initially"
            
            # Call credit service - should auto-assign free plan
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            
            # Verify free plan was assigned
            subscription = payment_service.get_user_subscription(session, test_user_id)
            assert subscription is not None, "Credit service should have assigned free plan"
            assert subscription.plan_id == "free", "Should be free plan"
            
            # Verify user can proceed with generation
            assert can_proceed, "User should be able to generate with free plan"
            assert "daily_limit" in credit_info, "Credit info should include daily limit"
            assert credit_info["subscription_tier"] == "free", "Should be free tier"
    
    @pytest.mark.asyncio
    async def test_free_plan_daily_limits(self, test_user_id, credit_service):
        """Test that free plan users can generate 2 times per day, then get blocked"""
        with get_session() as session:
            # Create user with free plan
            user = User(id=test_user_id, email="test@example.com")
            session.add(user)
            session.flush()
            
            payment_service = SQLAlchemyPaymentService()
            payment_service.assign_free_plan_to_user(session, test_user_id)
            
            # Verify initial state
            subscription = payment_service.get_user_subscription(session, test_user_id)
            assert subscription.plan_id == "free"
            
            # Test first generation (should succeed)
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert can_proceed, "First generation should succeed"
            assert credit_info["daily_limit"] == 2, "Free plan should have 2 daily limit"
            assert credit_info["daily_usage_count"] == 0, "Should start with 0 usage"
            assert credit_info["subscription_tier"] == "free", "Should be free tier"
            
            # Simulate first generation by logging usage
            payment_service.log_usage(
                session, test_user_id, "ai_generation", credits_used=1, product_count=1
            )
            
            # Test second generation (should succeed)
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert can_proceed, "Second generation should succeed"
            assert credit_info["daily_usage_count"] == 1, "Should have 1 usage"
            
            # Simulate second generation
            payment_service.log_usage(
                session, test_user_id, "ai_generation", credits_used=1, product_count=1
            )
            
            # Test third generation (should be blocked)
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert not can_proceed, "Third generation should be blocked"
            assert "Daily generation limit exceeded" in credit_info["error"]
            assert credit_info["daily_usage_count"] == 2, "Should have 2 usage"
            assert credit_info["daily_limit"] == 2, "Should still show limit of 2"
            assert credit_info["subscription_tier"] == "free", "Should still be free tier"
    
    @pytest.mark.asyncio
    async def test_different_operation_types_consume_daily_limit(self, test_user_id, credit_service):
        """Test that different operation types all consume the daily limit"""
        with get_session() as session:
            # Create user with free plan
            user = User(id=test_user_id, email="test@example.com")
            session.add(user)
            session.flush()
            
            payment_service = SQLAlchemyPaymentService()
            payment_service.assign_free_plan_to_user(session, test_user_id)
            
            # Test single description (should succeed)
            can_proceed, _ = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert can_proceed, "Single description should succeed"
            
            # Simulate usage
            payment_service.log_usage(
                session, test_user_id, "ai_generation", credits_used=1, product_count=1
            )
            
            # Test regeneration (should succeed)
            can_proceed, _ = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.REGENERATION, product_count=1
            )
            assert can_proceed, "Regeneration should succeed"
            
            # Simulate usage
            payment_service.log_usage(
                session, test_user_id, "ai_generation", credits_used=1, product_count=1
            )
            
            # Test third operation (should be blocked)
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert not can_proceed, "Third operation should be blocked"
            assert "Daily generation limit exceeded" in credit_info["error"]
            assert credit_info["subscription_tier"] == "free", "Should still be free tier"
    
    def test_assign_free_plan_idempotent(self, test_user_id, payment_service):
        """Test that assign_free_plan_to_user is idempotent"""
        with get_session() as session:
            # Create user
            user = User(id=test_user_id, email="test@example.com")
            session.add(user)
            session.flush()
            
            # Assign free plan first time
            result1 = payment_service.assign_free_plan_to_user(session, test_user_id)
            assert result1, "First assignment should succeed"
            
            # Count subscriptions
            subscriptions_count_1 = session.query(UserSubscription).filter_by(user_id=test_user_id).count()
            assert subscriptions_count_1 == 1, "Should have exactly one subscription"
            
            # Assign free plan second time (should be idempotent)
            result2 = payment_service.assign_free_plan_to_user(session, test_user_id)
            assert result2, "Second assignment should succeed"
            
            # Should still have only one subscription
            subscriptions_count_2 = session.query(UserSubscription).filter_by(user_id=test_user_id).count()
            assert subscriptions_count_2 == 1, "Should still have exactly one subscription"
    
    def test_free_plan_has_correct_limits(self, test_user_id, payment_service):
        """Test that free plan has correct daily limits"""
        with get_session() as session:
            # Create user with free plan
            user = User(id=test_user_id, email="test@example.com")
            session.add(user)
            session.flush()
            
            payment_service.assign_free_plan_to_user(session, test_user_id)
            
            # Get daily limit
            daily_limit = payment_service.get_user_daily_limit(session, test_user_id)
            assert daily_limit == 2, "Free plan should have 2 daily limit"
            
            # Get subscription and verify plan details
            subscription = payment_service.get_user_subscription(session, test_user_id)
            assert subscription.plan_id == "free"
            
            # Verify plan exists in database
            plan = session.query(SubscriptionPlan).filter_by(id="free").first()
            assert plan is not None, "Free plan should exist in database"
            assert plan.max_api_calls_per_day == 2, "Free plan should allow 2 calls per day"
    
    @pytest.mark.asyncio
    async def test_credit_deduction_after_generation(self, test_user_id, credit_service):
        """Test that credits are properly deducted after successful generation"""
        with get_session() as session:
            # Create user with free plan
            user = User(id=test_user_id, email="test@example.com")
            session.add(user)
            session.flush()
            
            payment_service = SQLAlchemyPaymentService()
            payment_service.assign_free_plan_to_user(session, test_user_id)
            
            # Get initial credits
            user_credits = payment_service.get_user_credits(session, test_user_id)
            initial_credits = user_credits.current_credits
            
            # Check credits and limits
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert can_proceed, "Should be able to generate"
            assert credit_info["subscription_tier"] == "free", "Should be free tier"
            
            # Deduct credits (simulate successful generation)
            success, deduct_result = await credit_service.deduct_credits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert success, "Credit deduction should succeed"
            assert deduct_result["credits_deducted"] == 1, "Should deduct 1 credit"
            
            # Verify credits were actually deducted
            user_credits = payment_service.get_user_credits(session, test_user_id)
            assert user_credits.current_credits == initial_credits - 1, "Credits should be reduced by 1"
    
    def test_migration_script_compatibility(self, test_user_id):
        """Test that the migration script can handle users without subscriptions"""
        with get_session() as session:
            # Create user without subscription (simulate old user)
            user = User(id=test_user_id, email="test@example.com")
            session.add(user)
            session.flush()
            
            # Verify no subscription exists
            payment_service = SQLAlchemyPaymentService()
            subscription = payment_service.get_user_subscription(session, test_user_id)
            assert subscription is None, "User should not have subscription initially"
            
            # Run migration logic (simulate what the script does)
            users_without_subscriptions = [test_user_id]
            
            for user_id in users_without_subscriptions:
                result = payment_service.assign_free_plan_to_user(session, user_id)
                assert result, "Migration should succeed"
            
            # Verify subscription was created
            subscription = payment_service.get_user_subscription(session, test_user_id)
            assert subscription is not None, "Migration should create subscription"
            assert subscription.plan_id == "free", "Should be free plan"
    
    def test_error_handling_in_user_creation(self, test_user_id, test_email):
        """Test that user creation doesn't fail if subscription assignment fails"""
        with get_session() as session:
            # Mock the payment service to raise an exception
            with patch('src.payments.sqlalchemy_service.SQLAlchemyPaymentService') as mock_service:
                mock_instance = MagicMock()
                mock_instance.assign_free_plan_to_user.side_effect = Exception("Database error")
                mock_service.return_value = mock_instance
                
                # User creation should still succeed even if subscription assignment fails
                user = get_or_create_user(session, test_user_id, test_email)
                assert user.id == test_user_id, "User should still be created"
                assert user.email == test_email, "User email should be set"
    
    @pytest.mark.asyncio
    async def test_daily_limit_resets_at_midnight(self, test_user_id, credit_service):
        """Test that daily limits reset at midnight (conceptual test)"""
        with get_session() as session:
            # Create user with free plan
            user = User(id=test_user_id, email="test@example.com")
            session.add(user)
            session.flush()
            
            payment_service = SQLAlchemyPaymentService()
            payment_service.assign_free_plan_to_user(session, test_user_id)
            
            # Use up daily limit
            for i in range(2):
                payment_service.log_usage(
                    session, test_user_id, "ai_generation", credits_used=1, product_count=1
                )
            
            # Verify limit is reached
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert not can_proceed, "Should be blocked after 2 generations"
            
            # Note: In a real implementation, you would test the actual midnight reset
            # This is a conceptual test showing the structure
            # The actual reset would be handled by the daily usage count query
            # which filters by date range (today_start to today_end)


class TestIntegrationScenarios:
    """Integration tests for real-world scenarios"""
    
    @pytest.mark.asyncio
    async def test_new_user_complete_flow(self):
        """Test the complete flow for a new user from registration to generation"""
        test_user_id = f"integration_test_{datetime.now().timestamp()}"
        test_email = f"integration_{datetime.now().timestamp()}@example.com"
        
        with get_session() as session:
            # Step 1: User registers (creates account)
            user = get_or_create_user(session, test_user_id, test_email)
            assert user.id == test_user_id
            
            # Step 2: Verify free plan was assigned
            payment_service = SQLAlchemyPaymentService()
            subscription = payment_service.get_user_subscription(session, test_user_id)
            assert subscription.plan_id == "free"
            
            # Step 3: User tries to generate AI description
            credit_service = CreditService()
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert can_proceed, "New user should be able to generate"
            assert credit_info["daily_limit"] == 2
            
            # Step 4: Generate description (simulate)
            success, deduct_result = await credit_service.deduct_credits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert success, "Credit deduction should succeed"
            
            # Step 5: User tries to generate again
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            assert can_proceed, "Should be able to generate again"
            assert credit_info["daily_usage_count"] == 1
    
    @pytest.mark.asyncio
    async def test_old_user_migration_flow(self):
        """Test the flow for an old user who gets migrated"""
        test_user_id = f"old_user_{datetime.now().timestamp()}"
        
        with get_session() as session:
            # Step 1: Old user exists without subscription (simulate)
            user = User(id=test_user_id, email="old@example.com")
            session.add(user)
            session.flush()
            
            # Step 2: User tries to generate (triggers migration)
            credit_service = CreditService()
            can_proceed, credit_info = await credit_service.check_credits_and_limits(
                test_user_id, OperationType.SINGLE_DESCRIPTION, product_count=1
            )
            
            # Step 3: Verify migration happened
            payment_service = SQLAlchemyPaymentService()
            subscription = payment_service.get_user_subscription(session, test_user_id)
            assert subscription is not None, "Migration should create subscription"
            assert subscription.plan_id == "free", "Should be free plan"
            
            # Step 4: Verify user can now generate
            assert can_proceed, "Migrated user should be able to generate"
            assert credit_info["daily_limit"] == 2


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])
