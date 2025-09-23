import React, { useState } from 'react';
import { Button, Banner, Spinner } from './UI';
import { paymentApi, handleApiError } from '../api/client';
import { SubscriptionPlan, CheckoutSession } from '../types';
import { useSubscriptionPlans } from '../hooks/useSubscriptionPlans';

interface PricingPlansProps {
  onPlanSelect?: (plan: SubscriptionPlan) => void;
  currentPlanId?: string;
  className?: string;
}

export function PricingPlans({ onPlanSelect, currentPlanId, className = "" }: PricingPlansProps) {
  const { data: plans = [], isLoading: loading, error: queryError, refetch } = useSubscriptionPlans();
  const [selectedPlan, setSelectedPlan] = useState<SubscriptionPlan | null>(null);
  const [checkoutLoading, setCheckoutLoading] = useState(false);
  const [billingInterval, setBillingInterval] = useState<'month' | 'year'>('month');

  // Convert query error to string for display
  const error = queryError ? handleApiError(queryError) : null;

  const handlePlanSelect = async (plan: SubscriptionPlan) => {
    // Test authentication first
    console.log('🔐 TESTING AUTHENTICATION');
    const { auth } = await import('../auth/firebase');
    const user = auth.currentUser;
    console.log('Current user:', user?.uid);
    
    if (user) {
      try {
        const token = await user.getIdToken();
        console.log('Token segments:', token.split('.').length);
        console.log('Token valid:', token.split('.').length === 3);
        console.log('Token preview:', token.substring(0, 50) + '...');
      } catch (error) {
        console.error('Token error:', error);
      }
    } else {
      console.error('❌ No authenticated user');
      alert('Please sign in to purchase a plan.');
      return;
    }
    
    // Free plan doesn't need a variant ID (it's not purchasable)
    if (plan.id === 'free') {
      alert('You are already on the free plan. Please select a paid plan to upgrade.');
      return;
    }
    
    // Paid plans must have a variant ID to be purchasable
    if (!plan.lemon_squeezy_variant_id) {
      // Show user-friendly error message
      alert('This plan is not available for purchase at the moment. Please try again later.');
      return;
    }

    try {
      setCheckoutLoading(true);
      setSelectedPlan(plan);
      
      const successUrl = `${window.location.origin}/billing?success=true`;
      const cancelUrl = `${window.location.origin}/pricing?cancelled=true`;
      
      console.log("=== CHECKOUT DEBUG ===");
      console.log("Plan variant ID:", plan.lemon_squeezy_variant_id);
      console.log("Success URL:", successUrl);
      console.log("Cancel URL:", cancelUrl);
      
      const response = await paymentApi.createCheckoutSession(
        plan.lemon_squeezy_variant_id,
        successUrl,
        cancelUrl
      );
      
      console.log("Full API response:", response);
      console.log("Response type:", typeof response);
      console.log("Response keys:", Object.keys(response || {}));
      
      // ✅ PROPER RESPONSE HANDLING
      if (response && response.checkout_url) {
        console.log("✅ Valid response, redirecting to:", response.checkout_url);
        window.location.href = response.checkout_url;
      } else {
        console.error("❌ Invalid response format:", response);
        alert("Checkout failed: Invalid response from server");
      }
    } catch (err) {
      // Handle checkout error with user-friendly message
      console.error('Checkout error:', err);
      const errorMessage = handleApiError(err);
      alert(`Unable to start checkout process: ${errorMessage}`);
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

  const getPlanGenerations = (plan: SubscriptionPlan) => {
    // For display purposes, show daily generations regardless of billing interval
    return plan.credits_per_period;
  };

  const getPlanCredits = (plan: SubscriptionPlan) => {
    return plan.billing_interval === 'year' ? plan.credits_per_period * 12 : plan.credits_per_period;
  };

  const filteredPlans = (plans || []).filter(plan => plan.billing_interval === billingInterval);

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
          <Button onClick={() => refetch()} variant="secondary">
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
              Save 50%
            </span>
          </button>
        </div>
      </div>

      {/* Plans Grid */}
      <div className={`grid gap-6 ${
        billingInterval === 'year' 
          ? 'grid-cols-1 md:grid-cols-1 lg:grid-cols-1 max-w-md mx-auto' 
          : 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3'
      }`}>
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
                      /{plan.billing_interval === 'month' ? 'month' : 'year'}
                    </span>
                  </div>

                  <div className="text-center">
                    <span className="text-2xl font-bold text-primary">
                      {getPlanGenerations(plan).toLocaleString()}
                    </span>
                    <span className="text-gray-400 ml-2">generations/day</span>
                  </div>
                </div>

                <div className="space-y-3 mb-6">
                  {(() => {
                    // Handle both array and object formats for features
                    const features = plan.features;
                    if (!features) return null;
                    
                    const featureList = Array.isArray(features) 
                      ? features 
                      : Object.values(features).filter(value => typeof value === 'string');
                    
                    return featureList.map((feature, index) => (
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
                    ));
                  })()}
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
        <p>No setup fees • Secure payments</p>
      </div>
    </div>
  );
}