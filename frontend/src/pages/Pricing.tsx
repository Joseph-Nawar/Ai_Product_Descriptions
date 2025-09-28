import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { usePaymentContext } from '../contexts/PaymentContext';
import { PricingPlans } from '../components/PricingPlans';
import { Button } from '../components/UI';
import { useNavigate } from 'react-router-dom';

export default function Pricing() {
  const { t } = useTranslation();
  const { payment } = usePaymentContext();
  const navigate = useNavigate();
  const [isRefreshing, setIsRefreshing] = useState(false);

  const handleRefresh = async () => {
    setIsRefreshing(true);
    try {
      await payment.refreshPaymentData();
    } catch (error) {
      console.error('Failed to refresh payment data:', error);
    } finally {
      setIsRefreshing(false);
    }
  };

  // Auto-refresh when component mounts (useful after returning from payment)
  useEffect(() => {
    handleRefresh();
  }, []); // Empty dependency array means this runs once on mount

  return (
    <div className="mx-auto max-w-7xl p-4 space-y-12 animate-fade-in">
      {/* Hero Section */}
      <section className="text-center py-16 animate-slide-in" style={{ animationDelay: '100ms' }}>
        <h1 className="text-5xl md:text-7xl font-extrabold tracking-tighter">
          <span className="bg-gradient-to-r from-accent-lightblue to-accent-cyan bg-clip-text text-transparent">
            {t('pricing.title', 'Simple, Transparent Pricing')}
          </span>
        </h1>
        <p className="mt-6 text-lg text-gray-400 max-w-2xl mx-auto">
          {t('pricing.subtitle', 'Choose the perfect plan for your AI product description needs')}
        </p>
      </section>

      {/* Pricing Plans - Now the main focus at the top */}
      <section className="animate-slide-in" style={{ animationDelay: '200ms' }}>
        <PricingPlans 
          currentPlanId={payment.currentSubscription?.plan_id}
          onPlanSelect={(plan) => {
            // Plan selection is handled by PricingPlans component
            console.log('Plan selected:', plan);
          }}
        />
      </section>

      {/* Current Status - Show for all users */}
      <section className="animate-slide-in" style={{ animationDelay: '300ms' }}>
        <div className="bg-gradient-to-r from-emerald-500/10 to-primary/10 border border-emerald-500/20 rounded-xl p-6">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-xl font-semibold text-white mb-2">
                Current Plan: {payment.currentSubscription?.plan?.name || 'Free Plan'}
              </h3>
              <p className="text-gray-400">
                Status: <span className="text-emerald-400 font-medium">
                  {payment.currentSubscription?.status === 'active' ? 'Active' : 
                   payment.currentSubscription?.status === 'cancelled' ? 'Cancelled' : 
                   payment.currentSubscription?.status || 'Free'}
                </span>
              </p>
            </div>
            <div className="flex gap-2">
              <Button
                onClick={handleRefresh}
                variant="secondary"
                disabled={isRefreshing}
              >
                {isRefreshing ? 'Refreshing...' : 'Refresh Status'}
              </Button>
              {payment.currentSubscription && (
                <Button
                  onClick={() => navigate('/pricing')}
                  variant="secondary"
                >
                  Manage Subscription
                </Button>
              )}
            </div>
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="animate-slide-in" style={{ animationDelay: '400ms' }}>
        <div className="bg-white/5 rounded-2xl border border-glass-border p-8">
          <h2 className="text-2xl font-bold text-white mb-6 text-center">
            {t('pricing.faqTitle', 'Frequently Asked Questions')}
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-4">
              <div>
                <h3 className="text-lg font-semibold text-white mb-2">
                  {t('pricing.faq1.question', 'How do credits work?')}
                </h3>
                <p className="text-gray-400">
                  {t('pricing.faq1.answer', 'Each product description generation costs 1 credit. Credits are included with your subscription and reset monthly.')}
                </p>
              </div>
            </div>
            
            <div className="space-y-4">
              <div>
                <h3 className="text-lg font-semibold text-white mb-2">
                  {t('pricing.faq3.question', 'What happens if I run out of credits?')}
                </h3>
                <p className="text-gray-400">
                  {t('pricing.faq3.answer', 'You can purchase additional credits or upgrade to a higher plan. We\'ll notify you when you\'re running low.')}
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
