import React, { useState, useEffect } from 'react';
import { Button, Input, Banner, Spinner } from './UI';
import { paymentApi, handleApiError } from '../api/client';
import { SubscriptionPlan, CheckoutSession } from '../types';

interface CheckoutFormProps {
  plan: SubscriptionPlan;
  onSuccess?: (session: CheckoutSession) => void;
  onCancel?: () => void;
  className?: string;
}

export function CheckoutForm({ plan, onSuccess, onCancel, className = "" }: CheckoutFormProps) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [successUrl, setSuccessUrl] = useState('');
  const [cancelUrl, setCancelUrl] = useState('');
  const [checkoutUrl, setCheckoutUrl] = useState<string | null>(null);

  useEffect(() => {
    // Set default URLs
    const baseUrl = window.location.origin;
    setSuccessUrl(`${baseUrl}/pricing?success=true&plan=${plan.id}`);
    setCancelUrl(`${baseUrl}/pricing?cancelled=true&plan=${plan.id}`);
  }, [plan.id]);

  const handleCreateCheckout = async () => {
    // Free plan doesn't need a variant ID (it's not purchasable)
    if (plan.id === 'free') {
      setError('You are already on the free plan. Please select a paid plan to upgrade.');
      return;
    }
    
    // Paid plans must have a variant ID to be purchasable
    if (!plan.lemon_squeezy_variant_id) {
      setError('This plan is not available for purchase at the moment.');
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const session: CheckoutSession = await paymentApi.createCheckoutSession(
        plan.lemon_squeezy_variant_id,
        successUrl,
        cancelUrl
      );

      setCheckoutUrl(session.checkout_url);
      
      if (onSuccess) {
        onSuccess(session);
      }
    } catch (err) {
      setError(handleApiError(err));
    } finally {
      setLoading(false);
    }
  };

  const handleRedirectToCheckout = () => {
    if (checkoutUrl) {
      window.location.href = checkoutUrl;
    }
  };

  const formatPrice = (price: number, currency: string) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency.toUpperCase(),
    }).format(price);
  };

  return (
    <div className={`max-w-md mx-auto ${className}`}>
      <div className="bg-white/5 rounded-xl border border-glass-border p-6 backdrop-blur-sm">
        <div className="text-center mb-6">
          <h2 className="text-2xl font-bold text-white mb-2">Complete Your Purchase</h2>
          <p className="text-gray-400">You're about to subscribe to {plan.name}</p>
        </div>

        {/* Plan Summary */}
        <div className="bg-white/5 rounded-lg p-4 mb-6 border border-glass-border">
          <div className="flex justify-between items-center mb-2">
            <span className="text-white font-semibold">{plan.name}</span>
            <span className="text-primary font-bold text-lg">
              {formatPrice(plan.price, plan.currency)}
            </span>
          </div>
          <div className="text-sm text-gray-400">
            Billed {plan.billing_interval === 'month' ? 'monthly' : 'annually'}
          </div>
          <div className="text-sm text-gray-400 mt-1">
            {plan.credits_per_period.toLocaleString()} credits per {plan.billing_interval}
          </div>
        </div>

        {/* Custom URLs (Optional) */}
        <div className="space-y-4 mb-6">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              Success URL (Optional)
            </label>
            <Input
              type="url"
              value={successUrl}
              onChange={(e) => setSuccessUrl(e.target.value)}
              placeholder="Where to redirect after successful payment"
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              Cancel URL (Optional)
            </label>
            <Input
              type="url"
              value={cancelUrl}
              onChange={(e) => setCancelUrl(e.target.value)}
              placeholder="Where to redirect if payment is cancelled"
            />
          </div>
        </div>

        {error && (
          <Banner type="error" className="mb-4">
            {error}
          </Banner>
        )}

        {/* Checkout URL Display */}
        {checkoutUrl && (
          <div className="mb-6">
            <Banner type="success" className="mb-4">
              Checkout session created successfully!
            </Banner>
            
            <div className="bg-white/5 rounded-lg p-4 border border-glass-border">
              <div className="text-sm text-gray-400 mb-2">Checkout URL:</div>
              <div className="text-xs text-gray-300 break-all bg-black/20 p-2 rounded">
                {checkoutUrl}
              </div>
            </div>
          </div>
        )}

        {/* Action Buttons */}
        <div className="space-y-3">
          {!checkoutUrl ? (
            <Button
              onClick={handleCreateCheckout}
              disabled={loading}
              variant="primary"
              className="w-full"
              glowing
            >
              {loading ? (
                <>
                  <Spinner size="sm" className="mr-2" />
                  Creating Checkout Session...
                </>
              ) : (
                'Create Checkout Session'
              )}
            </Button>
          ) : (
            <Button
              onClick={handleRedirectToCheckout}
              variant="primary"
              className="w-full"
              glowing
            >
              Proceed to Payment
            </Button>
          )}

          {onCancel && (
            <Button
              onClick={onCancel}
              variant="tertiary"
              className="w-full"
            >
              Cancel
            </Button>
          )}
        </div>

        {/* Security Notice */}
        <div className="mt-6 text-center">
          <div className="flex items-center justify-center text-sm text-gray-400">
            <svg className="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path
                fillRule="evenodd"
                d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                clipRule="evenodd"
              />
            </svg>
            Secure payment powered by Lemon Squeezy
          </div>
        </div>
      </div>
    </div>
  );
}



