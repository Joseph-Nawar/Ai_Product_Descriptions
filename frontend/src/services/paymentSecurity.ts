// frontend/src/services/paymentSecurity.ts
/**
 * Frontend payment security and validation service
 */

import { z } from 'zod';

// Validation schemas
export const checkoutRequestSchema = z.object({
  plan_id: z.string().min(1, 'Plan ID is required').max(50, 'Plan ID too long'),
  success_url: z.string().url('Success URL must be a valid URL'),
  cancel_url: z.string().url('Cancel URL must be a valid URL')
});

export const creditDeductionSchema = z.object({
  amount: z.number().int().min(1, 'Amount must be at least 1').max(50, 'Amount cannot exceed 50'),
  operation_context: z.record(z.any()).optional()
});

export const creditCheckSchema = z.object({
  batch_size: z.number().int().min(1, 'Batch size must be at least 1').max(100, 'Batch size cannot exceed 100')
});

// Security utilities
export class PaymentSecurityService {
  private static instance: PaymentSecurityService;
  private correlationId: string | null = null;

  private constructor() {}

  public static getInstance(): PaymentSecurityService {
    if (!PaymentSecurityService.instance) {
      PaymentSecurityService.instance = new PaymentSecurityService();
    }
    return PaymentSecurityService.instance;
  }

  /**
   * Generate a correlation ID for tracking requests
   */
  generateCorrelationId(): string {
    this.correlationId = `frontend_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    return this.correlationId;
  }

  /**
   * Get current correlation ID
   */
  getCorrelationId(): string {
    return this.correlationId || this.generateCorrelationId();
  }

  /**
   * Validate checkout request data
   */
  validateCheckoutRequest(data: any): { isValid: boolean; errors: string[]; sanitized?: any } {
    try {
      const sanitized = checkoutRequestSchema.parse(data);
      
      // Additional security checks
      const errors: string[] = [];
      
      // Check for suspicious URLs
      if (this.isSuspiciousUrl(sanitized.success_url)) {
        errors.push('Success URL appears suspicious');
      }
      
      if (this.isSuspiciousUrl(sanitized.cancel_url)) {
        errors.push('Cancel URL appears suspicious');
      }
      
      // Validate plan ID against known plans
      const validPlanIds = ['free', 'basic', 'pro', 'enterprise'];
      if (!validPlanIds.includes(sanitized.plan_id)) {
        errors.push('Invalid plan ID');
      }
      
      return {
        isValid: errors.length === 0,
        errors,
        sanitized: errors.length === 0 ? sanitized : undefined
      };
    } catch (error) {
      if (error instanceof z.ZodError) {
        return {
          isValid: false,
          errors: error.errors.map(e => `${e.path.join('.')}: ${e.message}`)
        };
      }
      return {
        isValid: false,
        errors: ['Validation failed']
      };
    }
  }

  /**
   * Validate credit deduction request
   */
  validateCreditDeduction(data: any): { isValid: boolean; errors: string[]; sanitized?: any } {
    try {
      const sanitized = creditDeductionSchema.parse(data);
      return {
        isValid: true,
        errors: [],
        sanitized
      };
    } catch (error) {
      if (error instanceof z.ZodError) {
        return {
          isValid: false,
          errors: error.errors.map(e => `${e.path.join('.')}: ${e.message}`)
        };
      }
      return {
        isValid: false,
        errors: ['Validation failed']
      };
    }
  }

  /**
   * Validate credit check request
   */
  validateCreditCheck(data: any): { isValid: boolean; errors: string[]; sanitized?: any } {
    try {
      const sanitized = creditCheckSchema.parse(data);
      return {
        isValid: true,
        errors: [],
        sanitized
      };
    } catch (error) {
      if (error instanceof z.ZodError) {
        return {
          isValid: false,
          errors: error.errors.map(e => `${e.path.join('.')}: ${e.message}`)
        };
      }
      return {
        isValid: false,
        errors: ['Validation failed']
      };
    }
  }

  /**
   * Check if URL appears suspicious
   */
  private isSuspiciousUrl(url: string): boolean {
    try {
      const urlObj = new URL(url);
      
      // Check for suspicious patterns
      const suspiciousPatterns = [
        /bit\.ly|tinyurl|t\.co/i,  // URL shorteners
        /[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/,  // IP addresses
        /localhost|127\.0\.0\.1/i,  // Local addresses (in production)
        /[^a-zA-Z0-9\-\.].*\.(tk|ml|ga|cf)$/i  // Suspicious TLDs
      ];
      
      return suspiciousPatterns.some(pattern => pattern.test(urlObj.hostname));
    } catch {
      return true; // Invalid URL is suspicious
    }
  }

  /**
   * Sanitize redirect URL
   */
  sanitizeRedirectUrl(url: string): string | null {
    try {
      const urlObj = new URL(url);
      
      // Only allow HTTPS in production
      if (process.env.NODE_ENV === 'production' && urlObj.protocol !== 'https:') {
        return null;
      }
      
      // Check against allowed domains
      const allowedDomains = [
        window.location.hostname,
        'localhost',
        '127.0.0.1'
        // Add your production domains here
      ];
      
      const isAllowed = allowedDomains.some(domain => 
        urlObj.hostname === domain || urlObj.hostname.endsWith(`.${domain}`)
      );
      
      if (!isAllowed) {
        return null;
      }
      
      return url;
    } catch {
      return null;
    }
  }

  /**
   * Validate subscription status before operations
   */
  validateSubscriptionStatus(subscription: any): { canProceed: boolean; reason?: string } {
    if (!subscription) {
      return { canProceed: false, reason: 'No subscription found' };
    }

    // Check if subscription is active
    if (subscription.status !== 'active' && subscription.subscription_tier !== 'free') {
      return { canProceed: false, reason: 'Subscription is not active' };
    }

    // Check expiration for paid plans
    if (subscription.subscription_tier !== 'free' && subscription.subscription_expires_at) {
      const expiresAt = new Date(subscription.subscription_expires_at);
      const now = new Date();
      
      if (expiresAt <= now) {
        return { canProceed: false, reason: 'Subscription has expired' };
      }
    }

    return { canProceed: true };
  }

  /**
   * Check for minimum required credits
   */
  validateCreditBalance(credits: number, required: number): { hasEnough: boolean; shortfall?: number } {
    if (credits >= required) {
      return { hasEnough: true };
    }
    
    return { 
      hasEnough: false, 
      shortfall: required - credits 
    };
  }

  /**
   * Detect potentially fraudulent patterns in user behavior
   */
  detectSuspiciousActivity(activityData: {
    rapidRequests?: number;
    unusualAmounts?: boolean;
    newUser?: boolean;
    largeAmount?: number;
  }): { isSuspicious: boolean; reasons: string[] } {
    const reasons: string[] = [];
    
    if (activityData.rapidRequests && activityData.rapidRequests > 10) {
      reasons.push('High frequency of requests');
    }
    
    if (activityData.unusualAmounts) {
      reasons.push('Unusual payment amounts detected');
    }
    
    if (activityData.newUser && activityData.largeAmount && activityData.largeAmount > 100) {
      reasons.push('New user attempting large transaction');
    }
    
    return {
      isSuspicious: reasons.length > 0,
      reasons
    };
  }

  /**
   * Generate secure headers for payment requests
   */
  generateSecureHeaders(): Record<string, string> {
    return {
      'X-Correlation-ID': this.getCorrelationId(),
      'X-Request-Time': new Date().toISOString(),
      'X-Client-Version': process.env.REACT_APP_VERSION || '1.0.0'
    };
  }

  /**
   * Log security events (client-side)
   */
  logSecurityEvent(event: {
    type: 'validation_error' | 'suspicious_activity' | 'security_check' | 'payment_attempt';
    data: Record<string, any>;
    severity: 'low' | 'medium' | 'high';
  }): void {
    const logEntry = {
      timestamp: new Date().toISOString(),
      correlationId: this.getCorrelationId(),
      userAgent: navigator.userAgent,
      url: window.location.href,
      ...event
    };

    // In production, you might want to send this to a logging service
    if (event.severity === 'high') {
      console.warn('Security Event:', logEntry);
    } else {
      console.log('Security Event:', logEntry);
    }

    // Store in session storage for debugging (remove in production)
    if (process.env.NODE_ENV === 'development') {
      const existingLogs = JSON.parse(sessionStorage.getItem('security_logs') || '[]');
      existingLogs.push(logEntry);
      
      // Keep only last 50 logs
      if (existingLogs.length > 50) {
        existingLogs.splice(0, existingLogs.length - 50);
      }
      
      sessionStorage.setItem('security_logs', JSON.stringify(existingLogs));
    }
  }
}

// Export singleton instance
export const paymentSecurity = PaymentSecurityService.getInstance();
