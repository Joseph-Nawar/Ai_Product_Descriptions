import axios, { AxiosError } from "axios";
import { getIdToken } from "../auth/token";

function trimTrailingSlash(s: string) { return s.endsWith("/") ? s.slice(0, -1) : s; }
const env = (import.meta as any).env || {};
const base = env.VITE_API_BASE_URL || env.VITE_API_BASE || "http://localhost:8000";
export const API_BASE = trimTrailingSlash(String(base));
export const api = axios.create({ baseURL: API_BASE, timeout: 300000, headers: { "Content-Type": "application/json" } });

// Add authentication interceptor
api.interceptors.request.use(async (config) => {
  const token = await getIdToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Enhanced error handling for rate limits and payment errors
export function handleApiError(error: unknown): string {
  if (axios.isAxiosError(error)) {
    const axiosError = error as AxiosError;
    
    if (axiosError.response?.status === 429) {
      const retryAfter = axiosError.response.headers['retry-after'];
      const seconds = retryAfter ? parseInt(retryAfter) : 60;
      return `Rate limit exceeded. Please wait ${seconds} seconds before trying again.`;
    }
    
    if (axiosError.response?.status === 400) {
      const errorData = axiosError.response.data as any;
      if (errorData?.error_code === 'INSUFFICIENT_CREDITS') {
        return "Insufficient credits. Please upgrade your plan or purchase more credits.";
      }
      if (errorData?.error_code === 'SUBSCRIPTION_REQUIRED') {
        return "Active subscription required. Please upgrade your plan to continue.";
      }
      if (errorData?.error_code === 'SUBSCRIPTION_EXPIRED') {
        return "Your subscription has expired. Please renew to continue using the service.";
      }
      return "Invalid request. Please check your input and try again.";
    }
    
    if (axiosError.response?.status === 401) {
      return "Authentication required. Please sign in and try again.";
    }
    
    if (axiosError.response?.status === 402) {
      return "Payment required. Please upgrade your plan or purchase credits to continue.";
    }
    
    if (axiosError.response?.status === 403) {
      const errorData = axiosError.response.data as any;
      if (errorData?.error_code === 'CREDIT_LIMIT_EXCEEDED') {
        return "Credit limit exceeded. Please upgrade your plan for higher limits.";
      }
      return "Access denied. Please check your subscription status.";
    }
    
    if (axiosError.response?.status === 500) {
      return "Server error. Please try again later.";
    }
    
    if (axiosError.code === 'ECONNABORTED') {
      return "Request timed out. Please try again.";
    }
  }
  
  return error instanceof Error ? error.message : "An unexpected error occurred.";
}

// Payment API will be imported lazily to avoid circular dependency
export const paymentApi = {
  // These will be populated when payments module is loaded
  getPlans: () => import('./payments').then(m => m.paymentsApi.plans.getPlans()),
  getSubscription: () => import('./payments').then(m => m.paymentsApi.subscription.getCurrent()),
  getCreditBalance: () => import('./payments').then(m => m.paymentsApi.credits.getCurrent()),
  getUsageStats: () => import('./payments').then(m => m.paymentsApi.usage.getStats()),
  getPaymentHistory: () => import('./payments').then(m => m.paymentsApi.history.getHistory()),
  createCheckoutSession: (variantId: string, successUrl?: string, cancelUrl?: string) => 
    import('./payments').then(m => m.paymentsApi.checkout.createSubscriptionCheckout(variantId, successUrl, cancelUrl)),
  cancelSubscription: (subscriptionId: string) => 
    import('./payments').then(m => m.paymentsApi.subscription.cancel(subscriptionId)),
  reactivateSubscription: (subscriptionId: string) => 
    import('./payments').then(m => m.paymentsApi.subscription.reactivate(subscriptionId)),
  updateSubscription: (subscriptionId: string, variantId: string) => 
    import('./payments').then(m => m.paymentsApi.subscription.update(subscriptionId, variantId)),
  handleWebhook: (webhookData: any) => 
    import('./payments').then(m => m.paymentsApi.webhook.handleWebhook(webhookData))
};