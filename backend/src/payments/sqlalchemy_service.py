# backend/src/payments/sqlalchemy_service.py
"""
SQLAlchemy-based payment service implementation

This module provides database operations using SQLAlchemy models
for the payment system.
"""

import logging
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional, List, Tuple
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_, or_, desc

# Removed get_session import - sessions will be passed as parameters
from ..models.payment_models import (
    SubscriptionPlan, UserSubscription, UserCredits, 
    PaymentHistory, UsageLog, SubscriptionTier, 
    SubscriptionStatus, PaymentStatus, UsageType
)

logger = logging.getLogger(__name__)


class SQLAlchemyPaymentService:
    """SQLAlchemy-based payment service"""
    
    def __init__(self):
        self.logger = logger
    
    def _ensure_session(self, session: Session = None) -> Tuple[Session, bool]:
        """
        Private helper to ensure a valid session exists.
        Returns (session, created) where created=True if it created a new session.
        """
        if session is not None and hasattr(session, 'query'):
            return session, False
        
        # Create a new session if none provided
        from src.database.connection import get_session_factory
        SessionLocal = get_session_factory()
        new_session = SessionLocal()
        return new_session, True
    
    def get_subscription_plans(self, session: Session) -> List[Dict[str, Any]]:
        """Get all active subscription plans"""
        plans = session.query(SubscriptionPlan).filter(
            SubscriptionPlan.is_active == True
        ).order_by(SubscriptionPlan.sort_order).all()
        
        return [plan.to_dict() for plan in plans]
    
    def get_subscription_plan(self, session: Session, plan_id: str) -> Optional[SubscriptionPlan]:
        """Get a specific subscription plan"""
        plan = session.query(SubscriptionPlan).filter_by(id=plan_id).first()
        if plan:
            session.expunge(plan)
        return plan
    
    def get_user_credits(self, user_id: str, session: Session = None) -> Optional[UserCredits]:
        """Get user credits"""
        session, created = self._ensure_session(session)
        
        try:
            user_credits = session.query(UserCredits).options(joinedload(UserCredits.subscription)).filter_by(user_id=user_id).first()
            if user_credits:
                session.expunge(user_credits)
            return user_credits
        finally:
            if created:
                session.close()
    
    def create_user_credits(self, session: Session, user_id: str, plan_id: str = "free") -> UserCredits:
        """Create new user credits record with correct initial credits"""
        # Ensure we have a valid session
        if not hasattr(session, 'query'):
            raise ValueError("Invalid session object provided to create_user_credits")
            
        # Get the plan to determine initial credits within the session
        plan = session.query(SubscriptionPlan).filter_by(id=plan_id).first()
        initial_credits = 2  # Default fallback for free plan
        if plan:
            initial_credits = plan.credits_per_period
        
        now = datetime.now(timezone.utc)
        user_credits = UserCredits(
            user_id=user_id,
            current_credits=initial_credits,
            total_credits_purchased=initial_credits if plan_id != "free" else 0,
            period_start=now,
            period_end=now + timedelta(days=30)
        )
        
        session.add(user_credits)
        session.flush()  # Get the ID without committing
        
        self.logger.info(f"Created user credits for {user_id}: {initial_credits} credits (plan: {plan_id})")
        return user_credits
    
    def assign_free_plan_to_user(self, user_id: str, session: Session = None) -> bool:
        """Assign free plan to user if they don't have a subscription (idempotent)"""
        session, created = self._ensure_session(session)
        
        try:
            # Check if user already has a subscription
            existing_subscription = self.get_user_subscription(user_id, session)
            if existing_subscription:
                self.logger.info(f"User {user_id} already has subscription: {existing_subscription.plan_id}")
                return True
            
            # Create free subscription
            subscription = self.create_user_subscription(session, user_id, "free")
            
            # Ensure user has credits record
            user_credits = self.get_user_credits(user_id, session)
            if not user_credits:
                user_credits = self.create_user_credits(session, user_id, "free")
            
            # Link user credits to subscription
            user_credits.subscription_id = subscription.id
            session.flush()
            
            self.logger.info(f"Successfully assigned free plan to user {user_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to assign free plan to user {user_id}: {str(e)}")
            return False
        finally:
            if created:
                session.close()
    
    def update_user_credits(self, session: Session, user_credits: UserCredits) -> bool:
        """Update user credits"""
        try:
            session.merge(user_credits)
            session.flush()  # Don't commit here, let the endpoint handle it
            return True
        except Exception as e:
            self.logger.error(f"Failed to update user credits: {str(e)}")
            return False
    
    def add_credits(self, session: Session, user_id: str, amount: int, source: str = "purchase") -> bool:
        """Add credits to user account"""
        user_credits = session.query(UserCredits).options(joinedload(UserCredits.subscription)).filter_by(user_id=user_id).first()
        
        if not user_credits:
            # Create new user credits if doesn't exist
            user_credits = self.create_user_credits(session, user_id)
        
        user_credits.add_credits(amount, source)
        session.flush()  # Don't commit here, let the endpoint handle it
        
        self.logger.info(f"Added {amount} credits to user {user_id} from {source}")
        return True
    
    def use_credits(self, user_id: str, amount: int, session: Session = None) -> Tuple[bool, Dict[str, Any]]:
        """Use credits from user account - ATOMIC OPERATION"""
        session, created = self._ensure_session(session)
        
        try:
            # Use SELECT FOR UPDATE to prevent race conditions (without joinedload to avoid outer join issues)
            user_credits = session.query(UserCredits).filter_by(user_id=user_id).with_for_update().first()
            
            if not user_credits:
                return False, {"error": "User not found"}
            
            # Check if user has enough credits
            if user_credits.current_credits < amount:
                return False, {
                    "error": "Insufficient credits",
                    "current_credits": user_credits.current_credits,
                    "required_credits": amount
                }
            
            # Atomically deduct credits
            user_credits.current_credits -= amount
            user_credits.total_credits_used += amount
            user_credits.credits_used_this_period += amount
            user_credits.updated_at = datetime.now(timezone.utc)
            
            session.flush()  # Don't commit here, let the endpoint handle it
            
            return True, {
                "credits_deducted": amount,
                "remaining_credits": user_credits.current_credits
            }
        finally:
            if created:
                session.close()
    
    def get_user_subscription(self, user_id: str, session: Session = None) -> Optional[UserSubscription]:
        """Get user's current subscription - returns the most recent subscription regardless of status"""
        session, created = self._ensure_session(session)
        
        try:
            # Get the most recent subscription for the user, regardless of status
            # This ensures we can see subscriptions that were just updated
            subscription = session.query(UserSubscription).filter(
                UserSubscription.user_id == user_id
            ).order_by(UserSubscription.updated_at.desc()).first()
            
            # If no subscription found, return None
            if not subscription:
                return None
                
            # Log the subscription details for debugging
            self.logger.info(f"Found subscription for user {user_id}: plan={subscription.plan_id}, status={subscription.status}")
            
            return subscription
        finally:
            if created:
                session.close()
    
    def create_user_subscription(
        self, 
        session: Session,
        user_id: str, 
        plan_id: str, 
        lemon_squeezy_subscription_id: str = None
    ) -> UserSubscription:
        """Create new user subscription"""
        now = datetime.now(timezone.utc)
        period_end = now + timedelta(days=30)  # Monthly subscription
        
        subscription = UserSubscription(
            id=f"sub_{user_id}_{int(now.timestamp())}",
            user_id=user_id,
            plan_id=plan_id,
            status="active",  # Use string value instead of enum
            current_period_start=now,
            current_period_end=period_end,
            lemon_squeezy_subscription_id=lemon_squeezy_subscription_id
        )
        
        session.add(subscription)
        session.flush()  # Don't commit here, let the endpoint handle it
        
        # Update user credits with subscription
        user_credits = session.query(UserCredits).options(joinedload(UserCredits.subscription)).filter_by(user_id=user_id).first()
        if user_credits:
            user_credits.subscription_id = subscription.id
            user_credits.period_start = now
            user_credits.period_end = period_end
            session.flush()  # Don't commit here, let the endpoint handle it
        
        self.logger.info(f"Created subscription for user {user_id}: {plan_id}")
        
        return subscription
    
    def update_subscription_status(
        self, 
        session: Session,
        subscription_id: str, 
        status: SubscriptionStatus
    ) -> bool:
        """Update subscription status"""
        subscription = session.query(UserSubscription).filter_by(id=subscription_id).first()
        
        if subscription:
            subscription.status = status
            session.flush()  # Don't commit here, let the endpoint handle it
            self.logger.info(f"Updated subscription {subscription_id} status to {status}")
            return True
        
        return False
    
    def update_user_subscription(self, session: Session, user_id: str, new_plan_id: str) -> bool:
        """Update user subscription plan"""
        try:
            # Get existing subscription
            subscription = self.get_user_subscription(user_id, session)
            
            if subscription:
                # Update existing subscription
                subscription.plan_id = new_plan_id
                subscription.status = "active"  # Use string value instead of enum
                
                # Update period end
                from datetime import datetime, timezone, timedelta
                now = datetime.now(timezone.utc)
                period_end = now + timedelta(days=30)
                subscription.current_period_end = period_end
                
                session.flush()
                self.logger.info(f"Updated subscription for user {user_id} to plan {new_plan_id}")
                return True
            else:
                # Create new subscription if none exists
                subscription = self.create_user_subscription(session, user_id, new_plan_id)
                self.logger.info(f"Created new subscription for user {user_id} with plan {new_plan_id}")
                return True
                
        except Exception as e:
            self.logger.error(f"Failed to update subscription for user {user_id}: {str(e)}")
            return False
    
    def add_payment_history(self, session: Session, payment: PaymentHistory) -> bool:
        """Add payment to history"""
        try:
            session.add(payment)
            session.flush()  # Don't commit here, let the endpoint handle it
            self.logger.info(f"Added payment history: {payment.id}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to add payment history: {str(e)}")
            return False
    
    def get_payment_history(self, session: Session, user_id: str, limit: int = 50) -> List[PaymentHistory]:
        """Get payment history for user"""
        payments = session.query(PaymentHistory).filter(
            PaymentHistory.user_id == user_id
        ).order_by(desc(PaymentHistory.created_at)).limit(limit).all()
        
        # Detach objects from session
        for payment in payments:
            session.expunge(payment)
        
        return payments
    
    def log_usage(
        self, 
        session: Session,
        user_id: str, 
        usage_type: UsageType, 
        credits_used: int = 1,
        **kwargs
    ) -> bool:
        """Log usage for billing and analytics"""
        try:
            usage_log = UsageLog(
                id=f"usage_{user_id}_{int(datetime.now(timezone.utc).timestamp())}",
                user_id=user_id,
                usage_type=usage_type,
                credits_used=credits_used,
                user_credits_id=user_id,
                **kwargs
            )
            
            session.add(usage_log)
            session.flush()  # Don't commit here, let the endpoint handle it
            
            self.logger.info(f"Logged usage for user {user_id}: {usage_type} ({credits_used} credits)")
            return True
        except Exception as e:
            self.logger.error(f"Failed to log usage: {str(e)}")
            return False
    
    def get_usage_stats(self, session: Session, user_id: str, days: int = 30) -> Dict[str, Any]:
        """Get usage statistics for user"""
        since = datetime.now(timezone.utc) - timedelta(days=days)
        
        # Get usage logs
        usage_logs = session.query(UsageLog).filter(
            and_(
                UsageLog.user_id == user_id,
                UsageLog.created_at >= since
            )
        ).all()
        
        # Calculate statistics
        total_credits_used = sum(log.credits_used for log in usage_logs)
        total_products = sum(log.product_count for log in usage_logs)
        total_tokens = sum(log.tokens_used or 0 for log in usage_logs)
        total_cost = sum(float(log.cost_usd or 0) for log in usage_logs)
        
        # Group by usage type
        usage_by_type = {}
        for log in usage_logs:
            usage_type = log.usage_type
            if usage_type not in usage_by_type:
                usage_by_type[usage_type] = {
                    "count": 0,
                    "credits": 0,
                    "products": 0
                }
            usage_by_type[usage_type]["count"] += 1
            usage_by_type[usage_type]["credits"] += log.credits_used
            usage_by_type[usage_type]["products"] += log.product_count
        
        return {
            "period_days": days,
            "total_credits_used": total_credits_used,
            "total_products_generated": total_products,
            "total_tokens_used": total_tokens,
            "total_cost_usd": total_cost,
            "usage_by_type": usage_by_type,
            "daily_average_credits": total_credits_used / days if days > 0 else 0
        }
    
    def get_daily_usage_count(self, user_id: str, session: Session = None) -> int:
        """Get the number of generations performed by user today"""
        session, created = self._ensure_session(session)
        
        try:
            now = datetime.now(timezone.utc)
            today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            today_end = today_start + timedelta(days=1)
            
            # Count usage logs for today
            usage_count = session.query(UsageLog).filter(
                and_(
                    UsageLog.user_id == user_id,
                    UsageLog.created_at >= today_start,
                    UsageLog.created_at < today_end,
                    UsageLog.usage_type == UsageType.AI_GENERATION
                )
            ).count()
            
            return usage_count
        finally:
            if created:
                session.close()
    
    def get_user_daily_limit(self, user_id: str, session: Session = None) -> int:
        """Get the daily generation limit for a user based on their subscription plan"""
        session, created = self._ensure_session(session)
        
        try:
            # Get user subscription
            subscription = self.get_user_subscription(user_id, session)
            
            if subscription and subscription.is_active():
                # Get plan details
                plan = subscription.plan
                return plan.max_api_calls_per_day
            else:
                # Free tier - get default free plan
                free_plan = session.query(SubscriptionPlan).filter_by(id="free").first()
                if free_plan:
                    return free_plan.max_api_calls_per_day
                else:
                    # Fallback to default free tier limit
                    return 2
        finally:
            if created:
                session.close()
    
    def check_rate_limits(self, session: Session, user_id: str) -> Tuple[bool, Dict[str, Any]]:
        """Check if user is within rate limits"""
        # Get user subscription
        subscription = self.get_user_subscription(session, user_id)
        
        if subscription and subscription.is_active():
            # Get plan rate limits
            plan = subscription.plan
            rate_limits = {
                "requests_per_minute": plan.requests_per_minute,
                "requests_per_hour": plan.requests_per_hour
            }
            
            # Check if user has credits (for free tier behavior)
            user_credits = self.get_user_credits(session, user_id)
            if user_credits and user_credits.current_credits <= 0:
                return False, {
                    "error": "No credits remaining",
                    "upgrade_required": True,
                    "rate_limits": rate_limits
                }
            
            return True, {"rate_limits": rate_limits}
        else:
            # Free tier - check credits
            user_credits = self.get_user_credits(session, user_id)
            if not user_credits:
                # Create free tier user
                user_credits = self.create_user_credits(session, user_id, "free")
            
            if user_credits.current_credits <= 0:
                return False, {
                    "error": "No credits remaining",
                    "upgrade_required": True,
                    "rate_limits": {"requests_per_minute": 5, "requests_per_hour": 50}
                }
            
            return True, {"rate_limits": {"requests_per_minute": 5, "requests_per_hour": 50}}
    
    def get_user_stats(self, session: Session, user_id: str) -> Dict[str, Any]:
        """Get comprehensive user statistics"""
        # Get user credits
        user_credits = self.get_user_credits(session, user_id)
        if not user_credits:
            return {"error": "User not found"}
        
        # Get subscription
        subscription = self.get_user_subscription(session, user_id)
        
        # Get recent payments
        recent_payments = self.get_payment_history(session, user_id, limit=5)
        
        # Get usage stats
        usage_stats = self.get_usage_stats(session, user_id, days=30)
        
        return {
            "user_id": user_id,
            "credits": user_credits.to_dict(),
            "subscription": subscription.to_dict() if subscription else None,
            "recent_payments": [payment.to_dict() for payment in recent_payments],
            "usage_stats": usage_stats,
            "created_at": user_credits.created_at.isoformat()
        }
    
    def health_check(self, session: Session) -> Dict[str, Any]:
        """Database health check"""
        try:
            # Test basic queries
            plan_count = session.query(SubscriptionPlan).count()
            user_count = session.query(UserCredits).count()
            payment_count = session.query(PaymentHistory).count()
            
            return {
                "status": "healthy",
                "type": "sqlalchemy",
                "plans_count": plan_count,
                "users_count": user_count,
                "payments_count": payment_count
            }
        except Exception as e:
            self.logger.error(f"Database health check failed: {str(e)}")
            return {
                "status": "unhealthy",
                "type": "sqlalchemy",
                "error": str(e)
            }
