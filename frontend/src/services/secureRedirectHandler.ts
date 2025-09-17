// frontend/src/services/secureRedirectHandler.ts
/**
 * Secure redirect handling for payment flows
 */

import { paymentSecurity } from './paymentSecurity';

interface RedirectValidationResult {
  isValid: boolean;
  sanitizedUrl?: string;
  reason?: string;
}

interface PaymentRedirectData {
  status: 'success' | 'cancelled' | 'failed';
  sessionId?: string;
  paymentId?: string;
  planId?: string;
  amount?: number;
  correlationId?: string;
  timestamp?: string;
  signature?: string;
}

export class SecureRedirectHandler {
  private static instance: SecureRedirectHandler;
  private readonly allowedOrigins: string[];
  private readonly maxRedirectAge: number = 10 * 60 * 1000; // 10 minutes

  private constructor() {
    // Configure allowed origins based on environment
    this.allowedOrigins = [
      window.location.origin,
      ...(process.env.REACT_APP_ALLOWED_REDIRECT_ORIGINS?.split(',') || [])
    ];
  }

  public static getInstance(): SecureRedirectHandler {
    if (!SecureRedirectHandler.instance) {
      SecureRedirectHandler.instance = new SecureRedirectHandler();
    }
    return SecureRedirectHandler.instance;
  }

  /**
   * Validate and sanitize redirect URL
   */
  validateRedirectUrl(url: string): RedirectValidationResult {
    try {
      const urlObj = new URL(url);
      
      // Check protocol - only allow HTTPS in production
      if (process.env.NODE_ENV === 'production' && urlObj.protocol !== 'https:') {
        return { 
          isValid: false, 
          reason: 'Only HTTPS URLs are allowed in production' 
        };
      }

      // Check origin against allowed list
      const isOriginAllowed = this.allowedOrigins.some(origin => {
        const allowedOrigin = new URL(origin);
        return urlObj.origin === allowedOrigin.origin;
      });

      if (!isOriginAllowed) {
        return { 
          isValid: false, 
          reason: 'Origin not in allowed list' 
        };
      }

      // Check for suspicious patterns
      if (this.hasSuspiciousPatterns(url)) {
        return { 
          isValid: false, 
          reason: 'URL contains suspicious patterns' 
        };
      }

      // Sanitize URL by removing potentially dangerous parameters
      const sanitizedUrl = this.sanitizeUrl(urlObj);

      return { 
        isValid: true, 
        sanitizedUrl 
      };

    } catch (error) {
      return { 
        isValid: false, 
        reason: 'Invalid URL format' 
      };
    }
  }

  /**
   * Handle payment success redirect
   */
  async handleSuccessRedirect(
    redirectUrl: string, 
    paymentData: PaymentRedirectData
  ): Promise<void> {
    // Validate redirect URL
    const validation = this.validateRedirectUrl(redirectUrl);
    if (!validation.isValid) {
      throw new Error(`Invalid redirect URL: ${validation.reason}`);
    }

    // Validate payment data
    const dataValidation = this.validatePaymentData(paymentData);
    if (!dataValidation.isValid) {
      throw new Error(`Invalid payment data: ${dataValidation.reason}`);
    }

    // Log successful redirect
    paymentSecurity.logSecurityEvent({
      type: 'payment_attempt',
      data: {
        event: 'success_redirect',
        redirectUrl: validation.sanitizedUrl,
        paymentData: {
          status: paymentData.status,
          planId: paymentData.planId,
          correlationId: paymentData.correlationId
        }
      },
      severity: 'low'
    });

    // Perform secure redirect
    await this.performSecureRedirect(validation.sanitizedUrl!, paymentData);
  }

  /**
   * Handle payment cancellation redirect
   */
  async handleCancelRedirect(
    redirectUrl: string, 
    paymentData: PaymentRedirectData
  ): Promise<void> {
    // Validate redirect URL
    const validation = this.validateRedirectUrl(redirectUrl);
    if (!validation.isValid) {
      throw new Error(`Invalid redirect URL: ${validation.reason}`);
    }

    // Log cancellation redirect
    paymentSecurity.logSecurityEvent({
      type: 'payment_attempt',
      data: {
        event: 'cancel_redirect',
        redirectUrl: validation.sanitizedUrl,
        paymentData: {
          status: paymentData.status,
          correlationId: paymentData.correlationId
        }
      },
      severity: 'low'
    });

    // Perform secure redirect
    await this.performSecureRedirect(validation.sanitizedUrl!, paymentData);
  }

  /**
   * Handle payment failure redirect
   */
  async handleFailureRedirect(
    redirectUrl: string, 
    paymentData: PaymentRedirectData,
    errorDetails?: any
  ): Promise<void> {
    // Validate redirect URL
    const validation = this.validateRedirectUrl(redirectUrl);
    if (!validation.isValid) {
      throw new Error(`Invalid redirect URL: ${validation.reason}`);
    }

    // Log failure redirect
    paymentSecurity.logSecurityEvent({
      type: 'payment_attempt',
      data: {
        event: 'failure_redirect',
        redirectUrl: validation.sanitizedUrl,
        paymentData: {
          status: paymentData.status,
          correlationId: paymentData.correlationId
        },
        errorDetails
      },
      severity: 'medium'
    });

    // Perform secure redirect
    await this.performSecureRedirect(validation.sanitizedUrl!, paymentData);
  }

  /**
   * Generate secure redirect URL with state
   */
  generateSecureRedirectUrl(
    baseUrl: string, 
    paymentData: PaymentRedirectData
  ): string {
    const validation = this.validateRedirectUrl(baseUrl);
    if (!validation.isValid) {
      throw new Error(`Invalid base URL: ${validation.reason}`);
    }

    const url = new URL(validation.sanitizedUrl!);
    
    // Add payment state parameters
    if (paymentData.status) {
      url.searchParams.set('status', paymentData.status);
    }
    if (paymentData.sessionId) {
      url.searchParams.set('session_id', paymentData.sessionId);
    }
    if (paymentData.correlationId) {
      url.searchParams.set('correlation_id', paymentData.correlationId);
    }
    
    // Add timestamp for validation
    url.searchParams.set('timestamp', Date.now().toString());
    
    // Add security token
    const securityToken = this.generateRedirectToken(paymentData);
    url.searchParams.set('token', securityToken);

    return url.toString();
  }

  /**
   * Validate payment redirect data from URL parameters
   */
  validateRedirectData(searchParams: URLSearchParams): {
    isValid: boolean;
    data?: PaymentRedirectData;
    reason?: string;
  } {
    try {
      const status = searchParams.get('status') as PaymentRedirectData['status'];
      const sessionId = searchParams.get('session_id') || undefined;
      const correlationId = searchParams.get('correlation_id') || undefined;
      const timestamp = searchParams.get('timestamp');
      const token = searchParams.get('token');

      // Validate required fields
      if (!status || !['success', 'cancelled', 'failed'].includes(status)) {
        return { isValid: false, reason: 'Invalid or missing status' };
      }

      if (!timestamp) {
        return { isValid: false, reason: 'Missing timestamp' };
      }

      // Check timestamp age
      const redirectAge = Date.now() - parseInt(timestamp);
      if (redirectAge > this.maxRedirectAge) {
        return { isValid: false, reason: 'Redirect data is too old' };
      }

      // Validate token if present
      if (token) {
        const tokenValid = this.validateRedirectToken(token, {
          status,
          sessionId,
          correlationId,
          timestamp
        });
        
        if (!tokenValid) {
          return { isValid: false, reason: 'Invalid security token' };
        }
      }

      const data: PaymentRedirectData = {
        status,
        sessionId,
        correlationId,
        timestamp
      };

      return { isValid: true, data };

    } catch (error) {
      return { isValid: false, reason: 'Failed to parse redirect data' };
    }
  }

  /**
   * Check for suspicious URL patterns
   */
  private hasSuspiciousPatterns(url: string): boolean {
    const suspiciousPatterns = [
      /javascript:/i,
      /data:/i,
      /vbscript:/i,
      /file:/i,
      /ftp:/i,
      /<script/i,
      /onclick/i,
      /onerror/i,
      /onload/i
    ];

    return suspiciousPatterns.some(pattern => pattern.test(url));
  }

  /**
   * Sanitize URL by removing potentially dangerous parameters
   */
  private sanitizeUrl(urlObj: URL): string {
    // Remove potentially dangerous parameters
    const dangerousParams = [
      'javascript',
      'script',
      'eval',
      'onclick',
      'onerror',
      'onload'
    ];

    dangerousParams.forEach(param => {
      if (urlObj.searchParams.has(param)) {
        urlObj.searchParams.delete(param);
      }
    });

    return urlObj.toString();
  }

  /**
   * Validate payment data structure
   */
  private validatePaymentData(data: PaymentRedirectData): {
    isValid: boolean;
    reason?: string;
  } {
    if (!data.status || !['success', 'cancelled', 'failed'].includes(data.status)) {
      return { isValid: false, reason: 'Invalid status' };
    }

    if (data.amount && (typeof data.amount !== 'number' || data.amount < 0)) {
      return { isValid: false, reason: 'Invalid amount' };
    }

    return { isValid: true };
  }

  /**
   * Generate security token for redirect validation
   */
  private generateRedirectToken(data: PaymentRedirectData): string {
    // In production, use a more sophisticated token generation
    const payload = JSON.stringify({
      status: data.status,
      sessionId: data.sessionId,
      correlationId: data.correlationId,
      timestamp: Date.now()
    });

    // Simple token generation (enhance for production)
    return btoa(payload).replace(/[+/=]/g, '');
  }

  /**
   * Validate redirect security token
   */
  private validateRedirectToken(token: string, expectedData: any): boolean {
    try {
      // Simple validation (enhance for production)
      const decoded = atob(token);
      const data = JSON.parse(decoded);
      
      return data.status === expectedData.status &&
             data.sessionId === expectedData.sessionId &&
             data.correlationId === expectedData.correlationId;
    } catch {
      return false;
    }
  }

  /**
   * Perform the actual secure redirect
   */
  private async performSecureRedirect(
    url: string, 
    paymentData: PaymentRedirectData
  ): Promise<void> {
    // Add a small delay to ensure all operations complete
    await new Promise(resolve => setTimeout(resolve, 100));

    // Use window.location.assign for secure redirect
    window.location.assign(url);
  }

  /**
   * Handle redirect from external payment provider
   */
  handleExternalRedirect(): PaymentRedirectData | null {
    try {
      const searchParams = new URLSearchParams(window.location.search);
      const validation = this.validateRedirectData(searchParams);

      if (!validation.isValid) {
        paymentSecurity.logSecurityEvent({
          type: 'security_check',
          data: {
            event: 'invalid_redirect_data',
            reason: validation.reason,
            url: window.location.href
          },
          severity: 'high'
        });
        return null;
      }

      // Log successful redirect handling
      paymentSecurity.logSecurityEvent({
        type: 'payment_attempt',
        data: {
          event: 'external_redirect_handled',
          status: validation.data?.status,
          correlationId: validation.data?.correlationId
        },
        severity: 'low'
      });

      return validation.data || null;

    } catch (error) {
      paymentSecurity.logSecurityEvent({
        type: 'security_check',
        data: {
          event: 'redirect_handling_error',
          error: error instanceof Error ? error.message : 'Unknown error'
        },
        severity: 'high'
      });
      return null;
    }
  }
}

// Export singleton instance
export const secureRedirectHandler = SecureRedirectHandler.getInstance();
