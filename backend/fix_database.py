#!/usr/bin/env python3
"""
Fix database by creating missing tables
This script creates the missing subscriptions table and other required tables
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def get_database_url():
    """Get database URL from environment variables"""
    # Try different possible environment variable names
    db_url = os.getenv('DATABASE_URL') or os.getenv('DB_URL') or os.getenv('POSTGRES_URL')
    
    if not db_url:
        print("❌ No database URL found in environment variables")
        print("Available environment variables:")
        for key, value in os.environ.items():
            if 'DATABASE' in key.upper() or 'DB' in key.upper() or 'POSTGRES' in key.upper():
                print(f"  {key}: {value[:50]}...")
        return None
    
    print(f"✅ Found database URL: {db_url[:50]}...")
    return db_url

def create_tables(engine):
    """Create the missing tables"""
    try:
        with engine.connect() as conn:
            # Create subscriptions table
            print("🔄 Creating subscriptions table...")
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS subscriptions (
                    id SERIAL PRIMARY KEY,
                    user_id VARCHAR NOT NULL,
                    provider VARCHAR NOT NULL DEFAULT 'lemon_squeezy',
                    plan VARCHAR NOT NULL,
                    status VARCHAR NOT NULL,
                    current_period_end TIMESTAMP WITH TIME ZONE,
                    lemon_squeezy_customer_id VARCHAR,
                    lemon_squeezy_subscription_id VARCHAR,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
                    updated_at TIMESTAMP WITH TIME ZONE
                )
            """))
            
            # Create indexes
            print("🔄 Creating indexes...")
            conn.execute(text("CREATE INDEX IF NOT EXISTS ix_subscriptions_user_id ON subscriptions (user_id)"))
            conn.execute(text("CREATE INDEX IF NOT EXISTS ix_subscriptions_status ON subscriptions (status)"))
            
            # Create webhook_events table
            print("🔄 Creating webhook_events table...")
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS webhook_events (
                    id SERIAL PRIMARY KEY,
                    event_id VARCHAR NOT NULL UNIQUE,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL
                )
            """))
            
            # Create transactions table
            print("🔄 Creating transactions table...")
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id SERIAL PRIMARY KEY,
                    user_id VARCHAR NOT NULL,
                    provider VARCHAR NOT NULL DEFAULT 'lemon_squeezy',
                    provider_ref VARCHAR NOT NULL,
                    amount NUMERIC(10, 2) NOT NULL,
                    currency VARCHAR(10) NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL
                )
            """))
            
            # Create usage table
            print("🔄 Creating usage table...")
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS usage (
                    id SERIAL PRIMARY KEY,
                    user_id VARCHAR NOT NULL,
                    key VARCHAR NOT NULL,
                    value INTEGER NOT NULL DEFAULT 0,
                    period VARCHAR NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
                    UNIQUE(user_id, key, period)
                )
            """))
            
            # Create user_credits table if it doesn't exist
            print("🔄 Creating user_credits table...")
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS user_credits (
                    id SERIAL PRIMARY KEY,
                    user_id VARCHAR NOT NULL UNIQUE,
                    credits INTEGER NOT NULL DEFAULT 0,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL
                )
            """))
            
            conn.commit()
            print("✅ All tables created successfully!")
            return True
            
    except SQLAlchemyError as e:
        print(f"❌ Error creating tables: {e}")
        return False

def main():
    """Main function"""
    print("🔧 Database Fix Script")
    print("=" * 50)
    
    # Get database URL
    db_url = get_database_url()
    if not db_url:
        sys.exit(1)
    
    # Create engine
    try:
        engine = create_engine(db_url)
        print("✅ Database connection established")
    except Exception as e:
        print(f"❌ Failed to connect to database: {e}")
        sys.exit(1)
    
    # Create tables
    if create_tables(engine):
        print("🎉 Database fix completed successfully!")
        sys.exit(0)
    else:
        print("💥 Database fix failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()

