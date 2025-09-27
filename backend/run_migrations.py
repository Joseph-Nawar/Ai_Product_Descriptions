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
        
        # Run migrations
        print("🔄 Running database migrations...")
        command.upgrade(alembic_cfg, "head")
        print("✅ Database migrations completed successfully!")
        
    except Exception as e:
        print(f"❌ Migration failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_migrations()
