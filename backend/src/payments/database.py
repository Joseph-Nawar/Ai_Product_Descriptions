# backend/src/payments/database.py
"""
Database integration for payment system

This module provides database operations for the payment system.
In production, replace the placeholder implementations with actual database operations.
"""

import os
import json
import logging
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from dataclasses import asdict

from .models import UserCredits, PaymentHistory, SubscriptionPlans, SubscriptionTier, PaymentStatus

logger = logging.getLogger(__name__)


class PaymentDatabase:
    """Database operations for payment system"""
    
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        self.use_database = bool(self.database_url)
        
        if self.use_database:
            self._initialize_database()
        else:
            logger.warning("No DATABASE_URL provided, using in-memory storage")
            self._initialize_memory_storage()
    
    def _initialize_database(self):
        """Initialize database connection"""
        try:
            # This is a placeholder for database initialization
            # In production, you would use SQLAlchemy, asyncpg, or similar
            logger.info("Database connection initialized")
        except Exception as e:
            logger.error(f"Failed to initialize database: {str(e)}")
            raise
    
    def _initialize_memory_storage(self):
        """Initialize in-memory storage for development"""
        self._user_credits = {}
        self._payment_history = {}
        self._subscription_plans = {}
        logger.info("In-memory storage initialized")
    
    async def get_user_credits(self, user_id: str) -> Optional[UserCredits]:
        """Get user credits from database"""
        if self.use_database:
            return await self._get_user_credits_from_db(user_id)
        else:
            return self._user_credits.get(user_id)
    
    async def _get_user_credits_from_db(self, user_id: str) -> Optional[UserCredits]:
        """Get user credits from actual database"""
        # Placeholder implementation
        # In production, implement actual database query
        try:
            # Example SQL query:
            # SELECT * FROM user_credits WHERE user_id = %s
            # Convert result to UserCredits object
            pass
        except Exception as e:
            logger.error(f"Database error getting user credits: {str(e)}")
            return None
    
    async def save_user_credits(self, user_credits: UserCredits) -> bool:
        """Save user credits to database"""
        if self.use_database:
            return await self._save_user_credits_to_db(user_credits)
        else:
            self._user_credits[user_credits.user_id] = user_credits
            return True
    
    async def _save_user_credits_to_db(self, user_credits: UserCredits) -> bool:
        """Save user credits to actual database"""
        # Placeholder implementation
        # In production, implement actual database insert/update
        try:
            # Example SQL query:
            # INSERT INTO user_credits (...) VALUES (...) ON CONFLICT (user_id) DO UPDATE SET ...
            pass
            return True
        except Exception as e:
            logger.error(f"Database error saving user credits: {str(e)}")
            return False
    
    async def get_payment_history(self, user_id: str, limit: int = 50) -> List[PaymentHistory]:
        """Get payment history for user"""
        if self.use_database:
            return await self._get_payment_history_from_db(user_id, limit)
        else:
            user_payments = [
                payment for payment in self._payment_history.values()
                if payment.user_id == user_id
            ]
            return sorted(user_payments, key=lambda x: x.created_at, reverse=True)[:limit]
    
    async def _get_payment_history_from_db(self, user_id: str, limit: int) -> List[PaymentHistory]:
        """Get payment history from actual database"""
        # Placeholder implementation
        # In production, implement actual database query
        try:
            # Example SQL query:
            # SELECT * FROM payment_history WHERE user_id = %s ORDER BY created_at DESC LIMIT %s
            pass
        except Exception as e:
            logger.error(f"Database error getting payment history: {str(e)}")
            return []
    
    async def save_payment_history(self, payment: PaymentHistory) -> bool:
        """Save payment to history"""
        if self.use_database:
            return await self._save_payment_history_to_db(payment)
        else:
            self._payment_history[payment.id] = payment
            return True
    
    async def _save_payment_history_to_db(self, payment: PaymentHistory) -> bool:
        """Save payment to actual database"""
        # Placeholder implementation
        # In production, implement actual database insert
        try:
            # Example SQL query:
            # INSERT INTO payment_history (...) VALUES (...)
            pass
            return True
        except Exception as e:
            logger.error(f"Database error saving payment history: {str(e)}")
            return False
    
    async def get_subscription_plans(self) -> List[SubscriptionPlans]:
        """Get all subscription plans"""
        if self.use_database:
            return await self._get_subscription_plans_from_db()
        else:
            return list(self._subscription_plans.values())
    
    async def _get_subscription_plans_from_db(self) -> List[SubscriptionPlans]:
        """Get subscription plans from actual database"""
        # Placeholder implementation
        # In production, implement actual database query
        try:
            # Example SQL query:
            # SELECT * FROM subscription_plans WHERE is_active = true
            pass
        except Exception as e:
            logger.error(f"Database error getting subscription plans: {str(e)}")
            return []
    
    async def save_subscription_plan(self, plan: SubscriptionPlans) -> bool:
        """Save subscription plan"""
        if self.use_database:
            return await self._save_subscription_plan_to_db(plan)
        else:
            self._subscription_plans[plan.id] = plan
            return True
    
    async def _save_subscription_plan_to_db(self, plan: SubscriptionPlans) -> bool:
        """Save subscription plan to actual database"""
        # Placeholder implementation
        # In production, implement actual database insert/update
        try:
            # Example SQL query:
            # INSERT INTO subscription_plans (...) VALUES (...) ON CONFLICT (id) DO UPDATE SET ...
            pass
            return True
        except Exception as e:
            logger.error(f"Database error saving subscription plan: {str(e)}")
            return False
    
    async def create_user_if_not_exists(self, user_id: str, email: str = None) -> UserCredits:
        """Create new user with free tier if not exists"""
        existing_user = await self.get_user_credits(user_id)
        if existing_user:
            return existing_user
        
        # Create new user with free tier
        new_user = UserCredits(
            user_id=user_id,
            current_credits=10,  # Free tier gets 10 credits
            subscription_tier=SubscriptionTier.FREE
        )
        
        await self.save_user_credits(new_user)
        logger.info(f"Created new user: {user_id}")
        return new_user
    
    async def get_user_stats(self, user_id: str) -> Dict[str, Any]:
        """Get comprehensive user statistics"""
        user_credits = await self.get_user_credits(user_id)
        if not user_credits:
            return {"error": "User not found"}
        
        payment_history = await self.get_payment_history(user_id, limit=10)
        
        return {
            "user_id": user_id,
            "current_credits": user_credits.current_credits,
            "subscription_tier": user_credits.subscription_tier.value,
            "total_credits_purchased": user_credits.total_credits_purchased,
            "total_credits_used": user_credits.total_credits_used,
            "subscription_expires_at": user_credits.subscription_expires_at.isoformat() if user_credits.subscription_expires_at else None,
            "recent_payments": [payment.to_dict() for payment in payment_history[:5]],
            "created_at": user_credits.created_at.isoformat()
        }
    
    async def health_check(self) -> Dict[str, Any]:
        """Database health check"""
        try:
            if self.use_database:
                # Test database connection
                # In production, implement actual database ping
                return {
                    "status": "healthy",
                    "type": "database",
                    "connected": True
                }
            else:
                return {
                    "status": "healthy",
                    "type": "memory",
                    "users_count": len(self._user_credits),
                    "payments_count": len(self._payment_history),
                    "plans_count": len(self._subscription_plans)
                }
        except Exception as e:
            logger.error(f"Database health check failed: {str(e)}")
            return {
                "status": "unhealthy",
                "type": "database" if self.use_database else "memory",
                "error": str(e)
            }


# Global database instance
db = PaymentDatabase()

