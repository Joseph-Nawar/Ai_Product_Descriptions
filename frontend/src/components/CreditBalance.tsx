import React, { useState, useEffect } from 'react';
import { Button, Banner, Spinner } from './UI';
import { paymentApi, handleApiError } from '../api/client';
import { CreditBalance as CreditBalanceType } from '../types';

interface CreditBalanceProps {
  onRefresh?: () => void;
  showPurchaseButton?: boolean;
  className?: string;
  compact?: boolean;
}

export function CreditBalance({ 
  onRefresh, 
  showPurchaseButton = true, 
  className = "",
  compact = false 
}: CreditBalanceProps) {
  const [balance, setBalance] = useState<CreditBalanceType | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);

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

  const handleRefresh = async () => {
    try {
      setRefreshing(true);
      await loadBalance();
      if (onRefresh) {
        onRefresh();
      }
    } finally {
      setRefreshing(false);
    }
  };

  const getUsagePercentage = () => {
    if (!balance || !balance.total_credits || balance.total_credits === 0) return 0;
    const usedCredits = balance.used_credits ?? 0;
    return Math.round((usedCredits / balance.total_credits) * 100);
  };

  const getStatusColor = () => {
    const percentage = getUsagePercentage();
    if (percentage >= 90) return 'text-red-400';
    if (percentage >= 75) return 'text-yellow-400';
    return 'text-emerald-400';
  };

  const getStatusText = () => {
    const percentage = getUsagePercentage();
    if (percentage >= 90) return 'Low Credits';
    if (percentage >= 75) return 'Moderate Usage';
    return 'Good Standing';
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  if (loading) {
    return (
      <div className={`flex justify-center items-center ${compact ? 'py-4' : 'py-8'} ${className}`}>
        <Spinner size="md" />
      </div>
    );
  }

  if (error) {
    return (
      <div className={className}>
        <Banner type="error">{error}</Banner>
        <div className="mt-4 text-center">
          <Button onClick={handleRefresh} variant="secondary" size="sm">
            Try Again
          </Button>
        </div>
      </div>
    );
  }

  if (!balance) {
    return (
      <div className={className}>
        <Banner type="error">Unable to load credit balance</Banner>
      </div>
    );
  }

  if (compact) {
    return (
      <div className={`bg-white/5 rounded-lg border border-glass-border p-4 ${className}`}>
        <div className="flex items-center justify-between">
          <div>
            <div className="text-sm text-gray-400">Credits</div>
            <div className="text-xl font-bold text-white">
              {(balance.current_credits ?? 0).toLocaleString()}
            </div>
          </div>
          <div className="text-right">
            <div className={`text-sm font-medium ${getStatusColor()}`}>
              {getStatusText()}
            </div>
            <div className="text-xs text-gray-400">
              {getUsagePercentage()}% used
            </div>
          </div>
        </div>
        
        <div className="mt-3">
          <div className="w-full bg-gray-700 rounded-full h-2">
            <div
              className={`h-2 rounded-full transition-all duration-300 ${
                getUsagePercentage() >= 90 ? 'bg-red-500' :
                getUsagePercentage() >= 75 ? 'bg-yellow-500' : 'bg-emerald-500'
              }`}
              style={{ width: `${getUsagePercentage()}%` }}
            />
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className={`bg-white/5 rounded-xl border border-glass-border p-6 backdrop-blur-sm ${className}`}>
      <div className="flex items-center justify-between mb-6">
        <h3 className="text-xl font-bold text-white">Credit Balance</h3>
        <Button
          onClick={handleRefresh}
          disabled={refreshing}
          variant="tertiary"
          size="sm"
        >
          {refreshing ? <Spinner size="sm" /> : 'Refresh'}
        </Button>
      </div>

      {/* Current Balance */}
      <div className="text-center mb-6">
        <div className="text-4xl font-bold text-primary mb-2">
          {(balance.current_credits ?? 0).toLocaleString()}
        </div>
        <div className="text-gray-400">Available Credits</div>
      </div>

      {/* Usage Statistics */}
      <div className="grid grid-cols-2 gap-4 mb-6">
        <div className="bg-white/5 rounded-lg p-4 text-center">
          <div className="text-2xl font-bold text-white">
            {(balance.used_credits ?? 0).toLocaleString()}
          </div>
          <div className="text-sm text-gray-400">Used</div>
        </div>
        <div className="bg-white/5 rounded-lg p-4 text-center">
          <div className="text-2xl font-bold text-white">
            {(balance.total_credits ?? 0).toLocaleString()}
          </div>
          <div className="text-sm text-gray-400">Total</div>
        </div>
      </div>

      {/* Usage Progress Bar */}
      <div className="mb-6">
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm text-gray-400">Usage</span>
          <span className={`text-sm font-medium ${getStatusColor()}`}>
            {getUsagePercentage()}% • {getStatusText()}
          </span>
        </div>
        <div className="w-full bg-gray-700 rounded-full h-3">
          <div
            className={`h-3 rounded-full transition-all duration-300 ${
              getUsagePercentage() >= 90 ? 'bg-red-500' :
              getUsagePercentage() >= 75 ? 'bg-yellow-500' : 'bg-emerald-500'
            }`}
            style={{ width: `${getUsagePercentage()}%` }}
          />
        </div>
      </div>

      {/* Reset Date */}
      {balance.reset_date && (
        <div className="text-center mb-6">
          <div className="text-sm text-gray-400">
            Credits reset on {formatDate(balance.reset_date)}
          </div>
        </div>
      )}

      {/* Low Credit Warning */}
      {getUsagePercentage() >= 75 && (
        <Banner 
          type={getUsagePercentage() >= 90 ? "error" : "info"} 
          className="mb-4"
        >
          {getUsagePercentage() >= 90 
            ? "You're running low on credits! Consider upgrading your plan or purchasing additional credits."
            : "You've used most of your credits. Consider upgrading your plan for more credits."
          }
        </Banner>
      )}

      {/* Action Buttons */}
      {showPurchaseButton && (
        <div className="space-y-3">
          <Button
            onClick={() => window.location.href = '/pricing'}
            variant="primary"
            className="w-full"
            glowing
          >
            {getUsagePercentage() >= 90 ? 'Get More Credits' : 'Upgrade Plan'}
          </Button>
          
          <Button
            onClick={() => window.location.href = '/billing'}
            variant="secondary"
            className="w-full"
          >
            Manage Subscription
          </Button>
        </div>
      )}
    </div>
  );
}



