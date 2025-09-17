# backend/src/payments/rate_limiting.py
"""
Rate limiting service for payment endpoints
"""

import time
import logging
import os
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict, deque
from datetime import datetime, timezone, timedelta
import threading
import asyncio

from .security import RateLimitConfig, AuditEventType, SecurityLevel

logger = logging.getLogger(__name__)


@dataclass
class RateLimitEntry:
    """Rate limit tracking entry"""
    requests: deque = field(default_factory=deque)
    penalty_until: Optional[datetime] = None
    last_request: Optional[datetime] = None


class RateLimitingService:
    """Advanced rate limiting service with multiple strategies"""
    
    def __init__(self):
        # Global toggle (env-driven)
        self.enabled = os.getenv("ENABLE_RATE_LIMITING", "true").lower() in ("1", "true", "yes", "on")
        self.rate_limits = defaultdict(lambda: defaultdict(RateLimitEntry))
        self.global_rate_limits = defaultdict(RateLimitEntry)
        self.lock = threading.RLock()
        
        # Rate limit configurations per endpoint
        self.endpoint_configs = {
            "checkout": RateLimitConfig(
                max_requests=5,
                time_window_seconds=300,  # 5 minutes
                burst_limit=8,
                penalty_duration_seconds=600  # 10 minutes penalty
            ),
            "webhook": RateLimitConfig(
                max_requests=100,
                time_window_seconds=60,  # 1 minute
                burst_limit=150,
                penalty_duration_seconds=300  # 5 minutes penalty
            ),
            "credit_check": RateLimitConfig(
                max_requests=30,
                time_window_seconds=60,  # 1 minute
                burst_limit=50,
                penalty_duration_seconds=120  # 2 minutes penalty
            ),
            "credit_deduct": RateLimitConfig(
                max_requests=10,
                time_window_seconds=60,  # 1 minute
                burst_limit=15,
                penalty_duration_seconds=300  # 5 minutes penalty
            ),
            "subscription": RateLimitConfig(
                max_requests=10,
                time_window_seconds=300,  # 5 minutes
                burst_limit=15,
                penalty_duration_seconds=900  # 15 minutes penalty
            ),
            "payment_history": RateLimitConfig(
                max_requests=20,
                time_window_seconds=60,  # 1 minute
                burst_limit=30,
                penalty_duration_seconds=60  # 1 minute penalty
            )
        }
        
        # Global rate limits (across all users)
        self.global_configs = {
            "checkout": RateLimitConfig(
                max_requests=100,
                time_window_seconds=60,
                burst_limit=150
            ),
            "webhook": RateLimitConfig(
                max_requests=1000,
                time_window_seconds=60,
                burst_limit=1500
            )
        }
        
        # Start cleanup task
        self._start_cleanup_task()
    
    def check_rate_limit(
        self,
        endpoint: str,
        user_id: str,
        ip_address: Optional[str] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        Check if request is within rate limits
        
        Args:
            endpoint: API endpoint name
            user_id: User identifier
            ip_address: Client IP address
            
        Returns:
            Tuple[bool, Dict[str, Any]]: (allowed, rate_limit_info)
        """
        # Fast path when disabled
        if not self.enabled:
            return True, {"rate_limiting": False, "endpoint": endpoint, "disabled": True}
        current_time = datetime.now(timezone.utc)
        
        with self.lock:
            # Check user-specific rate limit
            user_allowed, user_info = self._check_user_rate_limit(
                endpoint, user_id, current_time
            )
            
            # Check global rate limit
            global_allowed, global_info = self._check_global_rate_limit(
                endpoint, current_time
            )
            
            # Check IP-based rate limit (if provided)
            ip_allowed, ip_info = True, {}
            if ip_address:
                ip_allowed, ip_info = self._check_ip_rate_limit(
                    endpoint, ip_address, current_time
                )
            
            # Overall decision
            allowed = user_allowed and global_allowed and ip_allowed
            
            # Combine rate limit information
            rate_limit_info = {
                "user_limits": user_info,
                "global_limits": global_info,
                "ip_limits": ip_info,
                "endpoint": endpoint,
                "timestamp": current_time.isoformat()
            }
            
            if allowed:
                # Record successful request
                self._record_request(endpoint, user_id, current_time)
                if ip_address:
                    self._record_ip_request(endpoint, ip_address, current_time)
                self._record_global_request(endpoint, current_time)
            else:
                # Log rate limit violation
                rate_limit_info["violation_reason"] = self._get_violation_reason(
                    user_allowed, global_allowed, ip_allowed
                )
                
                # Apply penalty if configured
                self._apply_penalty(endpoint, user_id, current_time)
            
            return allowed, rate_limit_info
    
    def _check_user_rate_limit(
        self,
        endpoint: str,
        user_id: str,
        current_time: datetime
    ) -> Tuple[bool, Dict[str, Any]]:
        """Check user-specific rate limit"""
        config = self.endpoint_configs.get(endpoint)
        if not config:
            return True, {}
        
        entry = self.rate_limits[endpoint][user_id]
        
        # Check if user is in penalty period
        if entry.penalty_until and current_time < entry.penalty_until:
            remaining_penalty = (entry.penalty_until - current_time).total_seconds()
            return False, {
                "rate_limited": True,
                "reason": "penalty_period",
                "penalty_remaining_seconds": remaining_penalty,
                "penalty_until": entry.penalty_until.isoformat()
            }
        
        # Clean old requests outside time window
        cutoff_time = current_time - timedelta(seconds=config.time_window_seconds)
        while entry.requests and entry.requests[0] < cutoff_time:
            entry.requests.popleft()
        
        current_requests = len(entry.requests)
        
        # Check against burst limit first, then normal limit
        limit_to_check = config.burst_limit if config.burst_limit > 0 else config.max_requests
        
        if current_requests >= limit_to_check:
            return False, {
                "rate_limited": True,
                "reason": "request_limit_exceeded",
                "current_requests": current_requests,
                "limit": limit_to_check,
                "time_window_seconds": config.time_window_seconds,
                "reset_time": (cutoff_time + timedelta(seconds=config.time_window_seconds)).isoformat()
            }
        
        return True, {
            "rate_limited": False,
            "current_requests": current_requests,
            "limit": limit_to_check,
            "remaining_requests": limit_to_check - current_requests,
            "time_window_seconds": config.time_window_seconds
        }
    
    def _check_global_rate_limit(
        self,
        endpoint: str,
        current_time: datetime
    ) -> Tuple[bool, Dict[str, Any]]:
        """Check global rate limit"""
        config = self.global_configs.get(endpoint)
        if not config:
            return True, {}
        
        entry = self.global_rate_limits[endpoint]
        
        # Clean old requests
        cutoff_time = current_time - timedelta(seconds=config.time_window_seconds)
        while entry.requests and entry.requests[0] < cutoff_time:
            entry.requests.popleft()
        
        current_requests = len(entry.requests)
        limit_to_check = config.burst_limit if config.burst_limit > 0 else config.max_requests
        
        if current_requests >= limit_to_check:
            return False, {
                "global_rate_limited": True,
                "reason": "global_limit_exceeded",
                "current_requests": current_requests,
                "limit": limit_to_check
            }
        
        return True, {
            "global_rate_limited": False,
            "current_requests": current_requests,
            "limit": limit_to_check,
            "remaining_requests": limit_to_check - current_requests
        }
    
    def _check_ip_rate_limit(
        self,
        endpoint: str,
        ip_address: str,
        current_time: datetime
    ) -> Tuple[bool, Dict[str, Any]]:
        """Check IP-based rate limit"""
        # Use same config as user limits but with different key
        config = self.endpoint_configs.get(endpoint)
        if not config:
            return True, {}
        
        ip_key = f"ip_{ip_address}"
        entry = self.rate_limits[endpoint][ip_key]
        
        # Clean old requests
        cutoff_time = current_time - timedelta(seconds=config.time_window_seconds)
        while entry.requests and entry.requests[0] < cutoff_time:
            entry.requests.popleft()
        
        current_requests = len(entry.requests)
        # Use slightly higher limit for IP-based limiting
        ip_limit = int(config.max_requests * 1.5)
        
        if current_requests >= ip_limit:
            return False, {
                "ip_rate_limited": True,
                "reason": "ip_limit_exceeded",
                "ip_address": ip_address,
                "current_requests": current_requests,
                "limit": ip_limit
            }
        
        return True, {
            "ip_rate_limited": False,
            "ip_address": ip_address,
            "current_requests": current_requests,
            "limit": ip_limit,
            "remaining_requests": ip_limit - current_requests
        }
    
    def _record_request(self, endpoint: str, user_id: str, current_time: datetime):
        """Record a successful request"""
        entry = self.rate_limits[endpoint][user_id]
        entry.requests.append(current_time)
        entry.last_request = current_time
    
    def _record_ip_request(self, endpoint: str, ip_address: str, current_time: datetime):
        """Record an IP-based request"""
        ip_key = f"ip_{ip_address}"
        entry = self.rate_limits[endpoint][ip_key]
        entry.requests.append(current_time)
        entry.last_request = current_time
    
    def _record_global_request(self, endpoint: str, current_time: datetime):
        """Record a global request"""
        entry = self.global_rate_limits[endpoint]
        entry.requests.append(current_time)
        entry.last_request = current_time
    
    def _apply_penalty(self, endpoint: str, user_id: str, current_time: datetime):
        """Apply penalty for rate limit violation"""
        config = self.endpoint_configs.get(endpoint)
        if not config or config.penalty_duration_seconds <= 0:
            return
        
        entry = self.rate_limits[endpoint][user_id]
        entry.penalty_until = current_time + timedelta(seconds=config.penalty_duration_seconds)
        
        logger.warning(
            f"Applied rate limit penalty to user {user_id} for endpoint {endpoint}. "
            f"Penalty until: {entry.penalty_until}"
        )
    
    def _get_violation_reason(self, user_allowed: bool, global_allowed: bool, ip_allowed: bool) -> str:
        """Get human-readable violation reason"""
        reasons = []
        if not user_allowed:
            reasons.append("user_limit_exceeded")
        if not global_allowed:
            reasons.append("global_limit_exceeded")
        if not ip_allowed:
            reasons.append("ip_limit_exceeded")
        return ", ".join(reasons)
    
    def get_rate_limit_status(self, endpoint: str, user_id: str) -> Dict[str, Any]:
        """Get current rate limit status for a user"""
        current_time = datetime.now(timezone.utc)
        
        with self.lock:
            config = self.endpoint_configs.get(endpoint)
            if not config:
                return {"error": "Unknown endpoint"}
            
            entry = self.rate_limits[endpoint][user_id]
            
            # Clean old requests
            cutoff_time = current_time - timedelta(seconds=config.time_window_seconds)
            while entry.requests and entry.requests[0] < cutoff_time:
                entry.requests.popleft()
            
            current_requests = len(entry.requests)
            limit = config.burst_limit if config.burst_limit > 0 else config.max_requests
            
            status = {
                "endpoint": endpoint,
                "user_id": user_id,
                "current_requests": current_requests,
                "limit": limit,
                "remaining_requests": max(0, limit - current_requests),
                "time_window_seconds": config.time_window_seconds,
                "last_request": entry.last_request.isoformat() if entry.last_request else None,
                "penalty_active": entry.penalty_until and current_time < entry.penalty_until,
                "penalty_until": entry.penalty_until.isoformat() if entry.penalty_until else None
            }
            
            if entry.requests:
                # Calculate reset time based on oldest request
                reset_time = entry.requests[0] + timedelta(seconds=config.time_window_seconds)
                status["reset_time"] = reset_time.isoformat()
            
            return status
    
    def reset_user_limits(self, endpoint: str, user_id: str) -> bool:
        """Reset rate limits for a specific user (admin function)"""
        try:
            with self.lock:
                if endpoint in self.rate_limits and user_id in self.rate_limits[endpoint]:
                    del self.rate_limits[endpoint][user_id]
                    logger.info(f"Reset rate limits for user {user_id} on endpoint {endpoint}")
                    return True
                return False
        except Exception as e:
            logger.error(f"Error resetting rate limits: {str(e)}")
            return False
    
    def get_global_stats(self) -> Dict[str, Any]:
        """Get global rate limiting statistics"""
        if not self.enabled:
            return {"enabled": False}
        current_time = datetime.now(timezone.utc)
        stats = {}
        
        with self.lock:
            for endpoint, config in self.endpoint_configs.items():
                endpoint_stats = {
                    "total_users": len(self.rate_limits.get(endpoint, {})),
                    "config": {
                        "max_requests": config.max_requests,
                        "time_window_seconds": config.time_window_seconds,
                        "burst_limit": config.burst_limit,
                        "penalty_duration_seconds": config.penalty_duration_seconds
                    },
                    "active_penalties": 0,
                    "total_requests_last_window": 0
                }
                
                # Count active penalties and requests
                for user_id, entry in self.rate_limits.get(endpoint, {}).items():
                    if entry.penalty_until and current_time < entry.penalty_until:
                        endpoint_stats["active_penalties"] += 1
                    
                    # Count requests in current window
                    cutoff_time = current_time - timedelta(seconds=config.time_window_seconds)
                    current_requests = sum(1 for req_time in entry.requests if req_time >= cutoff_time)
                    endpoint_stats["total_requests_last_window"] += current_requests
                
                stats[endpoint] = endpoint_stats
        
        return stats
    
    def _start_cleanup_task(self):
        """Start background task to clean up old entries"""
        def cleanup_old_entries():
            while True:
                try:
                    current_time = datetime.now(timezone.utc)
                    cutoff_time = current_time - timedelta(hours=24)  # Keep data for 24 hours
                    
                    with self.lock:
                        # Clean user rate limits
                        for endpoint in list(self.rate_limits.keys()):
                            users_to_remove = []
                            for user_id, entry in self.rate_limits[endpoint].items():
                                # Remove if no recent activity and no active penalty
                                if (not entry.last_request or entry.last_request < cutoff_time) and \
                                   (not entry.penalty_until or entry.penalty_until < current_time):
                                    users_to_remove.append(user_id)
                            
                            for user_id in users_to_remove:
                                del self.rate_limits[endpoint][user_id]
                        
                        # Clean global rate limits
                        for endpoint, entry in self.global_rate_limits.items():
                            # Clean old requests
                            while entry.requests and entry.requests[0] < cutoff_time:
                                entry.requests.popleft()
                    
                    # Sleep for 1 hour before next cleanup
                    time.sleep(3600)
                    
                except Exception as e:
                    logger.error(f"Error in rate limit cleanup task: {str(e)}")
                    time.sleep(300)  # Sleep 5 minutes on error
        
        # Start cleanup thread
        cleanup_thread = threading.Thread(target=cleanup_old_entries, daemon=True)
        cleanup_thread.start()
        logger.info("Rate limiting cleanup task started")

    # Control methods
    def set_enabled(self, enabled: bool):
        self.enabled = bool(enabled)
        logger.info(f"Rate limiting {'enabled' if self.enabled else 'disabled'} via toggle")

    def is_enabled(self) -> bool:
        return self.enabled


# Global rate limiting service instance
rate_limiting_service = RateLimitingService()
