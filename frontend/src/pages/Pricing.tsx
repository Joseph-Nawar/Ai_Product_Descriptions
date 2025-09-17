import React from 'react';
import { useTranslation } from 'react-i18next';
import { usePaymentContext } from '../contexts/PaymentContext';
import { PricingPlans } from '../components/PricingPlans';
import { CreditBalance } from '../components/CreditBalance';
import { UsageStats } from '../components/UsageStats';
import { Button, Banner } from '../components/UI';
import { useNavigate } from 'react-router-dom';

export default function Pricing() {
  const { t } = useTranslation();
  const { payment } = usePaymentContext();
  const navigate = useNavigate();

  return (
    <div className="mx-auto max-w-7xl p-4 space-y-12 animate-fade-in">
      {/* Hero Section */}
      <section className="text-center py-16 animate-slide-in" style={{ animationDelay: '100ms' }}>
        <h1 className="text-5xl md:text-7xl font-extrabold tracking-tighter">
          <span className="bg-gradient-to-r from-accent-lightblue to-accent-cyan bg-clip-text text-transparent">
            {t('pricing.title', 'Choose Your Plan')}
          </span>
        </h1>
        <p className="mt-6 text-lg text-gray-400 max-w-2xl mx-auto">
          {t('pricing.subtitle', 'Select the perfect plan for your AI product description needs')}
        </p>
      </section>

      {/* Current Status */}
      {payment.currentSubscription && (
        <section className="animate-slide-in" style={{ animationDelay: '200ms' }}>
          <div className="bg-gradient-to-r from-emerald-500/10 to-primary/10 border border-emerald-500/20 rounded-xl p-6">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-xl font-semibold text-white mb-2">
                  Current Plan: {payment.currentSubscription.plan.name}
                </h3>
                <p className="text-gray-400">
                  Status: <span className="text-emerald-400 font-medium">
                    {payment.currentSubscription.status === 'active' ? 'Active' : 
                     payment.currentSubscription.status === 'cancelled' ? 'Cancelled' : 
                     payment.currentSubscription.status}
                  </span>
                </p>
              </div>
              <Button
                onClick={() => navigate('/billing')}
                variant="secondary"
              >
                Manage Subscription
              </Button>
            </div>
          </div>
        </section>
      )}

      {/* Credit Balance */}
      <section className="animate-slide-in" style={{ animationDelay: '300ms' }}>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <CreditBalance showPurchaseButton={true} />
          <UsageStats />
        </div>
      </section>

      {/* Pricing Plans */}
      <section className="animate-slide-in" style={{ animationDelay: '400ms' }}>
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-white mb-4">
            {t('pricing.plansTitle', 'Subscription Plans')}
          </h2>
          <p className="text-gray-400 max-w-2xl mx-auto">
            {t('pricing.plansDescription', 'Choose the plan that fits your needs. All plans include our AI-powered product description generation.')}
          </p>
        </div>
        
        <PricingPlans 
          currentPlanId={payment.currentSubscription?.plan_id}
          onPlanSelect={(plan) => {
            // Plan selection is handled by PricingPlans component
            console.log('Plan selected:', plan);
          }}
        />
      </section>

      {/* FAQ Section */}
      <section className="animate-slide-in" style={{ animationDelay: '500ms' }}>
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
              
              <div>
                <h3 className="text-lg font-semibold text-white mb-2">
                  {t('pricing.faq2.question', 'Can I cancel anytime?')}
                </h3>
                <p className="text-gray-400">
                  {t('pricing.faq2.answer', 'Yes, you can cancel your subscription at any time. You\'ll continue to have access until the end of your billing period.')}
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
              
              <div>
                <h3 className="text-lg font-semibold text-white mb-2">
                  {t('pricing.faq4.question', 'Do you offer refunds?')}
                </h3>
                <p className="text-gray-400">
                  {t('pricing.faq4.answer', 'We offer a 30-day money-back guarantee on all subscription plans.')}
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
