export type ProductInput = {
  id?: string;
  product_name: string;
  category: string;
  features: string;
  audience: string;
  keywords?: string;
  languageCode?: string; // New: Language for generation
};

export type GeneratedItem = {
  id: string;
  product_name: string;
  category: string;
  audience: string;
  description: string;
  keywords?: string;
  features: string; // Add original features for regeneration
  tone: string; // Add original tone for regeneration
  style_variation: string; // Add original style variation for regeneration
  languageCode?: string; // New: Language of the generated description
  regenerating?: boolean; // New: For UI loading state on a single row
};

export type BatchGenerationRequest = {
  products: ProductInput[];
  batchTone: string;
  batchStyle: string;
  languageCode: string; // New: Language for all descriptions in batch
};

export type BatchResponse = {
  batch_id: string;
  items: GeneratedItem[];
};

export type ApiError = { message: string; status?: number };

// Payment and Subscription Types
export type SubscriptionPlan = {
  id: string;
  name: string;
  description: string;
  price: number;
  currency: string;
  billing_interval: 'month' | 'year';
  credits_per_period: number;
  max_products_per_batch: number;
  features: string[] | Record<string, any>;
  popular?: boolean;
  lemon_squeezy_variant_id?: string;
  store_id?: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
};

export type UserSubscription = {
  id: string;
  plan_id: string;
  status: 'active' | 'cancelled' | 'past_due' | 'unpaid';
  current_period_start: string;
  current_period_end: string;
  cancel_at_period_end: boolean;
  lemon_squeezy_subscription_id?: string;
  plan: SubscriptionPlan;
};

export type CreditBalance = {
  current_credits: number;
  total_credits: number;
  used_credits: number;
  reset_date?: string;
};

export type UsageStats = {
  total_generations: number;
  credits_used_today: number;
  credits_used_this_month: number;
  average_generations_per_day: number;
  last_generation_date?: string;
};

export type PaymentTransaction = {
  id: string;
  amount: number;
  currency: string;
  status: 'completed' | 'pending' | 'failed' | 'refunded';
  type: 'subscription' | 'credit_purchase' | 'refund';
  description: string;
  created_at: string;
  lemon_squeezy_order_id?: string;
};

export type CheckoutSession = {
  checkout_url: string;
  session_id: string;
};

export type LemonSqueezyWebhook = {
  event: string;
  data: any;
};