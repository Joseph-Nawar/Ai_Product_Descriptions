2025-09-28T07:58:20.282785925Z INFO:     Application startup complete.
2025-09-28T07:58:20.283338826Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-28T07:58:20.929189342Z ==> No open ports detected, continuing to scan...
2025-09-28T07:58:21.111712121Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-28T07:58:21.155311847Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-28T07:58:21.155331207Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-28T07:58:21.155336737Z ✅ Gemini API key loaded successfully
2025-09-28T07:58:21.155341207Z 📊 Using model: gemini-1.5-pro, temperature: 0.8
2025-09-28T07:58:21.155345157Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-28T07:58:21.155348947Z ✅ AI Product Descriptions API started successfully
2025-09-28T07:58:21.155352747Z 🤖 Model: gemini-1.5-pro (Live mode)
2025-09-28T07:58:21.155357088Z 🌡️  Temperature: 0.8
2025-09-28T07:58:21.155360948Z ✅ API key configured - ready for AI generation
2025-09-28T07:58:21.155364658Z 💳 Credit service initialized - rate limiting enabled
2025-09-28T07:58:21.155368318Z 📋 Subscription plans initialized
2025-09-28T07:58:21.155372088Z INFO:     127.0.0.1:38558 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-28T07:58:25.627413472Z ==> Your service is live 🎉
2025-09-28T07:58:25.89981674Z ==> 
2025-09-28T07:58:25.97773362Z ==> ///////////////////////////////////////////////////////////
2025-09-28T07:58:26.053901179Z ==> 
2025-09-28T07:58:26.145605909Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-28T07:58:26.221757049Z ==> 
2025-09-28T07:58:26.300291878Z ==> ///////////////////////////////////////////////////////////
2025-09-28T07:58:27.839739578Z INFO:     34.82.29.197:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-28T07:58:41.38535486Z INFO:     41.238.10.39:0 - "WebSocket /ws/payments" [accepted]
2025-09-28T07:58:41.385698807Z INFO:     connection open
2025-09-28T07:58:48.580761725Z INFO:     connection closed
2025-09-28T07:58:53.60723133Z INFO:     41.238.10.39:0 - "WebSocket /ws/payments" [accepted]
2025-09-28T07:58:53.607387123Z INFO:     connection open
2025-09-28T07:58:53.843286131Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:53.844416536Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T07:58:53.894616907Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:53.956566854Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:53.998025815Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:54.272506202Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T07:58:54.480463052Z WARNING:src.database.deps:Remove from registry failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T07:58:54.48078813Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T07:58:54.481478174Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:54.658638036Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T07:58:54.661244722Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T07:58:54.706736611Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:54.860681068Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T07:58:54.862720442Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T07:58:54.917572954Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:55.064452747Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T07:58:55.066959192Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T07:58:55.107234737Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:55.302939352Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:55.521333639Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:58:55.702922047Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T08:02:30.174096654Z INFO:     41.238.10.39:0 - "OPTIONS /api/generate-batch HTTP/1.1" 200 OK
2025-09-28T08:02:30.467665884Z WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
2025-09-28T08:02:30.467686964Z E0000 00:00:1759046550.467537      57 alts_credentials.cc:93] ALTS creds ignored. Not running on GCP and untrusted ALTS is not enabled.
2025-09-28T08:02:33.677733757Z ERROR:root:Generation error for product row_0: Gemini API Error (RETRY_EXHAUSTED): All retry attempts exhausted: RetryError[<Future at 0x7fb3b95e4a50 state=finished raised NotFound>]
2025-09-28T08:02:33.677759837Z ERROR:root:Error type: Exception
2025-09-28T08:02:33.677786158Z WARNING:root:All retry attempts exhausted for product: AeroFlex Ergonomic Office Chair
2025-09-28T08:02:33.696340702Z INFO:     41.238.10.39:0 - "POST /api/generate-batch HTTP/1.1" 200 OK
2025-09-28T08:02:33.78355627Z WARNING:src.database.deps:Remove from registry failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T08:02:33.783951159Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T08:02:33.784443639Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T08:02:33.942813687Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T08:02:33.976431249Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T08:02:34.402313409Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T08:02:35.001720136Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T08:02:35.152980249Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK