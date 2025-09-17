import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { usePaymentContext } from '../contexts/PaymentContext';
import { CreditBalance } from '../components/CreditBalance';
import { UsageStats } from '../components/UsageStats';
import { PaymentHistory } from '../components/PaymentHistory';
import { BillingDashboard } from '../components/BillingDashboard';
import { Button, Banner, Spinner } from '../components/UI';
import { useSearchParams } from 'react-router-dom';

export default function Billing() {
  const { t } = useTranslation();
  const { payment } = usePaymentContext();
  const [searchParams] = useSearchParams();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

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

  const handleCancelSubscription = async () => {
    if (!payment.currentSubscription) return;
    
    setLoading(true);
    setError(null);
    
    try {
      await payment.handleCancelSubscription();
      setSuccess('Subscription cancelled successfully. You\'ll continue to have access until the end of your billing period.');
    } catch (err) {
      setError('Failed to cancel subscription. Please try again or contact support.');
    } finally {
      setLoading(false);
    }
  };

  const handleReactivateSubscription = async () => {
    if (!payment.currentSubscription) return;
    
    setLoading(true);
    setError(null);
    
    try {
      await payment.handleReactivateSubscription();
      setSuccess('Subscription reactivated successfully!');
    } catch (err) {
      setError('Failed to reactivate subscription. Please try again or contact support.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto max-w-7xl p-4 space-y-8 animate-fade-in">
      {/* Header */}
      <section className="text-center py-8 animate-slide-in" style={{ animationDelay: '100ms' }}>
        <h1 className="text-4xl md:text-6xl font-extrabold tracking-tighter">
          <span className="bg-gradient-to-r from-accent-lightblue to-accent-cyan bg-clip-text text-transparent">
            {t('billing.title', 'Billing & Subscription')}
          </span>
        </h1>
        <p className="mt-4 text-lg text-gray-400 max-w-2xl mx-auto">
          {t('billing.subtitle', 'Manage your subscription, view usage, and billing history')}
        </p>
      </section>

      {/* Status Messages */}
      {error && <Banner type="error">{error}</Banner>}
      {success && <Banner type="success">{success}</Banner>}

      {/* Current Subscription Status */}
      {payment.currentSubscription && (
        <section className="animate-slide-in" style={{ animationDelay: '200ms' }}>
          <div className="bg-white/5 rounded-2xl border border-glass-border p-6">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-bold text-white">Current Subscription</h2>
              <div className="flex items-center space-x-3">
                <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                  payment.currentSubscription.status === 'active' 
                    ? 'bg-emerald-500/20 text-emerald-400' 
                    : payment.currentSubscription.status === 'cancelled'
                    ? 'bg-red-500/20 text-red-400'
                    : 'bg-yellow-500/20 text-yellow-400'
                }`}>
                  {payment.currentSubscription.status === 'active' ? 'Active' : 
                   payment.currentSubscription.status === 'cancelled' ? 'Cancelled' : 
                   payment.currentSubscription.status}
                </span>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
              <div>
                <div className="text-sm text-gray-400 mb-1">Plan</div>
                <div className="text-lg font-semibold text-white">
                  {payment.currentSubscription.plan.name}
                </div>
              </div>
              <div>
                <div className="text-sm text-gray-400 mb-1">Next Billing</div>
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
                  ${payment.currentSubscription.plan.price} / {payment.currentSubscription.plan.interval}
                </div>
              </div>
            </div>

            {/* Subscription Actions */}
            <div className="flex items-center space-x-4">
              {payment.currentSubscription.status === 'active' ? (
                <Button
                  onClick={handleCancelSubscription}
                  disabled={loading}
                  variant="secondary"
                  className="text-red-400 border-red-400/20 hover:bg-red-500/10"
                >
                  {loading ? <Spinner size="sm" /> : 'Cancel Subscription'}
                </Button>
              ) : payment.currentSubscription.status === 'cancelled' ? (
                <Button
                  onClick={handleReactivateSubscription}
                  disabled={loading}
                  variant="primary"
                >
                  {loading ? <Spinner size="sm" /> : 'Reactivate Subscription'}
                </Button>
              ) : null}
              
              <Button
                onClick={() => window.location.href = '/pricing'}
                variant="tertiary"
              >
                Change Plan
              </Button>
            </div>
          </div>
        </section>
      )}

      {/* Billing Dashboard */}
      <section className="animate-slide-in" style={{ animationDelay: '300ms' }}>
        <BillingDashboard />
      </section>

      {/* Credit Balance and Usage */}
      <section className="animate-slide-in" style={{ animationDelay: '400ms' }}>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <CreditBalance showPurchaseButton={true} />
          <UsageStats />
        </div>
      </section>

      {/* Payment History */}
      <section className="animate-slide-in" style={{ animationDelay: '500ms' }}>
        <div className="bg-white/5 rounded-2xl border border-glass-border p-6">
          <h2 className="text-2xl font-bold text-white mb-6">Payment History</h2>
          <PaymentHistory />
        </div>
      </section>
    </div>
  );
}
