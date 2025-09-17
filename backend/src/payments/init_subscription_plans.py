# backend/src/payments/init_subscription_plans.py
"""
Initialize subscription plans with correct credit limits

This script ensures that the subscription plans are properly configured
with the correct credit limits as specified in the requirements.
"""

import logging
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from ..database.connection import get_session
from ..models.payment_models import SubscriptionPlan

logger = logging.getLogger(__name__)


def init_subscription_plans():
    """Initialize subscription plans with correct credit limits"""
    
    plans_data = [
        {
            "id": "free",
            "name": "Free Tier",
            "description": "Basic AI product description generation with limited credits",
            "price": 0.00,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 10,
            "max_products_per_batch": 5,
            "max_api_calls_per_day": 50,
            "requests_per_minute": 5,
            "requests_per_hour": 50,
            "features": {
                "ai_generation": True,
                "basic_templates": True,
                "csv_upload": True,
                "email_support": False,
                "priority_support": False,
                "custom_templates": False,
                "api_access": False
            },
            "is_active": True,
            "sort_order": 1
        },
        {
            "id": "basic",
            "name": "Basic Plan",
            "description": "Enhanced AI generation with more credits and features",
            "price": 9.99,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 100,
            "max_products_per_batch": 50,
            "max_api_calls_per_day": 500,
            "requests_per_minute": 20,
            "requests_per_hour": 500,
            "features": {
                "ai_generation": True,
                "basic_templates": True,
                "csv_upload": True,
                "email_support": True,
                "priority_support": False,
                "custom_templates": False,
                "api_access": False
            },
            "is_active": True,
            "sort_order": 2
        },
        {
            "id": "pro",
            "name": "Pro Plan",
            "description": "Professional AI generation with high credit limits and premium features",
            "price": 29.99,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 500,
            "max_products_per_batch": 200,
            "max_api_calls_per_day": 2000,
            "requests_per_minute": 50,
            "requests_per_hour": 2000,
            "features": {
                "ai_generation": True,
                "basic_templates": True,
                "csv_upload": True,
                "email_support": True,
                "priority_support": True,
                "custom_templates": True,
                "api_access": True
            },
            "is_active": True,
            "sort_order": 3
        },
        {
            "id": "enterprise",
            "name": "Enterprise Plan",
            "description": "Unlimited AI generation with premium features and white-label options",
            "price": 99.99,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 10000,  # Effectively unlimited
            "max_products_per_batch": 1000,
            "max_api_calls_per_day": 10000,
            "requests_per_minute": 100,
            "requests_per_hour": 10000,
            "features": {
                "ai_generation": True,
                "basic_templates": True,
                "csv_upload": True,
                "email_support": True,
                "priority_support": True,
                "custom_templates": True,
                "api_access": True,
                "white_label": True,
                "custom_integrations": True
            },
            "is_active": True,
            "sort_order": 4
        }
    ]
    
    with get_session() as session:
        try:
            for plan_data in plans_data:
                # Check if plan already exists
                existing_plan = session.query(SubscriptionPlan).filter_by(id=plan_data["id"]).first()
                
                if existing_plan:
                    # Update existing plan
                    for key, value in plan_data.items():
                        if hasattr(existing_plan, key):
                            setattr(existing_plan, key, value)
                    existing_plan.updated_at = datetime.now(timezone.utc)
                    logger.info(f"Updated subscription plan: {plan_data['id']}")
                else:
                    # Create new plan
                    plan = SubscriptionPlan(**plan_data)
                    session.add(plan)
                    logger.info(f"Created subscription plan: {plan_data['id']}")
            
            session.commit()
            logger.info("Successfully initialized subscription plans")
            
        except Exception as e:
            session.rollback()
            logger.error(f"Failed to initialize subscription plans: {str(e)}")
            raise


if __name__ == "__main__":
    init_subscription_plans()



