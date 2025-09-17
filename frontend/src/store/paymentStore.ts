import { create } from 'zustand';
import { subscribeWithSelector } from 'zustand/middleware';
import { persist, createJSONStorage } from 'zustand/middleware';
import type {
  SubscriptionPlan,
  UserSubscription,
  CreditBalance,
  UsageStats,
  PaymentTransaction,
  CheckoutSession
} from '../types';

// WebSocket connection state
interface WebSocketState {
  connected: boolean;
  reconnecting: boolean;
  lastMessage: string | null;
  reconnectAttempts: number;
}

// Payment store state
interface PaymentState {
  // Subscription data
  subscriptionPlans: SubscriptionPlan[];
  currentSubscription: UserSubscription | null;
  subscriptionLoading: boolean;
  subscriptionError: string | null;

  // Credit balance
  creditBalance: CreditBalance | null;
  creditLoading: boolean;
  creditError: string | null;

  // Usage statistics
  usageStats: UsageStats | null;
  usageLoading: boolean;
  usageError: string | null;

  // Payment history
  paymentHistory: PaymentTransaction[];
  historyLoading: boolean;
  historyError: string | null;
  historyPage: number;
  hasMoreHistory: boolean;

  // Checkout state
  checkoutSession: CheckoutSession | null;
  checkoutLoading: boolean;
  checkoutError: string | null;

  // WebSocket state
  wsState: WebSocketState;

  // UI state
  showUpgradePrompt: boolean;
  showCreditWarning: boolean;
  creditWarningThreshold: number;

  // Actions
  fetchSubscriptionPlans: () => Promise<void>;
  fetchCurrentSubscription: () => Promise<void>;
  fetchCreditBalance: () => Promise<void>;
  fetchUsageStats: () => Promise<void>;
  fetchPaymentHistory: (page?: number, reset?: boolean) => Promise<void>;
  
  // Subscription management
  createCheckoutSession: (variantId: string, successUrl?: string, cancelUrl?: string) => Promise<string | null>;
  cancelSubscription: (subscriptionId: string) => Promise<void>;
  reactivateSubscription: (subscriptionId: string) => Promise<void>;
  updateSubscription: (subscriptionId: string, variantId: string) => Promise<void>;

  // Credit management
  updateCredits: (amount: number, operation: 'add' | 'subtract' | 'set') => void;
  consumeCredits: (amount: number) => boolean;

  // WebSocket management
  connectWebSocket: () => void;
  disconnectWebSocket: () => void;
  handleWebSocketMessage: (message: any) => void;

  // UI actions
  setShowUpgradePrompt: (show: boolean) => void;
  setShowCreditWarning: (show: boolean) => void;
  setCreditWarningThreshold: (threshold: number) => void;

  // Utility actions
  reset: () => void;
  clearErrors: () => void;
  refreshAll: () => Promise<void>;

  // Offline support
  isOnline: boolean;
  setOnlineStatus: (status: boolean) => void;
  syncPendingActions: () => Promise<void>;
  pendingActions: Array<{ type: string; payload: any; timestamp: number }>;
  addPendingAction: (action: { type: string; payload: any }) => void;
}

const initialWebSocketState: WebSocketState = {
  connected: false,
  reconnecting: false,
  lastMessage: null,
  reconnectAttempts: 0,
};

const initialCreditBalance: CreditBalance = {
  current_credits: 0,
  total_credits: 0,
  used_credits: 0,
};

const initialUsageStats: UsageStats = {
  total_generations: 0,
  credits_used_today: 0,
  credits_used_this_month: 0,
  average_generations_per_day: 0,
};

export const usePaymentStore = create<PaymentState>()(
  subscribeWithSelector(
    persist(
      (set, get) => ({
        // Initial state
        subscriptionPlans: [],
        currentSubscription: null,
        subscriptionLoading: false,
        subscriptionError: null,

        creditBalance: initialCreditBalance,
        creditLoading: false,
        creditError: null,

        usageStats: initialUsageStats,
        usageLoading: false,
        usageError: null,

        paymentHistory: [],
        historyLoading: false,
        historyError: null,
        historyPage: 1,
        hasMoreHistory: true,

        checkoutSession: null,
        checkoutLoading: false,
        checkoutError: null,

        wsState: initialWebSocketState,

        showUpgradePrompt: false,
        showCreditWarning: false,
        creditWarningThreshold: 10,

        isOnline: navigator.onLine,
        pendingActions: [],

        // Subscription Plans
        fetchSubscriptionPlans: async () => {
          set({ subscriptionLoading: true, subscriptionError: null });
          try {
            const { paymentsApi } = await import('../api/payments');
            const plans = await paymentsApi.plans.getPlans();
            set({ 
              subscriptionPlans: plans,
              subscriptionLoading: false 
            });
          } catch (error) {
            set({ 
              subscriptionError: error instanceof Error ? error.message : 'Failed to fetch subscription plans',
              subscriptionLoading: false 
            });
          }
        },

        // Current Subscription
        fetchCurrentSubscription: async () => {
          set({ subscriptionLoading: true, subscriptionError: null });
          try {
            const { paymentsApi } = await import('../api/payments');
            const subscription = await paymentsApi.subscription.getCurrent();
            set({ 
              currentSubscription: subscription,
              subscriptionLoading: false 
            });
          } catch (error) {
            set({ 
              subscriptionError: error instanceof Error ? error.message : 'Failed to fetch subscription',
              subscriptionLoading: false 
            });
          }
        },

        // Credit Balance
        fetchCreditBalance: async () => {
          set({ creditLoading: true, creditError: null });
          try {
            const { paymentsApi } = await import('../api/payments');
            const balance = await paymentsApi.credits.getCurrent();
            set({ 
              creditBalance: balance,
              creditLoading: false 
            });
            
            // Check if we need to show credit warning
            const { creditWarningThreshold } = get();
            if (balance.current_credits <= creditWarningThreshold) {
              set({ showCreditWarning: true });
            }
          } catch (error) {
            set({ 
              creditError: error instanceof Error ? error.message : 'Failed to fetch credit balance',
              creditLoading: false 
            });
          }
        },

        // Usage Statistics
        fetchUsageStats: async () => {
          set({ usageLoading: true, usageError: null });
          try {
            const { paymentsApi } = await import('../api/payments');
            const stats = await paymentsApi.usage.getStats();
            set({ 
              usageStats: stats,
              usageLoading: false 
            });
          } catch (error) {
            set({ 
              usageError: error instanceof Error ? error.message : 'Failed to fetch usage stats',
              usageLoading: false 
            });
          }
        },

        // Payment History
        fetchPaymentHistory: async (page = 1, reset = false) => {
          set({ historyLoading: true, historyError: null });
          try {
            const { paymentsApi } = await import('../api/payments');
            const response = await paymentsApi.history.getHistory(page, 10);
            
            set(state => ({
              paymentHistory: reset ? response.data : [...state.paymentHistory, ...response.data],
              hasMoreHistory: response.has_more || false,
              historyPage: page,
              historyLoading: false
            }));
          } catch (error) {
            set({ 
              historyError: error instanceof Error ? error.message : 'Failed to fetch payment history',
              historyLoading: false 
            });
          }
        },

        // Checkout Session
        createCheckoutSession: async (variantId: string, successUrl?: string, cancelUrl?: string) => {
          set({ checkoutLoading: true, checkoutError: null });
          try {
            const { paymentsApi } = await import('../api/payments');
            const session = await paymentsApi.checkout.createSubscriptionCheckout(variantId, successUrl, cancelUrl);
            set({ 
              checkoutSession: session,
              checkoutLoading: false 
            });
            return session.checkout_url;
          } catch (error) {
            set({ 
              checkoutError: error instanceof Error ? error.message : 'Failed to create checkout session',
              checkoutLoading: false 
            });
            return null;
          }
        },

        // Cancel Subscription
        cancelSubscription: async (subscriptionId: string) => {
          try {
            const { paymentsApi } = await import('../api/payments');
            await paymentsApi.subscription.cancel(subscriptionId);
            
            // Refresh subscription data
            await get().fetchCurrentSubscription();
          } catch (error) {
            console.error('Failed to cancel subscription:', error);
            throw error;
          }
        },

        // Reactivate Subscription
        reactivateSubscription: async (subscriptionId: string) => {
          try {
            const { paymentsApi } = await import('../api/payments');
            await paymentsApi.subscription.reactivate(subscriptionId);
            
            // Refresh subscription data
            await get().fetchCurrentSubscription();
          } catch (error) {
            console.error('Failed to reactivate subscription:', error);
            throw error;
          }
        },

        // Update Subscription
        updateSubscription: async (subscriptionId: string, variantId: string) => {
          try {
            const { paymentsApi } = await import('../api/payments');
            await paymentsApi.subscription.update(subscriptionId, variantId);
            
            // Refresh subscription data
            await get().fetchCurrentSubscription();
          } catch (error) {
            console.error('Failed to update subscription:', error);
            throw error;
          }
        },

        // Credit Management
        updateCredits: (amount: number, operation: 'add' | 'subtract' | 'set') => {
          set(state => {
            if (!state.creditBalance) return state;
            
            let newCredits = state.creditBalance.current_credits;
            switch (operation) {
              case 'add':
                newCredits += amount;
                break;
              case 'subtract':
                newCredits = Math.max(0, newCredits - amount);
                break;
              case 'set':
                newCredits = amount;
                break;
            }
            
            return {
              creditBalance: {
                ...state.creditBalance,
                current_credits: newCredits,
                used_credits: state.creditBalance.total_credits - newCredits
              }
            };
          });
        },

        consumeCredits: (amount: number) => {
          const { creditBalance } = get();
          if (!creditBalance || creditBalance.current_credits < amount) {
            return false;
          }
          
          get().updateCredits(amount, 'subtract');
          return true;
        },

        // WebSocket Management
        connectWebSocket: () => {
          const { wsState } = get();
          if (wsState.connected || wsState.reconnecting) return;

          try {
            const wsUrl = import.meta.env.VITE_WS_URL || `ws://localhost:8000/ws/payments`;
            const ws = new WebSocket(wsUrl);
            
            set(state => ({
              wsState: {
                ...state.wsState,
                reconnecting: true,
                reconnectAttempts: state.wsState.reconnectAttempts + 1
              }
            }));

            ws.onopen = () => {
              set(state => ({
                wsState: {
                  ...state.wsState,
                  connected: true,
                  reconnecting: false,
                  reconnectAttempts: 0
                }
              }));
            };

            ws.onmessage = (event) => {
              try {
                const message = JSON.parse(event.data);
                get().handleWebSocketMessage(message);
              } catch (error) {
                console.error('Failed to parse WebSocket message:', error);
              }
            };

            ws.onclose = () => {
              set(state => ({
                wsState: {
                  ...state.wsState,
                  connected: false,
                  reconnecting: false
                }
              }));

              // Attempt to reconnect after a delay
              setTimeout(() => {
                if (get().wsState.reconnectAttempts < 5) {
                  get().connectWebSocket();
                }
              }, 5000);
            };

            ws.onerror = (error) => {
              console.error('WebSocket error:', error);
              set(state => ({
                wsState: {
                  ...state.wsState,
                  connected: false,
                  reconnecting: false
                }
              }));
            };

          } catch (error) {
            console.error('Failed to connect WebSocket:', error);
          }
        },

        disconnectWebSocket: () => {
          set(state => ({
            wsState: {
              ...state.wsState,
              connected: false,
              reconnecting: false
            }
          }));
        },

        handleWebSocketMessage: (message: any) => {
          set(state => ({
            wsState: {
              ...state.wsState,
              lastMessage: JSON.stringify(message)
            }
          }));

          // Handle different message types
          switch (message.type) {
            case 'credit_update':
              get().updateCredits(message.amount, 'set');
              break;
            case 'subscription_update':
              get().fetchCurrentSubscription();
              break;
            case 'payment_completed':
              get().refreshAll();
              break;
            case 'usage_update':
              get().fetchUsageStats();
              break;
          }
        },

        // UI Actions
        setShowUpgradePrompt: (show: boolean) => {
          set({ showUpgradePrompt: show });
        },

        setShowCreditWarning: (show: boolean) => {
          set({ showCreditWarning: show });
        },

        setCreditWarningThreshold: (threshold: number) => {
          set({ creditWarningThreshold: threshold });
        },

        // Utility Actions
        reset: () => {
          set({
            subscriptionPlans: [],
            currentSubscription: null,
            subscriptionLoading: false,
            subscriptionError: null,
            creditBalance: initialCreditBalance,
            creditLoading: false,
            creditError: null,
            usageStats: initialUsageStats,
            usageLoading: false,
            usageError: null,
            paymentHistory: [],
            historyLoading: false,
            historyError: null,
            historyPage: 1,
            hasMoreHistory: true,
            checkoutSession: null,
            checkoutLoading: false,
            checkoutError: null,
            showUpgradePrompt: false,
            showCreditWarning: false,
            pendingActions: []
          });
        },

        clearErrors: () => {
          set({
            subscriptionError: null,
            creditError: null,
            usageError: null,
            historyError: null,
            checkoutError: null
          });
        },

        refreshAll: async () => {
          const promises = [
            get().fetchSubscriptionPlans(),
            get().fetchCurrentSubscription(),
            get().fetchCreditBalance(),
            get().fetchUsageStats(),
            get().fetchPaymentHistory(1, true)
          ];
          
          await Promise.allSettled(promises);
        },

        // Offline Support
        setOnlineStatus: (status: boolean) => {
          set({ isOnline: status });
          
          if (status) {
            // Sync pending actions when coming back online
            get().syncPendingActions();
          }
        },

        addPendingAction: (action: { type: string; payload: any }) => {
          set(state => ({
            pendingActions: [
              ...state.pendingActions,
              {
                ...action,
                timestamp: Date.now()
              }
            ]
          }));
        },

        syncPendingActions: async () => {
          const { pendingActions, isOnline } = get();
          if (!isOnline || pendingActions.length === 0) return;

          const actions = [...pendingActions];
          set({ pendingActions: [] });

          for (const action of actions) {
            try {
              // Execute pending action based on type
              switch (action.type) {
                case 'consume_credits':
                  get().consumeCredits(action.payload.amount);
                  break;
                case 'update_subscription':
                  await get().updateSubscription(action.payload.subscriptionId, action.payload.variantId);
                  break;
                // Add more action types as needed
              }
            } catch (error) {
              console.error('Failed to sync pending action:', error);
              // Re-add failed action to pending list
              get().addPendingAction(action);
            }
          }
        }
      }),
      {
        name: 'payment-store',
        storage: createJSONStorage(() => localStorage),
        partialize: (state) => ({
          // Only persist essential data, not loading states or errors
          subscriptionPlans: state.subscriptionPlans,
          currentSubscription: state.currentSubscription,
          creditBalance: state.creditBalance,
          usageStats: state.usageStats,
          showUpgradePrompt: state.showUpgradePrompt,
          showCreditWarning: state.showCreditWarning,
          creditWarningThreshold: state.creditWarningThreshold,
          pendingActions: state.pendingActions
        })
      }
    )
  )
);

// Subscribe to online/offline status
if (typeof window !== 'undefined') {
  window.addEventListener('online', () => {
    usePaymentStore.getState().setOnlineStatus(true);
  });
  
  window.addEventListener('offline', () => {
    usePaymentStore.getState().setOnlineStatus(false);
  });
}

// Auto-connect WebSocket when store is initialized
usePaymentStore.subscribe(
  (state) => state.isOnline,
  (isOnline) => {
    if (isOnline) {
      usePaymentStore.getState().connectWebSocket();
    } else {
      usePaymentStore.getState().disconnectWebSocket();
    }
  }
);

// Export types for use in components
export type { PaymentState, WebSocketState };
