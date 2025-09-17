import { usePaymentStore } from '../store/paymentStore';
import { useAuth } from '../auth/AuthProvider';
import { useEffect, useCallback } from 'react';

/**
 * Custom hook for payment-related functionality
 * Provides easy access to payment state and actions
 */
export const usePayment = () => {
  const { user } = useAuth();
  const paymentStore = usePaymentStore();

  // Auto-refresh payment data when user changes
  useEffect(() => {
    if (user) {
      paymentStore.refreshAll();
    }
  }, [user, paymentStore.refreshAll]);

  // Helper functions
  const canGenerate = useCallback((creditsNeeded: number = 1): boolean => {
    const { creditBalance } = paymentStore;
    return creditBalance ? creditBalance.current_credits >= creditsNeeded : false;
  }, [paymentStore.creditBalance]);

  const isSubscriptionActive = useCallback((): boolean => {
    const { currentSubscription } = paymentStore;
    return currentSubscription?.status === 'active';
  }, [paymentStore.currentSubscription]);

  const shouldShowUpgradePrompt = useCallback((): boolean => {
    const { creditBalance, currentSubscription } = paymentStore;
    
    // Show upgrade prompt if no active subscription and low credits
    if (!isSubscriptionActive() && creditBalance && creditBalance.current_credits < 5) {
      return true;
    }
    
    return paymentStore.showUpgradePrompt;
  }, [paymentStore.creditBalance, paymentStore.currentSubscription, paymentStore.showUpgradePrompt, isSubscriptionActive]);

  const getUpgradeReason = useCallback((): string => {
    const { creditBalance, currentSubscription } = paymentStore;
    
    if (!currentSubscription) {
      return 'You don\'t have an active subscription. Upgrade to get unlimited generations!';
    }
    
    if (currentSubscription.status === 'cancelled') {
      return 'Your subscription was cancelled. Reactivate to continue enjoying unlimited generations!';
    }
    
    if (creditBalance && creditBalance.current_credits < 5) {
      return 'You\'re running low on credits. Upgrade your plan for unlimited generations!';
    }
    
    return 'Upgrade your plan to unlock premium features!';
  }, [paymentStore.creditBalance, paymentStore.currentSubscription]);

  const handleGeneration = useCallback(async (creditsNeeded: number = 1) => {
    const { consumeCredits, isOnline, addPendingAction } = paymentStore;
    
    if (!canGenerate(creditsNeeded)) {
      paymentStore.setShowUpgradePrompt(true);
      return false;
    }

    // Try to consume credits
    const success = consumeCredits(creditsNeeded);
    
    if (!success) {
      paymentStore.setShowUpgradePrompt(true);
      return false;
    }

    // If offline, add to pending actions
    if (!isOnline) {
      addPendingAction({
        type: 'consume_credits',
        payload: { amount: creditsNeeded }
      });
    }

    return true;
  }, [paymentStore, canGenerate]);

  const handleUpgrade = useCallback(async (variantId: string) => {
    const { createCheckoutSession } = paymentStore;
    
    try {
      const checkoutUrl = await createCheckoutSession(variantId);
      if (checkoutUrl) {
        window.location.href = checkoutUrl;
      }
    } catch (error) {
      console.error('Failed to create checkout session:', error);
    }
  }, [paymentStore.createCheckoutSession]);

  const handleCancelSubscription = useCallback(async () => {
    const { currentSubscription, cancelSubscription } = paymentStore;
    
    if (!currentSubscription) return;
    
    try {
      await cancelSubscription(currentSubscription.id);
    } catch (error) {
      console.error('Failed to cancel subscription:', error);
      throw error;
    }
  }, [paymentStore]);

  const handleReactivateSubscription = useCallback(async () => {
    const { currentSubscription, reactivateSubscription } = paymentStore;
    
    if (!currentSubscription) return;
    
    try {
      await reactivateSubscription(currentSubscription.id);
    } catch (error) {
      console.error('Failed to reactivate subscription:', error);
      throw error;
    }
  }, [paymentStore]);

  const refreshPaymentData = useCallback(async () => {
    try {
      await paymentStore.refreshAll();
    } catch (error) {
      console.error('Failed to refresh payment data:', error);
    }
  }, [paymentStore.refreshAll]);

  return {
    // State
    ...paymentStore,
    
    // Computed values
    canGenerate,
    isSubscriptionActive,
    shouldShowUpgradePrompt,
    getUpgradeReason,
    
    // Actions
    handleGeneration,
    handleUpgrade,
    handleCancelSubscription,
    handleReactivateSubscription,
    refreshPaymentData,
    
    // Quick access to common values
    creditBalance: paymentStore.creditBalance,
    currentSubscription: paymentStore.currentSubscription,
    subscriptionPlans: paymentStore.subscriptionPlans,
    usageStats: paymentStore.usageStats,
    paymentHistory: paymentStore.paymentHistory,
    isLoading: paymentStore.subscriptionLoading || paymentStore.creditLoading || paymentStore.usageLoading,
    hasError: !!(paymentStore.subscriptionError || paymentStore.creditError || paymentStore.usageError)
  };
};

/**
 * Hook for subscription-specific functionality
 */
export const useSubscription = () => {
  const payment = usePayment();
  
  return {
    subscription: payment.currentSubscription,
    plans: payment.subscriptionPlans,
    isLoading: payment.subscriptionLoading,
    error: payment.subscriptionError,
    isActive: payment.isSubscriptionActive(),
    cancel: payment.handleCancelSubscription,
    reactivate: payment.handleReactivateSubscription,
    update: payment.updateSubscription,
    refresh: payment.fetchCurrentSubscription
  };
};

/**
 * Hook for credit-specific functionality
 */
export const useCredits = () => {
  const payment = usePayment();
  
  return {
    balance: payment.creditBalance,
    isLoading: payment.creditLoading,
    error: payment.creditError,
    canGenerate: payment.canGenerate,
    consume: payment.consumeCredits,
    update: payment.updateCredits,
    refresh: payment.fetchCreditBalance,
    showWarning: payment.showCreditWarning,
    setShowWarning: payment.setShowCreditWarning
  };
};

/**
 * Hook for usage statistics
 */
export const useUsageStats = () => {
  const payment = usePayment();
  
  return {
    stats: payment.usageStats,
    isLoading: payment.usageLoading,
    error: payment.usageError,
    refresh: payment.fetchUsageStats
  };
};

/**
 * Hook for payment history
 */
export const usePaymentHistory = () => {
  const payment = usePayment();
  
  return {
    history: payment.paymentHistory,
    isLoading: payment.historyLoading,
    error: payment.historyError,
    hasMore: payment.hasMoreHistory,
    page: payment.historyPage,
    fetchMore: () => payment.fetchPaymentHistory(payment.historyPage + 1),
    refresh: () => payment.fetchPaymentHistory(1, true)
  };
};

/**
 * Hook for checkout functionality
 */
export const useCheckout = () => {
  const payment = usePayment();
  
  return {
    createSession: payment.createCheckoutSession,
    isLoading: payment.checkoutLoading,
    error: payment.checkoutError,
    session: payment.checkoutSession
  };
};

/**
 * Hook for WebSocket functionality
 */
export const useWebSocket = () => {
  const payment = usePayment();
  
  return {
    connected: payment.wsState.connected,
    reconnecting: payment.wsState.reconnecting,
    reconnectAttempts: payment.wsState.reconnectAttempts,
    lastMessage: payment.wsState.lastMessage,
    connect: payment.connectWebSocket,
    disconnect: payment.disconnectWebSocket
  };
};

/**
 * Hook for offline functionality
 */
export const useOffline = () => {
  const payment = usePayment();
  
  return {
    isOnline: payment.isOnline,
    pendingActions: payment.pendingActions,
    addPendingAction: payment.addPendingAction,
    syncPendingActions: payment.syncPendingActions
  };
};



