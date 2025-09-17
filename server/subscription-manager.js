// server/subscription-manager.js
// Subscription and usage management for Lemon Squeezy webhooks

// Plan configurations
const PLANS = {
  free: {
    name: 'Free',
    monthly_descriptions: 2,
    regenerations_per_description: 1,
    max_batch_size: 5,
    ai_model: 'basic',
    support_level: 'community',
    features: ['basic_ai', 'standard_templates']
  },
  basic: {
    name: 'Basic',
    monthly_descriptions: 10,
    regenerations_per_description: 3,
    max_batch_size: 20,
    ai_model: 'advanced',
    support_level: 'email',
    features: ['advanced_ai', 'custom_templates', 'priority_processing']
  },
  pro: {
    name: 'Pro',
    monthly_descriptions: 100,
    regenerations_per_description: -1, // unlimited
    max_batch_size: 100,
    ai_model: 'premium',
    support_level: 'priority',
    features: ['premium_ai', 'custom_prompts', 'api_access', 'white_label']
  }
};

// Map Lemon Squeezy variant IDs to plans (you'll update these with real IDs)
const VARIANT_TO_PLAN = {
  'free_variant_id': 'free',
  'basic_variant_id': 'basic', 
  'pro_variant_id': 'pro'
};

// In-memory storage for demo (replace with real database in production)
const users = new Map();
const usageLogs = [];

class SubscriptionManager {
  // Handle webhook events
  async handleWebhookEvent(eventName, payload) {
    console.log(`Processing webhook event: ${eventName}`);
    
    switch (eventName) {
      case 'subscription_created':
        await this.handleSubscriptionCreated(payload);
        break;
      case 'subscription_updated':
        await this.handleSubscriptionUpdated(payload);
        break;
      case 'subscription_cancelled':
        await this.handleSubscriptionCancelled(payload);
        break;
      case 'order_created':
        await this.handleOrderCreated(payload);
        break;
      default:
        console.log(`Unhandled event: ${eventName}`);
    }
  }

  // Handle new subscription
  async handleSubscriptionCreated(payload) {
    const { customer_email, variant_id, status } = payload.data.attributes;
    const plan = this.getPlanFromVariantId(variant_id);
    
    console.log(`New subscription created for ${customer_email}: ${plan.name}`);
    
    // Create or update user
    const user = {
      email: customer_email,
      subscription_id: payload.data.id,
      plan: plan.name,
      plan_config: plan,
      status: status,
      usage_count: 0,
      regenerations_used: 0,
      created_at: new Date(),
      reset_date: this.getNextResetDate()
    };
    
    users.set(customer_email, user);
    this.logUsage(customer_email, 'subscription_created', 0, { plan: plan.name });
  }

  // Handle subscription updates
  async handleSubscriptionUpdated(payload) {
    const { customer_email, variant_id, status } = payload.data.attributes;
    const plan = this.getPlanFromVariantId(variant_id);
    
    console.log(`Subscription updated for ${customer_email}: ${plan.name} (${status})`);
    
    const user = users.get(customer_email);
    if (user) {
      user.plan = plan.name;
      user.plan_config = plan;
      user.status = status;
      users.set(customer_email, user);
    }
    
    this.logUsage(customer_email, 'subscription_updated', 0, { 
      plan: plan.name, 
      status: status 
    });
  }

  // Handle subscription cancellation
  async handleSubscriptionCancelled(payload) {
    const { customer_email } = payload.data.attributes;
    
    console.log(`Subscription cancelled for ${customer_email}`);
    
    const user = users.get(customer_email);
    if (user) {
      user.status = 'cancelled';
      user.plan = 'free'; // Downgrade to free
      user.plan_config = PLANS.free;
      users.set(customer_email, user);
    }
    
    this.logUsage(customer_email, 'subscription_cancelled', 0, {});
  }

  // Handle one-time orders
  async handleOrderCreated(payload) {
    const { customer_email, total } = payload.data.attributes;
    
    console.log(`Order created for ${customer_email}: $${total}`);
    
    // For one-time purchases, you might want to add credits or features
    this.logUsage(customer_email, 'order_created', 0, { total: total });
  }

  // Check if user can perform an action
  canUserPerformAction(email, action, metadata = {}) {
    const user = users.get(email);
    if (!user) {
      return { allowed: false, reason: 'User not found' };
    }

    if (user.status !== 'active') {
      return { allowed: false, reason: 'Subscription not active' };
    }

    // Check monthly usage reset
    if (this.shouldResetUsage(user)) {
      this.resetUserUsage(user);
    }

    switch (action) {
      case 'generate_description':
        return this.canGenerateDescription(user, metadata);
      case 'regenerate_description':
        return this.canRegenerateDescription(user, metadata);
      case 'batch_generate':
        return this.canBatchGenerate(user, metadata);
      default:
        return { allowed: false, reason: 'Unknown action' };
    }
  }

  // Check if user can generate a description
  canGenerateDescription(user, metadata) {
    const { batch_size = 1 } = metadata;
    
    if (user.usage_count + batch_size > user.plan_config.monthly_descriptions) {
      return {
        allowed: false,
        reason: `Monthly limit reached. You have ${user.plan_config.monthly_descriptions - user.usage_count} descriptions remaining.`,
        upgrade_required: true
      };
    }

    if (batch_size > user.plan_config.max_batch_size) {
      return {
        allowed: false,
        reason: `Batch size limit exceeded. Maximum ${user.plan_config.max_batch_size} products per batch for ${user.plan} plan.`,
        upgrade_required: true
      };
    }

    return { allowed: true };
  }

  // Check if user can regenerate a description
  canRegenerateDescription(user, metadata) {
    const { description_id } = metadata;
    
    if (user.plan_config.regenerations_per_description === -1) {
      return { allowed: true }; // Unlimited
    }

    // Count regenerations for this specific description
    const regenerationsForDescription = usageLogs.filter(log => 
      log.user_email === user.email && 
      log.action === 'regenerate_description' && 
      log.metadata.description_id === description_id
    ).length;

    if (regenerationsForDescription >= user.plan_config.regenerations_per_description) {
      return {
        allowed: false,
        reason: `Regeneration limit reached for this description. ${user.plan} plan allows ${user.plan_config.regenerations_per_description} regenerations per description.`,
        upgrade_required: true
      };
    }

    return { allowed: true };
  }

  // Check if user can batch generate
  canBatchGenerate(user, metadata) {
    return this.canGenerateDescription(user, metadata);
  }

  // Record usage
  recordUsage(email, action, count = 1, metadata = {}) {
    const user = users.get(email);
    if (!user) return false;

    switch (action) {
      case 'generate_description':
        user.usage_count += count;
        break;
      case 'regenerate_description':
        user.regenerations_used += count;
        break;
    }

    users.set(email, user);
    this.logUsage(email, action, count, metadata);
    return true;
  }

  // Get user info
  getUserInfo(email) {
    const user = users.get(email);
    if (!user) return null;

    return {
      email: user.email,
      plan: user.plan,
      status: user.status,
      usage: {
        descriptions_used: user.usage_count,
        descriptions_limit: user.plan_config.monthly_descriptions,
        descriptions_remaining: user.plan_config.monthly_descriptions - user.usage_count,
        regenerations_per_description: user.plan_config.regenerations_per_description,
        max_batch_size: user.plan_config.max_batch_size
      },
      features: user.plan_config.features,
      reset_date: user.reset_date
    };
  }

  // Helper methods
  getPlanFromVariantId(variantId) {
    const planName = VARIANT_TO_PLAN[variantId] || 'free';
    return PLANS[planName];
  }

  shouldResetUsage(user) {
    return new Date() >= user.reset_date;
  }

  resetUserUsage(user) {
    user.usage_count = 0;
    user.regenerations_used = 0;
    user.reset_date = this.getNextResetDate();
    users.set(user.email, user);
    console.log(`Reset usage for ${user.email}`);
  }

  getNextResetDate() {
    const now = new Date();
    return new Date(now.getFullYear(), now.getMonth() + 1, 1);
  }

  logUsage(email, action, count, metadata) {
    usageLogs.push({
      user_email: email,
      action: action,
      count: count,
      timestamp: new Date(),
      metadata: metadata
    });
  }

  // Get all users (for admin purposes)
  getAllUsers() {
    return Array.from(users.values());
  }

  // Get usage statistics
  getUsageStats() {
    return {
      total_users: users.size,
      active_subscriptions: Array.from(users.values()).filter(u => u.status === 'active').length,
      total_usage_logs: usageLogs.length
    };
  }
}

module.exports = SubscriptionManager;


