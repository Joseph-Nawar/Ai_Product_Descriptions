# backend/src/payments/secure_operations.py
"""
Secure payment operations with atomic transactions and retry logic
"""

import logging
import asyncio
import time
from typing import Dict, Any, Optional, Tuple, List
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from contextlib import asynccontextmanager
from enum import Enum
import uuid
import json

from .security import PaymentSecurityService, AuditEventType, SecurityLevel
from .models import UserCredits, PaymentHistory, PaymentStatus

logger = logging.getLogger(__name__)


class OperationType(str, Enum):
    """Types of secure operations"""
    CREDIT_DEDUCTION = "credit_deduction"
    CREDIT_ADDITION = "credit_addition"
    SUBSCRIPTION_UPDATE = "subscription_update"
    PAYMENT_PROCESSING = "payment_processing"
    REFUND_PROCESSING = "refund_processing"


class TransactionStatus(str, Enum):
    """Transaction status"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"
    RETRY_PENDING = "retry_pending"


@dataclass
class SecureTransaction:
    """Secure transaction record"""
    transaction_id: str
    operation_type: OperationType
    user_id: str
    status: TransactionStatus = TransactionStatus.PENDING
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    data: Dict[str, Any] = field(default_factory=dict)
    retry_count: int = 0
    max_retries: int = 3
    error_message: Optional[str] = None
    rollback_data: Optional[Dict[str, Any]] = None
    correlation_id: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "transaction_id": self.transaction_id,
            "operation_type": self.operation_type.value,
            "user_id": self.user_id,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "data": self.data,
            "retry_count": self.retry_count,
            "max_retries": self.max_retries,
            "error_message": self.error_message,
            "rollback_data": self.rollback_data,
            "correlation_id": self.correlation_id
        }


@dataclass
class RetryConfig:
    """Retry configuration"""
    max_attempts: int = 3
    base_delay_seconds: float = 1.0
    max_delay_seconds: float = 60.0
    exponential_backoff: bool = True
    jitter: bool = True


class SecurePaymentOperations:
    """Service for secure payment operations with atomicity and retry logic"""
    
    def __init__(self, db_service, security_service: Optional[PaymentSecurityService] = None):
        self.db_service = db_service
        self.security_service = security_service or PaymentSecurityService()
        self.active_transactions: Dict[str, SecureTransaction] = {}
        self.transaction_locks: Dict[str, asyncio.Lock] = {}
        
        # Default retry configurations
        self.retry_configs = {
            OperationType.CREDIT_DEDUCTION: RetryConfig(max_attempts=3, base_delay_seconds=0.5),
            OperationType.CREDIT_ADDITION: RetryConfig(max_attempts=5, base_delay_seconds=1.0),
            OperationType.SUBSCRIPTION_UPDATE: RetryConfig(max_attempts=3, base_delay_seconds=2.0),
            OperationType.PAYMENT_PROCESSING: RetryConfig(max_attempts=3, base_delay_seconds=5.0),
            OperationType.REFUND_PROCESSING: RetryConfig(max_attempts=5, base_delay_seconds=10.0)
        }
    
    async def secure_credit_deduction(
        self,
        user_id: str,
        amount: int,
        operation_context: Optional[Dict[str, Any]] = None,
        correlation_id: Optional[str] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        Securely deduct credits with atomic operation and validation
        
        Args:
            user_id: User identifier
            amount: Credits to deduct
            operation_context: Additional context for the operation
            correlation_id: Correlation ID for tracking
            
        Returns:
            Tuple[bool, Dict[str, Any]]: (success, result_data)
        """
        transaction_id = str(uuid.uuid4())
        correlation_id = correlation_id or str(uuid.uuid4())
        
        transaction = SecureTransaction(
            transaction_id=transaction_id,
            operation_type=OperationType.CREDIT_DEDUCTION,
            user_id=user_id,
            data={
                "amount": amount,
                "context": operation_context or {}
            },
            correlation_id=correlation_id
        )
        
        try:
            async with self._get_user_lock(user_id):
                # Validate operation
                is_valid, validation_errors = await self._validate_credit_deduction(
                    user_id, amount, transaction
                )
                
                if not is_valid:
                    return False, {
                        "error": "Credit deduction validation failed",
                        "validation_errors": validation_errors,
                        "transaction_id": transaction_id
                    }
                
                # Execute with retry logic
                success, result = await self._execute_with_retry(
                    transaction, self._perform_credit_deduction
                )
                
                return success, result
                
        except Exception as e:
            logger.error(f"Error in secure credit deduction: {str(e)}")
            await self._handle_transaction_error(transaction, str(e))
            return False, {
                "error": "Credit deduction failed",
                "details": str(e),
                "transaction_id": transaction_id
            }
    
    async def secure_credit_addition(
        self,
        user_id: str,
        amount: int,
        source: str,
        operation_context: Optional[Dict[str, Any]] = None,
        correlation_id: Optional[str] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        Securely add credits with atomic operation
        
        Args:
            user_id: User identifier
            amount: Credits to add
            source: Source of credits (purchase, refund, bonus, etc.)
            operation_context: Additional context
            correlation_id: Correlation ID for tracking
            
        Returns:
            Tuple[bool, Dict[str, Any]]: (success, result_data)
        """
        transaction_id = str(uuid.uuid4())
        correlation_id = correlation_id or str(uuid.uuid4())
        
        transaction = SecureTransaction(
            transaction_id=transaction_id,
            operation_type=OperationType.CREDIT_ADDITION,
            user_id=user_id,
            data={
                "amount": amount,
                "source": source,
                "context": operation_context or {}
            },
            correlation_id=correlation_id
        )
        
        try:
            async with self._get_user_lock(user_id):
                # Validate operation
                is_valid, validation_errors = await self._validate_credit_addition(
                    user_id, amount, source, transaction
                )
                
                if not is_valid:
                    return False, {
                        "error": "Credit addition validation failed",
                        "validation_errors": validation_errors,
                        "transaction_id": transaction_id
                    }
                
                # Execute with retry logic
                success, result = await self._execute_with_retry(
                    transaction, self._perform_credit_addition
                )
                
                return success, result
                
        except Exception as e:
            logger.error(f"Error in secure credit addition: {str(e)}")
            await self._handle_transaction_error(transaction, str(e))
            return False, {
                "error": "Credit addition failed",
                "details": str(e),
                "transaction_id": transaction_id
            }
    
    async def secure_subscription_update(
        self,
        user_id: str,
        new_plan_id: str,
        operation_context: Optional[Dict[str, Any]] = None,
        correlation_id: Optional[str] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        Securely update subscription with validation
        
        Args:
            user_id: User identifier
            new_plan_id: New subscription plan ID
            operation_context: Additional context
            correlation_id: Correlation ID for tracking
            
        Returns:
            Tuple[bool, Dict[str, Any]]: (success, result_data)
        """
        transaction_id = str(uuid.uuid4())
        correlation_id = correlation_id or str(uuid.uuid4())
        
        transaction = SecureTransaction(
            transaction_id=transaction_id,
            operation_type=OperationType.SUBSCRIPTION_UPDATE,
            user_id=user_id,
            data={
                "new_plan_id": new_plan_id,
                "context": operation_context or {}
            },
            correlation_id=correlation_id
        )
        
        try:
            async with self._get_user_lock(user_id):
                # Get current subscription for rollback
                current_user_credits = await self._get_user_credits(user_id)
                if current_user_credits:
                    transaction.rollback_data = {
                        "previous_plan": current_user_credits.subscription_id,
                        "previous_tier": current_user_credits.subscription.plan_id if current_user_credits.subscription else None,
                        "previous_expires_at": current_user_credits.subscription.current_period_end.isoformat() if current_user_credits.subscription else None
                    }
                
                # Validate operation
                is_valid, validation_errors = await self._validate_subscription_update(
                    user_id, new_plan_id, transaction
                )
                
                if not is_valid:
                    return False, {
                        "error": "Subscription update validation failed",
                        "validation_errors": validation_errors,
                        "transaction_id": transaction_id
                    }
                
                # Execute with retry logic
                success, result = await self._execute_with_retry(
                    transaction, self._perform_subscription_update
                )
                
                return success, result
                
        except Exception as e:
            logger.error(f"Error in secure subscription update: {str(e)}")
            await self._handle_transaction_error(transaction, str(e))
            return False, {
                "error": "Subscription update failed",
                "details": str(e),
                "transaction_id": transaction_id
            }
    
    async def _validate_credit_deduction(
        self,
        user_id: str,
        amount: int,
        transaction: SecureTransaction
    ) -> Tuple[bool, List[str]]:
        """Validate credit deduction operation"""
        errors = []
        
        try:
            # Basic validation
            if amount <= 0:
                errors.append("Deduction amount must be positive")
            
            if amount > 1000:  # Maximum single deduction
                errors.append("Deduction amount exceeds maximum allowed")
            
            # Get current user credits
            user_credits = await self._get_user_credits(user_id)
            if not user_credits:
                errors.append("User credits not found")
                return False, errors
            
            # Check sufficient balance
            if user_credits.current_credits < amount:
                errors.append(f"Insufficient credits. Available: {user_credits.current_credits}, Required: {amount}")
            
            # Check rate limits and fraud detection
            fraud_result = self.security_service.detect_fraud(
                payment_data={"amount": amount, "operation": "credit_deduction"},
                user_data={
                    "user_id": user_id,
                    "current_credits": user_credits.current_credits,
                    "account_age_days": (datetime.now(timezone.utc) - user_credits.created_at).days,
                    "recent_deductions": user_credits.total_credits_used
                }
            )
            
            if fraud_result.is_fraudulent:
                errors.append(f"Fraud detection triggered: {', '.join(fraud_result.risk_factors)}")
            
            # Log validation
            self.security_service.log_audit_event(
                event_type=AuditEventType.CREDIT_DEDUCTED,
                user_id=user_id,
                event_data={
                    "amount": amount,
                    "validation_success": len(errors) == 0,
                    "errors": errors,
                    "transaction_id": transaction.transaction_id
                },
                security_level=SecurityLevel.MEDIUM,
                success=len(errors) == 0,
                correlation_id=transaction.correlation_id
            )
            
        except Exception as e:
            logger.error(f"Error validating credit deduction: {str(e)}")
            errors.append("Credit deduction validation error")
        
        return len(errors) == 0, errors
    
    async def _validate_credit_addition(
        self,
        user_id: str,
        amount: int,
        source: str,
        transaction: SecureTransaction
    ) -> Tuple[bool, List[str]]:
        """Validate credit addition operation"""
        errors = []
        
        try:
            # Basic validation
            if amount <= 0:
                errors.append("Addition amount must be positive")
            
            if amount > 10000:  # Maximum single addition
                errors.append("Addition amount exceeds maximum allowed")
            
            # Validate source
            valid_sources = ["purchase", "refund", "bonus", "correction", "subscription"]
            if source not in valid_sources:
                errors.append(f"Invalid credit source: {source}")
            
            # Get current user credits
            user_credits = await self._get_user_credits(user_id)
            if not user_credits:
                errors.append("User credits not found")
                return False, errors
            
            # Check maximum balance limits
            max_balance = 50000  # Maximum allowed balance
            if user_credits.current_credits + amount > max_balance:
                errors.append(f"Addition would exceed maximum balance limit of {max_balance}")
            
            # Log validation
            self.security_service.log_audit_event(
                event_type=AuditEventType.CREDIT_BALANCE_UPDATED,
                user_id=user_id,
                event_data={
                    "amount": amount,
                    "source": source,
                    "validation_success": len(errors) == 0,
                    "errors": errors,
                    "transaction_id": transaction.transaction_id
                },
                security_level=SecurityLevel.MEDIUM,
                success=len(errors) == 0,
                correlation_id=transaction.correlation_id
            )
            
        except Exception as e:
            logger.error(f"Error validating credit addition: {str(e)}")
            errors.append("Credit addition validation error")
        
        return len(errors) == 0, errors
    
    async def _validate_subscription_update(
        self,
        user_id: str,
        new_plan_id: str,
        transaction: SecureTransaction
    ) -> Tuple[bool, List[str]]:
        """Validate subscription update operation"""
        errors = []
        
        try:
            # Validate plan ID
            valid_plans = ["free", "basic", "pro", "enterprise"]
            if new_plan_id not in valid_plans:
                errors.append(f"Invalid plan ID: {new_plan_id}")
            
            # Get current user credits
            user_credits = await self._get_user_credits(user_id)
            if not user_credits:
                errors.append("User credits not found")
                return False, errors
            
            # Check if already on the same plan
            if user_credits.subscription_id == new_plan_id:
                errors.append("User is already on the requested plan")
            
            # Log validation
            self.security_service.log_audit_event(
                event_type=AuditEventType.SUBSCRIPTION_UPDATED,
                user_id=user_id,
                event_data={
                    "new_plan_id": new_plan_id,
                    "current_plan_id": user_credits.subscription_id,
                    "validation_success": len(errors) == 0,
                    "errors": errors,
                    "transaction_id": transaction.transaction_id
                },
                security_level=SecurityLevel.MEDIUM,
                success=len(errors) == 0,
                correlation_id=transaction.correlation_id
            )
            
        except Exception as e:
            logger.error(f"Error validating subscription update: {str(e)}")
            errors.append("Subscription update validation error")
        
        return len(errors) == 0, errors
    
    async def _execute_with_retry(
        self,
        transaction: SecureTransaction,
        operation_func
    ) -> Tuple[bool, Dict[str, Any]]:
        """Execute operation with retry logic"""
        retry_config = self.retry_configs.get(
            transaction.operation_type,
            RetryConfig()
        )
        
        self.active_transactions[transaction.transaction_id] = transaction
        
        for attempt in range(retry_config.max_attempts):
            try:
                transaction.retry_count = attempt
                transaction.status = TransactionStatus.IN_PROGRESS
                transaction.updated_at = datetime.now(timezone.utc)
                
                # Execute the operation
                success, result = await operation_func(transaction)
                
                if success:
                    transaction.status = TransactionStatus.COMPLETED
                    transaction.updated_at = datetime.now(timezone.utc)
                    
                    # Clean up transaction record
                    self.active_transactions.pop(transaction.transaction_id, None)
                    
                    return True, result
                else:
                    transaction.status = TransactionStatus.FAILED
                    transaction.error_message = result.get("error", "Unknown error")
                    
                    # Check if we should retry
                    if attempt < retry_config.max_attempts - 1:
                        transaction.status = TransactionStatus.RETRY_PENDING
                        
                        # Calculate delay with exponential backoff
                        delay = self._calculate_retry_delay(
                            attempt, retry_config
                        )
                        
                        logger.warning(
                            f"Transaction {transaction.transaction_id} failed, "
                            f"retrying in {delay} seconds (attempt {attempt + 1}/{retry_config.max_attempts})"
                        )
                        
                        await asyncio.sleep(delay)
                    else:
                        # No more retries, attempt rollback
                        await self._attempt_rollback(transaction)
                        self.active_transactions.pop(transaction.transaction_id, None)
                        
                        return False, result
                        
            except Exception as e:
                logger.error(f"Exception in transaction execution: {str(e)}")
                transaction.error_message = str(e)
                
                if attempt < retry_config.max_attempts - 1:
                    delay = self._calculate_retry_delay(attempt, retry_config)
                    await asyncio.sleep(delay)
                else:
                    transaction.status = TransactionStatus.FAILED
                    await self._attempt_rollback(transaction)
                    self.active_transactions.pop(transaction.transaction_id, None)
                    
                    return False, {
                        "error": "Transaction execution failed",
                        "details": str(e),
                        "transaction_id": transaction.transaction_id
                    }
        
        return False, {
            "error": "Transaction failed after all retry attempts",
            "transaction_id": transaction.transaction_id
        }
    
    async def _perform_credit_deduction(
        self,
        transaction: SecureTransaction
    ) -> Tuple[bool, Dict[str, Any]]:
        """Perform the actual credit deduction"""
        try:
            user_id = transaction.user_id
            amount = transaction.data["amount"]
            
            # Get current user credits with a fresh read
            user_credits = await self._get_user_credits(user_id)
            if not user_credits:
                return False, {"error": "User credits not found"}
            
            # Double-check balance (race condition protection)
            if user_credits.current_credits < amount:
                return False, {
                    "error": "Insufficient credits",
                    "available": user_credits.current_credits,
                    "required": amount
                }
            
            # Store original state for rollback
            transaction.rollback_data = {
                "original_credits": user_credits.current_credits,
                "original_used": user_credits.total_credits_used
            }
            
            # Update credits atomically
            success = await self.db_service.update_user_credits_atomic(
                user_id=user_id,
                credit_change=-amount,
                expected_current_credits=user_credits.current_credits
            )
            
            if not success:
                return False, {"error": "Atomic credit update failed (race condition detected)"}
            
            # Record the transaction in payment history
            await self._record_credit_transaction(
                user_id=user_id,
                amount=-amount,
                transaction_type="deduction",
                transaction_id=transaction.transaction_id,
                context=transaction.data.get("context", {})
            )
            
            # Log successful deduction
            self.security_service.log_audit_event(
                event_type=AuditEventType.CREDIT_DEDUCTED,
                user_id=user_id,
                event_data={
                    "amount": amount,
                    "transaction_id": transaction.transaction_id,
                    "remaining_credits": user_credits.current_credits - amount
                },
                security_level=SecurityLevel.MEDIUM,
                success=True,
                correlation_id=transaction.correlation_id
            )
            
            return True, {
                "credits_deducted": amount,
                "remaining_credits": user_credits.current_credits - amount,
                "transaction_id": transaction.transaction_id
            }
            
        except Exception as e:
            logger.error(f"Error performing credit deduction: {str(e)}")
            return False, {"error": str(e)}
    
    async def _perform_credit_addition(
        self,
        transaction: SecureTransaction
    ) -> Tuple[bool, Dict[str, Any]]:
        """Perform the actual credit addition"""
        try:
            user_id = transaction.user_id
            amount = transaction.data["amount"]
            source = transaction.data["source"]
            
            # Get current user credits
            user_credits = await self._get_user_credits(user_id)
            if not user_credits:
                return False, {"error": "User credits not found"}
            
            # Store original state for rollback
            transaction.rollback_data = {
                "original_credits": user_credits.current_credits,
                "original_purchased": user_credits.total_credits_purchased
            }
            
            # Update credits atomically
            success = await self.db_service.update_user_credits_atomic(
                user_id=user_id,
                credit_change=amount,
                expected_current_credits=user_credits.current_credits
            )
            
            if not success:
                return False, {"error": "Atomic credit update failed"}
            
            # Update purchased credits if this is a purchase
            if source == "purchase":
                await self.db_service.update_total_credits_purchased(
                    user_id=user_id,
                    additional_purchased=amount
                )
            
            # Record the transaction in payment history
            await self._record_credit_transaction(
                user_id=user_id,
                amount=amount,
                transaction_type="addition",
                transaction_id=transaction.transaction_id,
                context=transaction.data.get("context", {}),
                source=source
            )
            
            # Log successful addition
            self.security_service.log_audit_event(
                event_type=AuditEventType.CREDIT_BALANCE_UPDATED,
                user_id=user_id,
                event_data={
                    "amount": amount,
                    "source": source,
                    "transaction_id": transaction.transaction_id,
                    "new_balance": user_credits.current_credits + amount
                },
                security_level=SecurityLevel.MEDIUM,
                success=True,
                correlation_id=transaction.correlation_id
            )
            
            return True, {
                "credits_added": amount,
                "new_balance": user_credits.current_credits + amount,
                "source": source,
                "transaction_id": transaction.transaction_id
            }
            
        except Exception as e:
            logger.error(f"Error performing credit addition: {str(e)}")
            return False, {"error": str(e)}
    
    async def _perform_subscription_update(
        self,
        transaction: SecureTransaction
    ) -> Tuple[bool, Dict[str, Any]]:
        """Perform the actual subscription update"""
        try:
            user_id = transaction.user_id
            new_plan_id = transaction.data["new_plan_id"]
            
            # Update subscription atomically
            success = await self.db_service.update_user_subscription(
                user_id=user_id,
                new_plan_id=new_plan_id
            )
            
            if not success:
                return False, {"error": "Subscription update failed"}
            
            # Log successful update
            self.security_service.log_audit_event(
                event_type=AuditEventType.SUBSCRIPTION_UPDATED,
                user_id=user_id,
                event_data={
                    "new_plan_id": new_plan_id,
                    "transaction_id": transaction.transaction_id,
                    "previous_plan": transaction.rollback_data.get("previous_plan") if transaction.rollback_data else None
                },
                security_level=SecurityLevel.MEDIUM,
                success=True,
                correlation_id=transaction.correlation_id
            )
            
            return True, {
                "new_plan_id": new_plan_id,
                "transaction_id": transaction.transaction_id
            }
            
        except Exception as e:
            logger.error(f"Error performing subscription update: {str(e)}")
            return False, {"error": str(e)}
    
    def _calculate_retry_delay(self, attempt: int, config: RetryConfig) -> float:
        """Calculate retry delay with exponential backoff and jitter"""
        if config.exponential_backoff:
            delay = config.base_delay_seconds * (2 ** attempt)
        else:
            delay = config.base_delay_seconds
        
        # Apply maximum delay limit
        delay = min(delay, config.max_delay_seconds)
        
        # Add jitter to prevent thundering herd
        if config.jitter:
            import random
            jitter_factor = random.uniform(0.8, 1.2)
            delay *= jitter_factor
        
        return delay
    
    async def _attempt_rollback(self, transaction: SecureTransaction):
        """Attempt to rollback a failed transaction"""
        try:
            if not transaction.rollback_data:
                logger.warning(f"No rollback data for transaction {transaction.transaction_id}")
                return
            
            logger.info(f"Attempting rollback for transaction {transaction.transaction_id}")
            
            if transaction.operation_type == OperationType.CREDIT_DEDUCTION:
                # Restore original credits
                original_credits = transaction.rollback_data["original_credits"]
                await self.db_service.set_user_credits(
                    user_id=transaction.user_id,
                    credits=original_credits
                )
            
            elif transaction.operation_type == OperationType.CREDIT_ADDITION:
                # Remove added credits
                original_credits = transaction.rollback_data["original_credits"]
                await self.db_service.set_user_credits(
                    user_id=transaction.user_id,
                    credits=original_credits
                )
            
            elif transaction.operation_type == OperationType.SUBSCRIPTION_UPDATE:
                # Restore previous subscription
                if "previous_plan" in transaction.rollback_data:
                    await self.db_service.update_user_subscription(
                        user_id=transaction.user_id,
                        new_plan_id=transaction.rollback_data["previous_plan"]
                    )
            
            transaction.status = TransactionStatus.ROLLED_BACK
            
            # Log rollback
            self.security_service.log_audit_event(
                event_type=AuditEventType.CREDIT_BALANCE_UPDATED,
                user_id=transaction.user_id,
                event_data={
                    "operation": "rollback",
                    "transaction_id": transaction.transaction_id,
                    "operation_type": transaction.operation_type.value
                },
                security_level=SecurityLevel.HIGH,
                success=True,
                correlation_id=transaction.correlation_id
            )
            
        except Exception as e:
            logger.error(f"Error during rollback for transaction {transaction.transaction_id}: {str(e)}")
            transaction.status = TransactionStatus.FAILED
    
    async def _handle_transaction_error(self, transaction: SecureTransaction, error_message: str):
        """Handle transaction error"""
        transaction.status = TransactionStatus.FAILED
        transaction.error_message = error_message
        transaction.updated_at = datetime.now(timezone.utc)
        
        # Log error
        self.security_service.log_audit_event(
            event_type=AuditEventType.SECURITY_VIOLATION,
            user_id=transaction.user_id,
            event_data={
                "transaction_id": transaction.transaction_id,
                "operation_type": transaction.operation_type.value,
                "error": error_message
            },
            security_level=SecurityLevel.HIGH,
            success=False,
            error_message=error_message,
            correlation_id=transaction.correlation_id
        )
    
    async def _get_user_lock(self, user_id: str) -> asyncio.Lock:
        """Get or create a lock for a specific user"""
        if user_id not in self.transaction_locks:
            self.transaction_locks[user_id] = asyncio.Lock()
        return self.transaction_locks[user_id]
    
    async def _get_user_credits(self, user_id: str, db_session=None) -> Optional[UserCredits]:
        """Get user credits safely"""
        try:
            if db_session:
                return self.db_service.get_user_credits(user_id, db_session)
            else:
                return self.db_service.get_user_credits(user_id)
        except Exception as e:
            logger.error(f"Error getting user credits for {user_id}: {str(e)}")
            return None
    
    async def _record_credit_transaction(
        self,
        user_id: str,
        amount: int,
        transaction_type: str,
        transaction_id: str,
        context: Dict[str, Any],
        source: Optional[str] = None
    ):
        """Record credit transaction in payment history"""
        try:
            payment_history = PaymentHistory(
                user_id=user_id,
                amount=abs(amount),
                status=PaymentStatus.COMPLETED,
                transaction_id=transaction_id,
                payment_method="credits",
                payment_data={
                    "transaction_type": transaction_type,
                    "credit_amount": amount,
                    "source": source,
                    "context": context
                }
            )
            
            await self.db_service.create_payment_history(payment_history)
            
        except Exception as e:
            logger.error(f"Error recording credit transaction: {str(e)}")
    
    def get_transaction_status(self, transaction_id: str) -> Optional[Dict[str, Any]]:
        """Get transaction status"""
        transaction = self.active_transactions.get(transaction_id)
        if transaction:
            return transaction.to_dict()
        return None
    
    def get_active_transactions(self, user_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get active transactions, optionally filtered by user"""
        transactions = []
        for transaction in self.active_transactions.values():
            if user_id is None or transaction.user_id == user_id:
                transactions.append(transaction.to_dict())
        return transactions
