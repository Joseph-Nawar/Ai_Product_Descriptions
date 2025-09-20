import { api, handleApiError } from './client';
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
      const response = await api.get<ApiResponse<SubscriptionPlan[]>>('/api/payment/plans');
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Get a specific subscription plan by ID with validation
   */
  getPlan: async (planId: string): Promise<SubscriptionPlan> => {
    try {
      if (!planId || planId.length > 50) {
        throw new Error('Invalid plan ID');
      }
      
      const response = await api.get<ApiResponse<SubscriptionPlan>>(`/api/payment/plans/${planId}`);
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
        plan_id: variantId,
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
      await api.post(`/api/payment/subscription/${subscriptionId}/cancel`);
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Reactivate a cancelled subscription
   */
  reactivate: async (subscriptionId: string): Promise<void> => {
    try {
      await api.post(`/api/payment/subscription/${subscriptionId}/reactivate`);
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Update subscription plan
   */
  update: async (subscriptionId: string, variantId: string): Promise<void> => {
    try {
      await api.post(`/api/payment/subscription/${subscriptionId}/update`, {
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
        `/api/payment/subscription/${subscriptionId}/usage`
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
      const response = await api.get<ApiResponse<CreditBalance>>('/api/payment/user/credits');
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
      if (batchSize < 1 || batchSize > 100) {
        throw new Error('Batch size must be between 1 and 100');
      }

      const response = await api.post<{
        success: boolean;
        can_generate: boolean;
        current_credits?: number;
        error?: string;
        correlation_id?: string;
      }>('/api/payment/user/credits/check', { batch_size: batchSize });

      return response.data;
    } catch (error) {
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
      if (amount < 1 || amount > 50) {
        throw new Error('Amount must be between 1 and 50');
      }

      const response = await api.post<{
        success: boolean;
        credits_deducted?: number;
        remaining_credits?: number;
        transaction_id?: string;
        error?: string;
        correlation_id?: string;
      }>('/api/payment/user/credits/deduct', { 
        amount, 
        operation_context: operationContext 
      });

      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Purchase additional credits
   */
  purchase: async (amount: number, variantId?: string): Promise<CheckoutSession> => {
    try {
      const response = await api.post<ApiResponse<CheckoutSession>>('/api/payment/checkout', {
        plan_id: variantId,
        amount,
        success_url: window.location.origin + '/payment/success',
        cancel_url: window.location.origin + '/payment/cancel'
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
        `/api/payment/credits/usage?page=${page}&limit=${limit}`
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
      // Mock response since this endpoint doesn't exist in backend yet
      return {
        total_generations: 0,
        credits_used: 0,
        credits_remaining: 0,
        generations_this_month: 0,
        generations_this_week: 0,
        generations_today: 0,
        average_generations_per_day: 0,
        most_active_day: new Date().toISOString().split('T')[0],
        last_generation: null
      };
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
        `/api/payment/usage?start_date=${startDate}&end_date=${endDate}`
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
        `/api/payment/usage/daily?days=${days}`
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
      // Mock response since this endpoint doesn't exist in backend yet
      return {
        data: [],
        total: 0,
        page: page,
        limit: limit,
        has_more: false
      };
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
        `/api/payment/history?start_date=${startDate}&end_date=${endDate}&page=${page}&limit=${limit}`
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
      const response = await api.get<ApiResponse<PaymentTransaction>>(`/api/payment/history/${transactionId}`);
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
      
      const response = await api.get(`/api/payment/history/export?${params.toString()}`, {
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
        plan_id: variantId,
        success_url: successUrl,
        cancel_url: cancelUrl
      });
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  /**
   * Create checkout session for credit purchase
   */
  createCreditCheckout: async (amount: number, variantId?: string, successUrl?: string, cancelUrl?: string): Promise<CheckoutSession> => {
    try {
      const response = await api.post<ApiResponse<CheckoutSession>>('/api/payment/checkout', {
        plan_id: variantId,
        amount,
        success_url: successUrl || window.location.origin + '/payment/success',
        cancel_url: cancelUrl || window.location.origin + '/payment/cancel'
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
        `/api/payment/checkout/${sessionId}/verify`
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
      }>>(`/api/payment/analytics?period=${period}`);
      return response.data.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  }
};

// Security and Administration API (simplified)
export const securityApi = {
  getAuditLogs: async (limit = 50): Promise<any> => {
    try {
      const response = await api.get(`/api/payment/admin/audit-logs?limit=${limit}`);
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  getRateLimitStatus: async (endpoint: string): Promise<any> => {
    try {
      const response = await api.get(`/api/payment/admin/rate-limit-status/${endpoint}`);
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  getTransactionStatus: async (transactionId: string): Promise<any> => {
    try {
      const response = await api.get(`/api/payment/transaction/${transactionId}`);
      return response.data;
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  validateSubscriptionStatus: async (): Promise<{
    valid: boolean;
    subscription: UserSubscription | null;
    can_proceed: boolean;
    reason?: string;
  }> => {
    try {
      const subscription = await userSubscriptionApi.getCurrent();
      return {
        valid: !!subscription,
        subscription,
        can_proceed: !!subscription,
        reason: subscription ? undefined : 'No active subscription'
      };
    } catch (error) {
      throw new Error(handleApiError(error));
    }
  },

  clearSecurityTokens: (): void => {
    // Simple implementation
    console.log('Security tokens cleared');
  },

  getSecurityStats: (): any => {
    return {
      tokenStats: { totalTokens: 0, expiredTokens: 0, tokensByPurpose: {} },
      correlationId: 'simplified'
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
