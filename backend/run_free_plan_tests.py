#!/usr/bin/env python3
"""
Test runner script for Free plan assignment functionality

This script runs all the tests and provides a comprehensive report
of the Free plan assignment system.

Usage:
    python backend/run_free_plan_tests.py
"""

import sys
import os
import subprocess
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_pytest_tests():
    """Run the pytest tests for free plan assignment"""
    logger.info("🧪 Running pytest tests...")
    
    test_file = "backend/tests/test_free_plan_assignment.py"
    
    if not os.path.exists(test_file):
        logger.error(f"❌ Test file not found: {test_file}")
        return False
    
    try:
        # Run pytest with verbose output
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            test_file, 
            "-v", 
            "--tb=short",
            "--color=yes"
        ], capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(__file__)))
        
        logger.info("📊 Test Results:")
        print(result.stdout)
        
        if result.stderr:
            logger.warning("⚠️  Test Warnings/Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            logger.info("✅ All tests passed!")
            return True
        else:
            logger.error(f"❌ Tests failed with return code: {result.returncode}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error running tests: {str(e)}")
        return False


def run_migration_script():
    """Run the migration script to test it"""
    logger.info("🔄 Testing migration script...")
    
    migration_script = "backend/scripts/migrate_free_plan.py"
    
    if not os.path.exists(migration_script):
        logger.error(f"❌ Migration script not found: {migration_script}")
        return False
    
    try:
        # Run the migration script
        result = subprocess.run([
            sys.executable, migration_script
        ], capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(__file__)))
        
        logger.info("📊 Migration Results:")
        print(result.stdout)
        
        if result.stderr:
            logger.warning("⚠️  Migration Warnings/Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            logger.info("✅ Migration script completed successfully!")
            return True
        else:
            logger.error(f"❌ Migration script failed with return code: {result.returncode}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Error running migration script: {str(e)}")
        return False


def check_implementation_files():
    """Check that all required implementation files exist and are properly updated"""
    logger.info("🔍 Checking implementation files...")
    
    required_files = [
        "backend/app/repos/user_repo.py",
        "backend/src/payments/credit_service.py", 
        "backend/src/payments/sqlalchemy_service.py",
        "backend/scripts/migrate_free_plan.py",
        "backend/tests/test_free_plan_assignment.py"
    ]
    
    all_exist = True
    
    for file_path in required_files:
        if os.path.exists(file_path):
            logger.info(f"✅ {file_path} exists")
        else:
            logger.error(f"❌ {file_path} missing")
            all_exist = False
    
    return all_exist


def main():
    """Main test runner function"""
    print("🚀 Free Plan Assignment Test Suite")
    print("=" * 80)
    print(f"Started at: {datetime.now().isoformat()}")
    print()
    
    # Check implementation files
    files_ok = check_implementation_files()
    if not files_ok:
        logger.error("❌ Some implementation files are missing. Please check the setup.")
        return False
    
    print()
    
    # Run pytest tests
    tests_passed = run_pytest_tests()
    
    print()
    
    # Run migration script test
    migration_ok = run_migration_script()
    
    print()
    print("=" * 80)
    print("📊 Final Results:")
    print(f"   Implementation files: {'✅ PASS' if files_ok else '❌ FAIL'}")
    print(f"   Pytest tests: {'✅ PASS' if tests_passed else '❌ FAIL'}")
    print(f"   Migration script: {'✅ PASS' if migration_ok else '❌ FAIL'}")
    
    overall_success = files_ok and tests_passed and migration_ok
    
    if overall_success:
        print("\n🎉 All tests passed! Free plan assignment is working correctly.")
        print("\n📝 Next steps:")
        print("   1. Deploy the changes to your environment")
        print("   2. Run the migration script on your production database")
        print("   3. Test with real users to verify functionality")
        print("   4. Monitor logs for any issues")
    else:
        print("\n⚠️  Some tests failed. Please review the errors above.")
        print("\n🔧 Troubleshooting:")
        print("   1. Check that all dependencies are installed")
        print("   2. Verify database connection is working")
        print("   3. Ensure all required tables exist")
        print("   4. Check that subscription plans are properly initialized")
    
    print("=" * 80)
    return overall_success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


