# Free Plan Assignment and Credit Validation Bug Fixes

## Summary

Fixed critical bugs in the Free plan assignment and credit validation system that were preventing users from using the AI generation service.

## Issues Fixed

### 1. Datetime Comparison Error

**Problem**: `can't compare offset-naive and offset-aware datetimes`
**Root Cause**: Mixing naive `datetime.now()` with timezone-aware values
**Solution**: Standardized all datetime operations to use `datetime.now(timezone.utc)`

**Files Modified**:

- `backend/src/payments/sqlalchemy_service.py`
  - `get_daily_usage_count()` - Fixed timezone handling
  - `create_user_credits()` - Fixed timezone handling
  - `create_user_subscription()` - Fixed timezone handling

### 2. SQLAlchemy Session Misuse

**Problem**: `'generator' object does not support the context manager protocol`
**Root Cause**: Using `with sessionmaker()` instead of `with SessionLocal()`
**Solution**: Updated session creation to use proper session factory

**Files Modified**:

- `backend/src/payments/sqlalchemy_service.py`
  - `get_user_credits()` - Fixed session creation
  - `get_user_subscription()` - Fixed session creation
  - `assign_free_plan_to_user()` - Fixed session creation

### 3. Incorrect Credit Check

**Problem**: `'UserCredits' object has no attribute 'subscription_tier'`
**Root Cause**: Trying to read subscription tier from UserCredits instead of UserSubscription
**Solution**: Updated credit service to use `subscription.plan_id` for tier checks

**Files Modified**:

- `backend/src/payments/credit_service.py`
  - Replaced `tier_limits` with `plan_limits` dictionary
  - Updated all references from `user_credits.subscription_tier` to `subscription.plan_id`
  - Fixed error messages to use correct plan ID

### 4. Free Plan Users Still Blocked

**Problem**: Credit service raises 402 Payment Required even though Free users have 2 daily credits
**Root Cause**: Incorrect plan ID usage and missing subscription assignment
**Solution**:

- Fixed plan ID resolution in credit service
- Ensured proper Free plan assignment
- Updated daily limit checking logic

**Files Modified**:

- `backend/src/payments/credit_service.py`
  - Fixed plan ID resolution: `plan_id = subscription.plan_id if subscription else "free"`
  - Updated all error messages to use correct plan ID
  - Fixed daily limit checking logic

### 5. Helper Function Updates

**Problem**: `assign_free_plan_to_user()` not properly linking UserCredits to UserSubscription
**Solution**: Enhanced helper to properly link credits to subscription

**Files Modified**:

- `backend/src/payments/sqlalchemy_service.py`
  - `assign_free_plan_to_user()` - Added proper linking of UserCredits to UserSubscription
  - `create_user_subscription()` - Returns actual subscription object instead of dictionary

## Testing Updates

**Files Modified**:

- `backend/tests/test_free_plan_assignment.py`
  - Added assertions for `subscription_tier` in all test cases
  - Updated tests to verify correct plan ID usage
  - Enhanced test coverage for Free plan functionality

## Key Changes Made

### 1. Datetime Handling

```python
# Before (naive datetime)
today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

# After (timezone-aware)
now = datetime.now(timezone.utc)
today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
```

### 2. Session Management

```python
# Before (incorrect)
from src.database.connection import get_session
with get_session() as new_session:

# After (correct)
from src.database.connection import get_session_factory
SessionLocal = get_session_factory()
with SessionLocal() as new_session:
```

### 3. Plan ID Resolution

```python
# Before (incorrect)
tier_limit = self.tier_limits.get(user_credits.subscription_tier, 10)

# After (correct)
plan_id = subscription.plan_id if subscription else "free"
plan_limit = self.plan_limits.get(plan_id, 10)
```

### 4. Free Plan Assignment

```python
# Enhanced to properly link credits to subscription
def assign_free_plan_to_user(self, session: Session = None, user_id: str = None) -> bool:
    # ... existing logic ...

    # Link user credits to subscription
    user_credits.subscription_id = subscription.id
    session.flush()

    return True
```

## Verification

The fixes ensure that:

1. **New Free users** can generate 2 times per day without payment
2. **Existing users without subscriptions** are automatically assigned Free plan
3. **Daily limits are properly enforced** based on subscription plan
4. **Timezone handling is consistent** across all datetime operations
5. **Session management is correct** for all database operations
6. **Plan ID resolution is accurate** for all subscription tiers

## Testing

Run the updated tests to verify all fixes:

```bash
cd backend
python -m pytest tests/test_free_plan_assignment.py -v
```

## Deployment Checklist

- [ ] Deploy updated backend code
- [ ] Run migration script for existing users: `python scripts/migrate_free_plan.py`
- [ ] Monitor logs for successful Free plan assignments
- [ ] Verify Free users can generate 2 times per day
- [ ] Verify Free users are blocked after 2 generations
- [ ] Test Pro/Enterprise plans have higher limits

## Monitoring

Watch for these log messages:

- `"Successfully assigned free plan to user {user_id}"`
- `"Daily generation limit exceeded. Used: {count}, Limit: {limit}"`
- `"No subscription found for user {user_id}, assigning free plan"`

## Security Notes

- All datetime operations are now timezone-aware
- Session management follows proper SQLAlchemy patterns
- Plan ID resolution is consistent and secure
- Free plan assignment is idempotent and safe to run multiple times


