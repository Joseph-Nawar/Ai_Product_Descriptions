import React, { useState, useEffect } from 'react';
import { Button, Banner, Spinner } from './UI';
import { paymentApi, handleApiError } from '../api/client';
import { SubscriptionPlan, CheckoutSession } from '../types';

interface PricingPlansProps {
  onPlanSelect?: (plan: SubscriptionPlan) => void;
  currentPlanId?: string;
  className?: string;
}

export function PricingPlans({ onPlanSelect, currentPlanId, className = "" }: PricingPlansProps) {
  const [plans, setPlans] = useState<SubscriptionPlan[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedPlan, setSelectedPlan] = useState<SubscriptionPlan | null>(null);
  const [checkoutLoading, setCheckoutLoading] = useState(false);
  const [billingInterval, setBillingInterval] = useState<'month' | 'year'>('month');

  useEffect(() => {
    loadPlans();
  }, []);

  const loadPlans = async () => {
    try {
      setLoading(true);
      setError(null);
      const plansData = await paymentApi.getPlans();
      setPlans(plansData);
    } catch (err) {
      setError(handleApiError(err));
    } finally {
      setLoading(false);
    }
  };

  const handlePlanSelect = async (plan: SubscriptionPlan) => {
    if (!plan.lemon_squeezy_variant_id) {
      setError('This plan is not available for purchase at the moment.');
      return;
    }

    try {
      setCheckoutLoading(true);
      setSelectedPlan(plan);
      
      const successUrl = `${window.location.origin}/billing?success=true`;
      const cancelUrl = `${window.location.origin}/pricing?cancelled=true`;
      
      const session: CheckoutSession = await paymentApi.createCheckoutSession(
        plan.lemon_squeezy_variant_id,
        successUrl,
        cancelUrl
      );

      // Redirect to Lemon Squeezy checkout
      window.location.href = session.checkout_url;
    } catch (err) {
      setError(handleApiError(err));
      setCheckoutLoading(false);
      setSelectedPlan(null);
    }
  };

  const formatPrice = (price: number, currency: string) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency.toUpperCase(),
    }).format(price);
  };

  const getPlanCredits = (plan: SubscriptionPlan) => {
    return plan.interval === 'year' ? plan.credits * 12 : plan.credits;
  };

  const filteredPlans = plans.filter(plan => plan.interval === billingInterval);

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
          <Button onClick={loadPlans} variant="secondary">
            Try Again
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className={`space-y-8 ${className}`}>
      {/* Billing Toggle */}
      <div className="flex justify-center">
        <div className="bg-white/5 rounded-lg p-1 border border-glass-border">
          <button
            onClick={() => setBillingInterval('month')}
            className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${
              billingInterval === 'month'
                ? 'bg-primary text-white shadow-lg'
                : 'text-gray-400 hover:text-white'
            }`}
          >
            Monthly
          </button>
          <button
            onClick={() => setBillingInterval('year')}
            className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${
              billingInterval === 'year'
                ? 'bg-primary text-white shadow-lg'
                : 'text-gray-400 hover:text-white'
            }`}
          >
            Yearly
            <span className="ml-1 text-xs bg-emerald-500 text-white px-1.5 py-0.5 rounded">
              Save 20%
            </span>
          </button>
        </div>
      </div>

      {/* Plans Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredPlans.map((plan) => {
          const isCurrentPlan = currentPlanId === plan.id;
          const isSelected = selectedPlan?.id === plan.id;
          const isPopular = plan.popular;

          return (
            <div
              key={plan.id}
              className={`relative rounded-xl border-2 transition-all duration-300 ${
                isPopular
                  ? 'border-primary bg-gradient-to-b from-primary/10 to-transparent'
                  : 'border-glass-border bg-white/5'
              } ${isCurrentPlan ? 'ring-2 ring-emerald-500' : ''} ${
                isSelected ? 'scale-105 shadow-2xl' : 'hover:scale-105 hover:shadow-xl'
              }`}
            >
              {isPopular && (
                <div className="absolute -top-3 left-1/2 -translate-x-1/2">
                  <span className="bg-primary text-white px-4 py-1 rounded-full text-sm font-semibold">
                    Most Popular
                  </span>
                </div>
              )}

              {isCurrentPlan && (
                <div className="absolute -top-3 right-4">
                  <span className="bg-emerald-500 text-white px-3 py-1 rounded-full text-xs font-semibold">
                    Current Plan
                  </span>
                </div>
              )}

              <div className="p-6">
                <div className="text-center mb-6">
                  <h3 className="text-xl font-bold text-white mb-2">{plan.name}</h3>
                  <p className="text-gray-400 text-sm mb-4">{plan.description}</p>
                  
                  <div className="mb-4">
                    <span className="text-4xl font-bold text-white">
                      {formatPrice(plan.price, plan.currency)}
                    </span>
                    <span className="text-gray-400 ml-2">
                      /{plan.interval === 'month' ? 'month' : 'year'}
                    </span>
                  </div>

                  <div className="text-center">
                    <span className="text-2xl font-bold text-primary">
                      {getPlanCredits(plan).toLocaleString()}
                    </span>
                    <span className="text-gray-400 ml-2">credits</span>
                  </div>
                </div>

                <div className="space-y-3 mb-6">
                  {plan.features.map((feature, index) => (
                    <div key={index} className="flex items-center text-sm">
                      <svg
                        className="w-4 h-4 text-emerald-500 mr-3 flex-shrink-0"
                        fill="currentColor"
                        viewBox="0 0 20 20"
                      >
                        <path
                          fillRule="evenodd"
                          d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                          clipRule="evenodd"
                        />
                      </svg>
                      <span className="text-gray-300">{feature}</span>
                    </div>
                  ))}
                </div>

                <Button
                  onClick={() => handlePlanSelect(plan)}
                  disabled={isCurrentPlan || checkoutLoading}
                  variant={isPopular ? "primary" : "secondary"}
                  className="w-full"
                  glowing={isPopular}
                >
                  {checkoutLoading && isSelected ? (
                    <>
                      <Spinner size="sm" className="mr-2" />
                      Processing...
                    </>
                  ) : isCurrentPlan ? (
                    'Current Plan'
                  ) : (
                    `Get ${plan.name}`
                  )}
                </Button>
              </div>
            </div>
          );
        })}
      </div>

      {/* Additional Info */}
      <div className="text-center text-gray-400 text-sm">
        <p>All plans include 30-day money-back guarantee</p>
        <p className="mt-1">Cancel anytime • No setup fees • Secure payments</p>
      </div>
    </div>
  );
}



