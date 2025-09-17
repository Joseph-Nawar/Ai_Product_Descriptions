// server/index.js
// Lemon Squeezy webhook receiver – LOCAL TESTING
// Runs on http://localhost:3001/api/webhook
// Verifies HMAC-SHA256 hex digest from 'X-Signature' header against raw body.

const express = require('express');
const crypto = require('crypto');
const SubscriptionManager = require('./subscription-manager');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3001;
const subscriptionManager = new SubscriptionManager();

// Middleware for JSON parsing (for non-webhook routes)
app.use(express.json());

// Use raw body for signature verification (no JSON parser here)
app.post('/api/webhook', express.raw({ type: '*/*' }), async (req, res) => {
  try {
    const secret = process.env.LEMON_SQUEEZY_WEBHOOK_SECRET;
    if (!secret) {
      console.error('Missing LEMON_SQUEEZY_WEBHOOK_SECRET');
      return res.status(500).json({ error: 'Server misconfigured' });
    }

    const rawBody = req.body; // Buffer
    if (!rawBody || !Buffer.isBuffer(rawBody)) {
      return res.status(400).json({ error: 'Expected raw body' });
    }

    const header = req.get('X-Signature') || '';
    if (!header) {
      console.log('Missing X-Signature header');
      return res.status(400).json({ error: 'Missing X-Signature' });
    }

    // Lemon Squeezy sends signature as hex string directly
    const digest = crypto.createHmac('sha256', secret).update(rawBody).digest('hex');

    if (digest !== header) {
      console.warn('Invalid signature');
      return res.status(400).json({ error: 'Invalid signature' });
    }

    // Signature valid → parse JSON and handle
    const payload = JSON.parse(rawBody.toString('utf8'));
    const eventName = payload?.meta?.event_name || 'unknown_event';
    console.log('[LS WEBHOOK OK]', eventName, { id: payload?.data?.id });

    // Handle webhook events
    await subscriptionManager.handleWebhookEvent(eventName, payload);

    return res.status(200).json({ ok: true, event: eventName });
  } catch (err) {
    console.error('Webhook error:', err);
    return res.status(400).json({ error: 'Bad request' });
  }
});

// API endpoints for your frontend to check usage and limits
app.get('/api/user/:email', (req, res) => {
  const { email } = req.params;
  const userInfo = subscriptionManager.getUserInfo(email);
  
  if (!userInfo) {
    return res.status(404).json({ error: 'User not found' });
  }
  
  res.json(userInfo);
});

// Check if user can perform an action
app.post('/api/check-usage', (req, res) => {
  const { email, action, metadata } = req.body;
  
  if (!email || !action) {
    return res.status(400).json({ error: 'Email and action are required' });
  }
  
  const result = subscriptionManager.canUserPerformAction(email, action, metadata);
  res.json(result);
});

// Record usage after successful action
app.post('/api/record-usage', (req, res) => {
  const { email, action, count, metadata } = req.body;
  
  if (!email || !action) {
    return res.status(400).json({ error: 'Email and action are required' });
  }
  
  const success = subscriptionManager.recordUsage(email, action, count, metadata);
  res.json({ success });
});

// Admin endpoints (in production, add authentication)
app.get('/api/admin/users', (req, res) => {
  const users = subscriptionManager.getAllUsers();
  res.json(users);
});

app.get('/api/admin/stats', (req, res) => {
  const stats = subscriptionManager.getUsageStats();
  res.json(stats);
});

// Health check
app.get('/health', (_req, res) => res.status(200).json({ ok: true }));

app.listen(PORT, () => {
  console.log(`Webhook server (LOCAL TESTING) listening on http://localhost:${PORT}`);
  console.log(`API endpoints available:`);
  console.log(`  GET  /api/user/:email - Get user info and usage`);
  console.log(`  POST /api/check-usage - Check if user can perform action`);
  console.log(`  POST /api/record-usage - Record usage after action`);
  console.log(`  GET  /api/admin/users - Get all users (admin)`);
  console.log(`  GET  /api/admin/stats - Get usage statistics (admin)`);
});