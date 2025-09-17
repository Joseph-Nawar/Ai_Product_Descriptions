* [ ] DB live: alembic upgrade head succeeds against prod DB.
* [ ] No in-memory stores remain: grep for dict() or placeholder repos; all replaced with SQLAlchemy repos.
* [ ] Auth: calling a protected API without token → 401; with valid Firebase token → 200.
* [ ] CORS: only the configured prod origins are allowed; OPTIONS preflight succeeds.
* [ ] Webhook:
  * [ ] Valid signature → 200, webhook_events row created, subscriptions updated, transactions recorded.
  * [ ] Replay same event → 200, no duplicate DB rows (unique constraint enforced).
* [ ] Subscription states: events subscription_created, subscription_updated, subscription_cancelled/expired map to correct status and current_period_end.
* [ ] Entitlements: active subscription → paid endpoints return 200; inactive → 402/403 with clear message.
* [ ] Plans: /api/payment/plans returns the monthly/yearly variant IDs from env (not hardcoded).
* [ ] Secrets: verified all secrets only in env; repo contains no secrets.
* [ ] Security headers present in responses; HSTS enabled behind HTTPS.
* [ ] Rate limiting works (toggle via env).
* [ ] Health checks: /healthz ok; /readyz checks DB connectivity.
* [ ] Logs: webhook id, event type, user id (if known), subscription status transitions are logged in JSON.
* [ ] Sentry (if DSN provided) initializes without error.
