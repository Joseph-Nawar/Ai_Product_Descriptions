# backend/src/database/migrations.py
"""
Database migration utilities
"""

import os
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from sqlalchemy import text
from sqlalchemy.orm import Session

from .connection import get_engine, get_session
from ..models.payment_models import Base

logger = logging.getLogger(__name__)


class MigrationManager:
    """Manage database migrations"""
    
    def __init__(self, migration_dir: str = "migrations"):
        self.migration_dir = Path(migration_dir)
        self.migration_dir.mkdir(exist_ok=True)
        self._init_migration_table()
    
    def _init_migration_table(self):
        """Initialize migration tracking table"""
        try:
            with get_session() as session:
                session.execute(text("""
                    CREATE TABLE IF NOT EXISTS migrations (
                        id SERIAL PRIMARY KEY,
                        version VARCHAR(50) UNIQUE NOT NULL,
                        name VARCHAR(255) NOT NULL,
                        applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """))
                session.commit()
                logger.info("Migration table initialized")
        except Exception as e:
            logger.error(f"Failed to initialize migration table: {str(e)}")
            raise
    
    def get_applied_migrations(self) -> List[str]:
        """Get list of applied migrations"""
        try:
            with get_session() as session:
                result = session.execute(text("SELECT version FROM migrations ORDER BY applied_at"))
                return [row[0] for row in result.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get applied migrations: {str(e)}")
            return []
    
    def apply_migration(self, version: str, name: str, sql: str):
        """Apply a migration"""
        try:
            with get_session() as session:
                # Execute migration SQL - handle SQLite's single statement limitation
                if "sqlite" in str(session.bind.url):
                    # Split SQL statements and execute one by one for SQLite
                    statements = [stmt.strip() for stmt in sql.split(';') if stmt.strip()]
                    for statement in statements:
                        if statement and statement.upper().startswith('ALTER TABLE') and 'CONSTRAINT' in statement.upper():
                            # Skip constraint additions for SQLite
                            logger.info(f"Skipping constraint for SQLite: {statement[:50]}...")
                            continue
                        if statement:
                            session.execute(text(statement))
                else:
                    # For other databases, execute as a single statement
                    session.execute(text(sql))
                
                # Record migration
                session.execute(text("""
                    INSERT INTO migrations (version, name) 
                    VALUES (:version, :name)
                """), {"version": version, "name": name})
                
                session.commit()
                logger.info(f"Applied migration: {version} - {name}")
                
        except Exception as e:
            logger.error(f"Failed to apply migration {version}: {str(e)}")
            raise
    
    def create_migration_file(self, name: str) -> str:
        """Create a new migration file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        version = f"{timestamp}_{name}"
        filename = f"{version}.sql"
        filepath = self.migration_dir / filename
        
        # Create migration template
        template = f"""-- Migration: {name}
-- Version: {version}
-- Created: {datetime.now().isoformat()}

-- Add your migration SQL here
-- Example:
-- ALTER TABLE users ADD COLUMN new_field VARCHAR(255);
-- CREATE INDEX idx_users_new_field ON users(new_field);

-- Remember to update the model classes if needed
"""
        
        with open(filepath, 'w') as f:
            f.write(template)
        
        logger.info(f"Created migration file: {filepath}")
        return str(filepath)
    
    def run_pending_migrations(self):
        """Run all pending migrations"""
        applied = self.get_applied_migrations()
        
        # Get all migration files
        migration_files = sorted([f for f in self.migration_dir.glob("*.sql")])
        
        for filepath in migration_files:
            version = filepath.stem
            
            if version not in applied:
                logger.info(f"Running migration: {version}")
                
                with open(filepath, 'r') as f:
                    sql = f.read()
                
                # Extract name from SQL comment
                name = version.split('_', 1)[1] if '_' in version else version
                
                self.apply_migration(version, name, sql)


def create_migration(name: str, migration_dir: str = "migrations") -> str:
    """Create a new migration file"""
    manager = MigrationManager(migration_dir)
    return manager.create_migration_file(name)


def run_migrations(migration_dir: str = "migrations") -> None:
    """Run all pending migrations"""
    manager = MigrationManager(migration_dir)
    manager.run_pending_migrations()


def get_migration_status(migration_dir: str = "migrations") -> dict:
    """Get migration status"""
    manager = MigrationManager(migration_dir)
    applied = manager.get_applied_migrations()
    
    # Get all migration files
    migration_files = [f.stem for f in Path(migration_dir).glob("*.sql")]
    
    pending = [f for f in migration_files if f not in applied]
    
    return {
        "applied": applied,
        "pending": pending,
        "total_applied": len(applied),
        "total_pending": len(pending)
    }


# Pre-defined migrations for initial setup
INITIAL_MIGRATIONS = {
    "001_initial_schema": """
-- Initial database schema for payment system
-- This migration creates all the base tables

-- Subscription Plans
CREATE TABLE IF NOT EXISTS subscription_plans (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    billing_interval VARCHAR(20) NOT NULL DEFAULT 'month',
    credits_per_period INTEGER NOT NULL DEFAULT 0,
    max_products_per_batch INTEGER NOT NULL DEFAULT 0,
    max_api_calls_per_day INTEGER NOT NULL DEFAULT 0,
    requests_per_minute INTEGER NOT NULL DEFAULT 5,
    requests_per_hour INTEGER NOT NULL DEFAULT 50,
    features JSON NOT NULL DEFAULT '{}',
    lemon_squeezy_variant_id VARCHAR(255) UNIQUE,
    lemon_squeezy_product_id VARCHAR(255),
    is_active BOOLEAN NOT NULL DEFAULT true,
    sort_order INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User Subscriptions
CREATE TABLE IF NOT EXISTS user_subscriptions (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    plan_id VARCHAR(50) NOT NULL REFERENCES subscription_plans(id),
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    current_period_start TIMESTAMP WITH TIME ZONE NOT NULL,
    current_period_end TIMESTAMP WITH TIME ZONE NOT NULL,
    cancel_at_period_end BOOLEAN NOT NULL DEFAULT false,
    lemon_squeezy_subscription_id VARCHAR(255) UNIQUE,
    lemon_squeezy_customer_id VARCHAR(255),
    trial_start TIMESTAMP WITH TIME ZONE,
    trial_end TIMESTAMP WITH TIME ZONE,
    subscription_metadata JSON NOT NULL DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User Credits
CREATE TABLE IF NOT EXISTS user_credits (
    user_id VARCHAR(255) PRIMARY KEY,
    current_credits INTEGER NOT NULL DEFAULT 0,
    total_credits_purchased INTEGER NOT NULL DEFAULT 0,
    total_credits_used INTEGER NOT NULL DEFAULT 0,
    total_credits_expired INTEGER NOT NULL DEFAULT 0,
    subscription_id VARCHAR(255) REFERENCES user_subscriptions(id),
    last_credit_refill TIMESTAMP WITH TIME ZONE,
    next_credit_refill TIMESTAMP WITH TIME ZONE,
    credits_used_this_period INTEGER NOT NULL DEFAULT 0,
    period_start TIMESTAMP WITH TIME ZONE,
    period_end TIMESTAMP WITH TIME ZONE,
    credits_metadata JSON NOT NULL DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Payment History
CREATE TABLE IF NOT EXISTS payment_history (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    payment_method VARCHAR(50) NOT NULL DEFAULT 'lemon_squeezy',
    payment_provider VARCHAR(50) NOT NULL DEFAULT 'lemon_squeezy',
    lemon_squeezy_order_id VARCHAR(255) UNIQUE,
    lemon_squeezy_subscription_id VARCHAR(255),
    lemon_squeezy_customer_id VARCHAR(255),
    subscription_id VARCHAR(255) REFERENCES user_subscriptions(id),
    credits_awarded INTEGER NOT NULL DEFAULT 0,
    plan_id VARCHAR(50) REFERENCES subscription_plans(id),
    transaction_type VARCHAR(50) NOT NULL DEFAULT 'subscription',
    description TEXT,
    payment_metadata JSON NOT NULL DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP WITH TIME ZONE
);

-- Usage Logs
CREATE TABLE IF NOT EXISTS usage_logs (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    usage_type VARCHAR(50) NOT NULL DEFAULT 'ai_generation',
    credits_used INTEGER NOT NULL DEFAULT 1,
    product_count INTEGER NOT NULL DEFAULT 1,
    language_code VARCHAR(10),
    category VARCHAR(100),
    tokens_used INTEGER,
    response_time_ms INTEGER,
    cost_usd DECIMAL(10, 6),
    request_id VARCHAR(255),
    batch_id VARCHAR(255),
    endpoint_used VARCHAR(100),
    user_credits_id VARCHAR(255) REFERENCES user_credits(user_id),
    usage_metadata JSON NOT NULL DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_user_subscriptions_user_id ON user_subscriptions(user_id);
CREATE INDEX IF NOT EXISTS idx_user_subscriptions_status ON user_subscriptions(status);
CREATE INDEX IF NOT EXISTS idx_user_subscriptions_period_end ON user_subscriptions(current_period_end);
CREATE INDEX IF NOT EXISTS idx_user_subscriptions_ls_id ON user_subscriptions(lemon_squeezy_subscription_id);

CREATE INDEX IF NOT EXISTS idx_user_credits_subscription ON user_credits(subscription_id);
CREATE INDEX IF NOT EXISTS idx_user_credits_refill ON user_credits(next_credit_refill);

CREATE INDEX IF NOT EXISTS idx_payment_history_user_id ON payment_history(user_id);
CREATE INDEX IF NOT EXISTS idx_payment_history_status ON payment_history(status);
CREATE INDEX IF NOT EXISTS idx_payment_history_ls_order ON payment_history(lemon_squeezy_order_id);
CREATE INDEX IF NOT EXISTS idx_payment_history_ls_subscription ON payment_history(lemon_squeezy_subscription_id);
CREATE INDEX IF NOT EXISTS idx_payment_history_created ON payment_history(created_at);

CREATE INDEX IF NOT EXISTS idx_usage_logs_user_id ON usage_logs(user_id);
CREATE INDEX IF NOT EXISTS idx_usage_logs_type ON usage_logs(usage_type);
CREATE INDEX IF NOT EXISTS idx_usage_logs_created ON usage_logs(created_at);
CREATE INDEX IF NOT EXISTS idx_usage_logs_batch ON usage_logs(batch_id);
CREATE INDEX IF NOT EXISTS idx_usage_logs_request ON usage_logs(request_id);

CREATE INDEX IF NOT EXISTS idx_subscription_plans_active ON subscription_plans(is_active);
CREATE INDEX IF NOT EXISTS idx_subscription_plans_sort ON subscription_plans(sort_order);
""",

    "002_default_plans": """
-- Insert default subscription plans
INSERT INTO subscription_plans (id, name, description, price, currency, billing_interval, credits_per_period, max_products_per_batch, max_api_calls_per_day, requests_per_minute, requests_per_hour, features, is_active, sort_order) VALUES
('free', 'Free Tier', 'Basic AI product description generation', 0.00, 'USD', 'month', 10, 5, 50, 5, 50, '{"ai_generation": true, "basic_templates": true, "csv_upload": true, "email_support": false, "priority_support": false, "custom_templates": false, "api_access": false}', true, 1),
('basic', 'Basic Plan', 'Enhanced AI generation with more credits', 9.99, 'USD', 'month', 100, 50, 500, 20, 500, '{"ai_generation": true, "basic_templates": true, "csv_upload": true, "email_support": true, "priority_support": false, "custom_templates": false, "api_access": false}', true, 2),
('pro', 'Pro Plan', 'Professional AI generation with unlimited credits', 29.99, 'USD', 'month', 1000, 200, 2000, 50, 2000, '{"ai_generation": true, "basic_templates": true, "csv_upload": true, "email_support": true, "priority_support": true, "custom_templates": true, "api_access": true}', true, 3),
('enterprise', 'Enterprise Plan', 'Unlimited AI generation with premium features', 99.99, 'USD', 'month', 10000, 1000, 10000, 100, 10000, '{"ai_generation": true, "basic_templates": true, "csv_upload": true, "email_support": true, "priority_support": true, "custom_templates": true, "api_access": true, "white_label": true, "custom_integrations": true}', true, 4)
ON CONFLICT (id) DO NOTHING;
""",

    "003_add_constraints": """
-- Add check constraints
ALTER TABLE subscription_plans ADD CONSTRAINT IF NOT EXISTS check_positive_price CHECK (price >= 0);
ALTER TABLE subscription_plans ADD CONSTRAINT IF NOT EXISTS check_positive_credits CHECK (credits_per_period >= 0);
ALTER TABLE subscription_plans ADD CONSTRAINT IF NOT EXISTS check_positive_batch_limit CHECK (max_products_per_batch >= 0);
ALTER TABLE subscription_plans ADD CONSTRAINT IF NOT EXISTS check_positive_rate_limit CHECK (requests_per_minute > 0);

ALTER TABLE user_credits ADD CONSTRAINT IF NOT EXISTS check_positive_current_credits CHECK (current_credits >= 0);
ALTER TABLE user_credits ADD CONSTRAINT IF NOT EXISTS check_positive_purchased_credits CHECK (total_credits_purchased >= 0);
ALTER TABLE user_credits ADD CONSTRAINT IF NOT EXISTS check_positive_used_credits CHECK (total_credits_used >= 0);

ALTER TABLE payment_history ADD CONSTRAINT IF NOT EXISTS check_positive_amount CHECK (amount >= 0);
ALTER TABLE payment_history ADD CONSTRAINT IF NOT EXISTS check_positive_credits_awarded CHECK (credits_awarded >= 0);

ALTER TABLE usage_logs ADD CONSTRAINT IF NOT EXISTS check_positive_credits_used CHECK (credits_used > 0);
ALTER TABLE usage_logs ADD CONSTRAINT IF NOT EXISTS check_positive_product_count CHECK (product_count > 0);
"""
}


def run_initial_migrations():
    """Run initial migrations to set up the database"""
    manager = MigrationManager()
    
    # Check if we're using SQLite
    from .connection import get_engine
    is_sqlite = "sqlite" in str(get_engine().url)
    
    for version, sql in INITIAL_MIGRATIONS.items():
        if version not in manager.get_applied_migrations():
            # Skip constraint migration for SQLite
            if is_sqlite and version == "003_add_constraints":
                logger.info(f"Skipping constraint migration for SQLite: {version}")
                continue
                
            logger.info(f"Running initial migration: {version}")
            name = version.split('_', 1)[1]
            manager.apply_migration(version, name, sql)
    
    logger.info("Initial migrations completed")
