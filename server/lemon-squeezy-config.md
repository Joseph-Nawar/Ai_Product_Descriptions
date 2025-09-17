# Lemon Squeezy Product Configuration

## Setting Up Your 3-Tier Subscription System

### 1. Create Products in Lemon Squeezy Dashboard

Go to **Products → New Product** and create these three products:

#### **Free Plan**
- **Name**: "Free Plan"
- **Description**: "2 AI descriptions per month, 1 regeneration per description, max 5 products per batch"
- **Price**: $0/month
- **Billing**: Monthly
- **Variant Name**: "Free"
- **Note the Variant ID**: `free_variant_id` (replace with actual ID)

#### **Basic Plan**
- **Name**: "Basic Plan" 
- **Description**: "10 AI descriptions per month, 3 regenerations per description, max 20 products per batch, advanced AI model"
- **Price**: $5/month
- **Billing**: Monthly
- **Variant Name**: "Basic"
- **Note the Variant ID**: `basic_variant_id` (replace with actual ID)

#### **Pro Plan**
- **Name**: "Pro Plan"
- **Description**: "100 AI descriptions per month, unlimited regenerations, max 100 products per batch, premium AI model, custom prompts"
- **Price**: $20/month
- **Billing**: Monthly
- **Variant Name**: "Pro"
- **Note the Variant ID**: `pro_variant_id` (replace with actual ID)

### 2. Update Variant IDs in Code

After creating the products, update the variant IDs in `server/subscription-manager.js`:

```javascript
const VARIANT_TO_PLAN = {
  '1234567': 'free',      // Replace with actual Free variant ID
  '2345678': 'basic',     // Replace with actual Basic variant ID  
  '3456789': 'pro'        // Replace with actual Pro variant ID
};
```

### 3. Webhook Configuration

In Lemon Squeezy Dashboard → Settings → Webhooks:

- **Callback URL**: `https://your-domain.com/api/webhook`
- **Signing Secret**: Set a secure secret and update your `.env` file
- **Events to Monitor**:
  - `subscription_created`
  - `subscription_updated` 
  - `subscription_cancelled`
  - `order_created`

### 4. Test the Setup

1. **Create test subscriptions** for each tier
2. **Verify webhook events** are received correctly
3. **Test usage limits** with your frontend
4. **Test upgrade/downgrade** flows

### 5. Usage Limits Summary

| Feature | Free | Basic | Pro |
|---------|------|-------|-----|
| Monthly Descriptions | 2 | 10 | 100 |
| Regenerations per Description | 1 | 3 | Unlimited |
| Max Batch Size | 5 | 20 | 100 |
| AI Model | Basic | Advanced | Premium |
| Support | Community | Email | Priority |
| Custom Prompts | ❌ | ❌ | ✅ |
| API Access | ❌ | ❌ | ✅ |
| White Label | ❌ | ❌ | ✅ |

### 6. Frontend Integration Points

Your frontend should:

1. **Check usage before actions**:
   ```javascript
   const canGenerate = await subscriptionService.canGenerateDescriptions(email, batchSize);
   ```

2. **Show usage limits**:
   ```javascript
   const userInfo = await subscriptionService.getUserInfo(email);
   // Display: "5/10 descriptions used this month"
   ```

3. **Handle limit reached**:
   ```javascript
   if (!canGenerate.allowed && canGenerate.upgrade_required) {
     // Show upgrade prompt
   }
   ```

4. **Record usage after success**:
   ```javascript
   await subscriptionService.recordUsage(email, 'generate_description', count);
   ```

### 7. Production Deployment

1. **Deploy webhook server** to cloud service (Vercel, Railway, Heroku)
2. **Set up production database** (PostgreSQL, MongoDB)
3. **Update webhook URL** in Lemon Squeezy
4. **Test with real payments** (small amounts)
5. **Monitor webhook delivery** in Lemon Squeezy dashboard

### 8. Monitoring & Analytics

Track these metrics:
- Subscription conversion rates
- Usage patterns by plan
- Churn rates
- Revenue per user
- Feature adoption rates

Use the admin endpoints:
- `GET /api/admin/users` - All users
- `GET /api/admin/stats` - Usage statistics


