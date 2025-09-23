import { useQuery } from '@tanstack/react-query';
import { paymentApi } from '../api/client';
import { SubscriptionPlan } from '../types';

/**
 * Custom hook for fetching subscription plans with caching
 * Uses TanStack Query to prevent duplicate API calls and implement proper caching
 */
export const useSubscriptionPlans = () => {
  return useQuery({
    queryKey: ['subscription-plans'],
    queryFn: async (): Promise<SubscriptionPlan[]> => {
      const plans = await paymentApi.getPlans();
      return Array.isArray(plans) ? plans : [];
    },
    staleTime: 1000 * 60 * 30, // Cache for 30 minutes
    gcTime: 1000 * 60 * 60, // Keep in cache for 1 hour
    retry: 3,
    retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),
    refetchOnWindowFocus: false,
    refetchOnMount: false,
    refetchOnReconnect: false,
  });
};

/**
 * Hook for getting a specific plan by ID
 */
export const useSubscriptionPlan = (planId: string) => {
  const { data: plans, ...rest } = useSubscriptionPlans();
  
  const plan = plans?.find(p => p.id === planId);
  
  return {
    plan,
    ...rest
  };
};

