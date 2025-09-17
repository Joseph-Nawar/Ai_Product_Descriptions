// frontend/src/components/PaymentConfirmationDialog.tsx
import React, { useState, useEffect } from 'react';
import { AlertCircle, CheckCircle, XCircle, Shield, CreditCard, Clock } from 'lucide-react';
import { paymentSecurity } from '../services/paymentSecurity';
import { secureTokens } from '../services/secureTokens';

interface PaymentData {
  planId: string;
  planName: string;
  amount: number;
  currency: string;
  features: string[];
  billingCycle: string;
}

interface PaymentConfirmationDialogProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: (confirmationToken: string) => Promise<void>;
  paymentData: PaymentData;
  userInfo: {
    userId: string;
    email: string;
    currentPlan?: string;
  };
  loading?: boolean;
  error?: string;
}

export const PaymentConfirmationDialog: React.FC<PaymentConfirmationDialogProps> = ({
  isOpen,
  onClose,
  onConfirm,
  paymentData,
  userInfo,
  loading = false,
  error
}) => {
  const [confirmationToken, setConfirmationToken] = useState<string>('');
  const [securityChecks, setSecurityChecks] = useState({
    planValidation: false,
    subscriptionStatus: false,
    fraudCheck: false,
    userVerification: false
  });
  const [showDetails, setShowDetails] = useState(false);
  const [timeRemaining, setTimeRemaining] = useState(30);

  useEffect(() => {
    if (isOpen) {
      performSecurityChecks();
      startCountdown();
    }
  }, [isOpen]);

  const performSecurityChecks = async () => {
    // Validate plan
    const planValidation = paymentSecurity.validateCheckoutRequest({
      plan_id: paymentData.planId,
      success_url: `${window.location.origin}/payment/success`,
      cancel_url: `${window.location.origin}/payment/cancel`
    });

    setSecurityChecks(prev => ({
      ...prev,
      planValidation: planValidation.isValid
    }));

    // Check subscription status
    const subscriptionCheck = paymentSecurity.validateSubscriptionStatus({
      subscription_tier: userInfo.currentPlan || 'free',
      status: 'active'
    });

    setSecurityChecks(prev => ({
      ...prev,
      subscriptionStatus: subscriptionCheck.canProceed
    }));

    // Fraud detection
    const fraudCheck = paymentSecurity.detectSuspiciousActivity({
      newUser: !userInfo.currentPlan || userInfo.currentPlan === 'free',
      largeAmount: paymentData.amount
    });

    setSecurityChecks(prev => ({
      ...prev,
      fraudCheck: !fraudCheck.isSuspicious
    }));

    // User verification (basic check)
    setSecurityChecks(prev => ({
      ...prev,
      userVerification: !!userInfo.email && !!userInfo.userId
    }));

    // Generate confirmation token if all checks pass
    if (planValidation.isValid && subscriptionCheck.canProceed && !fraudCheck.isSuspicious) {
      const token = secureTokens.createPaymentConfirmationToken({
        planId: paymentData.planId,
        amount: paymentData.amount,
        userId: userInfo.userId
      });
      setConfirmationToken(token);
    }

    // Log security check
    paymentSecurity.logSecurityEvent({
      type: 'security_check',
      data: {
        checks: {
          planValidation: planValidation.isValid,
          subscriptionStatus: subscriptionCheck.canProceed,
          fraudCheck: !fraudCheck.isSuspicious,
          userVerification: !!userInfo.email
        },
        paymentData: {
          planId: paymentData.planId,
          amount: paymentData.amount
        }
      },
      severity: 'medium'
    });
  };

  const startCountdown = () => {
    const interval = setInterval(() => {
      setTimeRemaining(prev => {
        if (prev <= 1) {
          clearInterval(interval);
          onClose();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval);
  };

  const handleConfirm = async () => {
    if (!confirmationToken) {
      paymentSecurity.logSecurityEvent({
        type: 'security_check',
        data: { error: 'No confirmation token available' },
        severity: 'high'
      });
      return;
    }

    // Validate token before proceeding
    const tokenValidation = secureTokens.validatePaymentConfirmationToken(
      confirmationToken,
      { planId: paymentData.planId, userId: userInfo.userId }
    );

    if (!tokenValidation.isValid) {
      paymentSecurity.logSecurityEvent({
        type: 'security_check',
        data: { 
          error: 'Invalid confirmation token',
          reason: tokenValidation.reason 
        },
        severity: 'high'
      });
      return;
    }

    try {
      await onConfirm(confirmationToken);
    } catch (error) {
      paymentSecurity.logSecurityEvent({
        type: 'payment_attempt',
        data: { 
          error: error instanceof Error ? error.message : 'Unknown error',
          planId: paymentData.planId 
        },
        severity: 'high'
      });
    }
  };

  const allChecksPass = Object.values(securityChecks).every(Boolean);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-xl max-w-md w-full mx-4 max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b">
          <div className="flex items-center space-x-2">
            <Shield className="h-6 w-6 text-blue-600" />
            <h2 className="text-xl font-semibold text-gray-900">
              Confirm Payment
            </h2>
          </div>
          <div className="flex items-center space-x-2 text-sm text-gray-500">
            <Clock className="h-4 w-4" />
            <span>{timeRemaining}s</span>
          </div>
        </div>

        {/* Security Status */}
        <div className="p-6 border-b">
          <h3 className="text-sm font-medium text-gray-900 mb-3">Security Verification</h3>
          <div className="space-y-2">
            {Object.entries(securityChecks).map(([check, passed]) => (
              <div key={check} className="flex items-center space-x-2">
                {passed ? (
                  <CheckCircle className="h-4 w-4 text-green-600" />
                ) : (
                  <XCircle className="h-4 w-4 text-red-600" />
                )}
                <span className={`text-sm ${passed ? 'text-green-700' : 'text-red-700'}`}>
                  {check.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase())}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Payment Details */}
        <div className="p-6">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Payment Summary</h3>
          
          <div className="bg-gray-50 rounded-lg p-4 mb-4">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm font-medium text-gray-600">Plan:</span>
              <span className="text-sm text-gray-900">{paymentData.planName}</span>
            </div>
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm font-medium text-gray-600">Amount:</span>
              <span className="text-sm text-gray-900">
                {paymentData.currency} {paymentData.amount.toFixed(2)}
              </span>
            </div>
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm font-medium text-gray-600">Billing:</span>
              <span className="text-sm text-gray-900">{paymentData.billingCycle}</span>
            </div>
            {userInfo.currentPlan && userInfo.currentPlan !== 'free' && (
              <div className="flex items-center justify-between">
                <span className="text-sm font-medium text-gray-600">Current Plan:</span>
                <span className="text-sm text-gray-900 capitalize">{userInfo.currentPlan}</span>
              </div>
            )}
          </div>

          {/* Features */}
          <button
            onClick={() => setShowDetails(!showDetails)}
            className="text-blue-600 text-sm font-medium mb-2 hover:text-blue-700"
          >
            {showDetails ? 'Hide' : 'Show'} plan features
          </button>
          
          {showDetails && (
            <div className="bg-blue-50 rounded-lg p-3 mb-4">
              <h4 className="text-sm font-medium text-blue-900 mb-2">Included Features:</h4>
              <ul className="text-sm text-blue-800 space-y-1">
                {paymentData.features.map((feature, index) => (
                  <li key={index} className="flex items-center space-x-2">
                    <CheckCircle className="h-3 w-3 text-blue-600" />
                    <span>{feature}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Error Display */}
          {error && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-3 mb-4">
              <div className="flex items-center space-x-2">
                <AlertCircle className="h-4 w-4 text-red-600" />
                <span className="text-sm text-red-700">{error}</span>
              </div>
            </div>
          )}

          {/* Security Warning */}
          {!allChecksPass && (
            <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3 mb-4">
              <div className="flex items-center space-x-2">
                <AlertCircle className="h-4 w-4 text-yellow-600" />
                <span className="text-sm text-yellow-700">
                  Security verification failed. Please try again or contact support.
                </span>
              </div>
            </div>
          )}
        </div>

        {/* Actions */}
        <div className="flex space-x-3 p-6 border-t bg-gray-50">
          <button
            onClick={onClose}
            className="flex-1 px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            disabled={loading}
          >
            Cancel
          </button>
          <button
            onClick={handleConfirm}
            disabled={loading || !allChecksPass || !confirmationToken}
            className="flex-1 px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center space-x-2"
          >
            {loading ? (
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
            ) : (
              <>
                <CreditCard className="h-4 w-4" />
                <span>Confirm Payment</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
