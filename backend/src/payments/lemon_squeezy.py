# backend/src/payments/lemon_squeezy.py
"""
Lemon Squeezy Payment Service Implementation

This module provides comprehensive payment processing functionality using Lemon Squeezy
for the AI Product Descriptions application.
"""

import os
import json
import hmac
import hashlib
import logging
import asyncio
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional, List, Tuple
from urllib.parse import urlencode
import httpx
from dataclasses import asdict

from .models import (
    UserCredits, PaymentHistory, SubscriptionPlans, 
    SubscriptionTier, PaymentStatus, WebhookEventType, WebhookEvent
)
from .sqlalchemy_service import SQLAlchemyPaymentService

logger = logging.getLogger(__name__)


class LemonSqueezyService:
    """Main service class for Lemon Squeezy payment processing"""

    def __init__(self):
        self.api_key = os.getenv("LEMON_SQUEEZY_API_KEY")
        self.webhook_secret = os.getenv("LEMON_SQUEEZY_WEBHOOK_SECRET")
        self.store_id = os.getenv("LEMON_SQUEEZY_STORE_ID")
        self.monthly_variant_id = os.getenv("LEMON_SQUEEZY_MONTHLY_VARIANT_ID")
        self.yearly_variant_id = os.getenv("LEMON_SQUEEZY_YEARLY_VARIANT_ID")
        self.base_url = "https://api.lemonsqueezy.com/v1"
        
        if not self.api_key:
            raise ValueError("LEMON_SQUEEZY_API_KEY environment variable is required")
        if not self.webhook_secret:
            raise ValueError("LEMON_SQUEEZY_WEBHOOK_SECRET environment variable is required")
        if not self.store_id:
            raise ValueError("LEMON_SQUEEZY_STORE_ID environment variable is required")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json"
        }
        # Initialize SQLAlchemy service
        self.db_service = SQLAlchemyPaymentService()

        # Initialize default subscription plans
        self._initialize_default_plans()
    
    def _initialize_default_plans(self):
        """Initialize default subscription plans"""
        self.default_plans = {
            "free": SubscriptionPlans(
                id="free",
                name="Free Tier",
                description="Basic AI product description generation",
                price=0.0,
                credits_per_month=10,
                max_products_per_batch=5,
                features={
                    "ai_generation": True,
                    "basic_templates": True,
                    "csv_upload": True,
                    "email_support": False,
                    "priority_support": False,
                    "custom_templates": False,
                    "api_access": False
                }
            ),
            "basic": SubscriptionPlans(
                id="basic",
                name="Basic Plan",
                description="Enhanced AI generation with more credits",
                price=9.99,
                credits_per_month=100,
                max_products_per_batch=50,
                features={
                    "ai_generation": True,
                    "basic_templates": True,
                    "csv_upload": True,
                    "email_support": True,
                    "priority_support": False,
                    "custom_templates": False,
                    "api_access": False
                }
            ),
            "pro": SubscriptionPlans(
                id="pro",
                name="Pro Plan",
                description="Professional AI generation with unlimited credits",
                price=29.99,
                credits_per_month=1000,
                max_products_per_batch=200,
                features={
                    "ai_generation": True,
                    "basic_templates": True,
                    "csv_upload": True,
                    "email_support": True,
                    "priority_support": True,
                    "custom_templates": True,
                    "api_access": True
                }
            ),
            "enterprise": SubscriptionPlans(
                id="enterprise",
                name="Enterprise Plan",
                description="Unlimited AI generation with premium features",
                price=99.99,
                credits_per_month=10000,
                max_products_per_batch=1000,
                features={
                    "ai_generation": True,
                    "basic_templates": True,
                    "csv_upload": True,
                    "email_support": True,
                    "priority_support": True,
                    "custom_templates": True,
                    "api_access": True,
                    "white_label": True,
                    "custom_integrations": True
                }
            )
        }
    
    async def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make HTTP request to Lemon Squeezy API"""
        url = f"{self.base_url}/{endpoint}"
        
        async with httpx.AsyncClient() as client:
            try:
                if method.upper() == "GET":
                    response = await client.get(url, headers=self.headers)
                elif method.upper() == "POST":
                    response = await client.post(url, headers=self.headers, json=data)
                elif method.upper() == "PATCH":
                    response = await client.patch(url, headers=self.headers, json=data)
                elif method.upper() == "DELETE":
                    response = await client.delete(url, headers=self.headers)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")
                
                response.raise_for_status()
                return response.json()
                
            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
                raise Exception(f"Lemon Squeezy API error: {e.response.status_code} - {e.response.text}")
            except httpx.RequestError as e:
                logger.error(f"Request error: {str(e)}")
                raise Exception(f"Network error: {str(e)}")
    
    def verify_webhook_signature(self, payload: str, signature: str) -> bool:
        """Verify webhook signature using HMAC-SHA256"""
        try:
            expected_signature = hmac.new(
                self.webhook_secret.encode('utf-8'),
                payload.encode('utf-8'),
                hashlib.sha256
            ).hexdigest()
            
            return hmac.compare_digest(signature, expected_signature)
        except Exception as e:
            logger.error(f"Error verifying webhook signature: {str(e)}")
            return False
    
    async def create_checkout_session(
        self, 
        user_id: str, 
        plan_id: str, 
        success_url: str, 
        cancel_url: str
    ) -> Dict[str, Any]:
        """Create a checkout session for subscription purchase"""
        plan = self.default_plans.get(plan_id)
        if not plan:
            raise ValueError(f"Invalid plan ID: {plan_id}")

        if plan.price == 0:
            # Free plan - no checkout needed
            return {
                "success": True,
                "checkout_url": None,
                "message": "Free plan activated"
            }

        # Create checkout session data
        test_mode = os.getenv("LEMON_SQUEEZY_TEST_MODE", "true").lower() == "true"
        # Select variant either from env override or plan config
        variant_id = (
            self.monthly_variant_id if plan_id in ("basic", "monthly") and self.monthly_variant_id else
            self.yearly_variant_id if plan_id in ("pro", "yearly") and self.yearly_variant_id else
            plan.lemon_squeezy_variant_id
        )
        checkout_data = {
            "data": {
                "type": "checkouts",
                "attributes": {
                    "checkout_data": {
                        "email": f"user_{user_id}@example.com",  # This should be the actual user email
                        "custom": {
                            "user_id": user_id,
                            "plan_id": plan_id
                        }
                    },
                    "expires_at": (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat(),
                    "preview": False,
                    "test_mode": test_mode
                },
                "relationships": {
                    "store": {
                        "data": {
                            "type": "stores",
                            "id": self.store_id
                        }
                    },
                    "variant": {
                        "data": {
                            "type": "variants",
                            "id": variant_id
                        }
                    }
                }
            }
        }

        try:
            response = await self._make_request("POST", "checkouts", checkout_data)

            return {
                "success": True,
                "checkout_url": response["data"]["attributes"]["url"],
                "checkout_id": response["data"]["id"]
            }
        except Exception as e:
            logger.error(f"Error creating checkout session: {str(e)}")
            raise Exception(f"Failed to create checkout session: {str(e)}")
    
    async def get_subscription_plans(self) -> List[Dict[str, Any]]:
        """Get available subscription plans"""
        # Try to get from database first, fallback to default plans
        try:
            db_plans = self.db_service.get_subscription_plans()
            if db_plans:
                return db_plans
        except Exception as e:
            logger.warning(f"Failed to get plans from database: {str(e)}")
        
        # Fallback to default plans
        return [plan.to_dict() for plan in self.default_plans.values() if plan.is_active]
    
    async def get_user_credits(self, user_id: str) -> Optional[UserCredits]:
        """Get user credits from database"""
        return self.db_service.get_user_credits(user_id)
    
    async def update_user_credits(self, user_credits: UserCredits) -> bool:
        """Update user credits in database"""
        return self.db_service.update_user_credits(user_credits)
    
    async def add_payment_history(self, payment: PaymentHistory) -> bool:
        """Add payment to history"""
        return self.db_service.add_payment_history(payment)
    
    async def process_webhook(self, payload: str, signature: str) -> Dict[str, Any]:
        """Process incoming webhook from Lemon Squeezy"""
        # Verify signature
        if not self.verify_webhook_signature(payload, signature):
            logger.error("Invalid webhook signature")
            return {"success": False, "error": "Invalid signature"}
        
        try:
            data = json.loads(payload)
            event_type = data.get("meta", {}).get("event_name")
            
            if not event_type:
                logger.error("No event type in webhook payload")
                return {"success": False, "error": "No event type"}
            
            # Create webhook event
            webhook_event = WebhookEvent(
                event_type=WebhookEventType(event_type),
                data=data,
                signature=signature
            )
            
            # Process based on event type
            result = await self._handle_webhook_event(webhook_event)
            
            logger.info(f"Processed webhook event: {event_type}")
            return {"success": True, "result": result}
            
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in webhook payload: {str(e)}")
            return {"success": False, "error": "Invalid JSON"}
        except Exception as e:
            logger.error(f"Error processing webhook: {str(e)}")
            return {"success": False, "error": str(e)}
    
    async def _handle_webhook_event(self, event: WebhookEvent) -> Dict[str, Any]:
        """Handle specific webhook event types"""
        event_type = event.event_type
        data = event.data
        
        if event_type == WebhookEventType.PAYMENT_SUCCESS:
            return await self._handle_payment_success(data)
        elif event_type == WebhookEventType.PAYMENT_FAILED:
            return await self._handle_payment_failed(data)
        elif event_type == WebhookEventType.SUBSCRIPTION_CREATED:
            return await self._handle_subscription_created(data)
        elif event_type == WebhookEventType.SUBSCRIPTION_CANCELLED:
            return await self._handle_subscription_cancelled(data)
        elif event_type == WebhookEventType.SUBSCRIPTION_UPDATED:
            return await self._handle_subscription_updated(data)
        else:
            logger.warning(f"Unhandled webhook event type: {event_type}")
            return {"status": "ignored", "reason": "Unhandled event type"}
    
    async def _handle_payment_success(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle successful payment"""
        try:
            order_data = data.get("data", {})
            attributes = order_data.get("attributes", {})
            
            # Extract order information
            order_id = order_data.get("id")
            user_id = attributes.get("user_email", "").split("@")[0]  # Extract user ID from email
            amount = float(attributes.get("total", 0)) / 100  # Convert from cents
            currency = attributes.get("currency", "USD")
            
            # Get custom data
            custom_data = attributes.get("checkout_data", {}).get("custom", {})
            plan_id = custom_data.get("plan_id", "basic")
            
            # Get plan details
            plan = self.default_plans.get(plan_id)
            if not plan:
                logger.error(f"Unknown plan ID in payment: {plan_id}")
                return {"status": "error", "reason": "Unknown plan"}
            
            # Create payment history record
            payment = PaymentHistory(
                id=f"payment_{order_id}",
                user_id=user_id,
                amount=amount,
                currency=currency,
                status=PaymentStatus.COMPLETED,
                lemon_squeezy_order_id=order_id,
                credits_awarded=plan.credits_per_month,
                subscription_plan_id=plan_id
            )
            
            # Add to payment history
            await self.add_payment_history(payment)
            
            # Update user credits
            user_credits = await self.get_user_credits(user_id)
            if user_credits:
                user_credits.add_credits(plan.credits_per_month, "purchase")
                user_credits.subscription_tier = SubscriptionTier(plan_id)
                user_credits.subscription_plan_id = plan_id
                user_credits.subscription_expires_at = datetime.now(timezone.utc) + timedelta(days=30)
                await self.update_user_credits(user_credits)
            
            logger.info(f"Payment success processed: {order_id} for user {user_id}")
            return {"status": "success", "order_id": order_id, "credits_awarded": plan.credits_per_month}
            
        except Exception as e:
            logger.error(f"Error handling payment success: {str(e)}")
            return {"status": "error", "reason": str(e)}
    
    async def _handle_payment_failed(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle failed payment"""
        try:
            order_data = data.get("data", {})
            order_id = order_data.get("id")
            
            # Log failed payment
            logger.warning(f"Payment failed: {order_id}")
            
            return {"status": "logged", "order_id": order_id}
            
        except Exception as e:
            logger.error(f"Error handling payment failure: {str(e)}")
            return {"status": "error", "reason": str(e)}
    
    async def _handle_subscription_created(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle subscription creation"""
        try:
            subscription_data = data.get("data", {})
            subscription_id = subscription_data.get("id")
            attributes = subscription_data.get("attributes", {})
            
            # Extract subscription information
            user_id = attributes.get("user_email", "").split("@")[0]
            status = attributes.get("status")
            
            logger.info(f"Subscription created: {subscription_id} for user {user_id}, status: {status}")
            
            return {"status": "success", "subscription_id": subscription_id}
            
        except Exception as e:
            logger.error(f"Error handling subscription creation: {str(e)}")
            return {"status": "error", "reason": str(e)}
    
    async def _handle_subscription_cancelled(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle subscription cancellation"""
        try:
            subscription_data = data.get("data", {})
            subscription_id = subscription_data.get("id")
            attributes = subscription_data.get("attributes", {})
            
            # Extract subscription information
            user_id = attributes.get("user_email", "").split("@")[0]
            
            # Update user to free tier
            user_credits = await self.get_user_credits(user_id)
            if user_credits:
                user_credits.subscription_tier = SubscriptionTier.FREE
                user_credits.subscription_plan_id = None
                user_credits.subscription_expires_at = None
                await self.update_user_credits(user_credits)
            
            logger.info(f"Subscription cancelled: {subscription_id} for user {user_id}")
            
            return {"status": "success", "subscription_id": subscription_id}
            
        except Exception as e:
            logger.error(f"Error handling subscription cancellation: {str(e)}")
            return {"status": "error", "reason": str(e)}
    
    async def _handle_subscription_updated(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle subscription update"""
        try:
            subscription_data = data.get("data", {})
            subscription_id = subscription_data.get("id")
            attributes = subscription_data.get("attributes", {})
            
            # Extract subscription information
            user_id = attributes.get("user_email", "").split("@")[0]
            status = attributes.get("status")
            
            logger.info(f"Subscription updated: {subscription_id} for user {user_id}, status: {status}")
            
            return {"status": "success", "subscription_id": subscription_id}
            
        except Exception as e:
            logger.error(f"Error handling subscription update: {str(e)}")
            return {"status": "error", "reason": str(e)}
    
    async def check_rate_limit(self, user_id: str) -> Tuple[bool, Dict[str, Any]]:
        """Check if user is within rate limits"""
        return self.db_service.check_rate_limits(user_id)
    
    async def deduct_credits(self, user_id: str, amount: int = 1) -> Tuple[bool, Dict[str, Any]]:
        """Deduct credits from user account"""
        return self.db_service.use_credits(user_id, amount)
