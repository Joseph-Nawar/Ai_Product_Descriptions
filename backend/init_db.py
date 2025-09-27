#!/usr/bin/env python3
"""
Simple database initialization script for Render
"""
import os
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from sqlalchemy import create_engine, text
from src.database.config import get_database_url

def init_database():
    """Initialize database with basic tables"""
    try:
        # Get database URL
        database_url = get_database_url()
        if not database_url:
            print("❌ DATABASE_URL not found")
            return False
            
        # Create engine
        engine = create_engine(database_url)
        
        print("🔄 Initializing database...")
        
        # Create basic tables
        with engine.connect() as conn:
            # Create subscription_plans table
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS subscription_plans (
                    id VARCHAR(50) PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    price DECIMAL(10,2) NOT NULL DEFAULT 0,
                    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
                    billing_interval VARCHAR(20) NOT NULL DEFAULT 'monthly',
                    credits_per_period INTEGER NOT NULL DEFAULT 0,
                    max_products_per_batch INTEGER NOT NULL DEFAULT 5,
                    max_api_calls_per_day INTEGER,
                    requests_per_minute INTEGER,
                    requests_per_hour INTEGER,
                    features JSONB,
                    lemon_squeezy_variant_id VARCHAR(50),
                    lemon_squeezy_product_id VARCHAR(50),
                    is_active BOOLEAN NOT NULL DEFAULT true,
                    sort_order INTEGER NOT NULL DEFAULT 0,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                )
            """))
            
            # Create users table
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS users (
                    id VARCHAR(50) PRIMARY KEY,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    firebase_uid VARCHAR(255) UNIQUE NOT NULL,
                    subscription_plan_id VARCHAR(50) NOT NULL DEFAULT 'free',
                    credits_remaining INTEGER NOT NULL DEFAULT 0,
                    credits_used INTEGER NOT NULL DEFAULT 0,
                    is_active BOOLEAN NOT NULL DEFAULT true,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    FOREIGN KEY (subscription_plan_id) REFERENCES subscription_plans(id)
                )
            """))
            
            # Create usage_records table
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS usage_records (
                    id SERIAL PRIMARY KEY,
                    user_id VARCHAR(50) NOT NULL,
                    operation_type VARCHAR(50) NOT NULL,
                    credits_used INTEGER NOT NULL DEFAULT 0,
                    details JSONB,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """))
            
            # Create or recreate user_subscriptions table
            conn.execute(text("DROP TABLE IF EXISTS user_subscriptions CASCADE"))
            conn.execute(text("""
                CREATE TABLE user_subscriptions (
                    id VARCHAR(100) PRIMARY KEY,
                    user_id VARCHAR(50) NOT NULL,
                    plan_id VARCHAR(50) NOT NULL,
                    status VARCHAR(20) NOT NULL DEFAULT 'active',
                    current_period_start TIMESTAMP WITH TIME ZONE,
                    current_period_end TIMESTAMP WITH TIME ZONE,
                    cancel_at_period_end BOOLEAN NOT NULL DEFAULT false,
                    lemon_squeezy_subscription_id VARCHAR(100),
                    lemon_squeezy_customer_id VARCHAR(100),
                    trial_start TIMESTAMP WITH TIME ZONE,
                    trial_end TIMESTAMP WITH TIME ZONE,
                    subscription_metadata JSONB,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (plan_id) REFERENCES subscription_plans(id)
                )
            """))
            
            # Create or recreate user_credits table
            conn.execute(text("DROP TABLE IF EXISTS user_credits CASCADE"))
            conn.execute(text("""
                CREATE TABLE user_credits (
                    user_id VARCHAR(50) PRIMARY KEY,
                    current_credits INTEGER NOT NULL DEFAULT 0,
                    total_credits_purchased INTEGER NOT NULL DEFAULT 0,
                    total_credits_used INTEGER NOT NULL DEFAULT 0,
                    total_credits_expired INTEGER NOT NULL DEFAULT 0,
                    subscription_id VARCHAR(100),
                    last_credit_refill TIMESTAMP WITH TIME ZONE,
                    next_credit_refill TIMESTAMP WITH TIME ZONE,
                    credits_used_this_period INTEGER NOT NULL DEFAULT 0,
                    period_start TIMESTAMP WITH TIME ZONE,
                    period_end TIMESTAMP WITH TIME ZONE,
                    credits_metadata JSONB,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (subscription_id) REFERENCES user_subscriptions(id)
                )
            """))
            
            # Create or recreate transactions table
            conn.execute(text("DROP TABLE IF EXISTS transactions CASCADE"))
            conn.execute(text("""
                CREATE TABLE transactions (
                    id SERIAL PRIMARY KEY,
                    user_id VARCHAR(50) NOT NULL,
                    subscription_id VARCHAR(100),
                    lemon_squeezy_order_id VARCHAR(100),
                    lemon_squeezy_order_number VARCHAR(100),
                    amount DECIMAL(10,2) NOT NULL,
                    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
                    status VARCHAR(20) NOT NULL,
                    payment_method VARCHAR(50),
                    transaction_metadata JSONB,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (subscription_id) REFERENCES user_subscriptions(id)
                )
            """))
            
            # Create or recreate webhook_events table
            conn.execute(text("DROP TABLE IF EXISTS webhook_events CASCADE"))
            conn.execute(text("""
                CREATE TABLE webhook_events (
                    id SERIAL PRIMARY KEY,
                    event_id VARCHAR(100) UNIQUE NOT NULL,
                    event_type VARCHAR(50) NOT NULL,
                    event_data JSONB NOT NULL,
                    processed BOOLEAN NOT NULL DEFAULT false,
                    processing_error TEXT,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    processed_at TIMESTAMP WITH TIME ZONE
                )
            """))
            
            # Create or recreate usage_logs table
            conn.execute(text("DROP TABLE IF EXISTS usage_logs CASCADE"))
            conn.execute(text("""
                CREATE TABLE usage_logs (
                    id SERIAL PRIMARY KEY,
                    user_id VARCHAR(50) NOT NULL,
                    usage_type VARCHAR(50) NOT NULL,
                    credits_used INTEGER NOT NULL DEFAULT 0,
                    product_count INTEGER NOT NULL DEFAULT 0,
                    language_code VARCHAR(10),
                    category VARCHAR(100),
                    tokens_used INTEGER,
                    response_time_ms INTEGER,
                    cost_usd DECIMAL(10,4),
                    request_id VARCHAR(100),
                    batch_id VARCHAR(100),
                    endpoint_used VARCHAR(100),
                    user_credits_id VARCHAR(50),
                    usage_metadata JSONB,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """))
            
            # Insert default subscription plans
            conn.execute(text("""
                INSERT INTO subscription_plans (id, name, description, price, credits_per_period, max_products_per_batch, features, lemon_squeezy_variant_id, sort_order)
                VALUES 
                    ('free', 'Free Plan', 'Basic AI product description generation', 0.00, 10, 5, '{"ai_generation": true, "basic_templates": true, "csv_upload": true, "email_support": false}', NULL, 1),
                    ('pro', 'Pro Plan', 'Enhanced AI generation with more credits', 19.99, 100, 50, '{"ai_generation": true, "basic_templates": true, "csv_upload": true, "email_support": true, "priority_support": true, "custom_templates": true}', '1013286', 2),
                    ('enterprise', 'Enterprise Plan', 'Unlimited AI generation for businesses', 99.99, 1000, 200, '{"ai_generation": true, "basic_templates": true, "csv_upload": true, "email_support": true, "priority_support": true, "custom_templates": true, "api_access": true}', '1013276', 3),
                    ('pro-yearly', 'Pro Yearly Plan', 'Pro plan with yearly billing', 199.99, 1200, 50, '{"ai_generation": true, "basic_templates": true, "csv_upload": true, "email_support": true, "priority_support": true, "custom_templates": true}', '1013282', 4)
                ON CONFLICT (id) DO NOTHING
            """))
            
            conn.commit()
            
        print("✅ Database initialized successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Database initialization failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = init_database()
    sys.exit(0 if success else 1)
