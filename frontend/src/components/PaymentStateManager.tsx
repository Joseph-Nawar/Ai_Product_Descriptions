import React, { useEffect, ReactNode } from 'react';
import { usePayment } from '../hooks/usePayment';
import { useAuth } from '../auth/AuthProvider';

interface PaymentStateManagerProps {
  children: ReactNode;
  autoRefresh?: boolean;
  refreshInterval?: number; // in milliseconds
  showUpgradePrompt?: boolean;
  showCreditWarning?: boolean;
  creditWarningThreshold?: number;
}

/**
 * Component that manages payment state and provides automatic updates
 */
export const PaymentStateManager: React.FC<PaymentStateManagerProps> = ({
  children,
  autoRefresh = true,
  refreshInterval = 60000, // 1 minute
  showUpgradePrompt: enableUpgradePrompt = true,
  showCreditWarning: enableCreditWarning = true,
  creditWarningThreshold = 10
}) => {
  const { user } = useAuth();
  const {
    refreshPaymentData,
    setShowUpgradePrompt,
    setShowCreditWarning,
    setCreditWarningThreshold,
    creditBalance,
    currentSubscription,
    showUpgradePrompt: currentUpgradePrompt,
    showCreditWarning: currentCreditWarning
  } = usePayment();

  // Set credit warning threshold
  useEffect(() => {
    setCreditWarningThreshold(creditWarningThreshold);
  }, [creditWarningThreshold, setCreditWarningThreshold]);

  // Auto-refresh payment data when user is authenticated
  useEffect(() => {
    if (!user || !autoRefresh) return;

    const interval = setInterval(() => {
      refreshPaymentData();
    }, refreshInterval);

    return () => clearInterval(interval);
  }, [user, autoRefresh, refreshInterval, refreshPaymentData]);

  // Check for upgrade prompt conditions
  useEffect(() => {
    if (!enableUpgradePrompt) return;

    const shouldShow = Boolean(
      !currentSubscription || 
      currentSubscription.status === 'cancelled' ||
      (creditBalance && creditBalance.current_credits < 5)
    );

    setShowUpgradePrompt(shouldShow);
  }, [
    enableUpgradePrompt,
    currentSubscription,
    creditBalance,
    setShowUpgradePrompt
  ]);

  // Check for credit warning conditions
  useEffect(() => {
    if (!enableCreditWarning || !creditBalance) return;

    const shouldShow = creditBalance.current_credits <= creditWarningThreshold;
    setShowCreditWarning(shouldShow);
  }, [
    enableCreditWarning,
    creditBalance,
    creditWarningThreshold,
    setShowCreditWarning
  ]);

  return <>{children}</>;
};

/**
 * Component that shows upgrade prompt when conditions are met
 */
export const UpgradePrompt: React.FC<{
  onUpgrade?: () => void;
  onDismiss?: () => void;
  className?: string;
}> = ({ onUpgrade, onDismiss, className = '' }) => {
  const { showUpgradePrompt: currentUpgradePrompt, setShowUpgradePrompt, getUpgradeReason } = usePayment();

  if (!currentUpgradePrompt) return null;

  const handleDismiss = () => {
    setShowUpgradePrompt(false);
    onDismiss?.();
  };

  const handleUpgrade = () => {
    onUpgrade?.();
  };

  return (
    <div className={`bg-gradient-to-r from-blue-500 to-purple-600 text-white p-4 rounded-lg shadow-lg ${className}`}>
      <div className="flex items-center justify-between">
        <div className="flex-1">
          <h3 className="font-semibold text-lg mb-1">Upgrade Your Plan</h3>
          <p className="text-blue-100">{getUpgradeReason()}</p>
        </div>
        <div className="flex space-x-2 ml-4">
          <button
            onClick={handleDismiss}
            className="px-3 py-1 text-blue-200 hover:text-white transition-colors"
          >
            Dismiss
          </button>
          <button
            onClick={handleUpgrade}
            className="px-4 py-2 bg-white text-blue-600 rounded-md hover:bg-blue-50 transition-colors font-medium"
          >
            Upgrade Now
          </button>
        </div>
      </div>
    </div>
  );
};

/**
 * Component that shows credit warning when credits are low
 */
export const CreditWarning: React.FC<{
  onPurchase?: () => void;
  onDismiss?: () => void;
  className?: string;
}> = ({ onPurchase, onDismiss, className = '' }) => {
  const { 
    showCreditWarning: currentCreditWarning, 
    setShowCreditWarning, 
    creditBalance,
    creditWarningThreshold 
  } = usePayment();

  if (!currentCreditWarning || !creditBalance) return null;

  const handleDismiss = () => {
    setShowCreditWarning(false);
    onDismiss?.();
  };

  const handlePurchase = () => {
    onPurchase?.();
  };

  return (
    <div className={`bg-yellow-500 text-white p-4 rounded-lg shadow-lg ${className}`}>
      <div className="flex items-center justify-between">
        <div className="flex-1">
          <h3 className="font-semibold text-lg mb-1">Low Credits Warning</h3>
          <p className="text-yellow-100">
            You have {creditBalance.current_credits} credits remaining. 
            Consider purchasing more credits or upgrading your plan.
          </p>
        </div>
        <div className="flex space-x-2 ml-4">
          <button
            onClick={handleDismiss}
            className="px-3 py-1 text-yellow-200 hover:text-white transition-colors"
          >
            Dismiss
          </button>
          <button
            onClick={handlePurchase}
            className="px-4 py-2 bg-white text-yellow-600 rounded-md hover:bg-yellow-50 transition-colors font-medium"
          >
            Buy Credits
          </button>
        </div>
      </div>
    </div>
  );
};

/**
 * Component that shows payment loading states
 */
export const PaymentLoading: React.FC<{
  children: ReactNode;
  fallback?: ReactNode;
  className?: string;
}> = ({ children, fallback, className = '' }) => {
  const { isLoading } = usePayment();

  if (isLoading) {
    return (
      <div className={`flex items-center justify-center p-4 ${className}`}>
        {fallback || (
          <div className="flex items-center space-x-2">
            <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-500"></div>
            <span className="text-gray-600">Loading payment data...</span>
          </div>
        )}
      </div>
    );
  }

  return <>{children}</>;
};

/**
 * Component that shows payment errors
 */
export const PaymentError: React.FC<{
  children: ReactNode;
  onRetry?: () => void;
  className?: string;
}> = ({ children, onRetry, className = '' }) => {
  const { hasError, subscriptionError, creditError, usageError, refreshPaymentData } = usePayment();

  if (!hasError) return <>{children}</>;

  const handleRetry = () => {
    refreshPaymentData();
    onRetry?.();
  };

  const errors = [subscriptionError, creditError, usageError].filter(Boolean);

  return (
    <div className={`bg-red-50 border border-red-200 rounded-lg p-4 ${className}`}>
      <div className="flex items-start space-x-3">
        <div className="flex-shrink-0">
          <svg className="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
          </svg>
        </div>
        <div className="flex-1">
          <h3 className="text-sm font-medium text-red-800">Payment Error</h3>
          <div className="mt-2 text-sm text-red-700">
            {errors.map((error, index) => (
              <p key={index}>{error}</p>
            ))}
          </div>
          <div className="mt-3">
            <button
              onClick={handleRetry}
              className="text-sm bg-red-100 hover:bg-red-200 text-red-800 px-3 py-1 rounded-md transition-colors"
            >
              Retry
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

// Export all components
export {
  PaymentStateManager as PaymentStateManagerComponent,
  UpgradePrompt as UpgradePromptComponent,
  CreditWarning as CreditWarningComponent,
  PaymentLoading as PaymentLoadingComponent,
  PaymentError as PaymentErrorComponent
};
