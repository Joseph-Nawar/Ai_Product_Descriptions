# backend/src/payments/endpoints.py
"""
Payment API endpoints for Lemon Squeezy integration with comprehensive security
"""

import logging
from typing import Dict, Any, Optional
from fastapi import APIRouter, HTTPException, Depends, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid

from .lemon_squeezy import LemonSqueezyService
from .models import UserCredits, PaymentHistory
from .security import PaymentSecurityService, AuditEventType, SecurityLevel
from .rate_limiting import rate_limiting_service
from .secure_operations import SecurePaymentOperations
from ..auth.firebase import get_current_user
from ..auth.deps import get_authed_user_db
from src.database.deps import get_db
from app.services.billing_service import BillingService
from sqlalchemy.orm import Session
import json

logger = logging.getLogger(__name__)

# Create router for payment endpoints
router = APIRouter(prefix="/api/payment", tags=["payments"])

# Initialize services
lemon_squeezy = LemonSqueezyService()
security_service = PaymentSecurityService()
secure_operations = SecurePaymentOperations(lemon_squeezy.db_service, security_service)


class CheckoutRequest(BaseModel):
    """Request model for creating checkout session"""
    variant_id: str
    success_url: str
    cancel_url: str

    class Config:
        schema_extra = {
            "example": {
                "variant_id": "1009476",
                "success_url": "https://yourapp.com/payment/success",
                "cancel_url": "https://yourapp.com/payment/cancel"
            }
        }


class WebhookRequest(BaseModel):
    """Request model for webhook processing"""
    payload: str
    signature: str


class CreditCheckRequest(BaseModel):
    """Request model for credit checking"""
    batch_size: int = 1

    class Config:
        schema_extra = {
            "example": {
                "batch_size": 5
            }
        }


class CreditDeductionRequest(BaseModel):
    """Request model for credit deduction"""
    amount: int = 1
    operation_context: Optional[Dict[str, Any]] = None

    class Config:
        schema_extra = {
            "example": {
                "amount": 1,
                "operation_context": {
                    "product_generation": True,
                    "batch_id": "batch_123"
                }
            }
        }


def get_client_info(request: Request) -> Dict[str, Any]:
    """Extract client information from request"""
    return {
        "ip_address": request.client.host,
        "user_agent": request.headers.get("user-agent", ""),
        "correlation_id": request.headers.get("x-correlation-id", str(uuid.uuid4()))
    }


@router.get("/plans")
async def get_subscription_plans(request: Request, db: Session = Depends(get_db)):
    """Get available subscription plans with rate limiting and env variant IDs"""
    client_info = get_client_info(request)
    
    # Check rate limits
    allowed, rate_info = rate_limiting_service.check_rate_limit(
        endpoint="subscription",
        user_id="anonymous",  # Anonymous endpoint
        ip_address=client_info["ip_address"]
    )
    
    if not allowed:
        security_service.log_audit_event(
            event_type=AuditEventType.RATE_LIMIT_EXCEEDED,
            ip_address=client_info["ip_address"],
            event_data=rate_info,
            security_level=SecurityLevel.MEDIUM,
            success=False,
            correlation_id=client_info["correlation_id"]
        )
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Please try again later.",
            headers={"X-RateLimit-Info": str(rate_info)}
        )
    
    try:
        import os
        pro_id = os.getenv("LEMON_SQUEEZY_VARIANT_ID_PRO")
        enterprise_id = os.getenv("LEMON_SQUEEZY_VARIANT_ID_ENTERPRISE")
        yearly_id = os.getenv("LEMON_SQUEEZY_VARIANT_ID_YEARLY")
        store_id = os.getenv("LEMON_SQUEEZY_STORE_ID")
        # Return complete plan data with all required fields
        plans = await lemon_squeezy.get_subscription_plans(db_session=db)
        
        # Override variant IDs from environment if available
        for plan in plans:
            if plan["id"] == "pro" and pro_id:
                plan["lemon_squeezy_variant_id"] = pro_id
            elif plan["id"] == "enterprise" and enterprise_id:
                plan["lemon_squeezy_variant_id"] = enterprise_id
            elif plan["id"] == "pro-yearly" and yearly_id:
                plan["lemon_squeezy_variant_id"] = yearly_id
            # Free plan doesn't need a variant ID (it's not purchasable)
        
        security_service.log_audit_event(
            event_type=AuditEventType.SUBSCRIPTION_CREATED,
            ip_address=client_info["ip_address"],
            event_data={"plans_count": len(plans)},
            security_level=SecurityLevel.LOW,
            success=True,
            correlation_id=client_info["correlation_id"]
        )
        
        return {
            "success": True,
            "plans": plans,
            "rate_limit_info": rate_info
        }
    except Exception as e:
        logger.error(f"Error getting subscription plans: {str(e)}")
        security_service.log_audit_event(
            event_type=AuditEventType.SUBSCRIPTION_CREATED,
            ip_address=client_info["ip_address"],
            event_data={"error": str(e)},
            security_level=SecurityLevel.HIGH,
            success=False,
            error_message=str(e),
            correlation_id=client_info["correlation_id"]
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get subscription plans: {str(e)}"
        )


@router.post("/checkout")
async def create_checkout_session(
    request_data: CheckoutRequest,
    request: Request,
    auth = Depends(get_authed_user_db),
    db: Session = Depends(get_db)
):
    """Create a checkout session for subscription purchase with comprehensive security"""
    
    print("🎯 STEP 1: CREATE_CHECKOUT ENDPOINT CALLED")
    print(f"Request data: {request_data}")
    print(f"Variant ID: {request_data.variant_id}")
    print(f"Success URL: {request_data.success_url}")
    print(f"Cancel URL: {request_data.cancel_url}")
    
    try:
        print("🎯 STEP 2: GETTING CLIENT INFO")
        client_info = get_client_info(request)
        print(f"Client info: {client_info}")
        
        print("🎯 STEP 3: EXTRACTING AUTH DATA")
        claims = auth["claims"]
        user_row = auth["user"]
        user_id = claims.get("uid")
        print(f"User ID: {user_id}")
        print(f"User email: {user_row.email if user_row else 'None'}")
        
        print("🎯 STEP 4: VALIDATING USER")
        if not user_id:
            print("❌ STEP 4 FAILED: No user ID found")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User ID not found in token"
            )
        print("✅ STEP 4 SUCCESS: User validated")
        
        print("🎯 STEP 5: VALIDATING VARIANT ID")
        if not request_data.variant_id:
            print("❌ STEP 5 FAILED: No variant ID provided")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Variant ID is required"
            )
        print("✅ STEP 5 SUCCESS: Variant ID validated")
        
        print("🎯 STEP 6: CALLING LEMON_SQUEEZY SERVICE")
        try:
            result = await lemon_squeezy.create_checkout_session(
                user_id=user_id,
                user_email=user_row.email,
                variant_id=request_data.variant_id,
                success_url=request_data.success_url,
                cancel_url=request_data.cancel_url
            )
            print("✅ STEP 6 SUCCESS: Lemon Squeezy service call successful")
            print(f"Result: {result}")
            return result
            
        except Exception as e:
            print("❌ STEP 6 FAILED: Lemon Squeezy service call failed")
            print(f"Error type: {type(e).__name__}")
            print(f"Error message: {str(e)}")
            import traceback
            print(f"Full traceback: {traceback.format_exc()}")
            raise
            
    except Exception as e:
        print("=== CHECKOUT ENDPOINT ERROR ===")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        raise


@router.post("/webhook")
async def handle_webhook(request: Request, db: Session = Depends(get_db)):
    """Handle Lemon Squeezy webhook events with enhanced security"""
    print(f"🎯 WEBHOOK RECEIVED: {request.method} {request.url}")
    print(f"🎯 WEBHOOK HEADERS: {dict(request.headers)}")
    
    client_info = get_client_info(request)
    
    # Check rate limits for webhooks
    allowed, rate_info = rate_limiting_service.check_rate_limit(
        endpoint="webhook",
        user_id="webhook_system",
        ip_address=client_info["ip_address"]
    )
    
    if not allowed:
        security_service.log_audit_event(
            event_type=AuditEventType.RATE_LIMIT_EXCEEDED,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data=rate_info,
            security_level=SecurityLevel.HIGH,
            success=False,
            correlation_id=client_info["correlation_id"]
        )
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Webhook rate limit exceeded"
        )
    
    try:
        # Get raw body and signature
        body = await request.body()
        signature = request.headers.get("x-signature", "")
        
        if not signature:
            security_service.log_audit_event(
                event_type=AuditEventType.WEBHOOK_VERIFICATION_FAILED,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data={"error": "missing_signature"},
                security_level=SecurityLevel.HIGH,
                success=False,
                error_message="Missing signature header",
                correlation_id=client_info["correlation_id"]
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Missing signature header"
            )
        
        # Validate IP address (if configured)
        if not security_service.validate_ip_address(client_info["ip_address"]):
            security_service.log_audit_event(
                event_type=AuditEventType.SECURITY_VIOLATION,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data={"violation_type": "unauthorized_ip"},
                security_level=SecurityLevel.CRITICAL,
                success=False,
                error_message="Unauthorized IP address",
                correlation_id=client_info["correlation_id"]
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Unauthorized IP address"
            )
        
        # Verify webhook signature
        payload_str = body.decode("utf-8")
        is_valid_signature = security_service.verify_webhook_signature(payload_str, signature)
        
        if not is_valid_signature:
            security_service.log_audit_event(
                event_type=AuditEventType.WEBHOOK_VERIFICATION_FAILED,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data={"error": "invalid_signature"},
                security_level=SecurityLevel.CRITICAL,
                success=False,
                error_message="Invalid webhook signature",
                correlation_id=client_info["correlation_id"]
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid webhook signature"
            )
        
        # Compute deterministic event id for idempotency
        try:
            payload_json = json.loads(payload_str)
        except Exception:
            payload_json = {}
        event_id = (
            payload_json.get("meta", {}).get("event_id")
            or request.headers.get("x-event-id")
            or signature
        )

        # Idempotent handle via billing service; process minimal state transitions
        BillingService(db).handle_webhook(event_id, payload_json)

        # Note: Removed legacy processor to avoid database session conflicts
        # The BillingService handles all webhook processing now
        result = {"success": True, "message": "Webhook processed by BillingService"}
        
        if result["success"]:
            security_service.log_audit_event(
                event_type=AuditEventType.WEBHOOK_PROCESSED,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data={
                    "webhook_type": result.get("event_type", "unknown"),
                    "user_id": result.get("user_id")
                },
                security_level=SecurityLevel.MEDIUM,
                success=True,
                correlation_id=client_info["correlation_id"]
            )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "success": True, 
                    "message": "Webhook processed successfully",
                    "correlation_id": client_info["correlation_id"]
                }
            )
        else:
            error_msg = result.get('error', 'Unknown error')
            logger.error(f"Webhook processing failed: {error_msg}")
            security_service.log_audit_event(
                event_type=AuditEventType.WEBHOOK_VERIFICATION_FAILED,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data={"error": error_msg},
                security_level=SecurityLevel.HIGH,
                success=False,
                error_message=error_msg,
                correlation_id=client_info["correlation_id"]
            )
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "success": False, 
                    "error": error_msg,
                    "correlation_id": client_info["correlation_id"]
                }
            )
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        security_service.log_audit_event(
            event_type=AuditEventType.WEBHOOK_VERIFICATION_FAILED,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data={"error": str(e)},
            security_level=SecurityLevel.CRITICAL,
            success=False,
            error_message=str(e),
            correlation_id=client_info["correlation_id"]
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Webhook processing failed: {str(e)}"
        )


@router.get("/user/subscription")
async def get_user_subscription(auth = Depends(get_authed_user_db), db: Session = Depends(get_db)):
    """Get user's current subscription details (returns free tier if none exists)"""
    try:
        claims = auth["claims"]
        user_row = auth["user"]
        user_id = claims.get("uid")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User ID not found in token",
            )

        # Get subscription info
        subscription = lemon_squeezy.db_service.get_user_subscription(user_id, db)
        
        # Add comprehensive debugging information
        logger.info(f"🔍 Subscription lookup for user {user_id}: found={subscription is not None}")
        if subscription:
            logger.info(f"🔍 Subscription details: plan_id={subscription.plan_id}, status={subscription.status}, is_active={subscription.is_active()}")
            logger.info(f"🔍 Full subscription object: {subscription}")
        else:
            logger.warning(f"🔍 No subscription found for user {user_id}")
            # Let's also check what's in the database
            from src.models.payment_models import UserSubscription
            all_subs = db.query(UserSubscription).filter(UserSubscription.user_id == user_id).all()
            logger.info(f"🔍 All subscriptions for user {user_id}: {[{'id': sub.id, 'plan_id': sub.plan_id, 'status': sub.status} for sub in all_subs]}")
            
            # Let's also check if there are any subscriptions at all in the database
            total_subs = db.query(UserSubscription).count()
            logger.info(f"🔍 Total subscriptions in database: {total_subs}")
            
            # Let's check the exact query being used
            query = db.query(UserSubscription).filter(UserSubscription.user_id == user_id)
            logger.info(f"🔍 Query SQL: {query}")
            
            # Let's also check if there's a database session issue
            try:
                # Try to execute the query directly
                result = db.execute(query)
                logger.info(f"🔍 Direct query result: {result.fetchall()}")
            except Exception as e:
                logger.error(f"🔍 Direct query error: {str(e)}")
            
            # Let's also check if there's a database transaction issue
            try:
                # Check if we're in a transaction
                logger.info(f"🔍 Database in transaction: {db.in_transaction()}")
                logger.info(f"🔍 Database is active: {db.is_active}")
            except Exception as e:
                logger.error(f"🔍 Database transaction check error: {str(e)}")
            
            # Let's also check if there's a database connection issue
            try:
                from sqlalchemy import text
                db.execute(text("SELECT 1"))
                logger.info("🔍 Database connection is working")
            except Exception as e:
                logger.error(f"🔍 Database connection error: {str(e)}")
        
        if not subscription:
            # User has no subscription - return free tier details
            # This should not happen if assign_free_plan_to_user is working correctly
            # but we'll handle it gracefully
            logger.warning(f"User {user_id} has no subscription record, returning free tier")
            return {
                "success": True,
                "data": {
                    "id": f"free_{user_id}",
                    "user_id": user_id,
                    "plan_id": "free",
                    "status": "active",
                    "current_period_start": None,
                    "current_period_end": None,
                    "cancel_at_period_end": False,
                    "lemon_squeezy_subscription_id": None,
                    "lemon_squeezy_customer_id": None,
                    "trial_start": None,
                    "trial_end": None,
                    "subscription_metadata": {},
                    "created_at": None,
                    "updated_at": None,
                    "is_trial": False,
                    "is_active": True
                }
            }

        # Return subscription data
        subscription_data = subscription.to_dict()
        subscription_data.update({
            "is_trial": subscription.trial_start is not None,
            "is_active": subscription.is_active()
        })

        response_data = {
            "success": True,
            "data": subscription_data,
        }
        
        # Log the response data for debugging
        logger.info(f"🔍 Returning subscription data: {response_data}")
        
        return response_data

    except Exception as e:
        logger.error(f"Error getting user subscription: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get user subscription: {str(e)}",
        )


@router.get("/user/credits")
async def get_user_credits(auth = Depends(get_authed_user_db), db: Session = Depends(get_db)):
    """Get user's current credits and subscription status with daily credits remaining"""
    try:
        logger.info(f"🔍 Credits endpoint called - auth: {auth is not None}")
        claims = auth["claims"]
        user_row = auth["user"]
        user_id = claims.get("uid")
        logger.info(f"🔍 User ID from claims: {user_id}")
        logger.info(f"🔍 User row: {user_row}")
        
        if not user_id:
            logger.error("❌ No user ID found in claims")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User ID not found in token",
            )

        # Get user credits with error handling
        try:
            user_credits = lemon_squeezy.db_service.get_user_credits(user_id, db)
            if not user_credits:
                # Create new user with free tier
                logger.info(f"🔍 Creating new user credits for {user_id}")
                user_credits = lemon_squeezy.db_service.create_user_credits(db, user_id, "free")
        except Exception as db_error:
            logger.error(f"❌ Database error getting user credits: {str(db_error)}")
            # Return fallback data for free tier
            user_credits = type('obj', (object,), {
                'to_dict': lambda: {
                    'user_id': user_id,
                    'current_credits': 10,
                    'total_credits_purchased': 0,
                    'total_credits_used': 0,
                    'total_credits_expired': 0,
                    'credits_used_this_period': 0,
                    'subscription_id': None,
                    'last_credit_refill': None,
                    'next_credit_refill': None,
                    'period_start': None,
                    'period_end': None,
                    'credits_metadata': {}
                }
            })()

        # Get subscription info with error handling
        try:
            subscription = lemon_squeezy.db_service.get_user_subscription(user_id, db)
            plan_id = subscription.plan_id if subscription else "free"
        except Exception as sub_error:
            logger.error(f"❌ Database error getting subscription: {str(sub_error)}")
            plan_id = "free"
            subscription = None
        
        # Get daily limit and usage with error handling
        try:
            daily_limit = lemon_squeezy.db_service.get_user_daily_limit(user_id, db)
            daily_usage_count = lemon_squeezy.db_service.get_daily_usage_count(user_id, db)
        except Exception as usage_error:
            logger.error(f"❌ Database error getting usage: {str(usage_error)}")
            daily_limit = 10  # Free tier default
            daily_usage_count = 0
        
        remaining_daily_credits = max(0, daily_limit - daily_usage_count)

        # Return enhanced credit info
        credit_data = user_credits.to_dict()
        credit_data.update({
            "remaining_daily_credits": remaining_daily_credits,
            "daily_limit": daily_limit,
            "daily_usage_count": daily_usage_count,
            "subscription_tier": plan_id,
            "subscription_active": subscription.is_active() if subscription else False
        })

        logger.info(f"✅ Successfully returned credit data for user {user_id}")
        return {
            "success": True,
            "data": credit_data,
        }

    except HTTPException:
        # Re-raise HTTP exceptions (like 401)
        raise
    except Exception as e:
        logger.error(f"❌ Unexpected error getting user credits: {str(e)}")
        import traceback
        logger.error(f"❌ Full traceback: {traceback.format_exc()}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get user credits: {str(e)}",
        )


@router.get("/credits/test")
async def test_credits_endpoint():
    """Test endpoint for credits without authentication"""
    return {
        "success": True,
        "message": "Credits endpoint is accessible",
        "data": {
            "user_id": "test_user",
            "current_credits": 10,
            "subscription_tier": "free",
            "subscription_active": True
        }
    }

@router.get("/health")
async def payment_health_check(request: Request):
    """Health check for payment service with security monitoring"""
    client_info = get_client_info(request)
    
    try:
        # Test Lemon Squeezy service initialization
        plans = await lemon_squeezy.get_subscription_plans()
        
        # Get rate limiting statistics
        rate_limit_stats = rate_limiting_service.get_global_stats()
        
        # Get security service status
        recent_audit_logs = security_service.get_audit_logs(limit=10)
        
        health_data = {
            "success": True,
            "status": "healthy",
            "service": "lemon_squeezy",
            "plans_available": len(plans),
            "security_features": {
                "webhook_signature_verification": True,
                "rate_limiting": getattr(rate_limiting_service, "is_enabled", lambda: True)(),
                "fraud_detection": security_service.fraud_detection_enabled,
                "audit_logging": True
            },
            "rate_limiting_stats": rate_limit_stats,
            "recent_security_events": len(recent_audit_logs),
            "timestamp": client_info["correlation_id"]
        }
        
        security_service.log_audit_event(
            event_type=AuditEventType.PAYMENT_CREATED,  # Using existing type for health check
            ip_address=client_info["ip_address"],
            event_data={"health_check": "successful"},
            security_level=SecurityLevel.LOW,
            success=True,
            correlation_id=client_info["correlation_id"]
        )
        
        return health_data
        
    except Exception as e:
        logger.error(f"Payment service health check failed: {str(e)}")
        security_service.log_audit_event(
            event_type=AuditEventType.PAYMENT_FAILED,  # Using existing type for failed health check
            ip_address=client_info["ip_address"],
            event_data={"health_check": "failed", "error": str(e)},
            security_level=SecurityLevel.HIGH,
            success=False,
            error_message=str(e),
            correlation_id=client_info["correlation_id"]
        )
        return {
            "success": False,
            "status": "unhealthy",
            "service": "lemon_squeezy",
            "error": str(e),
            "correlation_id": client_info["correlation_id"]
        }
