import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { usePaymentContext } from '../contexts/PaymentContext';
import { Button, Banner, Spinner } from '../components/UI';
import { useSearchParams } from 'react-router-dom';
import { checkoutApi } from '../api/payments';

export default function Billing() {
  const { t } = useTranslation();
  const { payment } = usePaymentContext();
  const [searchParams] = useSearchParams();
  const [portalLoading, setPortalLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  // Show loading state while payment data is being fetched
  if (payment.isLoading) {
    return (
      <div className="mx-auto max-w-4xl p-4 space-y-8 animate-fade-in">
        <section className="text-center py-8">
          <h1 className="text-4xl md:text-6xl font-extrabold tracking-tighter">
            <span className="bg-gradient-to-r from-accent-lightblue to-accent-cyan bg-clip-text text-transparent">
              {t('billing.title', 'Billing & Subscription')}
            </span>
          </h1>
          <p className="mt-4 text-lg text-gray-400 max-w-2xl mx-auto">
            {t('billing.subtitle', 'Manage your subscription and billing')}
          </p>
        </section>
        <div className="flex items-center justify-center py-12">
          <Spinner size="lg" />
          <span className="ml-3 text-lg text-gray-400">Loading your billing information...</span>
        </div>
      </div>
    );
  }

  // Handle success/cancel from payment flow
  useEffect(() => {
    const successParam = searchParams.get('success');
    const cancelledParam = searchParams.get('cancelled');
    
    if (successParam === 'true') {
      setSuccess('Payment successful! Your subscription has been updated.');
      // Refresh payment data
      payment.refreshPaymentData();
    } else if (cancelledParam === 'true') {
      setError('Payment was cancelled. You can try again anytime.');
    }
  }, [searchParams, payment]);

  const handleManageSubscription = async () => {
    setPortalLoading(true);
    setError(null);
    
    try {
      const result = await checkoutApi.createPortalSession();
      // Redirect to the customer portal
      window.location.href = result.url;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to open customer portal';
      if (errorMessage.includes('No subscription found')) {
        setError('No subscription found. Please subscribe to a plan first to access the customer portal.');
      } else {
        setError(`Failed to open customer portal: ${errorMessage}`);
      }
    } finally {
      setPortalLoading(false);
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active':
        return 'bg-emerald-500/20 text-emerald-400';
      case 'cancelled':
        return 'bg-red-500/20 text-red-400';
      case 'past_due':
        return 'bg-yellow-500/20 text-yellow-400';
      default:
        return 'bg-gray-500/20 text-gray-400';
    }
  };

  const getStatusText = (status: string) => {
    switch (status) {
      case 'active':
        return 'Active';
      case 'cancelled':
        return 'Cancelled';
      case 'past_due':
        return 'Past Due';
      default:
        return status;
    }
  };

  return (
    <div className="mx-auto max-w-4xl p-4 space-y-8 animate-fade-in">
      {/* Header */}
      <section className="text-center py-8 animate-slide-in" style={{ animationDelay: '100ms' }}>
        <h1 className="text-4xl md:text-6xl font-extrabold tracking-tighter">
          <span className="bg-gradient-to-r from-accent-lightblue to-accent-cyan bg-clip-text text-transparent">
            {t('billing.title', 'Billing & Subscription')}
          </span>
        </h1>
        <p className="mt-4 text-lg text-gray-400 max-w-2xl mx-auto">
          {t('billing.subtitle', 'Manage your subscription and billing')}
        </p>
      </section>

      {/* Status Messages */}
      {error && <Banner type="error">{error}</Banner>}
      {success && <Banner type="success">{success}</Banner>}

      {/* Current Plan Card */}
      <section className="animate-slide-in" style={{ animationDelay: '200ms' }}>
        <div className="bg-white/5 rounded-2xl border border-glass-border p-8">
          {payment.currentSubscription ? (
            <div className="text-center">
              <div className="mb-6">
                <h2 className="text-3xl font-bold text-white mb-2">
                  Current Plan: {payment.currentSubscription.plan?.name ?? 'Unknown Plan'}
                </h2>
                <span className={`inline-block px-4 py-2 rounded-full text-sm font-medium ${getStatusColor(payment.currentSubscription.status)}`}>
                  {getStatusText(payment.currentSubscription.status)}
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div>
                  <div className="text-sm text-gray-400 mb-1">Next Billing Date</div>
                  <div className="text-lg font-semibold text-white">
                    {payment.currentSubscription.current_period_end 
                      ? new Date(payment.currentSubscription.current_period_end).toLocaleDateString()
                      : 'N/A'
                    }
                  </div>
                </div>
                <div>
                  <div className="text-sm text-gray-400 mb-1">Amount</div>
                  <div className="text-lg font-semibold text-white">
                    ${payment.currentSubscription.plan?.price ?? 0} / {payment.currentSubscription.plan?.billing_interval ?? 'month'}
                  </div>
                </div>
              </div>

              <Button
                onClick={handleManageSubscription}
                disabled={portalLoading}
                variant="primary"
                className="bg-gradient-to-r from-accent-lightblue to-accent-cyan hover:from-accent-lightblue/80 hover:to-accent-cyan/80 text-lg px-8 py-3"
              >
                {portalLoading ? <Spinner size="sm" /> : 'Manage Subscription'}
              </Button>
            </div>
          ) : (
            <div className="text-center">
              <h2 className="text-3xl font-bold text-white mb-4">You are currently on the Free plan</h2>
              <p className="text-gray-400 mb-8 max-w-md mx-auto">
                Upgrade to a paid plan to unlock unlimited product descriptions and premium features.
              </p>
              <Button
                onClick={() => window.location.href = '/pricing'}
                variant="primary"
                className="bg-gradient-to-r from-accent-lightblue to-accent-cyan hover:from-accent-lightblue/80 hover:to-accent-cyan/80 text-lg px-8 py-3"
              >
                View Plans
              </Button>
            </div>
          )}
        </div>
      </section>

      {/* Billing History - Commented out until implemented */}
      {/* 
      <section className="animate-slide-in" style={{ animationDelay: '300ms' }}>
        <div className="bg-white/5 rounded-2xl border border-glass-border p-6">
          <h2 className="text-2xl font-bold text-white mb-6">Billing History</h2>
          <div className="text-center py-8 text-gray-400">
            <p>Billing history will be available here once implemented.</p>
          </div>
        </div>
      </section>
      */}
    </div>
  );
}
