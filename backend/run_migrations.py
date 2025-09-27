#!/usr/bin/env python3
"""
Database migration runner for Render deployment
"""
import os
import sys
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from alembic.config import Config
from alembic import command

def run_migrations():
    """Run database migrations"""
    try:
        # Set up Alembic configuration
        alembic_cfg = Config(str(backend_dir / "alembic.ini"))
        
        # Check current revision first
        print("🔄 Checking current database state...")
        try:
            command.current(alembic_cfg)
        except:
            print("📝 No current revision found, initializing...")
        
        # Run migrations with error handling
        print("🔄 Running database migrations...")
        try:
            command.upgrade(alembic_cfg, "head")
            print("✅ Database migrations completed successfully!")
        except Exception as migration_error:
            print(f"⚠️ Migration error: {str(migration_error)}")
            print("🔄 Attempting to continue with existing schema...")
            
            # Check if we can connect and basic tables exist
            from src.database.connection import get_db
            from sqlalchemy import text
            
            try:
                db = next(get_db())
                # Test if basic tables exist
                result = db.execute(text("SELECT 1 FROM subscription_plans LIMIT 1"))
                print("✅ Database tables appear to exist, continuing...")
            except Exception as db_error:
                print(f"❌ Database connection failed: {str(db_error)}")
                raise migration_error
        
    except Exception as e:
        print(f"❌ Migration failed: {str(e)}")
        print("🔄 Attempting to use simple database initialization...")
        
        # Fallback to simple initialization
        try:
            from init_db import init_database
            if init_database():
                print("✅ Database initialized with simple script!")
            else:
                print("❌ Simple initialization also failed")
                sys.exit(1)
        except Exception as init_error:
            print(f"❌ Simple initialization failed: {str(init_error)}")
            sys.exit(1)

if __name__ == "__main__":
    run_migrations()
