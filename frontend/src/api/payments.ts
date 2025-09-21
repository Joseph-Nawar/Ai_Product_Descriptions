import { api, handleApiError } from './client';
import { paymentSecurity } from '../services/paymentSecurity';
import { secureTokens } from '../services/secureTokens';
import type {
  SubscriptionPlan,
  UserSubscription,
  CreditBalance,
  UsageStats,
  PaymentTransaction,
  CheckoutSession
} from '../types';

// API response types
interface ApiResponse<T> {
  data: T;
  message?: string;
  success: boolean;
  correlation_id?: string;
  rate_limit_info?: any;
}

interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  limit: number;
  has_more: boolean;
}

// Subscription Plans API
export const subscriptionPlansApi = {
  /**
   * Get all available subscription plans with security validation
   */
  getPlans: async (): Promise<SubscriptionPlan[]> => {
    try {
      const headers = paymentSecurity.generateSecureHeaders();
      const response = await api.get<ApiResponse<SubscriptionPlan[]>>('/api/payment/plans', {
        headers
      });
      
      // Log security event
      paymentSecurity.logSecurityEvent({
        type: 'security_check',
        data: {
          operation: 'get_plans',
          correlationId: response.data.correlation_id
        },
        severity: 'low'
      });
      
      return response.data.data;
    } catch (error) {
      paymentSecurity.logSecurityEvent({
        type: 'payment_attempt',
        data: {
          operation: 'get_plans',
          error: error instanceof Error ? error.message : 'Unknown error'
        },
        severity: 'medium'
      });
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get a specific subscription plan by ID with validation
   */
  getPlan: async (planId: string): Promise<SubscriptionPlan> => {
    try {
      // Validate plan ID
      if (!planId || planId.length > 50) {
        throw new Error('Invalid plan ID');
      }
      
      const headers = paymentSecurity.generateSecureHeaders();
      const response = await api.get<ApiResponse<SubscriptionPlan>>(`/payment/plans/${planId}`, {
        headers
      });
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  }
};

// User Subscription API
export const userSubscriptionApi = {
  /**
   * Get current user's subscription
   */
  getCurrent: async (): Promise<UserSubscription | null> => {
    try {
      const response = await api.get<ApiResponse<UserSubscription | null>>('/api/payment/user/subscription');
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Create a new subscription
   */
  create: async (variantId: string, successUrl?: string, cancelUrl?: string): Promise<CheckoutSession> => {
    try {
      const response = await api.post<ApiResponse<CheckoutSession>>('/api/payment/checkout', {
        variant_id: variantId,
        success_url: successUrl,
        cancel_url: cancelUrl
      });
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Cancel a subscription
   */
  cancel: async (subscriptionId: string): Promise<void> => {
    try {
      await api.post(`/payments/subscription/${subscriptionId}/cancel`);
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Reactivate a cancelled subscription
   */
  reactivate: async (subscriptionId: string): Promise<void> => {
    try {
      await api.post(`/payments/subscription/${subscriptionId}/reactivate`);
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Update subscription plan
   */
  update: async (subscriptionId: string, variantId: string): Promise<void> => {
    try {
      await api.post(`/payments/subscription/${subscriptionId}/update`, {
        variant_id: variantId
      });
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get subscription usage for current period
   */
  getUsage: async (subscriptionId: string): Promise<{ used: number; limit: number; reset_date: string }> => {
    try {
      const response = await api.get<ApiResponse<{ used: number; limit: number; reset_date: string }>>(
        `/payments/subscription/${subscriptionId}/usage`
      );
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  }
};

// Credit Balance API with Enhanced Security
export const creditBalanceApi = {
  /**
   * Get current credit balance with security validation
   */
  getCurrent: async (): Promise<CreditBalance> => {
    try {
      const headers = paymentSecurity.generateSecureHeaders();
      const response = await api.get<ApiResponse<CreditBalance>>('/api/payment/user/credits', {
        headers
      });
      
      paymentSecurity.logSecurityEvent({
        type: 'security_check',
        data: {
          operation: 'get_credits',
          correlationId: response.data.correlation_id
        },
        severity: 'low'
      });
      
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Check if sufficient credits are available for operation
   */
  checkSufficient: async (batchSize: number): Promise<{
    success: boolean;
    can_generate: boolean;
    current_credits?: number;
    error?: string;
    correlation_id?: string;
  }> => {
    try {
      // Validate batch size
      const validation = paymentSecurity.validateCreditCheck({ batch_size: batchSize });
      if (!validation.isValid) {
        throw new Error(`Validation failed: ${validation.errors.join(', ')}`);
      }

      const headers = paymentSecurity.generateSecureHeaders();
      const response = await api.post<{
        success: boolean;
        can_generate: boolean;
        current_credits?: number;
        error?: string;
        correlation_id?: string;
      }>('/api/payment/user/credits/check', validation.sanitized, { headers });

      paymentSecurity.logSecurityEvent({
        type: 'security_check',
        data: {
          operation: 'check_credits',
          batchSize,
          result: response.data.can_generate,
          correlationId: response.data.correlation_id
        },
        severity: 'low'
      });

      return response.data;
    } catch (error) {
      paymentSecurity.logSecurityEvent({
        type: 'payment_attempt',
        data: {
          operation: 'check_credits_failed',
          batchSize,
          error: error instanceof Error ? error.message : 'Unknown error'
        },
        severity: 'medium'
      });
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Deduct credits with secure transaction handling
   */
  deduct: async (amount: number, operationContext?: Record<string, any>): Promise<{
    success: boolean;
    credits_deducted?: number;
    remaining_credits?: number;
    transaction_id?: string;
    error?: string;
    correlation_id?: string;
  }> => {
    try {
      // Validate deduction request
      const validation = paymentSecurity.validateCreditDeduction({
        amount,
        operation_context: operationContext
      });
      
      if (!validation.isValid) {
        throw new Error(`Validation failed: ${validation.errors.join(', ')}`);
      }

      // Generate deduction token
      const deductionToken = secureTokens.createCreditDeductionToken('current_user', amount);
      
      const headers = {
        ...paymentSecurity.generateSecureHeaders(),
        'X-Deduction-Token': deductionToken
      };

      const response = await api.post<{
        success: boolean;
        credits_deducted?: number;
        remaining_credits?: number;
        transaction_id?: string;
        error?: string;
        correlation_id?: string;
      }>('/api/payment/user/credits/deduct', validation.sanitized, { headers });

      if (response.data.success) {
        paymentSecurity.logSecurityEvent({
          type: 'payment_attempt',
          data: {
            operation: 'deduct_credits',
            amount,
            remaining: response.data.remaining_credits,
            transactionId: response.data.transaction_id,
            correlationId: response.data.correlation_id
          },
          severity: 'medium'
        });
      } else {
        paymentSecurity.logSecurityEvent({
          type: 'payment_attempt',
          data: {
            operation: 'deduct_credits_failed',
            amount,
            error: response.data.error,
            correlationId: response.data.correlation_id
          },
          severity: 'high'
        });
      }

      return response.data;
    } catch (error) {
      paymentSecurity.logSecurityEvent({
        type: 'payment_attempt',
        data: {
          operation: 'deduct_credits_error',
          amount,
          error: error instanceof Error ? error.message : 'Unknown error'
        },
        severity: 'high'
      });
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Purchase additional credits
   */
  purchase: async (amount: number, variantId?: string): Promise<CheckoutSession> => {
    try {
      const response = await api.post<ApiResponse<CheckoutSession>>('/api/payment/checkout', {
        amount,
        variant_id: variantId
      });
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get credit usage history
   */
  getUsageHistory: async (page = 1, limit = 10): Promise<PaginatedResponse<{ id: string; amount: number; description: string; created_at: string }>> => {
    try {
      const response = await api.get<PaginatedResponse<{ id: string; amount: number; description: string; created_at: string }>>(
        `/payments/credits/usage?page=${page}&limit=${limit}`
      );
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  }
};

// Usage Statistics API
export const usageStatsApi = {
  /**
   * Get usage statistics
   */
  getStats: async (): Promise<UsageStats> => {
    try {
      const response = await api.get<ApiResponse<UsageStats>>('/api/payment/user/usage');
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get usage statistics for a specific period
   */
  getStatsForPeriod: async (startDate: string, endDate: string): Promise<UsageStats> => {
    try {
      const response = await api.get<ApiResponse<UsageStats>>(
        `/payments/usage?start_date=${startDate}&end_date=${endDate}`
      );
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get daily usage for the last 30 days
   */
  getDailyUsage: async (days = 30): Promise<Array<{ date: string; credits_used: number; generations: number }>> => {
    try {
      const response = await api.get<ApiResponse<Array<{ date: string; credits_used: number; generations: number }>>>(
        `/payments/usage/daily?days=${days}`
      );
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  }
};

// Payment History API
export const paymentHistoryApi = {
  /**
   * Get payment history
   */
  getHistory: async (page = 1, limit = 10): Promise<PaginatedResponse<PaymentTransaction>> => {
    try {
      const response = await api.get<PaginatedResponse<PaymentTransaction>>(
        `/payments/history?page=${page}&limit=${limit}`
      );
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get payment history for a specific period
   */
  getHistoryForPeriod: async (startDate: string, endDate: string, page = 1, limit = 10): Promise<PaginatedResponse<PaymentTransaction>> => {
    try {
      const response = await api.get<PaginatedResponse<PaymentTransaction>>(
        `/payments/history?start_date=${startDate}&end_date=${endDate}&page=${page}&limit=${limit}`
      );
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get a specific payment transaction
   */
  getTransaction: async (transactionId: string): Promise<PaymentTransaction> => {
    try {
      const response = await api.get<ApiResponse<PaymentTransaction>>(`/payments/history/${transactionId}`);
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Download payment history as CSV
   */
  downloadHistory: async (startDate?: string, endDate?: string): Promise<Blob> => {
    try {
      const params = new URLSearchParams();
      if (startDate) params.append('start_date', startDate);
      if (endDate) params.append('end_date', endDate);
      
      const response = await api.get(`/payments/history/export?${params.toString()}`, {
        responseType: 'blob'
      });
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  }
};

// Checkout API
export const checkoutApi = {
  /**
   * Create checkout session for subscription
   */
  createSubscriptionCheckout: async (variantId: string, successUrl?: string, cancelUrl?: string): Promise<CheckoutSession> => {
    try {
      const response = await api.post<ApiResponse<CheckoutSession>>('/api/payment/checkout', {
        variant_id: variantId,
        success_url: successUrl,
        cancel_url: cancelUrl
      });
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Create customer portal session for subscription management
   */
  createPortalSession: async (): Promise<{ url: string }> => {
    try {
      const headers = paymentSecurity.generateSecureHeaders();
      const response = await api.post<{
        success: boolean;
        url: string;
        rate_limit_info?: any;
      }>('/api/payment/portal', {}, { headers });
      
      // Log security event
      paymentSecurity.logSecurityEvent({
        type: 'security_check',
        data: {
          operation: 'create_portal_session',
          portalUrl: response.data.url
        },
        severity: 'medium'
      });
      
      return { url: response.data.url };
    } catch (error) {
      paymentSecurity.logSecurityEvent({
        type: 'payment_attempt',
        data: {
          operation: 'create_portal_session_failed',
          error: error instanceof Error ? error.message : 'Unknown error'
        },
        severity: 'medium'
      });
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Create checkout session for credit purchase
   */
  createCreditCheckout: async (amount: number, variantId?: string, successUrl?: string, cancelUrl?: string): Promise<CheckoutSession> => {
    try {
      const response = await api.post<ApiResponse<CheckoutSession>>('/api/payment/checkout', {
        amount,
        variant_id: variantId,
        success_url: successUrl,
        cancel_url: cancelUrl
      });
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Verify checkout session
   */
  verifySession: async (sessionId: string): Promise<{ valid: boolean; status: string; subscription?: UserSubscription; credits?: number }> => {
    try {
      const response = await api.get<ApiResponse<{ valid: boolean; status: string; subscription?: UserSubscription; credits?: number }>>(
        `/payments/checkout/${sessionId}/verify`
      );
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  }
};

// Webhook API
export const webhookApi = {
  /**
   * Handle webhook events (for testing purposes)
   */
  handleWebhook: async (webhookData: any): Promise<void> => {
    try {
      await api.post('/api/payment/webhook', webhookData);
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  }
};

// Analytics API
export const analyticsApi = {
  /**
   * Get payment analytics
   */
  getAnalytics: async (period: 'day' | 'week' | 'month' | 'year' = 'month'): Promise<{
    total_revenue: number;
    subscription_revenue: number;
    credit_revenue: number;
    active_subscriptions: number;
    new_subscriptions: number;
    cancelled_subscriptions: number;
    credit_purchases: number;
    usage_trends: Array<{ date: string; value: number }>;
  }> => {
    try {
      const response = await api.get<ApiResponse<{
        total_revenue: number;
        subscription_revenue: number;
        credit_revenue: number;
        active_subscriptions: number;
        new_subscriptions: number;
        cancelled_subscriptions: number;
        credit_purchases: number;
        usage_trends: Array<{ date: string; value: number }>;
      }>>(`/payments/analytics?period=${period}`);
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  }
};

// Security and Administration API
export const securityApi = {
  /**
   * Get audit logs for current user
   */
  getAuditLogs: async (limit = 50): Promise<{
    success: boolean;
    logs: Array<{
      event_type: string;
      timestamp: string;
      event_data: any;
      security_level: string;
      success: boolean;
      error_message?: string;
    }>;
    count: number;
    correlation_id: string;
  }> => {
    try {
      const headers = paymentSecurity.generateSecureHeaders();
      const response = await api.get<{
        success: boolean;
        logs: Array<{
          event_type: string;
          timestamp: string;
          event_data: any;
          security_level: string;
          success: boolean;
          error_message?: string;
        }>;
        count: number;
        correlation_id: string;
      }>(`/payment/admin/audit-logs?limit=${limit}`, { headers });
      
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get rate limit status for current user
   */
  getRateLimitStatus: async (endpoint: string): Promise<{
    success: boolean;
    rate_limit_status: {
      endpoint: string;
      current_requests: number;
      limit: number;
      remaining_requests: number;
      reset_time?: string;
      penalty_active: boolean;
    };
    correlation_id: string;
  }> => {
    try {
      const headers = paymentSecurity.generateSecureHeaders();
      const response = await api.get<{
        success: boolean;
        rate_limit_status: any;
        correlation_id: string;
      }>(`/payment/admin/rate-limit-status/${endpoint}`, { headers });
      
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get transaction status
   */
  getTransactionStatus: async (transactionId: string): Promise<{
    success: boolean;
    transaction: {
      transaction_id: string;
      operation_type: string;
      status: string;
      created_at: string;
      updated_at: string;
      retry_count: number;
      error_message?: string;
    };
    correlation_id: string;
  }> => {
    try {
      const headers = paymentSecurity.generateSecureHeaders();
      const response = await api.get<{
        success: boolean;
        transaction: any;
        correlation_id: string;
      }>(`/payment/transaction/${transactionId}`, { headers });
      
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Validate subscription status before operations
   */
  validateSubscriptionStatus: async (): Promise<{
    valid: boolean;
    subscription: UserSubscription | null;
    can_proceed: boolean;
    reason?: string;
  }> => {
    try {
      const subscription = await userSubscriptionApi.getCurrent();
      const validation = paymentSecurity.validateSubscriptionStatus(subscription);
      
      return {
        valid: !!subscription,
        subscription,
        can_proceed: validation.canProceed,
        reason: validation.reason
      };
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Clear security tokens (logout/security reset)
   */
  clearSecurityTokens: (): void => {
    secureTokens.clearAllTokens();
    paymentSecurity.logSecurityEvent({
      type: 'security_check',
      data: { operation: 'tokens_cleared' },
      severity: 'medium'
    });
  },

  /**
   * Get security statistics
   */
  getSecurityStats: (): {
    tokenStats: {
      totalTokens: number;
      expiredTokens: number;
      tokensByPurpose: Record<string, number>;
    };
    correlationId: string;
  } => {
    return {
      tokenStats: secureTokens.getTokenStats(),
      correlationId: paymentSecurity.getCorrelationId()
    };
  }
};

// Export all APIs as a single object for convenience
export const paymentsApi = {
  plans: subscriptionPlansApi,
  subscription: userSubscriptionApi,
  credits: creditBalanceApi,
  usage: usageStatsApi,
  history: paymentHistoryApi,
  checkout: checkoutApi,
  webhook: webhookApi,
  analytics: analyticsApi,
  security: securityApi
};

// Export individual APIs for specific use cases
export {
  subscriptionPlansApi as subscriptionPlans,
  userSubscriptionApi as userSubscription,
  creditBalanceApi as creditBalance,
  usageStatsApi as usageStats,
  paymentHistoryApi as paymentHistory,
  checkoutApi as checkout,
  webhookApi as webhook,
  analyticsApi as analytics,
  securityApi as security
};
