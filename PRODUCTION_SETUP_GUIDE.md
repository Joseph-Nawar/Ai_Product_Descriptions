# 🚀 Production Setup Guide

This guide will help you complete the setup for production deployment of your AI Product Descriptions application.

## 📋 Current Status

✅ **Completed:**
- Backend environment configuration
- Frontend environment configuration
- Firebase authentication setup
- Lemon Squeezy API key configured

⚠️ **Still Needed:**
- Lemon Squeezy store products and variant IDs
- Webhook secret (after deployment)
- Database setup and migrations
- Production domain configuration

## 🔧 Step-by-Step Setup Instructions

### 1. Lemon Squeezy Store Setup

#### A. Create Subscription Products

1. **Go to your Lemon Squeezy Dashboard:**
   - Visit: https://app.lemonsqueezy.com/
   - Navigate to your store (ID: 221931)

2. **Create Subscription Products:**

   **Basic Plan ($9.99/month):**
   - Name: "AI Descriptions Basic Plan"
   - Price: $9.99
   - Billing: Monthly
   - Description: "100 AI generations per month"
   - Features: Enhanced AI generation, email support

   **Pro Plan ($29.99/month):**
   - Name: "AI Descriptions Pro Plan"
   - Price: $29.99
   - Billing: Monthly
   - Description: "1000 AI generations per month"
   - Features: Priority support, custom templates, API access

   **Enterprise Plan ($99.99/month):**
   - Name: "AI Descriptions Enterprise Plan"
   - Price: $99.99
   - Billing: Monthly
   - Description: "10000 AI generations per month"
   - Features: White label, custom integrations, unlimited access

3. **Get Variant IDs:**
   - After creating each product, copy the **Variant ID** from the product URL
   - Update your `backend/.env` file:
   ```bash
   LEMON_SQUEEZY_MONTHLY_VARIANT_ID=your_actual_variant_id_here
   LEMON_SQUEEZY_YEARLY_VARIANT_ID=your_yearly_variant_id_here
   ```

#### B. Set Up Webhooks (After Deployment)

1. **Deploy your application first** (see deployment section below)
2. **Configure webhook endpoint:**
   - Go to Settings → Webhooks in Lemon Squeezy
   - Add webhook URL: `https://yourdomain.com/api/payment/webhook`
   - Select events: `order_created`, `subscription_created`, `subscription_updated`, `subscription_cancelled`
   - Copy the webhook secret
   - Update your `backend/.env`:
   ```bash
   LEMON_SQUEEZY_WEBHOOK_SECRET=your_webhook_secret_here
   ```

### 2. Database Setup

#### Option A: SQLite (Development - Default)
No additional setup required. The application will create the database automatically.

#### Option B: PostgreSQL (Production Recommended)

1. **Install PostgreSQL:**
   ```bash
   # Windows (using Chocolatey)
   choco install postgresql
   
   # Or download from: https://www.postgresql.org/download/windows/
   ```

2. **Create Database:**
   ```sql
   CREATE DATABASE ai_descriptions;
   CREATE USER ai_user WITH PASSWORD 'your_secure_password';
   GRANT ALL PRIVILEGES ON DATABASE ai_descriptions TO ai_user;
   ```

3. **Update backend/.env:**
   ```bash
   DATABASE_URL=postgresql+psycopg://ai_user:your_secure_password@localhost:5432/ai_descriptions
   ```

4. **Run Database Migrations:**
   ```bash
   cd backend
   python -m alembic upgrade head
   ```

### 3. Security Configuration

#### A. Generate Secure Secret Key
```bash
# Generate a secure secret key
python -c "import secrets; print(secrets.token_urlsafe(32))"
```
Update `SECRET_KEY` in `backend/.env` with the generated key.

#### B. Update CORS Origins
Update `CORS_ALLOWED_ORIGINS` in `backend/.env` with your production domains:
```bash
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com,http://localhost:5173
```

### 4. Production Deployment

#### A. Backend Deployment

1. **Set Production Environment:**
   ```bash
   # Update backend/.env
   ENV=production
   LEMON_SQUEEZY_TEST_MODE=false
   ```

2. **Deploy to your server:**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Run migrations
   python -m alembic upgrade head
   
   # Start with production server
   python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

#### B. Frontend Deployment

1. **Update API URL:**
   ```bash
   # Update frontend/.env
   VITE_API_BASE_URL=https://yourdomain.com
   VITE_NODE_ENV=production
   VITE_DEBUG_MODE=false
   ```

2. **Build and Deploy:**
   ```bash
   npm run build
   # Deploy the 'dist' folder to your hosting service
   ```

### 5. Testing Your Setup

#### A. Run Integration Tests
```bash
cd backend
python test_payment_integration.py
```

#### B. Test Authentication
1. Start both frontend and backend
2. Try signing up with Google
3. Verify user is created in Firebase

#### C. Test Payment Flow
1. Go to pricing page
2. Select a plan
3. Complete checkout (use test mode)
4. Verify webhook processing

## 🔍 Troubleshooting

### Common Issues

1. **Firebase Authentication Not Working:**
   - Verify Firebase project ID matches in both frontend and backend
   - Check that Firebase Authentication is enabled in Firebase Console
   - Ensure Google OAuth is configured

2. **Payment Integration Issues:**
   - Verify Lemon Squeezy API key is correct
   - Check that variant IDs are properly set
   - Ensure webhook URL is accessible

3. **Database Connection Issues:**
   - Verify DATABASE_URL format
   - Check database server is running
   - Ensure user has proper permissions

4. **CORS Issues:**
   - Update CORS_ALLOWED_ORIGINS with your domain
   - Check that frontend URL matches exactly

### Getting Help

1. **Check Logs:**
   ```bash
   # Backend logs
   tail -f backend/logs/app.log
   
   # Frontend console (browser dev tools)
   ```

2. **Test Individual Components:**
   ```bash
   # Test database connection
   python backend/test_database_models.py
   
   # Test payment service
   python backend/test_payment_integration.py
   ```

## 📊 Production Checklist

### Pre-Deployment
- [ ] Lemon Squeezy products created and variant IDs configured
- [ ] Database set up and migrations run
- [ ] Secure SECRET_KEY generated
- [ ] CORS origins updated for production
- [ ] Environment variables configured

### Post-Deployment
- [ ] Webhook endpoint configured in Lemon Squeezy
- [ ] Webhook secret added to environment
- [ ] Test authentication flow
- [ ] Test payment flow end-to-end
- [ ] Monitor logs for errors
- [ ] Set up monitoring and alerting

## 🎯 Next Steps

1. **Complete Lemon Squeezy setup** (create products, get variant IDs)
2. **Set up database** (PostgreSQL recommended for production)
3. **Deploy to production** (your preferred hosting service)
4. **Configure webhooks** (after deployment)
5. **Test everything** (authentication, payments, AI generation)

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review application logs
3. Verify all environment variables are set correctly
4. Test individual components using the provided test scripts

Your application is well-architected and should work smoothly once these final configuration steps are completed!
