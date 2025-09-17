# backend/src/payments/security.py
"""
Payment security utilities and validation
"""

import os
import hmac
import hashlib
import logging
import time
import json
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
from enum import Enum
import ipaddress
import re

logger = logging.getLogger(__name__)


class SecurityLevel(str, Enum):
    """Security level for operations"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AuditEventType(str, Enum):
    """Audit event types"""
    PAYMENT_CREATED = "payment_created"
    PAYMENT_COMPLETED = "payment_completed"
    PAYMENT_FAILED = "payment_failed"
    PAYMENT_REFUNDED = "payment_refunded"
    SUBSCRIPTION_CREATED = "subscription_created"
    SUBSCRIPTION_CANCELLED = "subscription_cancelled"
    SUBSCRIPTION_UPDATED = "subscription_updated"
    CREDIT_BALANCE_UPDATED = "credit_balance_updated"
    CREDIT_DEDUCTED = "credit_deducted"
    WEBHOOK_RECEIVED = "webhook_received"
    WEBHOOK_PROCESSED = "webhook_processed"
    WEBHOOK_VERIFICATION_FAILED = "webhook_verification_failed"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    FRAUD_DETECTED = "fraud_detected"
    SECURITY_VIOLATION = "security_violation"


@dataclass
class AuditLog:
    """Audit log entry"""
    event_type: AuditEventType
    user_id: Optional[str] = None
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    event_data: Dict[str, Any] = field(default_factory=dict)
    security_level: SecurityLevel = SecurityLevel.MEDIUM
    success: bool = True
    error_message: Optional[str] = None
    session_id: Optional[str] = None
    correlation_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "event_type": self.event_type.value,
            "user_id": self.user_id,
            "timestamp": self.timestamp.isoformat(),
            "ip_address": self.ip_address,
            "user_agent": self.user_agent,
            "event_data": self.event_data,
            "security_level": self.security_level.value,
            "success": self.success,
            "error_message": self.error_message,
            "session_id": self.session_id,
            "correlation_id": self.correlation_id
        }


@dataclass
class FraudDetectionResult:
    """Fraud detection analysis result"""
    is_fraudulent: bool = False
    confidence_score: float = 0.0  # 0.0 to 1.0
    risk_factors: List[str] = field(default_factory=list)
    recommended_action: str = "allow"  # allow, review, block
    additional_checks_required: List[str] = field(default_factory=list)


@dataclass
class RateLimitConfig:
    """Rate limiting configuration"""
    max_requests: int
    time_window_seconds: int
    burst_limit: int = 0  # Allow burst above normal rate
    penalty_duration_seconds: int = 300  # 5 minutes default


class PaymentSecurityService:
    """Comprehensive payment security service"""
    
    def __init__(self):
        self.webhook_secret = os.getenv("LEMON_SQUEEZY_WEBHOOK_SECRET")
        self.allowed_ips = self._parse_allowed_ips()
        self.rate_limits = self._initialize_rate_limits()
        self.fraud_detection_enabled = os.getenv("FRAUD_DETECTION_ENABLED", "true").lower() == "true"
        self.audit_logs: List[AuditLog] = []
        
    def _parse_allowed_ips(self) -> List[str]:
        """Parse allowed IP addresses for webhooks"""
        allowed_ips_env = os.getenv("LEMON_SQUEEZY_ALLOWED_IPS", "")
        if not allowed_ips_env:
            # Default Lemon Squeezy IP ranges (should be configured properly)
            return ["0.0.0.0/0"]  # WARNING: This allows all IPs - configure properly in production
        return [ip.strip() for ip in allowed_ips_env.split(",")]
    
    def _initialize_rate_limits(self) -> Dict[str, RateLimitConfig]:
        """Initialize rate limiting configurations"""
        return {
            "checkout": RateLimitConfig(max_requests=10, time_window_seconds=300, burst_limit=15),
            "webhook": RateLimitConfig(max_requests=100, time_window_seconds=60, burst_limit=150),
            "credit_check": RateLimitConfig(max_requests=60, time_window_seconds=60, burst_limit=80),
            "credit_deduct": RateLimitConfig(max_requests=30, time_window_seconds=60, burst_limit=40),
            "subscription": RateLimitConfig(max_requests=20, time_window_seconds=300, burst_limit=25)
        }
    
    def verify_webhook_signature(self, payload: str, signature: str) -> bool:
        """
        Verify Lemon Squeezy webhook signature
        
        Args:
            payload: Raw webhook payload
            signature: Signature from X-Signature header
            
        Returns:
            bool: True if signature is valid
        """
        try:
            if not self.webhook_secret:
                logger.error("Webhook secret not configured")
                return False
            
            if not signature:
                logger.error("No signature provided")
                return False
            
            # Remove 'sha256=' prefix if present
            if signature.startswith('sha256='):
                signature = signature[7:]
            
            # Calculate expected signature
            expected_signature = hmac.new(
                self.webhook_secret.encode('utf-8'),
                payload.encode('utf-8'),
                hashlib.sha256
            ).hexdigest()
            
            # Use secure comparison to prevent timing attacks
            is_valid = hmac.compare_digest(signature, expected_signature)
            
            # Log verification attempt
            self.log_audit_event(
                event_type=AuditEventType.WEBHOOK_RECEIVED,
                event_data={
                    "signature_provided": bool(signature),
                    "signature_valid": is_valid
                },
                success=is_valid,
                error_message=None if is_valid else "Invalid webhook signature",
                security_level=SecurityLevel.HIGH
            )
            
            return is_valid
            
        except Exception as e:
            logger.error(f"Error verifying webhook signature: {str(e)}")
            self.log_audit_event(
                event_type=AuditEventType.WEBHOOK_VERIFICATION_FAILED,
                event_data={"error": str(e)},
                success=False,
                error_message=str(e),
                security_level=SecurityLevel.CRITICAL
            )
            return False
    
    def validate_ip_address(self, ip_address: str) -> bool:
        """
        Validate if IP address is allowed for webhook requests
        
        Args:
            ip_address: Client IP address
            
        Returns:
            bool: True if IP is allowed
        """
        try:
            client_ip = ipaddress.ip_address(ip_address)
            
            for allowed_range in self.allowed_ips:
                if "/" in allowed_range:
                    # CIDR notation
                    if client_ip in ipaddress.ip_network(allowed_range, strict=False):
                        return True
                else:
                    # Single IP
                    if client_ip == ipaddress.ip_address(allowed_range):
                        return True
            
            logger.warning(f"IP address {ip_address} not in allowed ranges")
            return False
            
        except ValueError as e:
            logger.error(f"Invalid IP address {ip_address}: {str(e)}")
            return False
    
    def detect_fraud(self, payment_data: Dict[str, Any], user_data: Dict[str, Any]) -> FraudDetectionResult:
        """
        Detect potential fraudulent payment activity
        
        Args:
            payment_data: Payment information
            user_data: User information and history
            
        Returns:
            FraudDetectionResult: Fraud analysis result
        """
        if not self.fraud_detection_enabled:
            return FraudDetectionResult()
        
        result = FraudDetectionResult()
        risk_score = 0.0
        
        try:
            # Check for suspicious patterns
            
            # 1. Unusual payment amounts
            amount = payment_data.get("amount", 0)
            if amount > 1000:  # High amount threshold
                result.risk_factors.append("high_payment_amount")
                risk_score += 0.3
            
            # 2. Multiple rapid payments from same user
            recent_payments = user_data.get("recent_payment_count", 0)
            if recent_payments > 5:  # More than 5 payments in recent period
                result.risk_factors.append("multiple_rapid_payments")
                risk_score += 0.4
            
            # 3. New user with large payment
            user_age_days = user_data.get("account_age_days", 0)
            if user_age_days < 1 and amount > 50:
                result.risk_factors.append("new_user_large_payment")
                risk_score += 0.5
            
            # 4. Unusual geographic patterns
            user_country = user_data.get("country", "")
            payment_country = payment_data.get("country", "")
            if user_country and payment_country and user_country != payment_country:
                result.risk_factors.append("geographic_mismatch")
                risk_score += 0.2
            
            # 5. Velocity checks - too many payment attempts
            failed_attempts = user_data.get("recent_failed_payments", 0)
            if failed_attempts > 3:
                result.risk_factors.append("multiple_failed_attempts")
                risk_score += 0.3
            
            # 6. Email/Payment method pattern analysis
            email = user_data.get("email", "")
            if email and self._is_suspicious_email(email):
                result.risk_factors.append("suspicious_email_pattern")
                risk_score += 0.3
            
            # Determine final assessment
            result.confidence_score = min(risk_score, 1.0)
            
            if result.confidence_score >= 0.8:
                result.is_fraudulent = True
                result.recommended_action = "block"
                result.additional_checks_required = ["manual_review", "identity_verification"]
            elif result.confidence_score >= 0.5:
                result.is_fraudulent = False
                result.recommended_action = "review"
                result.additional_checks_required = ["enhanced_verification"]
            else:
                result.recommended_action = "allow"
            
            # Log fraud detection result
            self.log_audit_event(
                event_type=AuditEventType.FRAUD_DETECTED if result.is_fraudulent else AuditEventType.PAYMENT_CREATED,
                user_id=user_data.get("user_id"),
                event_data={
                    "fraud_score": result.confidence_score,
                    "risk_factors": result.risk_factors,
                    "recommended_action": result.recommended_action,
                    "payment_amount": amount
                },
                security_level=SecurityLevel.HIGH if result.is_fraudulent else SecurityLevel.MEDIUM
            )
            
        except Exception as e:
            logger.error(f"Error in fraud detection: {str(e)}")
            result.risk_factors.append("fraud_detection_error")
        
        return result
    
    def _is_suspicious_email(self, email: str) -> bool:
        """Check if email shows suspicious patterns"""
        suspicious_patterns = [
            r'^[a-z]+\d+@',  # Simple pattern like 'user123@'
            r'^\w+\.\w+\.\w+@',  # Multiple dots in username
            r'@10minutemail\.',  # Temporary email services
            r'@guerrillamail\.',
            r'@mailinator\.',
        ]
        
        for pattern in suspicious_patterns:
            if re.match(pattern, email.lower()):
                return True
        return False
    
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate payment data for security and completeness
        
        Args:
            payment_data: Payment data to validate
            
        Returns:
            Tuple[bool, List[str]]: (is_valid, error_messages)
        """
        errors = []
        
        try:
            # Required fields validation
            required_fields = ["amount", "currency", "user_id"]
            for field in required_fields:
                if field not in payment_data or not payment_data[field]:
                    errors.append(f"Missing required field: {field}")
            
            # Amount validation
            amount = payment_data.get("amount")
            if amount is not None:
                if not isinstance(amount, (int, float)) or amount <= 0:
                    errors.append("Amount must be a positive number")
                if amount > 10000:  # Maximum amount check
                    errors.append("Amount exceeds maximum allowed limit")
            
            # Currency validation
            currency = payment_data.get("currency", "").upper()
            allowed_currencies = ["USD", "EUR", "GBP", "CAD", "AUD"]
            if currency and currency not in allowed_currencies:
                errors.append(f"Unsupported currency: {currency}")
            
            # User ID validation
            user_id = payment_data.get("user_id", "")
            if user_id and (len(user_id) < 8 or len(user_id) > 128):
                errors.append("Invalid user ID format")
            
            # Plan ID validation (if present)
            plan_id = payment_data.get("plan_id", "")
            if plan_id:
                allowed_plans = ["free", "basic", "pro", "enterprise"]
                if plan_id not in allowed_plans:
                    errors.append(f"Invalid plan ID: {plan_id}")
            
            # URL validation (if present)
            for url_field in ["success_url", "cancel_url"]:
                url = payment_data.get(url_field, "")
                if url and not self._is_valid_url(url):
                    errors.append(f"Invalid {url_field} format")
            
        except Exception as e:
            logger.error(f"Error validating payment data: {str(e)}")
            errors.append("Payment data validation error")
        
        is_valid = len(errors) == 0
        
        # Log validation result
        self.log_audit_event(
            event_type=AuditEventType.PAYMENT_CREATED,
            user_id=payment_data.get("user_id"),
            event_data={
                "validation_result": is_valid,
                "error_count": len(errors),
                "errors": errors
            },
            success=is_valid,
            error_message="; ".join(errors) if errors else None,
            security_level=SecurityLevel.MEDIUM
        )
        
        return is_valid, errors
    
    def _is_valid_url(self, url: str) -> bool:
        """Validate URL format and security"""
        if not url:
            return False
        
        # Basic URL pattern validation
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        return url_pattern.match(url) is not None
    
    def log_audit_event(
        self,
        event_type: AuditEventType,
        user_id: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        event_data: Optional[Dict[str, Any]] = None,
        security_level: SecurityLevel = SecurityLevel.MEDIUM,
        success: bool = True,
        error_message: Optional[str] = None,
        session_id: Optional[str] = None,
        correlation_id: Optional[str] = None
    ) -> None:
        """
        Log audit event for security monitoring
        
        Args:
            event_type: Type of event
            user_id: User identifier
            ip_address: Client IP address
            user_agent: Client user agent
            event_data: Additional event data
            security_level: Security level of the event
            success: Whether the operation was successful
            error_message: Error message if applicable
            session_id: Session identifier
            correlation_id: Correlation identifier for tracking
        """
        try:
            audit_log = AuditLog(
                event_type=event_type,
                user_id=user_id,
                ip_address=ip_address,
                user_agent=user_agent,
                event_data=event_data or {},
                security_level=security_level,
                success=success,
                error_message=error_message,
                session_id=session_id,
                correlation_id=correlation_id
            )
            
            # Store audit log (in production, this should go to a secure logging system)
            self.audit_logs.append(audit_log)
            
            # Log to application logger
            log_level = logging.WARNING if not success else logging.INFO
            if security_level == SecurityLevel.CRITICAL:
                log_level = logging.ERROR
            
            logger.log(
                log_level,
                f"AUDIT: {event_type.value} - User: {user_id} - Success: {success} - "
                f"Security Level: {security_level.value} - IP: {ip_address}"
            )
            
            # For high-security events, also log to security-specific logger
            if security_level in [SecurityLevel.HIGH, SecurityLevel.CRITICAL]:
                security_logger = logging.getLogger("security")
                security_logger.warning(json.dumps(audit_log.to_dict()))
            
        except Exception as e:
            logger.error(f"Error logging audit event: {str(e)}")
    
    def get_audit_logs(
        self,
        user_id: Optional[str] = None,
        event_types: Optional[List[AuditEventType]] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        security_level: Optional[SecurityLevel] = None,
        limit: int = 100
    ) -> List[AuditLog]:
        """
        Retrieve audit logs with filtering
        
        Args:
            user_id: Filter by user ID
            event_types: Filter by event types
            start_time: Filter by start time
            end_time: Filter by end time
            security_level: Filter by security level
            limit: Maximum number of logs to return
            
        Returns:
            List[AuditLog]: Filtered audit logs
        """
        filtered_logs = []
        
        for log in self.audit_logs:
            # Apply filters
            if user_id and log.user_id != user_id:
                continue
            if event_types and log.event_type not in event_types:
                continue
            if start_time and log.timestamp < start_time:
                continue
            if end_time and log.timestamp > end_time:
                continue
            if security_level and log.security_level != security_level:
                continue
            
            filtered_logs.append(log)
            
            if len(filtered_logs) >= limit:
                break
        
        return sorted(filtered_logs, key=lambda x: x.timestamp, reverse=True)
