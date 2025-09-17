import React, { useState, useEffect } from 'react';
import { Button, Banner, Spinner } from './UI';
import { paymentApi, handleApiError } from '../api/client';
import { CreditBalance } from '../types';

interface UpgradePromptProps {
  threshold?: number; // Percentage threshold to show prompt (default: 75)
  onUpgrade?: () => void;
  onDismiss?: () => void;
  className?: string;
  variant?: 'banner' | 'modal' | 'inline';
}

export function UpgradePrompt({ 
  threshold = 75, 
  onUpgrade, 
  onDismiss,
  className = "",
  variant = 'banner'
}: UpgradePromptProps) {
  const [balance, setBalance] = useState<CreditBalance | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [dismissed, setDismissed] = useState(false);

  useEffect(() => {
    loadBalance();
  }, []);

  const loadBalance = async () => {
    try {
      setLoading(true);
      setError(null);
      const balanceData = await paymentApi.getCreditBalance();
      setBalance(balanceData);
    } catch (err) {
      setError(handleApiError(err));
    } finally {
      setLoading(false);
    }
  };

  const getUsagePercentage = () => {
    if (!balance || balance.total_credits === 0) return 0;
    return Math.round((balance.used_credits / balance.total_credits) * 100);
  };

  const shouldShowPrompt = () => {
    if (dismissed || !balance) return false;
    return getUsagePercentage() >= threshold;
  };

  const getPromptType = () => {
    const percentage = getUsagePercentage();
    if (percentage >= 95) return 'critical';
    if (percentage >= 85) return 'warning';
    return 'info';
  };

  const getPromptMessage = () => {
    const percentage = getUsagePercentage();
    const remaining = balance?.current_credits || 0;
    
    if (percentage >= 95) {
      return `You're almost out of credits! Only ${remaining} credits remaining.`;
    } else if (percentage >= 85) {
      return `You've used ${percentage}% of your credits. Consider upgrading your plan.`;
    } else {
      return `You've used ${percentage}% of your credits. Upgrade for more capacity.`;
    }
  };

  const getPromptTitle = () => {
    const type = getPromptType();
    switch (type) {
      case 'critical': return 'Low Credits Alert';
      case 'warning': return 'Credit Usage Warning';
      default: return 'Upgrade Recommendation';
    }
  };

  const handleUpgrade = () => {
    if (onUpgrade) {
      onUpgrade();
    } else {
      window.location.href = '/pricing';
    }
  };

  const handleDismiss = () => {
    setDismissed(true);
    if (onDismiss) {
      onDismiss();
    }
  };

  if (loading) {
    return (
      <div className={`flex justify-center items-center py-4 ${className}`}>
        <Spinner size="sm" />
      </div>
    );
  }

  if (error || !shouldShowPrompt()) {
    return null;
  }

  const promptType = getPromptType();
  const title = getPromptTitle();
  const message = getPromptMessage();

  if (variant === 'modal') {
    return (
      <div className={`fixed inset-0 bg-black/50 flex items-center justify-center z-50 ${className}`}>
        <div className="bg-gray-900 rounded-xl border border-glass-border p-6 max-w-md mx-4 backdrop-blur-sm">
          <div className="text-center mb-6">
            <div className="text-4xl mb-4">
              {promptType === 'critical' ? '🚨' : promptType === 'warning' ? '⚠️' : '💡'}
            </div>
            <h3 className="text-xl font-bold text-white mb-2">{title}</h3>
            <p className="text-gray-400">{message}</p>
          </div>

          <div className="space-y-3">
            <Button
              onClick={handleUpgrade}
              variant="primary"
              className="w-full"
              glowing
            >
              {promptType === 'critical' ? 'Get More Credits Now' : 'Upgrade Plan'}
            </Button>
            
            <Button
              onClick={handleDismiss}
              variant="tertiary"
              className="w-full"
            >
              Dismiss
            </Button>
          </div>
        </div>
      </div>
    );
  }

  if (variant === 'inline') {
    return (
      <div className={`bg-white/5 rounded-lg border border-glass-border p-4 ${className}`}>
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="text-2xl">
              {promptType === 'critical' ? '🚨' : promptType === 'warning' ? '⚠️' : '💡'}
            </div>
            <div>
              <div className="text-white font-semibold">{title}</div>
              <div className="text-sm text-gray-400">{message}</div>
            </div>
          </div>
          
          <div className="flex items-center space-x-2">
            <Button
              onClick={handleUpgrade}
              variant="primary"
              size="sm"
            >
              {promptType === 'critical' ? 'Get Credits' : 'Upgrade'}
            </Button>
            <Button
              onClick={handleDismiss}
              variant="tertiary"
              size="sm"
            >
              ×
            </Button>
          </div>
        </div>
      </div>
    );
  }

  // Default banner variant
  return (
    <Banner 
      type={promptType === 'critical' ? 'error' : promptType === 'warning' ? 'info' : 'info'}
      className={`${className}`}
    >
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="text-xl">
            {promptType === 'critical' ? '🚨' : promptType === 'warning' ? '⚠️' : '💡'}
          </div>
          <div>
            <div className="font-semibold">{title}</div>
            <div className="text-sm opacity-90">{message}</div>
          </div>
        </div>
        
        <div className="flex items-center space-x-2">
          <Button
            onClick={handleUpgrade}
            variant="primary"
            size="sm"
          >
            {promptType === 'critical' ? 'Get Credits' : 'Upgrade'}
          </Button>
          <Button
            onClick={handleDismiss}
            variant="tertiary"
            size="sm"
          >
            Dismiss
          </Button>
        </div>
      </div>
    </Banner>
  );
}

// Hook for using upgrade prompt logic
export function useUpgradePrompt(threshold = 75) {
  const [balance, setBalance] = useState<CreditBalance | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadBalance = async () => {
      try {
        setLoading(true);
        const balanceData = await paymentApi.getCreditBalance();
        setBalance(balanceData);
      } catch (err) {
        console.error('Failed to load balance:', err);
      } finally {
        setLoading(false);
      }
    };

    loadBalance();
  }, []);

  const getUsagePercentage = () => {
    if (!balance || balance.total_credits === 0) return 0;
    return Math.round((balance.used_credits / balance.total_credits) * 100);
  };

  const shouldShowPrompt = getUsagePercentage() >= threshold;
  const promptType = shouldShowPrompt ? 
    (getUsagePercentage() >= 95 ? 'critical' : getUsagePercentage() >= 85 ? 'warning' : 'info') : 
    null;

  return {
    balance,
    loading,
    usagePercentage: getUsagePercentage(),
    shouldShowPrompt,
    promptType,
    refreshBalance: () => {
      setLoading(true);
      paymentApi.getCreditBalance()
        .then(setBalance)
        .catch(console.error)
        .finally(() => setLoading(false));
    }
  };
}



