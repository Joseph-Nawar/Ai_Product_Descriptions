# Lemon Squeezy Payment Service Setup Guide

This guide will help you set up the Lemon Squeezy payment service for the AI Product Descriptions application.

## Prerequisites

1. **Lemon Squeezy Account**: Sign up at [lemon squeezy](https://lemonsqueezy.com)
2. **Store Setup**: Create a store in your Lemon Squeezy dashboard
3. **Products/Variants**: Create subscription products with variants for each plan

## Environment Configuration

### 1. Copy Environment Template

```bash
cp env.example .env
```

### 2. Configure Lemon Squeezy Variables

Add the following variables to your `.env` file:

```env
# Lemon Squeezy Configuration
LEMON_SQUEEZY_API_KEY=your_api_key_here
LEMON_SQUEEZY_WEBHOOK_SECRET=your_webhook_secret_here
LEMON_SQUEEZY_STORE_ID=your_store_id_here
LEMON_SQUEEZY_TEST_MODE=true
```

### 3. Get Your Lemon Squeezy Credentials

#### API Key
1. Go to your Lemon Squeezy dashboard
2. Navigate to Settings → API
3. Create a new API key
4. Copy the key to `LEMON_SQUEEZY_API_KEY`

#### Store ID
1. In your Lemon Squeezy dashboard, go to Settings → General
2. Copy your Store ID to `LEMON_SQUEEZY_STORE_ID`

#### Webhook Secret
1. Go to Settings → Webhooks
2. Create a new webhook endpoint: `https://yourdomain.com/api/payment/webhook`
3. Copy the webhook secret to `LEMON_SQUEEZY_WEBHOOK_SECRET`

## Product Setup in Lemon Squeezy

### 1. Create Subscription Products

Create the following products in your Lemon Squeezy store:

#### Basic Plan ($9.99/month)
- **Name**: AI Descriptions Basic Plan
- **Price**: $9.99
- **Billing**: Monthly
- **Description**: 100 AI generations per month

#### Pro Plan ($29.99/month)
- **Name**: AI Descriptions Pro Plan
- **Price**: $29.99
- **Billing**: Monthly
- **Description**: 1000 AI generations per month

#### Enterprise Plan ($99.99/month)
- **Name**: AI Descriptions Enterprise Plan
- **Price**: $99.99
- **Billing**: Monthly
- **Description**: 10000 AI generations per month

### 2. Get Variant IDs

After creating products, you'll need to get the variant IDs:

1. Go to each product in your dashboard
2. Copy the variant ID from the URL or product details
3. Update the `lemon_squeezy_variant_id` in the code:

```python
# In backend/src/payments/lemon_squeezy.py
self.default_plans = {
    "basic": SubscriptionPlans(
        # ... other fields ...
        lemon_squeezy_variant_id="your_basic_variant_id_here"
    ),
    "pro": SubscriptionPlans(
        # ... other fields ...
        lemon_squeezy_variant_id="your_pro_variant_id_here"
    ),
    "enterprise": SubscriptionPlans(
        # ... other fields ...
        lemon_squeezy_variant_id="your_enterprise_variant_id_here"
    )
}
```

## Webhook Configuration

### 1. Set Up Webhook Endpoint

The webhook endpoint is automatically available at:
```
POST /api/payment/webhook
```

### 2. Configure in Lemon Squeezy

1. Go to Settings → Webhooks in your Lemon Squeezy dashboard
2. Add webhook URL: `https://yourdomain.com/api/payment/webhook`
3. Select events to listen for:
   - `order_created`
   - `subscription_created`
   - `subscription_updated`
   - `subscription_cancelled`
   - `subscription_resumed`
   - `subscription_paused`

### 3. Test Webhook

Use the webhook testing tool in Lemon Squeezy dashboard to verify your endpoint is working.

## Database Integration

### Current Implementation

The current implementation uses in-memory storage for demonstration purposes. For production, you should integrate with a proper database.

### Recommended Database Schema

```sql
-- User Credits Table
CREATE TABLE user_credits (
    user_id VARCHAR(255) PRIMARY KEY,
    current_credits INTEGER DEFAULT 0,
    total_credits_purchased INTEGER DEFAULT 0,
    total_credits_used INTEGER DEFAULT 0,
    subscription_tier VARCHAR(50) DEFAULT 'free',
    subscription_plan_id VARCHAR(100),
    subscription_expires_at TIMESTAMP,
    last_credit_refill TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Payment History Table
CREATE TABLE payment_history (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    status VARCHAR(50) DEFAULT 'pending',
    payment_method VARCHAR(50) DEFAULT 'lemon_squeezy',
    lemon_squeezy_order_id VARCHAR(255),
    lemon_squeezy_subscription_id VARCHAR(255),
    credits_awarded INTEGER DEFAULT 0,
    subscription_plan_id VARCHAR(100),
    metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user_credits(user_id)
);

-- Subscription Plans Table
CREATE TABLE subscription_plans (
    id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    interval VARCHAR(20) DEFAULT 'month',
    credits_per_month INTEGER DEFAULT 0,
    max_products_per_batch INTEGER DEFAULT 0,
    features JSON,
    lemon_squeezy_variant_id VARCHAR(255),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## API Endpoints

### Payment Endpoints

- `GET /api/payment/plans` - Get available subscription plans
- `POST /api/payment/checkout` - Create checkout session
- `POST /api/payment/webhook` - Handle Lemon Squeezy webhooks
- `GET /api/payment/user/credits` - Get user credits
- `POST /api/payment/user/credits/check` - Check if user can generate
- `POST /api/payment/user/credits/deduct` - Deduct credits after generation
- `GET /api/payment/user/subscription` - Get user subscription details
- `GET /api/payment/health` - Payment service health check

### Integration with AI Endpoints

The payment system is integrated with the existing AI generation endpoints:

- `POST /api/generate-description` - Now requires authentication and checks credits
- `POST /api/generate-batch` - Now requires authentication and checks credits

## Testing

### 1. Test Mode

Set `LEMON_SQUEEZY_TEST_MODE=true` in your environment for testing.

### 2. Test Credit System

```bash
# Check user credits
curl -H "Authorization: Bearer YOUR_FIREBASE_TOKEN" \
     http://localhost:8000/api/payment/user/credits

# Test generation (will deduct credits)
curl -X POST \
     -H "Authorization: Bearer YOUR_FIREBASE_TOKEN" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "title=Test Product&features=Great features&category=electronics" \
     http://localhost:8000/api/generate-description
```

### 3. Test Webhook

Use the webhook testing tool in Lemon Squeezy dashboard or send a test payload:

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -H "x-signature: YOUR_WEBHOOK_SIGNATURE" \
     -d '{"meta":{"event_name":"order_created"},"data":{"id":"test_order"}}' \
     http://localhost:8000/api/payment/webhook
```

## Security Considerations

1. **Webhook Signature Verification**: Always verify webhook signatures
2. **Rate Limiting**: Implement proper rate limiting based on subscription tiers
3. **Credit Validation**: Always validate credits before processing
4. **Error Handling**: Implement comprehensive error handling and logging
5. **Data Validation**: Validate all incoming data from Lemon Squeezy

## Production Deployment

### 1. Environment Variables

Ensure all production environment variables are set correctly:

```env
LEMON_SQUEEZY_TEST_MODE=false
LEMON_SQUEEZY_API_KEY=your_production_api_key
LEMON_SQUEEZY_WEBHOOK_SECRET=your_production_webhook_secret
LEMON_SQUEEZY_STORE_ID=your_production_store_id
```

### 2. Database Integration

Replace the placeholder database methods with actual database operations:

- `get_user_credits()` - Query your database
- `update_user_credits()` - Update your database
- `add_payment_history()` - Insert into your database

### 3. Monitoring

Set up monitoring for:
- Webhook processing success/failure rates
- Credit deduction accuracy
- Payment processing errors
- API response times

### 4. Backup and Recovery

Implement proper backup strategies for:
- User credit data
- Payment history
- Subscription status

## Troubleshooting

### Common Issues

1. **Webhook Signature Verification Fails**
   - Check that `LEMON_SQUEEZY_WEBHOOK_SECRET` matches your dashboard
   - Ensure webhook payload is not modified

2. **Credit Deduction Fails**
   - Verify user exists in database
   - Check credit balance before deduction
   - Ensure proper error handling

3. **Checkout Session Creation Fails**
   - Verify `LEMON_SQUEEZY_STORE_ID` is correct
   - Check that variant IDs exist
   - Ensure API key has proper permissions

4. **Rate Limiting Issues**
   - Check subscription tier assignment
   - Verify rate limit configuration
   - Monitor API usage patterns

### Logs

Check application logs for detailed error information:

```bash
# View logs
tail -f logs/app.log

# Filter payment-related logs
grep "payment\|credit\|webhook" logs/app.log
```

## Support

For issues related to:
- **Lemon Squeezy API**: Contact Lemon Squeezy support
- **Payment Integration**: Check the application logs and webhook processing
- **Credit System**: Verify database operations and user authentication

