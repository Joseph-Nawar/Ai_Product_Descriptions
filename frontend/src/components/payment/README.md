# Payment UI Components

This directory contains comprehensive payment UI components for the AI Product Descriptions application, integrated with Lemon Squeezy for subscription management and payments.

## Components Overview

### 1. PricingPlans.tsx
Displays subscription plans with features comparison and handles plan selection.

**Features:**
- Monthly/Yearly billing toggle with savings indicator
- Plan comparison with features list
- Popular plan highlighting
- Current plan indication
- Lemon Squeezy checkout integration
- Responsive design with glassmorphism styling

**Props:**
- `onPlanSelect?: (plan: SubscriptionPlan) => void` - Callback when a plan is selected
- `currentPlanId?: string` - ID of the user's current plan
- `className?: string` - Additional CSS classes

**Usage:**
```tsx
import { PricingPlans } from './components/payment';

<PricingPlans 
  currentPlanId={userSubscription?.plan_id}
  onPlanSelect={(plan) => console.log('Selected plan:', plan)}
/>
```

### 2. CheckoutForm.tsx
Handles Lemon Squeezy checkout session creation and redirection.

**Features:**
- Plan summary display
- Custom success/cancel URL configuration
- Checkout session creation
- Secure payment redirect
- Loading states and error handling

**Props:**
- `plan: SubscriptionPlan` - The plan to purchase
- `onSuccess?: (session: CheckoutSession) => void` - Success callback
- `onCancel?: () => void` - Cancel callback
- `className?: string` - Additional CSS classes

**Usage:**
```tsx
import { CheckoutForm } from './components/payment';

<CheckoutForm 
  plan={selectedPlan}
  onSuccess={(session) => console.log('Checkout created:', session)}
  onCancel={() => setShowCheckout(false)}
/>
```

### 3. BillingDashboard.tsx
Comprehensive subscription and billing management interface.

**Features:**
- Current subscription overview
- Subscription management (cancel, reactivate, upgrade)
- Credit balance display
- Usage statistics
- Payment history
- Upgrade modal
- Real-time data updates

**Props:**
- `className?: string` - Additional CSS classes

**Usage:**
```tsx
import { BillingDashboard } from './components/payment';

<BillingDashboard />
```

### 4. CreditBalance.tsx
Displays current credit balance with usage statistics.

**Features:**
- Current credits display
- Usage percentage and progress bar
- Status indicators (low, moderate, good)
- Reset date information
- Low credit warnings
- Compact and full display modes

**Props:**
- `onRefresh?: () => void` - Refresh callback
- `showPurchaseButton?: boolean` - Show purchase/upgrade buttons
- `className?: string` - Additional CSS classes
- `compact?: boolean` - Compact display mode

**Usage:**
```tsx
import { CreditBalance } from './components/payment';

<CreditBalance 
  compact={true}
  showPurchaseButton={true}
  onRefresh={() => console.log('Balance refreshed')}
/>
```

### 5. UsageStats.tsx
Shows detailed usage analytics and statistics.

**Features:**
- Total generations count
- Daily and monthly usage
- Average usage trends
- Usage insights and recommendations
- Visual charts and progress bars
- Activity trend analysis

**Props:**
- `onRefresh?: () => void` - Refresh callback
- `className?: string` - Additional CSS classes
- `showCharts?: boolean` - Show visual charts

**Usage:**
```tsx
import { UsageStats } from './components/payment';

<UsageStats 
  showCharts={true}
  onRefresh={() => console.log('Stats refreshed')}
/>
```

### 6. PaymentHistory.tsx
Displays payment and transaction history.

**Features:**
- Transaction list with pagination
- Status indicators (completed, pending, failed, refunded)
- Transaction type icons
- Amount formatting
- Load more functionality
- Transaction summary statistics

**Props:**
- `onRefresh?: () => void` - Refresh callback
- `className?: string` - Additional CSS classes
- `itemsPerPage?: number` - Items per page (default: 10)

**Usage:**
```tsx
import { PaymentHistory } from './components/payment';

<PaymentHistory 
  itemsPerPage={20}
  onRefresh={() => console.log('History refreshed')}
/>
```

### 7. UpgradePrompt.tsx
Shows upgrade prompts when credits are low.

**Features:**
- Configurable threshold levels
- Multiple display variants (banner, modal, inline)
- Critical, warning, and info states
- Dismissible prompts
- Custom upgrade actions

**Props:**
- `threshold?: number` - Usage percentage threshold (default: 75)
- `onUpgrade?: () => void` - Custom upgrade action
- `onDismiss?: () => void` - Dismiss callback
- `className?: string` - Additional CSS classes
- `variant?: 'banner' | 'modal' | 'inline'` - Display variant

**Usage:**
```tsx
import { UpgradePrompt } from './components/payment';

<UpgradePrompt 
  threshold={80}
  variant="banner"
  onUpgrade={() => window.location.href = '/pricing'}
/>
```

## Hook: useUpgradePrompt

A custom hook for managing upgrade prompt logic.

**Returns:**
- `balance: CreditBalance | null` - Current credit balance
- `loading: boolean` - Loading state
- `usagePercentage: number` - Current usage percentage
- `shouldShowPrompt: boolean` - Whether to show prompt
- `promptType: string | null` - Prompt type (critical, warning, info)
- `refreshBalance: () => void` - Function to refresh balance

**Usage:**
```tsx
import { useUpgradePrompt } from './components/payment';

const { shouldShowPrompt, promptType, refreshBalance } = useUpgradePrompt(75);
```

## API Integration

All components use the `paymentApi` object from `../api/client` which provides:

- `getPlans()` - Fetch subscription plans
- `getSubscription()` - Get user's current subscription
- `getCreditBalance()` - Get credit balance
- `getUsageStats()` - Get usage statistics
- `getPaymentHistory(page, limit)` - Get payment history
- `createCheckoutSession(variantId, successUrl, cancelUrl)` - Create checkout session
- `cancelSubscription(subscriptionId)` - Cancel subscription
- `reactivateSubscription(subscriptionId)` - Reactivate subscription
- `updateSubscription(subscriptionId, variantId)` - Update subscription
- `handleWebhook(webhookData)` - Handle webhook events

## Types

All payment-related types are defined in `../../types.ts`:

- `SubscriptionPlan` - Subscription plan structure
- `UserSubscription` - User's subscription details
- `CreditBalance` - Credit balance information
- `UsageStats` - Usage statistics
- `PaymentTransaction` - Payment transaction details
- `CheckoutSession` - Checkout session information
- `LemonSqueezyWebhook` - Webhook data structure

## Styling

All components use the existing UI design system with:
- Glassmorphism effects
- Gradient backgrounds
- Consistent color scheme
- Responsive design
- Loading states and animations
- Error handling with banners

## Error Handling

Components include comprehensive error handling:
- API error display with user-friendly messages
- Retry mechanisms
- Loading states
- Graceful fallbacks

## Security

- All API calls include authentication headers
- Secure payment redirects to Lemon Squeezy
- Input validation and sanitization
- CSRF protection through proper API integration

## Responsive Design

All components are fully responsive and work on:
- Desktop (1024px+)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)

## Accessibility

Components include:
- ARIA labels and roles
- Keyboard navigation support
- Screen reader compatibility
- High contrast support
- Focus management



