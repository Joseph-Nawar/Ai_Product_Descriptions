#!/usr/bin/env python3
"""
Database initialization script

This script initializes the database with tables and default data.
Run this script to set up your database for the first time.
"""

import asyncio
import logging
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add backend directory to path
BACKEND_DIR = Path(__file__).parent.parent.parent
sys.path.insert(0, str(BACKEND_DIR))

from src.database.connection import init_database, check_database_connection, get_database_info
from src.database.migrations import run_initial_migrations, get_migration_status
from src.models.payment_models import SubscriptionPlan, SubscriptionTier
from src.database.connection import get_session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_default_plans():
    """Create default subscription plans - SINGLE SOURCE OF TRUTH"""
    logger.info("Creating default subscription plans...")
    
    # STANDARDIZED PLAN DEFINITIONS - This is the ONLY place plans should be defined
    default_plans = [
        {
            "id": "free",
            "name": "Free Tier",
            "description": "Basic AI product description generation - 2 generations per day",
            "price": 0.00,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 2,  # 2 generations per day
            "max_products_per_batch": 5,
            "max_api_calls_per_day": 2,  # Daily limit
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
            "description": "Professional AI generation - 5 generations per day",
            "price": 4.99,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 5,  # 5 generations per day
            "max_products_per_batch": 200,
            "max_api_calls_per_day": 5,  # Daily limit
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
            "id": "enterprise",
            "name": "Enterprise Plan",
            "description": "Unlimited AI generation - 15 generations per day",
            "price": 14.99,
            "currency": "USD",
            "billing_interval": "month",
            "credits_per_period": 15,  # 15 generations per day
            "max_products_per_batch": 1000,
            "max_api_calls_per_day": 15,  # Daily limit
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
            "sort_order": 3
        },
        {
            "id": "yearly",
            "name": "Yearly Plan",
            "description": "Unlimited AI generation - 15 generations per day - Save 50%",
            "price": 99.99,  # Yearly price with 50% discount
            "currency": "USD",
            "billing_interval": "year",
            "credits_per_period": 15,  # 15 generations per day (same as enterprise)
            "max_products_per_batch": 1000,
            "max_api_calls_per_day": 15,  # Daily limit
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
        for plan_data in default_plans:
            # Check if plan already exists
            existing_plan = session.query(SubscriptionPlan).filter_by(id=plan_data["id"]).first()
            
            if not existing_plan:
                plan = SubscriptionPlan(**plan_data)
                session.add(plan)
                logger.info(f"Created plan: {plan_data['name']}")
            else:
                logger.info(f"Plan already exists: {plan_data['name']}")
        
        session.commit()
        logger.info("Default plans setup completed")


def verify_database_setup():
    """Verify database setup is correct"""
    logger.info("Verifying database setup...")
    
    with get_session() as session:
        # Check if all tables exist
        from sqlalchemy import inspect
        inspector = inspect(session.bind)
        tables = inspector.get_table_names()
        
        expected_tables = [
            "subscription_plans",
            "user_subscriptions", 
            "user_credits",
            "payment_history",
            "usage_logs",
            "migrations"
        ]
        
        missing_tables = [table for table in expected_tables if table not in tables]
        
        if missing_tables:
            logger.error(f"Missing tables: {missing_tables}")
            return False
        
        # Check if default plans exist
        plan_count = session.query(SubscriptionPlan).count()
        if plan_count == 0:
            logger.error("No subscription plans found")
            return False
        
        logger.info(f"Found {plan_count} subscription plans")
        logger.info("Database setup verification completed successfully")
        return True


def main():
    """Main initialization function"""
    logger.info("🚀 Starting database initialization...")
    
    try:
        # Check database connection
        logger.info("1. Checking database connection...")
        if not check_database_connection():
            logger.error("❌ Database connection failed")
            return False
        logger.info("✅ Database connection successful")
        
        # Get database info
        logger.info("2. Getting database information...")
        db_info = get_database_info()
        logger.info(f"✅ Database: {db_info.get('url', 'Unknown')}")
        logger.info(f"✅ Version: {db_info.get('version', 'Unknown')}")
        
        # Initialize database tables
        logger.info("3. Initializing database tables...")
        init_database()
        logger.info("✅ Database tables created")
        
        # Run initial migrations
        logger.info("4. Running initial migrations...")
        run_initial_migrations()
        logger.info("✅ Initial migrations completed")
        
        # Create default plans
        logger.info("5. Creating default subscription plans...")
        create_default_plans()
        logger.info("✅ Default plans created")
        
        # Verify setup
        logger.info("6. Verifying database setup...")
        if not verify_database_setup():
            logger.error("❌ Database setup verification failed")
            return False
        logger.info("✅ Database setup verified")
        
        # Show migration status
        logger.info("7. Migration status:")
        migration_status = get_migration_status()
        logger.info(f"✅ Applied migrations: {migration_status['total_applied']}")
        logger.info(f"✅ Pending migrations: {migration_status['total_pending']}")
        
        logger.info("🎉 Database initialization completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

