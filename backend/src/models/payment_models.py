# backend/src/models/payment_models.py
"""
SQLAlchemy database models for the payment system
"""

from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Optional

from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, 
    ForeignKey, Numeric, JSON, Index, CheckConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func

Base = declarative_base()


class SubscriptionTier(str, Enum):
    """Subscription tier levels"""
    FREE = "free"
    BASIC = "basic"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class SubscriptionStatus(str, Enum):
    """Subscription status values"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    CANCELLED = "cancelled"
    PAUSED = "paused"
    EXPIRED = "expired"
    TRIAL = "trial"


class PaymentStatus(str, Enum):
    """Payment status values"""
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"
    CANCELLED = "cancelled"
    PARTIALLY_REFUNDED = "partially_refunded"


class UsageType(str, Enum):
    """Usage tracking types"""
    AI_GENERATION = "ai_generation"
    BATCH_PROCESSING = "batch_processing"
    API_CALL = "api_call"
    CSV_UPLOAD = "csv_upload"


class SubscriptionPlan(Base):
    """Available subscription plans"""
    __tablename__ = "subscription_plans"
    
    id = Column(String(50), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False, default=0.00)
    currency = Column(String(3), nullable=False, default="USD")
    billing_interval = Column(String(20), nullable=False, default="month")  # month, year
    
    # Credit and usage limits
    credits_per_period = Column(Integer, nullable=False, default=0)
    max_products_per_batch = Column(Integer, nullable=False, default=0)
    max_api_calls_per_day = Column(Integer, nullable=False, default=0)
    
    # Rate limiting
    requests_per_minute = Column(Integer, nullable=False, default=5)
    requests_per_hour = Column(Integer, nullable=False, default=50)
    
    # Features and capabilities
    features = Column(JSON, nullable=False, default=dict)
    
    # Lemon Squeezy integration
    lemon_squeezy_variant_id = Column(String(255), unique=True, nullable=True)
    lemon_squeezy_product_id = Column(String(255), nullable=True)
    
    # Plan metadata
    is_active = Column(Boolean, nullable=False, default=True)
    sort_order = Column(Integer, nullable=False, default=0)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    user_subscriptions = relationship("UserSubscription", back_populates="plan")
    
    # Indexes
    __table_args__ = (
        Index('idx_subscription_plans_active', 'is_active'),
        Index('idx_subscription_plans_sort', 'sort_order'),
        CheckConstraint('price >= 0', name='check_positive_price'),
        CheckConstraint('credits_per_period >= 0', name='check_positive_credits'),
        CheckConstraint('max_products_per_batch >= 0', name='check_positive_batch_limit'),
        CheckConstraint('requests_per_minute > 0', name='check_positive_rate_limit'),
    )
    
    @validates('currency')
    def validate_currency(self, key, currency):
        """Validate currency code"""
        if currency and len(currency) != 3:
            raise ValueError("Currency must be a 3-letter code")
        return currency.upper() if currency else "USD"
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": float(self.price),
            "currency": self.currency,
            "billing_interval": self.billing_interval,
            "credits_per_period": self.credits_per_period,
            "max_products_per_batch": self.max_products_per_batch,
            "max_api_calls_per_day": self.max_api_calls_per_day,
            "requests_per_minute": self.requests_per_minute,
            "requests_per_hour": self.requests_per_hour,
            "features": self.features,
            "lemon_squeezy_variant_id": self.lemon_squeezy_variant_id,
            "is_active": self.is_active,
            "sort_order": self.sort_order,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class UserSubscription(Base):
    """User subscription tracking"""
    __tablename__ = "user_subscriptions"
    
    id = Column(String(255), primary_key=True)
    user_id = Column(String(255), nullable=False, index=True)  # Firebase UID
    
    # Subscription details
    plan_id = Column(String(50), ForeignKey("subscription_plans.id"), nullable=False)
    status = Column(String(20), nullable=False, default=SubscriptionStatus.ACTIVE)
    
    # Billing information
    current_period_start = Column(DateTime(timezone=True), nullable=False)
    current_period_end = Column(DateTime(timezone=True), nullable=False)
    cancel_at_period_end = Column(Boolean, nullable=False, default=False)
    
    # Lemon Squeezy integration
    lemon_squeezy_subscription_id = Column(String(255), unique=True, nullable=True)
    lemon_squeezy_customer_id = Column(String(255), nullable=True)
    
    # Trial information
    trial_start = Column(DateTime(timezone=True), nullable=True)
    trial_end = Column(DateTime(timezone=True), nullable=True)
    
    # Subscription metadata
    subscription_metadata = Column(JSON, nullable=False, default=dict)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    plan = relationship("SubscriptionPlan", back_populates="user_subscriptions")
    user_credits = relationship("UserCredits", back_populates="subscription", uselist=False)
    payment_history = relationship("PaymentHistory", back_populates="subscription")
    
    # Indexes
    __table_args__ = (
        Index('idx_user_subscriptions_user_id', 'user_id'),
        Index('idx_user_subscriptions_status', 'status'),
        Index('idx_user_subscriptions_period_end', 'current_period_end'),
        Index('idx_user_subscriptions_ls_id', 'lemon_squeezy_subscription_id'),
    )
    
    @validates('status')
    def validate_status(self, key, status):
        """Validate subscription status"""
        if status not in [s.value for s in SubscriptionStatus]:
            raise ValueError(f"Invalid subscription status: {status}")
        return status
    
    def is_active(self) -> bool:
        """Check if subscription is currently active"""
        now = datetime.now(timezone.utc).replace(tzinfo=None)
        return (
            self.status == SubscriptionStatus.ACTIVE and
            self.current_period_end > now
        )
    
    def is_trial(self) -> bool:
        """Check if subscription is in trial period"""
        if not self.trial_start or not self.trial_end:
            return False
        now = datetime.now(timezone.utc).replace(tzinfo=None)
        return self.trial_start <= now <= self.trial_end
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "plan_id": self.plan_id,
            "status": self.status,
            "current_period_start": self.current_period_start.isoformat() if self.current_period_start else None,
            "current_period_end": self.current_period_end.isoformat() if self.current_period_end else None,
            "cancel_at_period_end": self.cancel_at_period_end,
            "lemon_squeezy_subscription_id": self.lemon_squeezy_subscription_id,
            "lemon_squeezy_customer_id": self.lemon_squeezy_customer_id,
            "trial_start": self.trial_start.isoformat() if self.trial_start else None,
            "trial_end": self.trial_end.isoformat() if self.trial_end else None,
            "subscription_metadata": self.subscription_metadata,
            "is_active": self.is_active(),
            "is_trial": self.is_trial(),
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class UserCredits(Base):
    """User credit tracking"""
    __tablename__ = "user_credits"
    
    user_id = Column(String(255), primary_key=True)  # Firebase UID
    
    # Credit balances
    current_credits = Column(Integer, nullable=False, default=0)
    total_credits_purchased = Column(Integer, nullable=False, default=0)
    total_credits_used = Column(Integer, nullable=False, default=0)
    total_credits_expired = Column(Integer, nullable=False, default=0)
    
    # Subscription relationship
    subscription_id = Column(String(255), ForeignKey("user_subscriptions.id"), nullable=True)
    
    # Credit refill tracking
    last_credit_refill = Column(DateTime(timezone=True), nullable=True)
    next_credit_refill = Column(DateTime(timezone=True), nullable=True)
    
    # Usage tracking for current period
    credits_used_this_period = Column(Integer, nullable=False, default=0)
    period_start = Column(DateTime(timezone=True), nullable=True)
    period_end = Column(DateTime(timezone=True), nullable=True)
    
    # Credits metadata
    credits_metadata = Column(JSON, nullable=False, default=dict)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    subscription = relationship("UserSubscription", back_populates="user_credits")
    usage_logs = relationship("UsageLog", back_populates="user_credits")
    
    # Indexes
    __table_args__ = (
        Index('idx_user_credits_subscription', 'subscription_id'),
        Index('idx_user_credits_refill', 'next_credit_refill'),
        CheckConstraint('current_credits >= 0', name='check_positive_current_credits'),
        CheckConstraint('total_credits_purchased >= 0', name='check_positive_purchased_credits'),
        CheckConstraint('total_credits_used >= 0', name='check_positive_used_credits'),
    )
    
    def can_use_credits(self, amount: int) -> bool:
        """Check if user can use specified amount of credits"""
        return self.current_credits >= amount
    
    def use_credits(self, amount: int) -> bool:
        """Use credits if available"""
        if self.can_use_credits(amount):
            self.current_credits -= amount
            self.total_credits_used += amount
            self.credits_used_this_period += amount
            self.updated_at = datetime.now(timezone.utc)
            return True
        return False
    
    def add_credits(self, amount: int, source: str = "purchase") -> None:
        """Add credits to user account"""
        self.current_credits += amount
        if source == "purchase":
            self.total_credits_purchased += amount
        self.last_credit_refill = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
    
    def get_usage_stats(self) -> dict:
        """Get usage statistics"""
        return {
            "current_credits": self.current_credits,
            "total_purchased": self.total_credits_purchased,
            "total_used": self.total_credits_used,
            "total_expired": self.total_credits_expired,
            "used_this_period": self.credits_used_this_period,
            "last_refill": self.last_credit_refill.isoformat() if self.last_credit_refill else None,
            "next_refill": self.next_credit_refill.isoformat() if self.next_credit_refill else None
        }
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            "user_id": self.user_id,
            "current_credits": self.current_credits,
            "total_credits_purchased": self.total_credits_purchased,
            "total_credits_used": self.total_credits_used,
            "total_credits_expired": self.total_credits_expired,
            "subscription_id": self.subscription_id,
            "last_credit_refill": self.last_credit_refill.isoformat() if self.last_credit_refill else None,
            "next_credit_refill": self.next_credit_refill.isoformat() if self.next_credit_refill else None,
            "credits_used_this_period": self.credits_used_this_period,
            "period_start": self.period_start.isoformat() if self.period_start else None,
            "period_end": self.period_end.isoformat() if self.period_end else None,
            "credits_metadata": self.credits_metadata,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class PaymentHistory(Base):
    """Payment transaction history"""
    __tablename__ = "payment_history"
    
    id = Column(String(255), primary_key=True)
    user_id = Column(String(255), nullable=False, index=True)  # Firebase UID
    
    # Payment details
    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String(3), nullable=False, default="USD")
    status = Column(String(20), nullable=False, default=PaymentStatus.PENDING)
    
    # Payment method and provider
    payment_method = Column(String(50), nullable=False, default="lemon_squeezy")
    payment_provider = Column(String(50), nullable=False, default="lemon_squeezy")
    
    # Lemon Squeezy integration
    lemon_squeezy_order_id = Column(String(255), unique=True, nullable=True)
    lemon_squeezy_subscription_id = Column(String(255), nullable=True)
    lemon_squeezy_customer_id = Column(String(255), nullable=True)
    
    # Subscription and credits
    subscription_id = Column(String(255), ForeignKey("user_subscriptions.id"), nullable=True)
    credits_awarded = Column(Integer, nullable=False, default=0)
    plan_id = Column(String(50), ForeignKey("subscription_plans.id"), nullable=True)
    
    # Transaction details
    transaction_type = Column(String(50), nullable=False, default="subscription")  # subscription, one_time, refund
    description = Column(Text, nullable=True)
    
    # Payment metadata
    payment_metadata = Column(JSON, nullable=False, default=dict)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    processed_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    subscription = relationship("UserSubscription", back_populates="payment_history")
    plan = relationship("SubscriptionPlan")
    
    # Indexes
    __table_args__ = (
        Index('idx_payment_history_user_id', 'user_id'),
        Index('idx_payment_history_status', 'status'),
        Index('idx_payment_history_ls_order', 'lemon_squeezy_order_id'),
        Index('idx_payment_history_ls_subscription', 'lemon_squeezy_subscription_id'),
        Index('idx_payment_history_created', 'created_at'),
        CheckConstraint('amount >= 0', name='check_positive_amount'),
        CheckConstraint('credits_awarded >= 0', name='check_positive_credits_awarded'),
    )
    
    @validates('status')
    def validate_status(self, key, status):
        """Validate payment status"""
        if status not in [s.value for s in PaymentStatus]:
            raise ValueError(f"Invalid payment status: {status}")
        return status
    
    @validates('currency')
    def validate_currency(self, key, currency):
        """Validate currency code"""
        if currency and len(currency) != 3:
            raise ValueError("Currency must be a 3-letter code")
        return currency.upper() if currency else "USD"
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "amount": float(self.amount),
            "currency": self.currency,
            "status": self.status,
            "payment_method": self.payment_method,
            "payment_provider": self.payment_provider,
            "lemon_squeezy_order_id": self.lemon_squeezy_order_id,
            "lemon_squeezy_subscription_id": self.lemon_squeezy_subscription_id,
            "lemon_squeezy_customer_id": self.lemon_squeezy_customer_id,
            "subscription_id": self.subscription_id,
            "credits_awarded": self.credits_awarded,
            "plan_id": self.plan_id,
            "transaction_type": self.transaction_type,
            "description": self.description,
            "payment_metadata": self.payment_metadata,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "processed_at": self.processed_at.isoformat() if self.processed_at else None
        }


class UsageLog(Base):
    """AI generation usage tracking for billing and analytics"""
    __tablename__ = "usage_logs"
    
    id = Column(String(255), primary_key=True)
    user_id = Column(String(255), nullable=False, index=True)  # Firebase UID
    
    # Usage details
    usage_type = Column(String(50), nullable=False, default=UsageType.AI_GENERATION)
    credits_used = Column(Integer, nullable=False, default=1)
    
    # Generation details
    product_count = Column(Integer, nullable=False, default=1)  # For batch processing
    language_code = Column(String(10), nullable=True)
    category = Column(String(100), nullable=True)
    
    # Performance metrics
    tokens_used = Column(Integer, nullable=True)
    response_time_ms = Column(Integer, nullable=True)
    cost_usd = Column(Numeric(10, 6), nullable=True)
    
    # Request details
    request_id = Column(String(255), nullable=True)
    batch_id = Column(String(255), nullable=True)
    endpoint_used = Column(String(100), nullable=True)
    
    # User credits relationship
    user_credits_id = Column(String(255), ForeignKey("user_credits.user_id"), nullable=True)
    
    # Usage metadata
    usage_metadata = Column(JSON, nullable=False, default=dict)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    user_credits = relationship("UserCredits", back_populates="usage_logs")
    
    # Indexes
    __table_args__ = (
        Index('idx_usage_logs_user_id', 'user_id'),
        Index('idx_usage_logs_type', 'usage_type'),
        Index('idx_usage_logs_created', 'created_at'),
        Index('idx_usage_logs_batch', 'batch_id'),
        Index('idx_usage_logs_request', 'request_id'),
        CheckConstraint('credits_used > 0', name='check_positive_credits_used'),
        CheckConstraint('product_count > 0', name='check_positive_product_count'),
    )
    
    @validates('usage_type')
    def validate_usage_type(self, key, usage_type):
        """Validate usage type"""
        if usage_type not in [t.value for t in UsageType]:
            raise ValueError(f"Invalid usage type: {usage_type}")
        return usage_type
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "usage_type": self.usage_type,
            "credits_used": self.credits_used,
            "product_count": self.product_count,
            "language_code": self.language_code,
            "category": self.category,
            "tokens_used": self.tokens_used,
            "response_time_ms": self.response_time_ms,
            "cost_usd": float(self.cost_usd) if self.cost_usd else None,
            "request_id": self.request_id,
            "batch_id": self.batch_id,
            "endpoint_used": self.endpoint_used,
            "user_credits_id": self.user_credits_id,
            "usage_metadata": self.usage_metadata,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
