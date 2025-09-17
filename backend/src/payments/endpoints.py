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
from app.db.session import get_db
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
    plan_id: str
    success_url: str
    cancel_url: str

    class Config:
        schema_extra = {
            "example": {
                "plan_id": "basic",
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
async def get_subscription_plans(request: Request):
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
        monthly_id = os.getenv("LEMON_SQUEEZY_MONTHLY_VARIANT_ID")
        yearly_id = os.getenv("LEMON_SQUEEZY_YEARLY_VARIANT_ID")
        store_id = os.getenv("LEMON_SQUEEZY_STORE_ID")
        # Return basic env-wired plans; fall back to service defaults if missing
        env_plans = []
        if monthly_id:
            env_plans.append({
                "id": "monthly",
                "name": "Monthly",
                "interval": "month",
                "lemon_squeezy_variant_id": monthly_id,
                "store_id": store_id,
            })
        if yearly_id:
            env_plans.append({
                "id": "yearly",
                "name": "Yearly",
                "interval": "year",
                "lemon_squeezy_variant_id": yearly_id,
                "store_id": store_id,
            })
        plans = env_plans or await lemon_squeezy.get_subscription_plans()
        
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
    auth = Depends(get_authed_user_db)
):
    """Create a checkout session for subscription purchase with comprehensive security"""
    client_info = get_client_info(request)
    claims = auth["claims"]
    user_row = auth["user"]
    user_id = claims.get("uid")
    
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID not found in token"
        )
    
    # Check rate limits
    allowed, rate_info = rate_limiting_service.check_rate_limit(
        endpoint="checkout",
        user_id=user_id,
        ip_address=client_info["ip_address"]
    )
    
    if not allowed:
        security_service.log_audit_event(
            event_type=AuditEventType.RATE_LIMIT_EXCEEDED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
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
        # Validate payment data
        payment_data = {
            "plan_id": request_data.plan_id,
            "success_url": request_data.success_url,
            "cancel_url": request_data.cancel_url,
            "user_id": user_id,
            "amount": 0,  # Will be determined by plan
            "currency": "USD"
        }
        
        is_valid, validation_errors = security_service.validate_payment_data(payment_data)
        if not is_valid:
            security_service.log_audit_event(
                event_type=AuditEventType.PAYMENT_FAILED,
                user_id=user_id,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data={"validation_errors": validation_errors},
                security_level=SecurityLevel.MEDIUM,
                success=False,
                error_message="; ".join(validation_errors),
                correlation_id=client_info["correlation_id"]
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Payment data validation failed: {'; '.join(validation_errors)}"
            )
        
        # Fraud detection
        user_credits = await lemon_squeezy.get_user_credits(user_id)
        user_data = {
            "user_id": user_id,
            "email": claims.get("email", ""),
            "account_age_days": (user_credits.created_at - user_credits.created_at).days if user_credits else 0,
            "recent_payment_count": 0,  # This should be fetched from payment history
            "recent_failed_payments": 0,  # This should be fetched from payment history
            "country": ""  # This should be determined from user profile
        }
        
        fraud_result = security_service.detect_fraud(payment_data, user_data)
        if fraud_result.is_fraudulent:
            security_service.log_audit_event(
                event_type=AuditEventType.FRAUD_DETECTED,
                user_id=user_id,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data={
                    "fraud_score": fraud_result.confidence_score,
                    "risk_factors": fraud_result.risk_factors,
                    "recommended_action": fraud_result.recommended_action
                },
                security_level=SecurityLevel.CRITICAL,
                success=False,
                error_message="Fraudulent activity detected",
                correlation_id=client_info["correlation_id"]
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Payment request rejected due to security concerns"
            )
        
        result = await lemon_squeezy.create_checkout_session(
            user_id=user_id,
            plan_id=request_data.plan_id,
            success_url=request_data.success_url,
            cancel_url=request_data.cancel_url
        )
        
        # Log successful checkout creation
        security_service.log_audit_event(
            event_type=AuditEventType.PAYMENT_CREATED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data={
                "plan_id": request_data.plan_id,
                "checkout_url": result.get("checkout_url", ""),
                "fraud_score": fraud_result.confidence_score
            },
            security_level=SecurityLevel.MEDIUM,
            success=True,
            correlation_id=client_info["correlation_id"]
        )
        
        return {
            "success": True,
            "data": result,
            "fraud_check": {
                "confidence_score": fraud_result.confidence_score,
                "recommended_action": fraud_result.recommended_action
            },
            "rate_limit_info": rate_info
        }
        
    except ValueError as e:
        security_service.log_audit_event(
            event_type=AuditEventType.PAYMENT_FAILED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data={"validation_error": str(e)},
            security_level=SecurityLevel.MEDIUM,
            success=False,
            error_message=str(e),
            correlation_id=client_info["correlation_id"]
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Error creating checkout session: {str(e)}")
        security_service.log_audit_event(
            event_type=AuditEventType.PAYMENT_FAILED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data={"error": str(e)},
            security_level=SecurityLevel.HIGH,
            success=False,
            error_message=str(e),
            correlation_id=client_info["correlation_id"]
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create checkout session: {str(e)}"
        )


@router.post("/webhook")
async def handle_webhook(request: Request, db: Session = Depends(get_db)):
    """Handle Lemon Squeezy webhook events with enhanced security"""
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

        # Continue to legacy processor for backward-compatible side-effects if any
        result = await lemon_squeezy.process_webhook(payload=payload_str, signature=signature)
        
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


@router.get("/user/credits")
async def get_user_credits(auth = Depends(get_authed_user_db)):
    """Get user's current credits and subscription status"""
    try:
        claims = auth["claims"]
        user_row = auth["user"]
        user_id = claims.get("uid")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User ID not found in token",
            )

        user_credits = await lemon_squeezy.get_user_credits(user_id)
        if not user_credits:
            # Create new user with free tier
            user_credits = lemon_squeezy.db_service.create_user_credits(user_id, "free")

        return {
            "success": True,
            "data": user_credits.to_dict(),
        }

    except Exception as e:
        logger.error(f"Error getting user credits: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get user credits: {str(e)}",
        )


@router.post("/user/credits/check")
async def check_user_credits(
    request_data: CreditCheckRequest,
    request: Request,
    auth = Depends(get_authed_user_db)
):
    """Check if user has sufficient credits for generation with enhanced security"""
    client_info = get_client_info(request)
    claims = auth["claims"]
    user_row = auth["user"]
    user_id = claims.get("uid")
    
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID not found in token"
        )
    
    # Check rate limits
    allowed, rate_info = rate_limiting_service.check_rate_limit(
        endpoint="credit_check",
        user_id=user_id,
        ip_address=client_info["ip_address"]
    )
    
    if not allowed:
        security_service.log_audit_event(
            event_type=AuditEventType.RATE_LIMIT_EXCEEDED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
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
        batch_size = request_data.batch_size
        
        # Validate batch size
        if batch_size <= 0 or batch_size > 100:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Batch size must be between 1 and 100"
            )
        
        # Check rate limits first
        can_proceed, rate_limit_info = await lemon_squeezy.check_rate_limit(user_id)
        
        if not can_proceed:
            security_service.log_audit_event(
                event_type=AuditEventType.RATE_LIMIT_EXCEEDED,
                user_id=user_id,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data=rate_limit_info,
                security_level=SecurityLevel.MEDIUM,
                success=False,
                correlation_id=client_info["correlation_id"]
            )
            return {
                "success": False,
                "can_generate": False,
                "error": rate_limit_info.get("error"),
                "upgrade_required": rate_limit_info.get("upgrade_required", False),
                "rate_limits": rate_limit_info.get("rate_limits", {}),
                "correlation_id": client_info["correlation_id"]
            }
        
        # Check if user can generate the requested batch size
        user_credits = await lemon_squeezy.get_user_credits(user_id)
        if user_credits and not user_credits.can_generate(batch_size):
            security_service.log_audit_event(
                event_type=AuditEventType.CREDIT_DEDUCTED,
                user_id=user_id,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data={
                    "check_result": "insufficient_credits",
                    "requested_batch_size": batch_size,
                    "available_credits": user_credits.current_credits
                },
                security_level=SecurityLevel.LOW,
                success=False,
                correlation_id=client_info["correlation_id"]
            )
            return {
                "success": False,
                "can_generate": False,
                "error": "Insufficient credits for batch size",
                "current_credits": user_credits.current_credits,
                "required_credits": batch_size,
                "upgrade_required": True,
                "correlation_id": client_info["correlation_id"]
            }
        
        # Log successful credit check
        security_service.log_audit_event(
            event_type=AuditEventType.CREDIT_DEDUCTED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data={
                "check_result": "sufficient_credits",
                "requested_batch_size": batch_size,
                "available_credits": user_credits.current_credits if user_credits else 0
            },
            security_level=SecurityLevel.LOW,
            success=True,
            correlation_id=client_info["correlation_id"]
        )
        
        return {
            "success": True,
            "can_generate": True,
            "rate_limits": rate_limit_info.get("rate_limits", {}),
            "current_credits": user_credits.current_credits if user_credits else 0,
            "correlation_id": client_info["correlation_id"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error checking user credits: {str(e)}")
        security_service.log_audit_event(
            event_type=AuditEventType.CREDIT_DEDUCTED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data={"error": str(e)},
            security_level=SecurityLevel.HIGH,
            success=False,
            error_message=str(e),
            correlation_id=client_info["correlation_id"]
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to check user credits: {str(e)}"
        )


@router.post("/user/credits/deduct")
async def deduct_user_credits(
    request_data: CreditDeductionRequest,
    request: Request,
    auth = Depends(get_authed_user_db)
):
    """Deduct credits from user account after successful generation with secure operations"""
    client_info = get_client_info(request)
    claims = auth["claims"]
    user_row = auth["user"]
    user_id = claims.get("uid")
    
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID not found in token"
        )
    
    # Check rate limits
    allowed, rate_info = rate_limiting_service.check_rate_limit(
        endpoint="credit_deduct",
        user_id=user_id,
        ip_address=client_info["ip_address"]
    )
    
    if not allowed:
        security_service.log_audit_event(
            event_type=AuditEventType.RATE_LIMIT_EXCEEDED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
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
        amount = request_data.amount
        operation_context = request_data.operation_context or {}
        
        # Validate amount
        if amount <= 0 or amount > 50:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Credit deduction amount must be between 1 and 50"
            )
        
        # Use secure credit deduction
        success, result = await secure_operations.secure_credit_deduction(
            user_id=user_id,
            amount=amount,
            operation_context=operation_context,
            correlation_id=client_info["correlation_id"]
        )
        
        if not success:
            security_service.log_audit_event(
                event_type=AuditEventType.CREDIT_DEDUCTED,
                user_id=user_id,
                ip_address=client_info["ip_address"],
                user_agent=client_info["user_agent"],
                event_data={
                    "amount": amount,
                    "error": result.get("error"),
                    "transaction_id": result.get("transaction_id")
                },
                security_level=SecurityLevel.MEDIUM,
                success=False,
                error_message=result.get("error"),
                correlation_id=client_info["correlation_id"]
            )
            return {
                "success": False,
                "error": result.get("error"),
                "upgrade_required": result.get("upgrade_required", False),
                "correlation_id": client_info["correlation_id"]
            }
        
        # Log successful deduction
        security_service.log_audit_event(
            event_type=AuditEventType.CREDIT_DEDUCTED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data={
                "amount": amount,
                "remaining_credits": result.get("remaining_credits"),
                "transaction_id": result.get("transaction_id")
            },
            security_level=SecurityLevel.MEDIUM,
            success=True,
            correlation_id=client_info["correlation_id"]
        )
        
        return {
            "success": True,
            "credits_deducted": result.get("credits_deducted", amount),
            "remaining_credits": result.get("remaining_credits", 0),
            "transaction_id": result.get("transaction_id"),
            "correlation_id": client_info["correlation_id"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deducting user credits: {str(e)}")
        security_service.log_audit_event(
            event_type=AuditEventType.CREDIT_DEDUCTED,
            user_id=user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data={"error": str(e)},
            security_level=SecurityLevel.HIGH,
            success=False,
            error_message=str(e),
            correlation_id=client_info["correlation_id"]
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to deduct user credits: {str(e)}"
        )


@router.get("/user/subscription")
async def get_user_subscription(auth = Depends(get_authed_user_db)):
    """Get user's subscription details"""
    try:
        claims = auth["claims"]
        user_row = auth["user"]
        user_id = claims.get("uid")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User ID not found in token",
            )

        user_credits = await lemon_squeezy.get_user_credits(user_id)
        if not user_credits:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        # Get plan details
        plans = await lemon_squeezy.get_subscription_plans()
        current_plan = None
        for plan in plans:
            if plan["id"] == user_credits.subscription_plan_id:
                current_plan = plan
                break

        return {
            "success": True,
            "data": {
                "subscription_tier": user_credits.subscription_tier.value,
                "subscription_plan": current_plan,
                "subscription_expires_at": user_credits.subscription_expires_at.isoformat() if user_credits.subscription_expires_at else None,
                "current_credits": user_credits.current_credits,
                "total_credits_purchased": user_credits.total_credits_purchased,
                "total_credits_used": user_credits.total_credits_used,
            },
        }

    except Exception as e:
        logger.error(f"Error getting user subscription: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get user subscription: {str(e)}",
        )


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


# Security and Administration Endpoints

@router.get("/admin/audit-logs")
async def get_audit_logs(
    request: Request,
    user_id: Optional[str] = None,
    limit: int = 50,
    auth = Depends(get_authed_user_db)
):
    """Get audit logs (admin only)"""
    client_info = get_client_info(request)
    claims = auth["claims"]
    user_row = auth["user"]
    current_user_id = claims.get("uid")
    
    # Check if user is admin (you should implement proper admin role checking)
    # For now, we'll assume any authenticated user can access their own logs
    if user_id and user_id != current_user_id:
        # Check if current user is admin
        user_email = claims.get("email", "")
        admin_emails = ["admin@yourapp.com", "security@yourapp.com"]  # Configure these
        if user_email not in admin_emails:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions to access other user's audit logs"
            )
    
    try:
        logs = security_service.get_audit_logs(
            user_id=user_id,
            limit=limit
        )
        
        return {
            "success": True,
            "logs": [log.to_dict() for log in logs],
            "count": len(logs),
            "correlation_id": client_info["correlation_id"]
        }
        
    except Exception as e:
        logger.error(f"Error getting audit logs: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get audit logs: {str(e)}"
        )


@router.get("/admin/rate-limit-status/{endpoint}")
async def get_rate_limit_status(
    endpoint: str,
    request: Request,
    auth = Depends(get_authed_user_db)
):
    """Get rate limit status for user and endpoint"""
    client_info = get_client_info(request)
    claims = auth["claims"]
    user_row = auth["user"]
    user_id = claims.get("uid")
    
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID not found in token"
        )
    
    try:
        status_info = rate_limiting_service.get_rate_limit_status(endpoint, user_id)
        
        return {
            "success": True,
            "rate_limit_status": status_info,
            "correlation_id": client_info["correlation_id"]
        }
        
    except Exception as e:
        logger.error(f"Error getting rate limit status: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get rate limit status: {str(e)}"
        )


@router.post("/admin/reset-rate-limits")
async def reset_user_rate_limits(
    request: Request,
    endpoint: str,
    target_user_id: str,
    auth = Depends(get_authed_user_db)
):
    """Reset rate limits for a user (admin only)"""
    client_info = get_client_info(request)
    claims = auth["claims"]
    user_row = auth["user"]
    current_user_id = claims.get("uid")
    
    # Check admin permissions
    user_email = claims.get("email", "")
    admin_emails = ["admin@yourapp.com", "security@yourapp.com"]
    if user_email not in admin_emails:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions for rate limit reset"
        )
    
    try:
        success = rate_limiting_service.reset_user_limits(endpoint, target_user_id)
        
        security_service.log_audit_event(
            event_type=AuditEventType.RATE_LIMIT_EXCEEDED,  # Using existing type for admin action
            user_id=current_user_id,
            ip_address=client_info["ip_address"],
            user_agent=client_info["user_agent"],
            event_data={
                "admin_action": "rate_limit_reset",
                "target_user_id": target_user_id,
                "endpoint": endpoint,
                "success": success
            },
            security_level=SecurityLevel.HIGH,
            success=success,
            correlation_id=client_info["correlation_id"]
        )
        
        return {
            "success": success,
            "message": f"Rate limits reset for user {target_user_id} on endpoint {endpoint}" if success else "Failed to reset rate limits",
            "correlation_id": client_info["correlation_id"]
        }
        
    except Exception as e:
        logger.error(f"Error resetting rate limits: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to reset rate limits: {str(e)}"
        )


@router.get("/admin/transactions")
async def get_active_transactions(
    request: Request,
    user_filter: Optional[str] = None,
    auth = Depends(get_authed_user_db)
):
    """Get active secure transactions (admin only)"""
    client_info = get_client_info(request)
    
    # Check admin permissions
    claims = auth["claims"]
    user_row = auth["user"]
    user_email = claims.get("email", "")
    admin_emails = ["admin@yourapp.com", "security@yourapp.com"]
    if user_email not in admin_emails:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions to view transactions"
        )
    
    try:
        transactions = secure_operations.get_active_transactions(user_id=user_filter)
        
        return {
            "success": True,
            "transactions": transactions,
            "count": len(transactions),
            "correlation_id": client_info["correlation_id"]
        }
        
    except Exception as e:
        logger.error(f"Error getting active transactions: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get active transactions: {str(e)}"
        )


@router.get("/transaction/{transaction_id}")
async def get_transaction_status(
    transaction_id: str,
    request: Request,
    auth = Depends(get_authed_user_db)
):
    """Get transaction status"""
    client_info = get_client_info(request)
    claims = auth["claims"]
    user_row = auth["user"]
    user_id = claims.get("uid")
    
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID not found in token"
        )
    
    try:
        transaction = secure_operations.get_transaction_status(transaction_id)
        
        if not transaction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Transaction not found"
            )
        
        # Check if user can access this transaction
        if transaction["user_id"] != user_id:
            # Check admin permissions
            user_email = claims.get("email", "")
            admin_emails = ["admin@yourapp.com", "security@yourapp.com"]
            if user_email not in admin_emails:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Insufficient permissions to view this transaction"
                )
        
        return {
            "success": True,
            "transaction": transaction,
            "correlation_id": client_info["correlation_id"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting transaction status: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get transaction status: {str(e)}"
        )
