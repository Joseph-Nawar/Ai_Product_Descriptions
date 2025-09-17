// frontend/src/services/secureTokens.ts
/**
 * Secure token handling service for payment operations
 */

interface TokenValidationResult {
  isValid: boolean;
  reason?: string;
  expiresAt?: Date;
}

interface SecureTokenData {
  token: string;
  expiresAt: Date;
  issuedAt: Date;
  purpose: string;
  correlationId?: string;
}

export class SecureTokenService {
  private static instance: SecureTokenService;
  private tokenCache: Map<string, SecureTokenData> = new Map();
  private readonly TOKEN_VALIDITY_MINUTES = 30;

  private constructor() {
    // Clean up expired tokens periodically
    setInterval(() => this.cleanupExpiredTokens(), 5 * 60 * 1000); // Every 5 minutes
  }

  public static getInstance(): SecureTokenService {
    if (!SecureTokenService.instance) {
      SecureTokenService.instance = new SecureTokenService();
    }
    return SecureTokenService.instance;
  }

  /**
   * Generate a secure token for payment operations
   */
  generateSecureToken(purpose: string, correlationId?: string): string {
    const tokenId = this.generateTokenId();
    const now = new Date();
    const expiresAt = new Date(now.getTime() + this.TOKEN_VALIDITY_MINUTES * 60 * 1000);

    const tokenData: SecureTokenData = {
      token: tokenId,
      expiresAt,
      issuedAt: now,
      purpose,
      correlationId
    };

    this.tokenCache.set(tokenId, tokenData);
    return tokenId;
  }

  /**
   * Validate a secure token
   */
  validateToken(token: string, expectedPurpose?: string): TokenValidationResult {
    const tokenData = this.tokenCache.get(token);

    if (!tokenData) {
      return { isValid: false, reason: 'Token not found' };
    }

    const now = new Date();
    if (tokenData.expiresAt <= now) {
      this.tokenCache.delete(token);
      return { isValid: false, reason: 'Token expired' };
    }

    if (expectedPurpose && tokenData.purpose !== expectedPurpose) {
      return { isValid: false, reason: 'Token purpose mismatch' };
    }

    return { 
      isValid: true, 
      expiresAt: tokenData.expiresAt 
    };
  }

  /**
   * Consume a token (single use)
   */
  consumeToken(token: string, expectedPurpose?: string): TokenValidationResult {
    const validation = this.validateToken(token, expectedPurpose);
    
    if (validation.isValid) {
      this.tokenCache.delete(token);
    }
    
    return validation;
  }

  /**
   * Invalidate all tokens for a specific purpose
   */
  invalidateTokensByPurpose(purpose: string): void {
    for (const [token, data] of this.tokenCache.entries()) {
      if (data.purpose === purpose) {
        this.tokenCache.delete(token);
      }
    }
  }

  /**
   * Get token info without consuming it
   */
  getTokenInfo(token: string): SecureTokenData | null {
    return this.tokenCache.get(token) || null;
  }

  /**
   * Clean up expired tokens
   */
  private cleanupExpiredTokens(): void {
    const now = new Date();
    for (const [token, data] of this.tokenCache.entries()) {
      if (data.expiresAt <= now) {
        this.tokenCache.delete(token);
      }
    }
  }

  /**
   * Generate a cryptographically secure token ID
   */
  private generateTokenId(): string {
    // Use crypto.getRandomValues for secure random generation
    const array = new Uint8Array(32);
    crypto.getRandomValues(array);
    
    // Convert to base64 and make URL-safe
    const base64 = btoa(String.fromCharCode(...array));
    return base64.replace(/\+/g, '-').replace(/\//g, '_').replace(/=/g, '');
  }

  /**
   * Create a payment confirmation token
   */
  createPaymentConfirmationToken(paymentData: {
    planId: string;
    amount: number;
    userId: string;
  }): string {
    const purpose = `payment_confirm_${paymentData.planId}_${paymentData.userId}`;
    return this.generateSecureToken(purpose);
  }

  /**
   * Create a credit deduction token
   */
  createCreditDeductionToken(userId: string, amount: number): string {
    const purpose = `credit_deduct_${userId}_${amount}`;
    return this.generateSecureToken(purpose);
  }

  /**
   * Create a subscription change token
   */
  createSubscriptionChangeToken(userId: string, fromPlan: string, toPlan: string): string {
    const purpose = `subscription_change_${userId}_${fromPlan}_${toPlan}`;
    return this.generateSecureToken(purpose);
  }

  /**
   * Validate payment confirmation token
   */
  validatePaymentConfirmationToken(
    token: string, 
    paymentData: { planId: string; userId: string }
  ): TokenValidationResult {
    const expectedPurpose = `payment_confirm_${paymentData.planId}_${paymentData.userId}`;
    return this.validateToken(token, expectedPurpose);
  }

  /**
   * Clear all tokens (logout/security reset)
   */
  clearAllTokens(): void {
    this.tokenCache.clear();
  }

  /**
   * Get token statistics
   */
  getTokenStats(): {
    totalTokens: number;
    expiredTokens: number;
    tokensByPurpose: Record<string, number>;
  } {
    const now = new Date();
    let expiredCount = 0;
    const purposeCount: Record<string, number> = {};

    for (const data of this.tokenCache.values()) {
      if (data.expiresAt <= now) {
        expiredCount++;
      }
      
      const purposeKey = data.purpose.split('_')[0]; // Get base purpose
      purposeCount[purposeKey] = (purposeCount[purposeKey] || 0) + 1;
    }

    return {
      totalTokens: this.tokenCache.size,
      expiredTokens: expiredCount,
      tokensByPurpose: purposeCount
    };
  }
}

// Export singleton instance
export const secureTokens = SecureTokenService.getInstance();
