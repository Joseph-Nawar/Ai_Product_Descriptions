#!/usr/bin/env python3
"""
Migration script to update subscription plans to the new structure

This script updates the existing subscription plans in the database to match
the new simplified three-tier structure with generation limits.
"""

import logging
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add backend directory to path
BACKEND_DIR = Path(__file__).parent
sys.path.insert(0, str(BACKEND_DIR))

from src.database.connection import get_session
from src.models.payment_models import SubscriptionPlan

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def update_subscription_plans():
    """Update subscription plans to the new structure"""
    logger.info("🔄 Updating subscription plans to new structure...")
    
    # New plan structure
    new_plans = [
        {
            "id": "free",
            "name": "Free Tier",
            "description": "Basic AI product description generation",
            "price": 0.00,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 2,  # 2 generations per day
            "max_products_per_batch": 5,
            "max_api_calls_per_day": 2,
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
            "id": "pro",
            "name": "Pro Plan",
            "description": "Professional AI generation with enhanced features",
            "price": 4.99,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 5,  # 5 generations per day
            "max_products_per_batch": 200,
            "max_api_calls_per_day": 5,
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
            "sort_order": 2
        },
        {
            "id": "pro-yearly",
            "name": "Yearly Plan",
            "description": "Unlimited AI generation with enhanced features - Save 50%",
            "price": 99.99,  # Yearly price with 50% discount
            "currency": "USD",
            "billing_interval": "year",
            "credits_per_period": 20,  # 20 generations per day
            "max_products_per_batch": 200,
            "max_api_calls_per_day": 5,
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
            "description": "Unlimited AI generation with premium features",
            "price": 14.99,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 15,  # 15 generations per day
            "max_products_per_batch": 1000,
            "max_api_calls_per_day": 15,
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
            # Deactivate old plans that are no longer needed
            old_plan_ids = ["basic"]  # Remove the old "basic" plan
            for old_id in old_plan_ids:
                old_plan = session.query(SubscriptionPlan).filter_by(id=old_id).first()
                if old_plan:
                    old_plan.is_active = False
                    logger.info(f"Deactivated old plan: {old_id}")
            
            # Update or create new plans
            for plan_data in new_plans:
                existing_plan = session.query(SubscriptionPlan).filter_by(id=plan_data["id"]).first()
                
                if existing_plan:
                    # Update existing plan
                    for key, value in plan_data.items():
                        if hasattr(existing_plan, key):
                            setattr(existing_plan, key, value)
                    logger.info(f"Updated plan: {plan_data['id']}")
                else:
                    # Create new plan
                    plan = SubscriptionPlan(**plan_data)
                    session.add(plan)
                    logger.info(f"Created new plan: {plan_data['id']}")
            
            session.commit()
            logger.info("✅ Successfully updated subscription plans")
            
            # Show summary
            active_plans = session.query(SubscriptionPlan).filter_by(is_active=True).order_by(SubscriptionPlan.sort_order).all()
            logger.info(f"📊 Active plans ({len(active_plans)}):")
            for plan in active_plans:
                logger.info(f"  - {plan.name}: {plan.credits_per_period} generations/day, ${plan.price}/{plan.billing_interval}")
            
        except Exception as e:
            session.rollback()
            logger.error(f"❌ Failed to update subscription plans: {str(e)}")
            raise


def main():
    """Main function"""
    logger.info("🚀 Starting subscription plans migration...")
    
    try:
        update_subscription_plans()
        logger.info("🎉 Migration completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"❌ Migration failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
