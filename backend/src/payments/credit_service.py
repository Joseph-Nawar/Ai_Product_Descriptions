# backend/src/payments/credit_service.py
"""
Enhanced Credit-Based Rate Limiting Service

This module provides comprehensive credit-based rate limiting functionality
for the AI Product Descriptions application.
"""

import logging
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional, Tuple, List
from enum import Enum

from .sqlalchemy_service import SQLAlchemyPaymentService
from ..models.payment_models import (
    UserCredits, UserSubscription, SubscriptionPlan,
    SubscriptionTier, SubscriptionStatus, UsageType, UsageLog
)

logger = logging.getLogger(__name__)


class OperationType(str, Enum):
    """Types of operations that consume credits"""
    SINGLE_DESCRIPTION = "single_description"
    BATCH_SMALL = "batch_small"  # 5-10 products
    BATCH_LARGE = "batch_large"  # 10+ products
    REGENERATION = "regeneration"
    CSV_UPLOAD = "csv_upload"


class CreditService:
    """Enhanced credit-based rate limiting service"""
    
    def __init__(self):
        self.db_service = SQLAlchemyPaymentService()
        
        # Credit costs for different operations
        self.credit_costs = {
            OperationType.SINGLE_DESCRIPTION: 1,
            OperationType.BATCH_SMALL: 5,  # 5-10 products
            OperationType.BATCH_LARGE: 10,  # 10+ products
            OperationType.REGENERATION: 1,
            OperationType.CSV_UPLOAD: 1  # Per product in CSV
        }
        
        # Subscription tier limits (credits per month) - matching requirements
        self.tier_limits = {
            SubscriptionTier.FREE: 10,        # Free: 10 credits/month
            SubscriptionTier.BASIC: 100,      # Basic: 100 credits/month  
            SubscriptionTier.PRO: 500,        # Pro: 500 credits/month
            SubscriptionTier.ENTERPRISE: -1   # Enterprise: Unlimited (-1 means unlimited)
        }
    
    def calculate_credit_cost(self, operation_type: OperationType, product_count: int = 1) -> int:
        """Calculate credit cost for an operation"""
        base_cost = self.credit_costs.get(operation_type, 1)
        
        if operation_type == OperationType.CSV_UPLOAD:
            # CSV upload costs 1 credit per product
            return product_count
        elif operation_type == OperationType.BATCH_SMALL:
            # Batch small (5-10 products) costs 5 credits
            return base_cost
        elif operation_type == OperationType.BATCH_LARGE:
            # Batch large (10+ products) costs 10 credits
            return base_cost
        else:
            # Single description and regeneration cost 1 credit each
            return base_cost
    
    def determine_operation_type(self, product_count: int, is_regeneration: bool = False) -> OperationType:
        """Determine operation type based on parameters"""
        if is_regeneration:
            return OperationType.REGENERATION
        elif product_count == 1:
            return OperationType.SINGLE_DESCRIPTION
        elif 5 <= product_count <= 10:
            return OperationType.BATCH_SMALL
        elif product_count > 10:
            return OperationType.BATCH_LARGE
        else:
            return OperationType.SINGLE_DESCRIPTION
    
    async def check_credits_and_limits(
        self, 
        user_id: str, 
        operation_type: OperationType, 
        product_count: int = 1
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        Check if user has sufficient credits and is within limits
        
        Returns:
            Tuple[bool, Dict]: (can_proceed, info_dict)
        """
        try:
            # Get user credits
            user_credits = self.db_service.get_user_credits(user_id)
            if not user_credits:
                # Create new user with free tier
                user_credits = self.db_service.create_user_credits(user_id, "free")
            
            # Get user subscription
            subscription = self.db_service.get_user_subscription(user_id)
            
            # Calculate required credits
            required_credits = self.calculate_credit_cost(operation_type, product_count)
            
            # Check subscription tier limits
            tier_limit = self.tier_limits.get(user_credits.subscription_tier, 10)
            
            # Check if user has enough credits
            if user_credits.current_credits < required_credits:
                return False, {
                    "error": f"Insufficient credits. Required: {required_credits}, Available: {user_credits.current_credits}",
                    "upgrade_required": True,
                    "current_credits": user_credits.current_credits,
                    "required_credits": required_credits,
                    "operation_type": operation_type.value,
                    "subscription_tier": user_credits.subscription_tier.value,
                    "tier_limit": tier_limit
                }
            
            # Check monthly tier limits (for non-enterprise users)
            if tier_limit > 0:  # Not unlimited
                if user_credits.credits_used_this_period + required_credits > tier_limit:
                    return False, {
                        "error": f"Monthly tier limit exceeded. Used: {user_credits.credits_used_this_period}, Limit: {tier_limit}",
                        "upgrade_required": True,
                        "current_credits": user_credits.current_credits,
                        "required_credits": required_credits,
                        "credits_used_this_period": user_credits.credits_used_this_period,
                        "tier_limit": tier_limit,
                        "subscription_tier": user_credits.subscription_tier.value
                    }
            
            # Check if subscription is active (for paid tiers)
            if subscription and not subscription.is_active():
                return False, {
                    "error": "Subscription expired. Please renew your subscription.",
                    "upgrade_required": True,
                    "current_credits": user_credits.current_credits,
                    "required_credits": required_credits,
                    "subscription_tier": user_credits.subscription_tier.value
                }
            
            # NEW: Check daily generation limits based on subscription plan
            daily_usage_count = self.db_service.get_daily_usage_count(user_id)
            daily_limit = self.db_service.get_user_daily_limit(user_id)
            
            # Check if user has exceeded their daily limit
            if daily_usage_count >= daily_limit:
                return False, {
                    "error": f"Daily generation limit exceeded. Used: {daily_usage_count}, Limit: {daily_limit}",
                    "upgrade_required": True,
                    "current_credits": user_credits.current_credits,
                    "required_credits": required_credits,
                    "daily_usage_count": daily_usage_count,
                    "daily_limit": daily_limit,
                    "subscription_tier": user_credits.subscription_tier.value
                }
            
            # Check rate limits
            can_proceed_rate, rate_info = self.db_service.check_rate_limits(user_id)
            if not can_proceed_rate:
                return False, {
                    "error": rate_info.get("error", "Rate limit exceeded"),
                    "upgrade_required": rate_info.get("upgrade_required", False),
                    "rate_limits": rate_info.get("rate_limits", {}),
                    "current_credits": user_credits.current_credits,
                    "required_credits": required_credits
                }
            
            # All checks passed
            return True, {
                "current_credits": user_credits.current_credits,
                "required_credits": required_credits,
                "remaining_after": user_credits.current_credits - required_credits,
                "operation_type": operation_type.value,
                "subscription_tier": user_credits.subscription_tier.value,
                "tier_limit": tier_limit,
                "credits_used_this_period": user_credits.credits_used_this_period,
                "daily_usage_count": daily_usage_count,
                "daily_limit": daily_limit,
                "rate_limits": rate_info.get("rate_limits", {})
            }
            
        except Exception as e:
            logger.error(f"Error checking credits and limits for user {user_id}: {str(e)}")
            return False, {
                "error": f"Internal error checking credits: {str(e)}",
                "upgrade_required": False
            }
    
    async def deduct_credits(
        self, 
        user_id: str, 
        operation_type: OperationType, 
        product_count: int = 1,
        request_id: str = None,
        batch_id: str = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        Deduct credits after successful operation
        
        Returns:
            Tuple[bool, Dict]: (success, result_dict)
        """
        try:
            # Calculate required credits
            required_credits = self.calculate_credit_cost(operation_type, product_count)
            
            # Deduct credits
            success, result = self.db_service.use_credits(user_id, required_credits)
            
            if success:
                # Log usage
                self.db_service.log_usage(
                    user_id=user_id,
                    usage_type=UsageType.AI_GENERATION,
                    credits_used=required_credits,
                    product_count=product_count,
                    request_id=request_id,
                    batch_id=batch_id,
                    endpoint_used=operation_type.value
                )
                
                # Get updated user credits
                user_credits = self.db_service.get_user_credits(user_id)
                
                return True, {
                    "credits_deducted": required_credits,
                    "remaining_credits": user_credits.current_credits if user_credits else 0,
                    "operation_type": operation_type.value,
                    "product_count": product_count,
                    "usage_logged": True
                }
            else:
                return False, result
                
        except Exception as e:
            logger.error(f"Error deducting credits for user {user_id}: {str(e)}")
            return False, {
                "error": f"Failed to deduct credits: {str(e)}"
            }
    
    async def get_user_credit_info(self, user_id: str) -> Dict[str, Any]:
        """Get comprehensive user credit information"""
        try:
            user_credits = self.db_service.get_user_credits(user_id)
            if not user_credits:
                user_credits = self.db_service.create_user_credits(user_id, "free")
            
            subscription = self.db_service.get_user_subscription(user_id)
            tier_limit = self.tier_limits.get(user_credits.subscription_tier, 10)
            
            # Calculate next refresh date
            next_refresh = None
            if user_credits.period_end:
                next_refresh = user_credits.period_end
            elif subscription and subscription.current_period_end:
                next_refresh = subscription.current_period_end
            else:
                # Default to 30 days from now for free tier
                next_refresh = datetime.now(timezone.utc) + timedelta(days=30)
            
            return {
                "user_id": user_id,
                "current_credits": user_credits.current_credits,
                "total_credits_purchased": user_credits.total_credits_purchased,
                "total_credits_used": user_credits.total_credits_used,
                "credits_used_this_period": user_credits.credits_used_this_period,
                "subscription_tier": user_credits.subscription_tier.value,
                "tier_limit": tier_limit,
                "is_unlimited": tier_limit == -1,
                "credits_remaining_this_period": max(0, tier_limit - user_credits.credits_used_this_period) if tier_limit > 0 else -1,
                "next_credit_refresh": next_refresh.isoformat() if next_refresh else None,
                "subscription_active": subscription.is_active() if subscription else False,
                "subscription_expires": subscription.current_period_end.isoformat() if subscription and subscription.current_period_end else None,
                "credit_costs": {
                    "single_description": self.credit_costs[OperationType.SINGLE_DESCRIPTION],
                    "batch_small": self.credit_costs[OperationType.BATCH_SMALL],
                    "batch_large": self.credit_costs[OperationType.BATCH_LARGE],
                    "regeneration": self.credit_costs[OperationType.REGENERATION],
                    "csv_upload": self.credit_costs[OperationType.CSV_UPLOAD]
                }
            }
            
        except Exception as e:
            logger.error(f"Error getting user credit info for {user_id}: {str(e)}")
            return {
                "error": f"Failed to get credit info: {str(e)}"
            }
    
    async def refresh_credits_for_subscription(self, user_id: str) -> bool:
        """Refresh credits for monthly subscription"""
        try:
            user_credits = self.db_service.get_user_credits(user_id)
            if not user_credits:
                return False
            
            subscription = self.db_service.get_user_subscription(user_id)
            if not subscription or not subscription.is_active():
                return False
            
            # Get plan details
            plan = self.db_service.get_subscription_plan(subscription.plan_id)
            if not plan:
                return False
            
            # Check if it's time to refresh (new billing period)
            now = datetime.now(timezone.utc)
            if user_credits.period_end and now < user_credits.period_end:
                return False  # Not time to refresh yet
            
            # Reset period usage and add new credits
            user_credits.credits_used_this_period = 0
            user_credits.period_start = now
            user_credits.period_end = subscription.current_period_end or (now + timedelta(days=30))
            
            # Add monthly credits
            monthly_credits = plan.credits_per_period
            user_credits.add_credits(monthly_credits, "subscription_refresh")
            
            # Update in database
            success = self.db_service.update_user_credits(user_credits)
            
            if success:
                logger.info(f"Refreshed {monthly_credits} credits for user {user_id}")
            
            return success
            
        except Exception as e:
            logger.error(f"Error refreshing credits for user {user_id}: {str(e)}")
            return False
    
    async def check_and_refresh_credits(self, user_id: str) -> bool:
        """Check if credits need refreshing and refresh if necessary"""
        try:
            user_credits = self.db_service.get_user_credits(user_id)
            if not user_credits:
                return False
            
            # Check if we need to refresh credits
            now = datetime.now(timezone.utc)
            if user_credits.period_end and now >= user_credits.period_end:
                return await self.refresh_credits_for_subscription(user_id)
            
            return True  # No refresh needed
            
        except Exception as e:
            logger.error(f"Error checking credit refresh for user {user_id}: {str(e)}")
            return False
