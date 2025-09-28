# backend/src/payments/models.py
"""
Database models for payment and subscription management
"""

from datetime import datetime, timezone
from typing import Optional, Dict, Any
from dataclasses import dataclass, field
from enum import Enum
import json


class SubscriptionTier(str, Enum):
    """Subscription tier levels"""
    FREE = "free"
    BASIC = "basic"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class PaymentStatus(str, Enum):
    """Payment status values"""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"
    CANCELLED = "cancelled"


class WebhookEventType(str, Enum):
    """Lemon Squeezy webhook event types"""
    PAYMENT_SUCCESS = "payment_success"
    PAYMENT_FAILED = "payment_failed"
    SUBSCRIPTION_CREATED = "subscription_created"
    SUBSCRIPTION_CANCELLED = "subscription_cancelled"
    SUBSCRIPTION_UPDATED = "subscription_updated"
    SUBSCRIPTION_RESUMED = "subscription_resumed"
    SUBSCRIPTION_PAUSED = "subscription_paused"
    ORDER_CREATED = "order_created"
    ORDER_REFUNDED = "order_refunded"
    PAYMENT_REFUNDED = "payment_refunded"


@dataclass
class SubscriptionPlans:
    """Subscription plan configuration"""
    id: str
    name: str
    description: str
    price: float
    currency: str = "USD"
    interval: str = "month"  # month, year
    credits_per_month: int = 0
    max_products_per_batch: int = 0
    features: Dict[str, Any] = field(default_factory=dict)
    lemon_squeezy_variant_id: Optional[str] = None
    is_active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "currency": self.currency,
            "interval": self.interval,
            "credits_per_month": self.credits_per_month,
            "max_products_per_batch": self.max_products_per_batch,
            "features": self.features,
            "lemon_squeezy_variant_id": self.lemon_squeezy_variant_id,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SubscriptionPlans":
        """Create from dictionary"""
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            price=data["price"],
            currency=data.get("currency", "USD"),
            interval=data.get("interval", "month"),
            credits_per_month=data.get("credits_per_month", 0),
            max_products_per_batch=data.get("max_products_per_batch", 0),
            features=data.get("features", {}),
            lemon_squeezy_variant_id=data.get("lemon_squeezy_variant_id"),
            is_active=data.get("is_active", True),
            created_at=datetime.fromisoformat(data["created_at"].replace('Z', '+00:00')),
            updated_at=datetime.fromisoformat(data["updated_at"].replace('Z', '+00:00'))
        )


@dataclass
class UserCredits:
    """User credit tracking"""
    user_id: str
    current_credits: int = 0
    total_credits_purchased: int = 0
    total_credits_used: int = 0
    subscription_tier: SubscriptionTier = SubscriptionTier.FREE
    subscription_plan_id: Optional[str] = None
    subscription_expires_at: Optional[datetime] = None
    last_credit_refill: Optional[datetime] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def add_credits(self, amount: int, source: str = "purchase") -> None:
        """Add credits to user account"""
        self.current_credits += amount
        if source == "purchase":
            self.total_credits_purchased += amount
        self.last_credit_refill = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def use_credits(self, amount: int) -> bool:
        """Use credits if available"""
        if self.current_credits >= amount:
            self.current_credits -= amount
            self.total_credits_used += amount
            self.updated_at = datetime.now(timezone.utc)
            return True
        return False

    def can_generate(self, batch_size: int = 1) -> bool:
        """Check if user can generate given batch size"""
        if self.subscription_tier == SubscriptionTier.FREE:
            return self.current_credits >= batch_size
        return True  # Paid tiers have unlimited generation

    def get_rate_limit(self) -> Dict[str, int]:
        """Get rate limits based on subscription tier"""
        limits = {
            SubscriptionTier.FREE: {"requests_per_minute": 5, "requests_per_hour": 50},
            SubscriptionTier.BASIC: {"requests_per_minute": 20, "requests_per_hour": 500},
            SubscriptionTier.PRO: {"requests_per_minute": 50, "requests_per_hour": 2000},
            SubscriptionTier.ENTERPRISE: {"requests_per_minute": 100, "requests_per_hour": 10000}
        }
        return limits.get(self.subscription_tier, limits[SubscriptionTier.FREE])

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "user_id": self.user_id,
            "current_credits": self.current_credits,
            "total_credits_purchased": self.total_credits_purchased,
            "total_credits_used": self.total_credits_used,
            "subscription_tier": self.subscription_tier.value,
            "subscription_plan_id": self.subscription_plan_id,
            "subscription_expires_at": self.subscription_expires_at.isoformat() if self.subscription_expires_at else None,
            "last_credit_refill": self.last_credit_refill.isoformat() if self.last_credit_refill else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "UserCredits":
        """Create from dictionary"""
        return cls(
            user_id=data["user_id"],
            current_credits=data.get("current_credits", 0),
            total_credits_purchased=data.get("total_credits_purchased", 0),
            total_credits_used=data.get("total_credits_used", 0),
            subscription_tier=SubscriptionTier(data.get("subscription_tier", "free")),
            subscription_plan_id=data.get("subscription_plan_id"),
            subscription_expires_at=datetime.fromisoformat(data["subscription_expires_at"].replace('Z', '+00:00')) if data.get("subscription_expires_at") else None,
            last_credit_refill=datetime.fromisoformat(data["last_credit_refill"].replace('Z', '+00:00')) if data.get("last_credit_refill") else None,
            created_at=datetime.fromisoformat(data["created_at"].replace('Z', '+00:00')),
            updated_at=datetime.fromisoformat(data["updated_at"].replace('Z', '+00:00'))
        )


@dataclass
class PaymentHistory:
    """Payment transaction history"""
    id: str
    user_id: str
    amount: float
    currency: str = "USD"
    status: PaymentStatus = PaymentStatus.PENDING
    payment_method: str = "lemon_squeezy"
    lemon_squeezy_order_id: Optional[str] = None
    lemon_squeezy_subscription_id: Optional[str] = None
    credits_awarded: int = 0
    subscription_plan_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "amount": self.amount,
            "currency": self.currency,
            "status": self.status.value,
            "payment_method": self.payment_method,
            "lemon_squeezy_order_id": self.lemon_squeezy_order_id,
            "lemon_squeezy_subscription_id": self.lemon_squeezy_subscription_id,
            "credits_awarded": self.credits_awarded,
            "subscription_plan_id": self.subscription_plan_id,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PaymentHistory":
        """Create from dictionary"""
        return cls(
            id=data["id"],
            user_id=data["user_id"],
            amount=data["amount"],
            currency=data.get("currency", "USD"),
            status=PaymentStatus(data.get("status", "pending")),
            payment_method=data.get("payment_method", "lemon_squeezy"),
            lemon_squeezy_order_id=data.get("lemon_squeezy_order_id"),
            lemon_squeezy_subscription_id=data.get("lemon_squeezy_subscription_id"),
            credits_awarded=data.get("credits_awarded", 0),
            subscription_plan_id=data.get("subscription_plan_id"),
            metadata=data.get("metadata", {}),
            created_at=datetime.fromisoformat(data["created_at"].replace('Z', '+00:00')),
            updated_at=datetime.fromisoformat(data["updated_at"].replace('Z', '+00:00'))
        )


@dataclass
class WebhookEvent:
    """Webhook event data"""
    event_type: WebhookEventType
    data: Dict[str, Any]
    signature: str
    received_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "event_type": self.event_type.value,
            "data": self.data,
            "signature": self.signature,
            "received_at": self.received_at.isoformat()
        }

