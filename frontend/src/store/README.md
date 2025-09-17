# Payment State Management System

This directory contains the comprehensive payment state management system for the AI Product Descriptions application. The system provides real-time payment tracking, offline support, WebSocket integration, and seamless integration with the authentication system.

## Architecture Overview

The payment state management system consists of several interconnected components:

```
┌─────────────────────────────────────────────────────────────┐
│                    Payment State Management                 │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Zustand     │  │ WebSocket   │  │ Offline Sync        │  │
│  │ Store       │  │ Service     │  │ Service             │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
│           │               │                   │              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Payment     │  │ Real-time   │  │ Local Storage       │  │
│  │ Context     │  │ Updates     │  │ Cache               │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
│           │               │                   │              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Custom      │  │ Payment     │  │ Auth Integration    │  │
│  │ Hooks       │  │ API         │  │                     │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Components

### 1. Payment Store (`paymentStore.ts`)

The core state management using Zustand with persistence and WebSocket integration.

**Features:**
- Real-time credit balance updates
- Subscription status monitoring
- Usage statistics tracking
- Payment history management
- WebSocket connection state
- Offline action queuing
- Local storage persistence

**Key Actions:**
```typescript
// Fetch data
fetchSubscriptionPlans()
fetchCurrentSubscription()
fetchCreditBalance()
fetchUsageStats()
fetchPaymentHistory()

// Subscription management
createCheckoutSession(variantId, successUrl?, cancelUrl?)
cancelSubscription(subscriptionId)
reactivateSubscription(subscriptionId)
updateSubscription(subscriptionId, variantId)

// Credit management
updateCredits(amount, operation)
consumeCredits(amount)

// WebSocket management
connectWebSocket()
disconnectWebSocket()
handleWebSocketMessage(message)

// Offline support
addPendingAction(action)
syncPendingActions()
```

### 2. Payment API (`../api/payments.ts`)

Comprehensive API layer for all payment-related operations.

**API Modules:**
- `subscriptionPlansApi` - Subscription plan management
- `userSubscriptionApi` - User subscription operations
- `creditBalanceApi` - Credit balance and purchases
- `usageStatsApi` - Usage statistics and analytics
- `paymentHistoryApi` - Payment transaction history
- `checkoutApi` - Checkout session management
- `webhookApi` - Webhook handling
- `analyticsApi` - Payment analytics

### 3. Custom Hooks (`../hooks/usePayment.ts`)

Specialized hooks for different payment functionalities.

**Available Hooks:**
- `usePayment()` - Main payment hook with all functionality
- `useSubscription()` - Subscription-specific functionality
- `useCredits()` - Credit balance and consumption
- `useUsageStats()` - Usage statistics
- `usePaymentHistory()` - Payment history
- `useCheckout()` - Checkout operations
- `useWebSocket()` - WebSocket connection status
- `useOffline()` - Offline functionality

### 4. WebSocket Service (`../services/websocketService.ts`)

Real-time communication service for payment updates.

**Features:**
- Automatic connection management
- Reconnection with exponential backoff
- Heartbeat/ping-pong mechanism
- Message type handling
- Online/offline status detection
- Authentication integration

**Message Types:**
- `credit_update` - Credit balance changes
- `subscription_update` - Subscription status changes
- `payment_completed` - Payment completion notifications
- `usage_update` - Usage statistics updates
- `subscription_cancelled` - Subscription cancellation
- `subscription_reactivated` - Subscription reactivation
- `credit_warning` - Low credit warnings

### 5. Offline Sync Service (`../services/offlineSyncService.ts`)

Handles offline payment actions and synchronization.

**Features:**
- Action queuing for offline scenarios
- Automatic sync when back online
- Retry logic with exponential backoff
- Local storage persistence
- Action validation and cleanup

**Supported Actions:**
- `consume_credits` - Credit consumption
- `update_subscription` - Subscription updates
- `cancel_subscription` - Subscription cancellation
- `reactivate_subscription` - Subscription reactivation
- `purchase_credits` - Credit purchases

### 6. Payment Context (`../contexts/PaymentContext.tsx`)

React context provider for payment functionality.

**Features:**
- Centralized payment state management
- WebSocket connection lifecycle
- Online/offline status handling
- HOC wrapper for easy integration

### 7. Payment State Manager Components (`../components/PaymentStateManager.tsx`)

UI components for payment state management.

**Components:**
- `PaymentStateManager` - Main state management component
- `UpgradePrompt` - Upgrade prompt display
- `CreditWarning` - Low credit warning
- `PaymentLoading` - Loading state display
- `PaymentError` - Error state display

## Usage Examples

### Basic Payment Integration

```typescript
import { usePayment } from '../hooks/usePayment';

function MyComponent() {
  const {
    creditBalance,
    currentSubscription,
    canGenerate,
    handleGeneration,
    handleUpgrade
  } = usePayment();

  const handleGenerateClick = async () => {
    const success = await handleGeneration(1);
    if (!success) {
      // Show upgrade prompt or handle insufficient credits
    }
  };

  return (
    <div>
      <p>Credits: {creditBalance?.current_credits || 0}</p>
      <button onClick={handleGenerateClick}>
        Generate Description
      </button>
    </div>
  );
}
```

### Using Payment Context

```typescript
import { PaymentProvider, usePaymentContext } from '../contexts/PaymentContext';

function App() {
  return (
    <PaymentProvider>
      <MyComponent />
    </PaymentProvider>
  );
}

function MyComponent() {
  const { payment, ws } = usePaymentContext();
  
  return (
    <div>
      <p>WebSocket Connected: {ws.isConnected()}</p>
      <p>Credits: {payment.creditBalance?.current_credits}</p>
    </div>
  );
}
```

### Subscription Management

```typescript
import { useSubscription } from '../hooks/usePayment';

function SubscriptionManager() {
  const {
    subscription,
    plans,
    isActive,
    cancel,
    reactivate
  } = useSubscription();

  const handleCancel = async () => {
    try {
      await cancel();
      alert('Subscription cancelled successfully');
    } catch (error) {
      alert('Failed to cancel subscription');
    }
  };

  return (
    <div>
      <h3>Current Subscription</h3>
      {subscription ? (
        <div>
          <p>Plan: {subscription.plan.name}</p>
          <p>Status: {subscription.status}</p>
          {isActive() ? (
            <button onClick={handleCancel}>Cancel Subscription</button>
          ) : (
            <button onClick={() => reactivate()}>Reactivate</button>
          )}
        </div>
      ) : (
        <p>No active subscription</p>
      )}
    </div>
  );
}
```

### Offline Support

```typescript
import { useOffline } from '../hooks/usePayment';

function OfflineIndicator() {
  const { isOnline, pendingActions, syncPendingActions } = useOffline();

  if (!isOnline) {
    return (
      <div className="bg-yellow-500 text-white p-2">
        Offline - {pendingActions.length} actions pending
      </div>
    );
  }

  return null;
}
```

## Configuration

### Environment Variables

```env
# WebSocket URL
VITE_WS_URL=ws://localhost:8000/ws/payments

# API Base URL
VITE_API_BASE_URL=http://localhost:8000
```

### Store Configuration

The payment store uses localStorage for persistence with the following configuration:

```typescript
{
  name: 'payment-store',
  storage: createJSONStorage(() => localStorage),
  partialize: (state) => ({
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
```

## Error Handling

The system includes comprehensive error handling:

1. **API Errors** - Handled with user-friendly messages
2. **WebSocket Errors** - Automatic reconnection with backoff
3. **Offline Errors** - Actions queued for later sync
4. **Network Errors** - Graceful degradation and retry logic

## Performance Considerations

1. **Persistence** - Only essential data is persisted to localStorage
2. **WebSocket** - Heartbeat mechanism prevents connection drops
3. **Offline Sync** - Actions are batched and synced efficiently
4. **Memory Management** - Old actions are automatically cleaned up

## Testing

The system is designed to be easily testable:

```typescript
import { renderHook } from '@testing-library/react';
import { usePayment } from '../hooks/usePayment';

test('should handle credit consumption', () => {
  const { result } = renderHook(() => usePayment());
  
  const success = result.current.handleGeneration(1);
  expect(success).toBe(true);
});
```

## Security Considerations

1. **Token Management** - Firebase tokens are automatically included in API calls
2. **WebSocket Auth** - Authentication tokens are sent on connection
3. **Action Validation** - Offline actions are validated before sync
4. **Error Sanitization** - Sensitive information is not exposed in error messages

## Migration Guide

To integrate this payment system into existing components:

1. Wrap your app with `PaymentProvider`
2. Replace direct API calls with `usePayment` hook
3. Use `PaymentStateManager` for automatic state management
4. Add `UpgradePrompt` and `CreditWarning` components as needed

## Troubleshooting

### Common Issues

1. **WebSocket Connection Fails**
   - Check `VITE_WS_URL` environment variable
   - Verify backend WebSocket endpoint is running
   - Check network connectivity

2. **Payment Data Not Loading**
   - Verify user is authenticated
   - Check API endpoint availability
   - Review browser console for errors

3. **Offline Actions Not Syncing**
   - Check `offlineSyncService` status
   - Verify action types are supported
   - Review localStorage for pending actions

### Debug Mode

Enable debug logging by setting:

```typescript
localStorage.setItem('payment-debug', 'true');
```

This will log all payment store actions and WebSocket messages to the console.



