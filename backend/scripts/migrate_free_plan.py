#!/usr/bin/env python3
"""
Migration script to assign Free plan to existing users without subscriptions

This script finds all existing users who don't have a UserSubscription record
and automatically assigns them the Free tier subscription.

Usage:
    python backend/scripts/migrate_free_plan.py
"""

import sys
import os
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any

# Add the backend directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from database.connection import get_session
from payments.sqlalchemy_service import SQLAlchemyPaymentService
from models.payment_models import User, UserSubscription, UserCredits, SubscriptionStatus

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def find_users_without_subscriptions(session: Session) -> List[str]:
    """Find all user IDs that don't have an active subscription"""
    try:
        # Get all users
        all_users = session.query(User).all()
        user_ids = [user.id for user in all_users]
        
        if not user_ids:
            logger.info("No users found in database")
            return []
        
        # Get users with active subscriptions
        users_with_subscriptions = session.query(UserSubscription.user_id).filter(
            UserSubscription.status == SubscriptionStatus.ACTIVE
        ).distinct().all()
        
        subscribed_user_ids = {sub.user_id for sub in users_with_subscriptions}
        
        # Find users without subscriptions
        users_without_subscriptions = [
            user_id for user_id in user_ids 
            if user_id not in subscribed_user_ids
        ]
        
        logger.info(f"Found {len(user_ids)} total users")
        logger.info(f"Found {len(subscribed_user_ids)} users with subscriptions")
        logger.info(f"Found {len(users_without_subscriptions)} users without subscriptions")
        
        return users_without_subscriptions
        
    except Exception as e:
        logger.error(f"Error finding users without subscriptions: {str(e)}")
        return []


def migrate_user_to_free_plan(session: Session, user_id: str, payment_service: SQLAlchemyPaymentService) -> Dict[str, Any]:
    """Migrate a single user to the free plan"""
    try:
        # Check if user already has a subscription (double-check)
        existing_subscription = payment_service.get_user_subscription(session, user_id)
        if existing_subscription:
            return {
                "user_id": user_id,
                "status": "skipped",
                "reason": f"Already has subscription: {existing_subscription.plan_id}",
                "success": True
            }
        
        # Assign free plan
        success = payment_service.assign_free_plan_to_user(session, user_id)
        
        if success:
            # Verify the assignment
            subscription = payment_service.get_user_subscription(session, user_id)
            user_credits = payment_service.get_user_credits(session, user_id)
            
            return {
                "user_id": user_id,
                "status": "migrated",
                "subscription_plan": subscription.plan_id if subscription else None,
                "credits": user_credits.current_credits if user_credits else 0,
                "success": True
            }
        else:
            return {
                "user_id": user_id,
                "status": "failed",
                "reason": "Failed to assign free plan",
                "success": False
            }
            
    except Exception as e:
        logger.error(f"Error migrating user {user_id}: {str(e)}")
        return {
            "user_id": user_id,
            "status": "error",
            "reason": str(e),
            "success": False
        }


def run_migration() -> Dict[str, Any]:
    """Run the migration for all users without subscriptions"""
    logger.info("🚀 Starting Free Plan Migration")
    logger.info("=" * 60)
    
    migration_results = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "total_users_processed": 0,
        "successful_migrations": 0,
        "skipped_users": 0,
        "failed_migrations": 0,
        "user_results": []
    }
    
    try:
        with get_session() as session:
            payment_service = SQLAlchemyPaymentService()
            
            # Find users without subscriptions
            users_to_migrate = find_users_without_subscriptions(session)
            
            if not users_to_migrate:
                logger.info("✅ No users need migration - all users already have subscriptions")
                migration_results["completed_at"] = datetime.now(timezone.utc).isoformat()
                return migration_results
            
            logger.info(f"📋 Migrating {len(users_to_migrate)} users to Free plan...")
            
            # Migrate each user
            for i, user_id in enumerate(users_to_migrate, 1):
                logger.info(f"Processing user {i}/{len(users_to_migrate)}: {user_id}")
                
                result = migrate_user_to_free_plan(session, user_id, payment_service)
                migration_results["user_results"].append(result)
                migration_results["total_users_processed"] += 1
                
                if result["success"]:
                    if result["status"] == "migrated":
                        migration_results["successful_migrations"] += 1
                        logger.info(f"  ✅ Migrated to Free plan")
                    else:
                        migration_results["skipped_users"] += 1
                        logger.info(f"  ⏭️  Skipped: {result['reason']}")
                else:
                    migration_results["failed_migrations"] += 1
                    logger.error(f"  ❌ Failed: {result['reason']}")
            
            # Commit all changes
            session.commit()
            logger.info("✅ All changes committed to database")
            
    except Exception as e:
        logger.error(f"❌ Migration failed with error: {str(e)}")
        migration_results["error"] = str(e)
        return migration_results
    
    migration_results["completed_at"] = datetime.now(timezone.utc).isoformat()
    
    # Log summary
    logger.info("\n" + "=" * 60)
    logger.info("📊 Migration Summary:")
    logger.info(f"   Total users processed: {migration_results['total_users_processed']}")
    logger.info(f"   Successful migrations: {migration_results['successful_migrations']}")
    logger.info(f"   Skipped users: {migration_results['skipped_users']}")
    logger.info(f"   Failed migrations: {migration_results['failed_migrations']}")
    logger.info("=" * 60)
    
    return migration_results


def verify_migration() -> bool:
    """Verify that the migration was successful"""
    logger.info("🔍 Verifying migration results...")
    
    try:
        with get_session() as session:
            payment_service = SQLAlchemyPaymentService()
            
            # Check if any users still lack subscriptions
            users_without_subscriptions = find_users_without_subscriptions(session)
            
            if not users_without_subscriptions:
                logger.info("✅ Verification passed - all users now have subscriptions")
                return True
            else:
                logger.warning(f"⚠️  Verification failed - {len(users_without_subscriptions)} users still lack subscriptions")
                for user_id in users_without_subscriptions[:5]:  # Show first 5
                    logger.warning(f"   - {user_id}")
                if len(users_without_subscriptions) > 5:
                    logger.warning(f"   ... and {len(users_without_subscriptions) - 5} more")
                return False
                
    except Exception as e:
        logger.error(f"❌ Verification failed with error: {str(e)}")
        return False


if __name__ == "__main__":
    print("🔄 Free Plan Migration Script")
    print("=" * 80)
    
    # Run the migration
    results = run_migration()
    
    # Verify the results
    verification_passed = verify_migration()
    
    # Final status
    print("\n" + "=" * 80)
    if verification_passed and results.get("failed_migrations", 0) == 0:
        print("🎉 Migration completed successfully!")
        print("✅ All users now have Free plan subscriptions")
    else:
        print("⚠️  Migration completed with issues")
        if results.get("failed_migrations", 0) > 0:
            print(f"❌ {results['failed_migrations']} users failed to migrate")
        if not verification_passed:
            print("❌ Verification failed - some users may still lack subscriptions")
    
    print("\n📝 Next steps:")
    print("   1. Test the application with migrated users")
    print("   2. Verify that users can generate AI descriptions")
    print("   3. Check that daily limits are enforced correctly")
    print("   4. Monitor logs for any issues")


