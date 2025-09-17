# backend/src/payments/sqlalchemy_service.py
"""
SQLAlchemy-based payment service implementation

This module provides database operations using SQLAlchemy models
for the payment system.
"""

import logging
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional, List, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc

from ..database.connection import get_session
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
    
    def get_subscription_plans(self) -> List[Dict[str, Any]]:
        """Get all active subscription plans"""
        with get_session() as session:
            plans = session.query(SubscriptionPlan).filter(
                SubscriptionPlan.is_active == True
            ).order_by(SubscriptionPlan.sort_order).all()
            
            return [plan.to_dict() for plan in plans]
    
    def get_subscription_plan(self, plan_id: str) -> Optional[SubscriptionPlan]:
        """Get a specific subscription plan"""
        with get_session() as session:
            plan = session.query(SubscriptionPlan).filter_by(id=plan_id).first()
            if plan:
                session.expunge(plan)
            return plan
    
    def get_user_credits(self, user_id: str) -> Optional[UserCredits]:
        """Get user credits"""
        with get_session() as session:
            user_credits = session.query(UserCredits).filter_by(user_id=user_id).first()
            if user_credits:
                session.expunge(user_credits)
            return user_credits
    
    def create_user_credits(self, user_id: str, plan_id: str = "free") -> UserCredits:
        """Create new user credits record"""
        with get_session() as session:
            # Get the plan to determine initial credits within the session
            plan = session.query(SubscriptionPlan).filter_by(id=plan_id).first()
            initial_credits = 10  # Default fallback
            if plan:
                initial_credits = plan.credits_per_period
            
            user_credits = UserCredits(
                user_id=user_id,
                current_credits=initial_credits,
                total_credits_purchased=initial_credits if plan_id != "free" else 0,
                period_start=datetime.now(timezone.utc),
                period_end=datetime.now(timezone.utc) + timedelta(days=30)
            )
            
            session.add(user_credits)
            session.commit()
            session.refresh(user_credits)
            
            # Detach the object from the session so it can be used outside
            session.expunge(user_credits)
            
            self.logger.info(f"Created user credits for {user_id}: {initial_credits} credits")
            return user_credits
    
    def update_user_credits(self, user_credits: UserCredits) -> bool:
        """Update user credits"""
        try:
            with get_session() as session:
                session.merge(user_credits)
                session.commit()
                return True
        except Exception as e:
            self.logger.error(f"Failed to update user credits: {str(e)}")
            return False
    
    def add_credits(self, user_id: str, amount: int, source: str = "purchase") -> bool:
        """Add credits to user account"""
        with get_session() as session:
            user_credits = session.query(UserCredits).filter_by(user_id=user_id).first()
            
            if not user_credits:
                # Create new user credits if doesn't exist
                user_credits = self.create_user_credits(user_id)
            
            user_credits.add_credits(amount, source)
            session.commit()
            
            self.logger.info(f"Added {amount} credits to user {user_id} from {source}")
            return True
    
    def use_credits(self, user_id: str, amount: int) -> Tuple[bool, Dict[str, Any]]:
        """Use credits from user account"""
        with get_session() as session:
            user_credits = session.query(UserCredits).filter_by(user_id=user_id).first()
            
            if not user_credits:
                return False, {"error": "User not found"}
            
            if user_credits.use_credits(amount):
                session.commit()
                return True, {
                    "credits_deducted": amount,
                    "remaining_credits": user_credits.current_credits
                }
            else:
                return False, {
                    "error": "Insufficient credits",
                    "current_credits": user_credits.current_credits,
                    "required_credits": amount
                }
    
    def get_user_subscription(self, user_id: str) -> Optional[UserSubscription]:
        """Get user's current subscription"""
        with get_session() as session:
            return session.query(UserSubscription).filter(
                and_(
                    UserSubscription.user_id == user_id,
                    UserSubscription.status == SubscriptionStatus.ACTIVE
                )
            ).first()
    
    def create_user_subscription(
        self, 
        user_id: str, 
        plan_id: str, 
        lemon_squeezy_subscription_id: str = None
    ) -> UserSubscription:
        """Create new user subscription"""
        with get_session() as session:
            now = datetime.now(timezone.utc)
            period_end = now + timedelta(days=30)  # Monthly subscription
            
            subscription = UserSubscription(
                id=f"sub_{user_id}_{int(now.timestamp())}",
                user_id=user_id,
                plan_id=plan_id,
                status=SubscriptionStatus.ACTIVE,
                current_period_start=now,
                current_period_end=period_end,
                lemon_squeezy_subscription_id=lemon_squeezy_subscription_id
            )
            
            session.add(subscription)
            session.commit()
            session.refresh(subscription)
            
            # Update user credits with subscription
            user_credits = session.query(UserCredits).filter_by(user_id=user_id).first()
            if user_credits:
                user_credits.subscription_id = subscription.id
                user_credits.period_start = now
                user_credits.period_end = period_end
                session.commit()
            
            self.logger.info(f"Created subscription for user {user_id}: {plan_id}")
            
            # Return subscription data as dictionary to avoid session issues
            return {
                "id": subscription.id,
                "user_id": subscription.user_id,
                "plan_id": subscription.plan_id,
                "status": subscription.status,
                "current_period_start": subscription.current_period_start,
                "current_period_end": subscription.current_period_end,
                "is_active": subscription.is_active(),
                "is_trial": subscription.is_trial()
            }
    
    def update_subscription_status(
        self, 
        subscription_id: str, 
        status: SubscriptionStatus
    ) -> bool:
        """Update subscription status"""
        with get_session() as session:
            subscription = session.query(UserSubscription).filter_by(id=subscription_id).first()
            
            if subscription:
                subscription.status = status
                session.commit()
                self.logger.info(f"Updated subscription {subscription_id} status to {status}")
                return True
            
            return False
    
    def add_payment_history(self, payment: PaymentHistory) -> bool:
        """Add payment to history"""
        try:
            with get_session() as session:
                session.add(payment)
                session.commit()
                self.logger.info(f"Added payment history: {payment.id}")
                return True
        except Exception as e:
            self.logger.error(f"Failed to add payment history: {str(e)}")
            return False
    
    def get_payment_history(self, user_id: str, limit: int = 50) -> List[PaymentHistory]:
        """Get payment history for user"""
        with get_session() as session:
            payments = session.query(PaymentHistory).filter(
                PaymentHistory.user_id == user_id
            ).order_by(desc(PaymentHistory.created_at)).limit(limit).all()
            
            # Detach objects from session
            for payment in payments:
                session.expunge(payment)
            
            return payments
    
    def log_usage(
        self, 
        user_id: str, 
        usage_type: UsageType, 
        credits_used: int = 1,
        **kwargs
    ) -> bool:
        """Log usage for billing and analytics"""
        try:
            with get_session() as session:
                usage_log = UsageLog(
                    id=f"usage_{user_id}_{int(datetime.now().timestamp())}",
                    user_id=user_id,
                    usage_type=usage_type,
                    credits_used=credits_used,
                    user_credits_id=user_id,
                    **kwargs
                )
                
                session.add(usage_log)
                session.commit()
                
                self.logger.info(f"Logged usage for user {user_id}: {usage_type} ({credits_used} credits)")
                return True
        except Exception as e:
            self.logger.error(f"Failed to log usage: {str(e)}")
            return False
    
    def get_usage_stats(self, user_id: str, days: int = 30) -> Dict[str, Any]:
        """Get usage statistics for user"""
        with get_session() as session:
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
    
    def check_rate_limits(self, user_id: str) -> Tuple[bool, Dict[str, Any]]:
        """Check if user is within rate limits"""
        with get_session() as session:
            # Get user subscription
            subscription = self.get_user_subscription(user_id)
            
            if subscription and subscription.is_active():
                # Get plan rate limits
                plan = subscription.plan
                rate_limits = {
                    "requests_per_minute": plan.requests_per_minute,
                    "requests_per_hour": plan.requests_per_hour
                }
                
                # Check if user has credits (for free tier behavior)
                user_credits = self.get_user_credits(user_id)
                if user_credits and user_credits.current_credits <= 0:
                    return False, {
                        "error": "No credits remaining",
                        "upgrade_required": True,
                        "rate_limits": rate_limits
                    }
                
                return True, {"rate_limits": rate_limits}
            else:
                # Free tier - check credits
                user_credits = self.get_user_credits(user_id)
                if not user_credits:
                    # Create free tier user
                    user_credits = self.create_user_credits(user_id, "free")
                
                if user_credits.current_credits <= 0:
                    return False, {
                        "error": "No credits remaining",
                        "upgrade_required": True,
                        "rate_limits": {"requests_per_minute": 5, "requests_per_hour": 50}
                    }
                
                return True, {"rate_limits": {"requests_per_minute": 5, "requests_per_hour": 50}}
    
    def get_user_stats(self, user_id: str) -> Dict[str, Any]:
        """Get comprehensive user statistics"""
        with get_session() as session:
            # Get user credits
            user_credits = self.get_user_credits(user_id)
            if not user_credits:
                return {"error": "User not found"}
            
            # Get subscription
            subscription = self.get_user_subscription(user_id)
            
            # Get recent payments
            recent_payments = self.get_payment_history(user_id, limit=5)
            
            # Get usage stats
            usage_stats = self.get_usage_stats(user_id, days=30)
            
            return {
                "user_id": user_id,
                "credits": user_credits.to_dict(),
                "subscription": subscription.to_dict() if subscription else None,
                "recent_payments": [payment.to_dict() for payment in recent_payments],
                "usage_stats": usage_stats,
                "created_at": user_credits.created_at.isoformat()
            }
    
    def health_check(self) -> Dict[str, Any]:
        """Database health check"""
        try:
            with get_session() as session:
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
