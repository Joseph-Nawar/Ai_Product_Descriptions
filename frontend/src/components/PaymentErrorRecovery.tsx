// frontend/src/components/PaymentErrorRecovery.tsx
import React, { useState, useEffect } from 'react';
import { AlertTriangle, RefreshCw, ArrowLeft, HelpCircle, Shield } from 'lucide-react';
import { paymentSecurity } from '../services/paymentSecurity';
import { secureTokens } from '../services/secureTokens';

interface PaymentErrorRecoveryProps {
  error: {
    type: 'network' | 'validation' | 'payment_failed' | 'security' | 'rate_limit' | 'unknown';
    message: string;
    code?: string;
    correlationId?: string;
    retryable?: boolean;
  };
  onRetry?: () => Promise<void>;
  onCancel: () => void;
  onContactSupport?: () => void;
  maxRetries?: number;
  currentRetries?: number;
}

export const PaymentErrorRecovery: React.FC<PaymentErrorRecoveryProps> = ({
  error,
  onRetry,
  onCancel,
  onContactSupport,
  maxRetries = 3,
  currentRetries = 0
}) => {
  const [isRetrying, setIsRetrying] = useState(false);
  const [retryCountdown, setRetryCountdown] = useState(0);
  const [showDetails, setShowDetails] = useState(false);

  useEffect(() => {
    // Log error for security monitoring
    paymentSecurity.logSecurityEvent({
      type: 'payment_attempt',
      data: {
        errorType: error.type,
        errorMessage: error.message,
        errorCode: error.code,
        correlationId: error.correlationId,
        retryCount: currentRetries
      },
      severity: error.type === 'security' ? 'high' : 'medium'
    });
  }, [error, currentRetries]);

  const handleRetry = async () => {
    if (!onRetry || currentRetries >= maxRetries) return;

    setIsRetrying(true);
    setRetryCountdown(3);

    // Countdown before retry
    const countdown = setInterval(() => {
      setRetryCountdown(prev => {
        if (prev <= 1) {
          clearInterval(countdown);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    // Wait for countdown
    await new Promise(resolve => setTimeout(resolve, 3000));

    try {
      await onRetry();
    } catch (retryError) {
      console.error('Retry failed:', retryError);
    } finally {
      setIsRetrying(false);
      clearInterval(countdown);
    }
  };

  const getErrorIcon = () => {
    switch (error.type) {
      case 'security':
        return <Shield className="h-8 w-8 text-red-600" />;
      case 'rate_limit':
        return <AlertTriangle className="h-8 w-8 text-yellow-600" />;
      default:
        return <AlertTriangle className="h-8 w-8 text-red-600" />;
    }
  };

  const getErrorTitle = () => {
    switch (error.type) {
      case 'network':
        return 'Network Connection Issue';
      case 'validation':
        return 'Payment Information Invalid';
      case 'payment_failed':
        return 'Payment Processing Failed';
      case 'security':
        return 'Security Verification Failed';
      case 'rate_limit':
        return 'Too Many Requests';
      default:
        return 'Payment Error';
    }
  };

  const getErrorDescription = () => {
    switch (error.type) {
      case 'network':
        return 'We encountered a network issue while processing your payment. Please check your internet connection and try again.';
      case 'validation':
        return 'There was an issue with the payment information provided. Please review your details and try again.';
      case 'payment_failed':
        return 'Your payment could not be processed. This might be due to insufficient funds, card restrictions, or other payment method issues.';
      case 'security':
        return 'Our security systems detected an issue with this transaction. For your protection, the payment was not processed.';
      case 'rate_limit':
        return 'You have made too many payment attempts in a short time. Please wait a moment before trying again.';
      default:
        return 'An unexpected error occurred while processing your payment. Please try again or contact support if the issue persists.';
    }
  };

  const getRecoveryOptions = () => {
    const options = [];

    // Retry option
    if (error.retryable !== false && onRetry && currentRetries < maxRetries) {
      options.push({
        key: 'retry',
        label: isRetrying ? `Retrying in ${retryCountdown}s...` : 'Try Again',
        action: handleRetry,
        primary: true,
        disabled: isRetrying,
        icon: <RefreshCw className={`h-4 w-4 ${isRetrying ? 'animate-spin' : ''}`} />
      });
    }

    // Contact support option
    if (onContactSupport) {
      options.push({
        key: 'support',
        label: 'Contact Support',
        action: onContactSupport,
        primary: false,
        icon: <HelpCircle className="h-4 w-4" />
      });
    }

    // Cancel/Go back option
    options.push({
      key: 'cancel',
      label: 'Go Back',
      action: onCancel,
      primary: false,
      icon: <ArrowLeft className="h-4 w-4" />
    });

    return options;
  };

  const shouldShowRetryInfo = () => {
    return error.retryable !== false && onRetry && maxRetries > 1;
  };

  return (
    <div className="max-w-md mx-auto bg-white rounded-lg shadow-lg p-6">
      {/* Error Icon and Title */}
      <div className="text-center mb-6">
        <div className="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-red-50 mb-4">
          {getErrorIcon()}
        </div>
        <h2 className="text-xl font-semibold text-gray-900 mb-2">
          {getErrorTitle()}
        </h2>
        <p className="text-gray-600 text-sm">
          {getErrorDescription()}
        </p>
      </div>

      {/* Error Details (Collapsible) */}
      <div className="mb-6">
        <button
          onClick={() => setShowDetails(!showDetails)}
          className="text-sm text-blue-600 hover:text-blue-700 font-medium"
        >
          {showDetails ? 'Hide' : 'Show'} technical details
        </button>
        
        {showDetails && (
          <div className="mt-3 p-3 bg-gray-50 rounded-lg text-xs font-mono">
            <div className="space-y-1">
              <div><strong>Error Type:</strong> {error.type}</div>
              <div><strong>Message:</strong> {error.message}</div>
              {error.code && <div><strong>Code:</strong> {error.code}</div>}
              {error.correlationId && <div><strong>Correlation ID:</strong> {error.correlationId}</div>}
              <div><strong>Retry Count:</strong> {currentRetries}/{maxRetries}</div>
              <div><strong>Timestamp:</strong> {new Date().toISOString()}</div>
            </div>
          </div>
        )}
      </div>

      {/* Retry Information */}
      {shouldShowRetryInfo() && (
        <div className="mb-6 p-3 bg-blue-50 rounded-lg">
          <div className="text-sm text-blue-800">
            <strong>Retry Information:</strong>
            <div className="mt-1">
              Attempt {currentRetries + 1} of {maxRetries + 1}
            </div>
            {currentRetries < maxRetries && (
              <div className="text-xs mt-1 text-blue-600">
                You can try {maxRetries - currentRetries} more time{maxRetries - currentRetries !== 1 ? 's' : ''}
              </div>
            )}
          </div>
        </div>
      )}

      {/* Security Notice for Security Errors */}
      {error.type === 'security' && (
        <div className="mb-6 p-3 bg-red-50 border border-red-200 rounded-lg">
          <div className="flex items-start space-x-2">
            <Shield className="h-4 w-4 text-red-600 mt-0.5" />
            <div className="text-sm text-red-800">
              <strong>Security Notice:</strong> This transaction was blocked for your protection. 
              If you believe this is an error, please contact our support team with the correlation ID above.
            </div>
          </div>
        </div>
      )}

      {/* Rate Limit Notice */}
      {error.type === 'rate_limit' && (
        <div className="mb-6 p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
          <div className="text-sm text-yellow-800">
            <strong>Rate Limit Notice:</strong> Please wait a few minutes before attempting another payment. 
            This helps us maintain security and service quality.
          </div>
        </div>
      )}

      {/* Recovery Actions */}
      <div className="space-y-3">
        {getRecoveryOptions().map((option) => (
          <button
            key={option.key}
            onClick={option.action}
            disabled={option.disabled}
            className={`w-full px-4 py-2 rounded-lg font-medium text-sm flex items-center justify-center space-x-2 transition-colors ${
              option.primary
                ? 'bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed'
            }`}
          >
            {option.icon}
            <span>{option.label}</span>
          </button>
        ))}
      </div>

      {/* Help Text */}
      <div className="mt-6 text-center">
        <p className="text-xs text-gray-500">
          If you continue to experience issues, please contact our support team. 
          Include the correlation ID for faster assistance.
        </p>
      </div>
    </div>
  );
};
