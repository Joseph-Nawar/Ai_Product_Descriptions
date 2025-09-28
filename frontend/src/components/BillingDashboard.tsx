import React, { useState, useEffect } from 'react';
import { Button, Banner, Spinner } from './UI';
import { paymentApi, handleApiError } from '../api/client';
import { UserSubscription, SubscriptionPlan, CreditBalance, UsageStats as UsageStatsType } from '../types';
import { CreditBalance as CreditBalanceComponent } from './CreditBalance';
import { UsageStats } from './UsageStats';
import { PaymentHistory } from './PaymentHistory';
import { UpgradePrompt } from './UpgradePrompt';

interface BillingDashboardProps {
  className?: string;
}

export function BillingDashboard({ className = "" }: BillingDashboardProps) {
  const [subscription, setSubscription] = useState<UserSubscription | null>(null);
  const [plans, setPlans] = useState<SubscriptionPlan[]>([]);
  const [balance, setBalance] = useState<CreditBalance | null>(null);
  const [usageStats, setUsageStats] = useState<UsageStatsType | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [actionLoading, setActionLoading] = useState<string | null>(null);
  const [showUpgradeModal, setShowUpgradeModal] = useState(false);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      setLoading(true);
      setError(null);
      
      // Ensure authentication token is available before making API calls
      const { getIdToken } = await import('../auth/token');
      const token = await getIdToken();
      
      if (!token) {
        console.warn('No authentication token available, skipping API calls');
        setError('Authentication required. Please sign in and try again.');
        return;
      }
      
      // Sequential API calls to prevent database locking
      const subscriptionData = await paymentApi.getSubscription().catch(() => null);
      setSubscription(subscriptionData);
      
      const plansData = await paymentApi.getPlans();
      setPlans(plansData);
      
      const balanceData = await paymentApi.getCreditBalance();
      setBalance(balanceData);
      
      // TODO: Endpoint not yet implemented. Commented out to prevent 404s and rate limiting.
      // const usageData = await paymentApi.getUsageStats();
      // setUsageStats(usageData);
    } catch (err) {
      setError(handleApiError(err));
    } finally {
      setLoading(false);
    }
  };

  const handleCancelSubscription = async () => {
    if (!subscription) return;

    try {
      setActionLoading('cancel');
      await paymentApi.cancelSubscription(subscription.id);
      await loadDashboardData();
    } catch (err) {
      setError(handleApiError(err));
    } finally {
      setActionLoading(null);
    }
  };

  const handleReactivateSubscription = async () => {
    if (!subscription) return;

    try {
      setActionLoading('reactivate');
      await paymentApi.reactivateSubscription(subscription.id);
      await loadDashboardData();
    } catch (err) {
      setError(handleApiError(err));
    } finally {
      setActionLoading(null);
    }
  };

  const handleUpgradePlan = async (newPlanId: string) => {
    if (!subscription) return;

    try {
      setActionLoading('upgrade');
      const newPlan = plans.find(p => p.id === newPlanId);
      if (newPlan?.lemon_squeezy_variant_id) {
        await paymentApi.updateSubscription(subscription.id, newPlan.lemon_squeezy_variant_id);
        await loadDashboardData();
        setShowUpgradeModal(false);
      }
    } catch (err) {
      setError(handleApiError(err));
    } finally {
      setActionLoading(null);
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };

  const formatPrice = (price: number, currency: string) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency.toUpperCase(),
    }).format(price);
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active': return 'text-emerald-400 bg-emerald-500/10 border-emerald-500/30';
      case 'cancelled': return 'text-red-400 bg-red-500/10 border-red-500/30';
      case 'past_due': return 'text-yellow-400 bg-yellow-500/10 border-yellow-500/30';
      case 'unpaid': return 'text-red-400 bg-red-500/10 border-red-500/30';
      default: return 'text-gray-400 bg-gray-500/10 border-gray-500/30';
    }
  };

  if (loading) {
    return (
      <div className={`flex justify-center items-center py-12 ${className}`}>
        <Spinner size="lg" />
      </div>
    );
  }

  if (error) {
    return (
      <div className={className}>
        <Banner type="error">{error}</Banner>
        <div className="mt-4 text-center">
          <Button onClick={loadDashboardData} variant="secondary">
            Try Again
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className={`space-y-8 ${className}`}>
      {/* Header */}
      <div className="text-center">
        <h1 className="text-3xl font-bold text-white mb-2">Billing Dashboard</h1>
        <p className="text-gray-400">Manage your subscription and billing information</p>
      </div>

      {/* Upgrade Prompt */}
      <UpgradePrompt variant="banner" />

      {/* Current Subscription */}
      {subscription ? (
        <div className="bg-white/5 rounded-xl border border-glass-border p-6 backdrop-blur-sm">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-xl font-bold text-white">Current Subscription</h2>
            <div className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium border ${getStatusColor(subscription.status)}`}>
              {subscription.status.charAt(0).toUpperCase() + subscription.status.slice(1)}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
            <div>
              <div className="text-sm text-gray-400 mb-1">Plan</div>
              <div className="text-lg font-semibold text-white">{subscription.plan.name}</div>
            </div>
            <div>
              <div className="text-sm text-gray-400 mb-1">Price</div>
              <div className="text-lg font-semibold text-white">
                {formatPrice(subscription.plan.price, subscription.plan.currency)}
                <span className="text-sm text-gray-400 ml-1">
                  /{subscription.plan.billing_interval}
                </span>
              </div>
            </div>
            <div>
              <div className="text-sm text-gray-400 mb-1">Credits</div>
              <div className="text-lg font-semibold text-white">
                {subscription.plan.credits_per_period.toLocaleString()}
              </div>
            </div>
            <div>
              <div className="text-sm text-gray-400 mb-1">Next Billing</div>
              <div className="text-lg font-semibold text-white">
                {formatDate(subscription.current_period_end)}
              </div>
            </div>
          </div>

          {/* Subscription Actions */}
          <div className="flex flex-wrap gap-3">
            {subscription.status === 'active' && !subscription.cancel_at_period_end && (
              <Button
                onClick={() => setShowUpgradeModal(true)}
                variant="primary"
                disabled={actionLoading === 'upgrade'}
              >
                {actionLoading === 'upgrade' ? <Spinner size="sm" className="mr-2" /> : null}
                Upgrade Plan
              </Button>
            )}
            
            {subscription.status === 'active' && !subscription.cancel_at_period_end && (
              <Button
                onClick={handleCancelSubscription}
                variant="secondary"
                disabled={actionLoading === 'cancel'}
              >
                {actionLoading === 'cancel' ? <Spinner size="sm" className="mr-2" /> : null}
                Cancel Subscription
              </Button>
            )}
            
            {subscription.cancel_at_period_end && (
              <Button
                onClick={handleReactivateSubscription}
                variant="primary"
                disabled={actionLoading === 'reactivate'}
              >
                {actionLoading === 'reactivate' ? <Spinner size="sm" className="mr-2" /> : null}
                Reactivate Subscription
              </Button>
            )}
            
            <Button
              onClick={() => window.location.href = '/pricing'}
              variant="tertiary"
            >
              View All Plans
            </Button>
          </div>

          {subscription.cancel_at_period_end && (
            <Banner type="info" className="mt-4">
              Your subscription will be cancelled at the end of the current billing period on {formatDate(subscription.current_period_end)}.
            </Banner>
          )}
        </div>
      ) : (
        <div className="bg-white/5 rounded-xl border border-glass-border p-6 backdrop-blur-sm text-center">
          <div className="text-6xl mb-4">💳</div>
          <h2 className="text-xl font-bold text-white mb-2">No Active Subscription</h2>
          <p className="text-gray-400 mb-6">
            You're currently on the free plan. Upgrade to get more credits and features.
          </p>
          <Button
            onClick={() => window.location.href = '/pricing'}
            variant="primary"
            glowing
          >
            View Pricing Plans
          </Button>
        </div>
      )}

      {/* Credit Balance and Usage Stats */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <CreditBalanceComponent />
        <div className="bg-white/5 rounded-xl border border-glass-border p-6 backdrop-blur-sm">
          <h3 className="text-lg font-bold text-white mb-4">Quick Stats</h3>
          {usageStats ? (
            <div className="space-y-4">
              <div className="flex justify-between">
                <span className="text-gray-400">Total Generations</span>
                <span className="text-white font-semibold">{usageStats.total_generations.toLocaleString()}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-400">Today's Usage</span>
                <span className="text-white font-semibold">{usageStats.credits_used_today.toLocaleString()}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-400">Monthly Usage</span>
                <span className="text-white font-semibold">{usageStats.credits_used_this_month.toLocaleString()}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-400">Daily Average</span>
                <span className="text-white font-semibold">{usageStats.average_generations_per_day.toFixed(1)}</span>
              </div>
            </div>
          ) : (
            <div className="text-center py-8">
              <Spinner size="md" />
            </div>
          )}
        </div>
      </div>

      {/* Detailed Usage Stats */}
      <UsageStats />

      {/* Payment History */}
      <PaymentHistory />

      {/* Upgrade Modal */}
      {showUpgradeModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="bg-gray-900 rounded-xl border border-glass-border p-6 max-w-2xl mx-4 backdrop-blur-sm max-h-[80vh] overflow-y-auto">
            <div className="flex items-center justify-between mb-6">
              <h3 className="text-xl font-bold text-white">Upgrade Your Plan</h3>
              <Button
                onClick={() => setShowUpgradeModal(false)}
                variant="tertiary"
                size="sm"
              >
                ×
              </Button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {plans
                .filter(plan => plan.id !== subscription?.plan_id)
                .map((plan) => (
                  <div
                    key={plan.id}
                    className="bg-white/5 rounded-lg border border-glass-border p-4 hover:bg-white/10 transition-all cursor-pointer"
                    onClick={() => handleUpgradePlan(plan.id)}
                  >
                    <div className="text-center">
                      <h4 className="text-lg font-semibold text-white mb-2">{plan.name}</h4>
                      <div className="text-2xl font-bold text-primary mb-2">
                        {formatPrice(plan.price, plan.currency)}
                        <span className="text-sm text-gray-400 ml-1">/{plan.billing_interval}</span>
                      </div>
                      <div className="text-sm text-gray-400 mb-4">
                        {plan.credits_per_period.toLocaleString()} credits
                      </div>
                      <Button
                        variant="primary"
                        size="sm"
                        className="w-full"
                        disabled={actionLoading === 'upgrade'}
                      >
                        {actionLoading === 'upgrade' ? <Spinner size="sm" className="mr-2" /> : null}
                        Upgrade
                      </Button>
                    </div>
                  </div>
                ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}



