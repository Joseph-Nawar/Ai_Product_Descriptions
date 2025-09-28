2025-09-28T16:57:34.972855179Z [notice] A new release of pip is available: 25.1.1 -> 25.2
2025-09-28T16:57:34.972858019Z [notice] To update, run: pip install --upgrade pip
2025-09-28T16:57:39.229839409Z ==> Uploading build...
2025-09-28T16:57:55.461548591Z ==> Uploaded in 12.2s. Compression took 4.1s
2025-09-28T16:57:55.55831944Z ==> Build successful 🎉
2025-09-28T16:57:58.07393248Z ==> Deploying...
2025-09-28T16:58:31.976736762Z ==> Running '  cd backend && python fix_database.py && python run_migrations.py && uvicorn src.main:app --host 0.0.0.0 --port $PORT'
2025-09-28T16:58:34.416684575Z 🔧 Database Fix Script
2025-09-28T16:58:34.416729316Z ==================================================
2025-09-28T16:58:34.416735936Z ✅ Found database URL: postgresql://ai_descriptions_db_user:ijlatK7LezNTw...
2025-09-28T16:58:34.416739126Z ✅ Database connection established
2025-09-28T16:58:34.416741617Z 🔄 Creating subscriptions table...
2025-09-28T16:58:34.416743957Z 🔄 Creating indexes...
2025-09-28T16:58:34.416746527Z 🔄 Creating webhook_events table...
2025-09-28T16:58:34.416748807Z 🔄 Creating transactions table...
2025-09-28T16:58:34.416751347Z 🔄 Creating usage table...
2025-09-28T16:58:34.416753677Z 🔄 Creating user_credits table...
2025-09-28T16:58:34.416756257Z ✅ All tables created successfully!
2025-09-28T16:58:34.416758667Z 🎉 Database fix completed successfully!
2025-09-28T16:58:41.891165778Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-28T16:58:41.891470567Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-28T16:58:41.891610481Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-28T16:58:41.891617212Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-28T16:58:42.131518043Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-28T16:58:42.131546734Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-28T16:58:42.131551194Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-28T16:58:42.131650727Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-28T16:58:42.18030789Z INFO  [alembic.runtime.migration] Running upgrade  -> 0001_initial, initial tables
2025-09-28T16:58:42.18032892Z INFO  [alembic.runtime.migration] Running upgrade  -> 0001_initial, initial tables
2025-09-28T16:58:42.782685007Z 🔄 Checking current database state...
2025-09-28T16:58:42.782747739Z 🔄 Running database migrations...
2025-09-28T16:58:42.782755669Z ⚠️ Migration error: (psycopg2.errors.DuplicateTable) relation "users" already exists
2025-09-28T16:58:42.78276075Z 
2025-09-28T16:58:42.78276575Z [SQL: 
2025-09-28T16:58:42.78277081Z CREATE TABLE users (
2025-09-28T16:58:42.78277479Z 	id VARCHAR NOT NULL, 
2025-09-28T16:58:42.78277897Z 	email VARCHAR, 
2025-09-28T16:58:42.78278351Z 	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
2025-09-28T16:58:42.78278767Z 	PRIMARY KEY (id)
2025-09-28T16:58:42.78279176Z )
2025-09-28T16:58:42.782795911Z 
2025-09-28T16:58:42.782800161Z ]
2025-09-28T16:58:42.782804251Z (Background on this error at: https://sqlalche.me/e/20/f405)
2025-09-28T16:58:42.782808701Z 🔄 Attempting to continue with existing schema...
2025-09-28T16:58:42.782813351Z ❌ Migration failed: cannot import name 'get_db' from 'src.database.connection' (/opt/render/project/src/backend/src/database/connection.py)
2025-09-28T16:58:42.782817741Z 🔄 Attempting to use simple database initialization...
2025-09-28T16:58:42.782822531Z 🔄 Initializing database...
2025-09-28T16:58:42.782826421Z ✅ Database initialized successfully!
2025-09-28T16:58:42.782830352Z ✅ Database initialized with simple script!
2025-09-28T16:59:00.015299413Z ==> No open ports detected, continuing to scan...
2025-09-28T16:59:00.25749548Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-28T16:59:02.882369851Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-28T16:59:02.882393551Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-28T16:59:02.882398982Z   warnings.warn(message, UserWarning)
2025-09-28T16:59:03.067165929Z INFO:     Started server process [56]
2025-09-28T16:59:03.067189009Z INFO:     Waiting for application startup.
2025-09-28T16:59:03.659343213Z INFO:     Application startup complete.
2025-09-28T16:59:03.659879279Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-28T16:59:04.674302791Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-28T16:59:04.674323872Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-28T16:59:04.674327792Z ✅ Gemini API key loaded successfully
2025-09-28T16:59:04.674330642Z 📊 Using model: gemini-flash-latest, temperature: 0.8
2025-09-28T16:59:04.674333442Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-28T16:59:04.674336492Z ✅ Gemini model 'gemini-flash-latest' configured successfully
2025-09-28T16:59:04.674338962Z ✅ AI Product Descriptions API started successfully
2025-09-28T16:59:04.674341762Z 🤖 Model: gemini-flash-latest (Live mode)
2025-09-28T16:59:04.674344862Z 🌡️  Temperature: 0.8
2025-09-28T16:59:04.674347522Z ✅ API key configured - ready for AI generation
2025-09-28T16:59:04.674350363Z 💳 Credit service initialized - rate limiting enabled
2025-09-28T16:59:04.674353232Z 📋 Subscription plans initialized
2025-09-28T16:59:04.674355503Z INFO:     127.0.0.1:42734 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-28T16:59:08.866064456Z ==> Your service is live 🎉
2025-09-28T16:59:08.945625505Z ==> 
2025-09-28T16:59:09.022698775Z ==> ///////////////////////////////////////////////////////////
2025-09-28T16:59:09.097578175Z ==> 
2025-09-28T16:59:09.174186294Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-28T16:59:09.314040813Z ==> 
2025-09-28T16:59:09.390778972Z ==> ///////////////////////////////////////////////////////////
2025-09-28T16:59:10.543982224Z INFO:     34.168.108.203:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-28T16:59:42.735395223Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:42.740482024Z INFO:     41.238.10.39:0 - "WebSocket /ws/payments" [accepted]
2025-09-28T16:59:42.740961128Z INFO:     connection open
2025-09-28T16:59:42.858692788Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:42.860046228Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:43.013621851Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T16:59:43.034275873Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T16:59:43.573990842Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:43.574298101Z ERROR:src.payments.endpoints:Error getting user subscription: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T16:59:43.57493639Z WARNING:src.database.deps:Rollback failed: Method 'rollback()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T16:59:43.57495782Z ERROR:src.database.deps:Database session error: 500: Failed to get user subscription: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T16:59:43.575156626Z WARNING:src.database.deps:Close failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T16:59:43.575559858Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 500 Internal Server Error
2025-09-28T16:59:43.581228026Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:43.801241208Z ERROR:src.payments.endpoints:Error getting user subscription: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T16:59:43.801400133Z WARNING:src.database.deps:Rollback failed: Method 'rollback()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T16:59:43.801439044Z ERROR:src.database.deps:Database session error: 500: Failed to get user subscription: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T16:59:43.801545687Z WARNING:src.database.deps:Close failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T16:59:43.801617999Z WARNING:src.database.deps:Remove from registry failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T16:59:43.801991381Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 500 Internal Server Error
2025-09-28T16:59:43.802628129Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:43.963208189Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:43.966510457Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T16:59:43.968766824Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T16:59:44.008147402Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:44.176990877Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:44.179099839Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T16:59:44.181699296Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T16:59:44.202544964Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:44.428932085Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:44.621075681Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:44.849615626Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:48.60067573Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/plans HTTP/1.1" 200 OK
2025-09-28T16:59:48.787128827Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:48.879286049Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T16:59:49.09757486Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T16:59:49.100087744Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:49.100770464Z INFO:     41.238.10.39:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-28T16:59:49.246291258Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:49.248212115Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T16:59:49.267627481Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T16:59:49.269864157Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:49.800149196Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:49.80197034Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T16:59:49.804624949Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T16:59:49.884174057Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:52.64746638Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/checkout HTTP/1.1" 200 OK
2025-09-28T16:59:53.228550885Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:53.232731609Z 🎯 STEP 1: CREATE_CHECKOUT ENDPOINT CALLED
2025-09-28T16:59:53.293434228Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T16:59:53.293453139Z Request data: variant_id='1013286' success_url='https://www.productgeniepro.com/billing?success=true' cancel_url='https://www.productgeniepro.com/pricing?cancelled=true'
2025-09-28T16:59:53.293457019Z Variant ID: 1013286
2025-09-28T16:59:53.293460839Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-28T16:59:53.293463549Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-28T16:59:53.293466449Z 🎯 STEP 2: GETTING CLIENT INFO
2025-09-28T16:59:53.293470319Z Client info: {'ip_address': '41.238.10.39', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36', 'correlation_id': 'ea63afe5-006a-41ba-bcd4-e515c5be2103'}
2025-09-28T16:59:53.293475949Z 🎯 STEP 3: EXTRACTING AUTH DATA
2025-09-28T16:59:53.29347852Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:53.29348087Z User email: ziad321hussein@gmail.com
2025-09-28T16:59:53.29348327Z 🎯 STEP 4: VALIDATING USER
2025-09-28T16:59:53.29348583Z ✅ STEP 4 SUCCESS: User validated
2025-09-28T16:59:53.29348818Z 🎯 STEP 5: VALIDATING VARIANT ID
2025-09-28T16:59:53.29349056Z ✅ STEP 5 SUCCESS: Variant ID validated
2025-09-28T16:59:53.29349309Z 🎯 STEP 6: CALLING LEMON_SQUEEZY SERVICE
2025-09-28T16:59:53.29349558Z 🎯 LEMON SQUEEZY PAYLOAD DEBUG 🎯
2025-09-28T16:59:53.29349782Z === VARIABLES ===
2025-09-28T16:59:53.29350008Z Variant ID: 1013286
2025-09-28T16:59:53.29350224Z Store ID: 224253
2025-09-28T16:59:53.293504461Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:53.293506661Z User Email: ziad321hussein@gmail.com
2025-09-28T16:59:53.293509541Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-28T16:59:53.293512001Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-28T16:59:53.293514131Z Test Mode: True
2025-09-28T16:59:53.293516331Z === PAYLOAD BEING SENT ===
2025-09-28T16:59:53.293518441Z {
2025-09-28T16:59:53.293520631Z   "data": {
2025-09-28T16:59:53.293523041Z     "type": "checkouts",
2025-09-28T16:59:53.293525211Z     "attributes": {
2025-09-28T16:59:53.293527391Z       "checkout_options": {
2025-09-28T16:59:53.293529521Z         "embed": false,
2025-09-28T16:59:53.293531611Z         "media": false
2025-09-28T16:59:53.293533821Z       },
2025-09-28T16:59:53.293536071Z       "checkout_data": {
2025-09-28T16:59:53.293538362Z         "email": "ziad321hussein@gmail.com",
2025-09-28T16:59:53.293540762Z         "custom": {
2025-09-28T16:59:53.293544022Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-28T16:59:53.293546332Z         }
2025-09-28T16:59:53.293548702Z       },
2025-09-28T16:59:53.293550912Z       "product_options": {
2025-09-28T16:59:53.293553302Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true"
2025-09-28T16:59:53.293566952Z       }
2025-09-28T16:59:53.293569592Z     },
2025-09-28T16:59:53.293571943Z     "relationships": {
2025-09-28T16:59:53.293574392Z       "store": {
2025-09-28T16:59:53.293576883Z         "data": {
2025-09-28T16:59:53.293579323Z           "type": "stores",
2025-09-28T16:59:53.293581633Z           "id": "224253"
2025-09-28T16:59:53.293584293Z         }
2025-09-28T16:59:53.293586733Z       },
2025-09-28T16:59:53.293589213Z       "variant": {
2025-09-28T16:59:53.293591423Z         "data": {
2025-09-28T16:59:53.293593413Z           "type": "variants",
2025-09-28T16:59:53.293595443Z           "id": "1013286"
2025-09-28T16:59:53.293597493Z         }
2025-09-28T16:59:53.293599853Z       }
2025-09-28T16:59:53.293602263Z     }
2025-09-28T16:59:53.293604533Z   }
2025-09-28T16:59:53.293606784Z }
2025-09-28T16:59:53.293609173Z === HEADERS ===
2025-09-28T16:59:53.293611664Z {
2025-09-28T16:59:53.293616444Z   "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NGQ1OWNlZi1kYmI4LTRlYTUtYjE3OC1kMjU0MGZjZDY5MTkiLCJqdGkiOiJkOGY2NTljZjdhMzA3ZGNjM2RjNTk4ZjNiMzU4YTk3YTczYzdhNGJkNDg2ZDlkM2JhYTE4OGQ4Y2MxMGU1Zjc5YWQzODJkZTgyYjgxNjRiNiIsImlhdCI6MTc1ODgyNzU5MC41NzYwMjcsIm5iZiI6MTc1ODgyNzU5MC41NzYwMjksImV4cCI6MjA3NDM2MDM5MC41NjA2NzcsInN1YiI6IjU1NzE5NjQiLCJzY29wZXMiOltdfQ.v6DQ8CrPGAovPSiYrv6Y3GkQ3DWHPcC0aAiZ9mP5BsXCwXoz5Kf1OY-fLAHC4ikcmx2RYZuLbSrF_Xxa4mvw2exFnJMsODiiuzItzhdVGUwR89IzbFAD6hcto-w0ERT3gjP781BJ-lxa7pzC4tCADeRhAtMPM7MZ7h7g-0JsRjXyNDrM0ArKoN84kiGHojmPCBomBuXTQ-mC_VQEWn8PKxTbZEem7FoyP4ydK46xYQu-naukuPTOZHRQ44Mdz_16JQ7Cda2pbfJo2osSPGaLTYUKvH0-aF2jlZToxGCPPr8LbPsHo1-96W2D6CBkCF0kFd6BQd0PKw64X-2ywolNwyna51cLKvkZuOHrh2Z8XVG0GONxeo6b1mFzgs8PzSkaPJ5Er_vhcRQVhAolOVmBHcZ61FUUJ208hR1FUVzMHlrTWtcTAi6HUjthHZB2ZL0xrIkDcWQPxG38i8ArAslXFLytqDTU3tePixq0WDHHBnBq8XSbleFoLH8rdc0j4v5KEPoJyXUS7MrHkiJ602WwLFPuczEdkRPvnSNeRKhsSlPkO8SiQFdHZ6VLCGQoEWDvm7SL2U6lmOJ2T1imOAGiTveGoliycICl_HQo29Fk0VFMFVa_jei7HCgdsLArClUHceqfx5UTOsrWxcd8zr75ALBqDzIWT9tpG5ifdTappes",
2025-09-28T16:59:53.293619524Z   "Accept": "application/vnd.api+json",
2025-09-28T16:59:53.293622324Z   "Content-Type": "application/vnd.api+json",
2025-09-28T16:59:53.293624884Z   "Version": "2021-07-07"
2025-09-28T16:59:53.293627054Z }
2025-09-28T16:59:53.293629554Z === API ENDPOINT ===
2025-09-28T16:59:53.293631984Z POST https://api.lemonsqueezy.com/v1/checkouts
2025-09-28T16:59:53.293634474Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T16:59:53.293657335Z === RESPONSE ===
2025-09-28T16:59:53.293661035Z Status: Unknown
2025-09-28T16:59:53.293663615Z Response: {
2025-09-28T16:59:53.293666365Z   "jsonapi": {
2025-09-28T16:59:53.293668825Z     "version": "1.0"
2025-09-28T16:59:53.293671295Z   },
2025-09-28T16:59:53.293673806Z   "links": {
2025-09-28T16:59:53.293676915Z     "self": "https://api.lemonsqueezy.com/v1/checkouts/ba9ef527-1226-4e3e-852c-722a3f3701fe"
2025-09-28T16:59:53.293679466Z   },
2025-09-28T16:59:53.293682146Z   "data": {
2025-09-28T16:59:53.293684806Z     "type": "checkouts",
2025-09-28T16:59:53.293687436Z     "id": "ba9ef527-1226-4e3e-852c-722a3f3701fe",
2025-09-28T16:59:53.293690046Z     "attributes": {
2025-09-28T16:59:53.293692766Z       "store_id": 224253,
2025-09-28T16:59:53.293695386Z       "variant_id": 1013286,
2025-09-28T16:59:53.293697886Z       "custom_price": null,
2025-09-28T16:59:53.293700556Z       "product_options": {
2025-09-28T16:59:53.293703176Z         "name": "",
2025-09-28T16:59:53.293705666Z         "description": "",
2025-09-28T16:59:53.293738837Z         "media": [],
2025-09-28T16:59:53.293745668Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true",
2025-09-28T16:59:53.293754698Z         "receipt_button_text": "",
2025-09-28T16:59:53.293757318Z         "receipt_link_url": "",
2025-09-28T16:59:53.293759958Z         "receipt_thank_you_note": "",
2025-09-28T16:59:53.293762628Z         "enabled_variants": [],
2025-09-28T16:59:53.293765998Z         "confirmation_title": "",
2025-09-28T16:59:53.293768908Z         "confirmation_message": "",
2025-09-28T16:59:53.293771458Z         "confirmation_button_text": ""
2025-09-28T16:59:53.293773998Z       },
2025-09-28T16:59:53.293776729Z       "checkout_options": {
2025-09-28T16:59:53.293779329Z         "embed": false,
2025-09-28T16:59:53.293781829Z         "media": false,
2025-09-28T16:59:53.293784569Z         "logo": true,
2025-09-28T16:59:53.293786959Z         "desc": true,
2025-09-28T16:59:53.293789629Z         "discount": true,
2025-09-28T16:59:53.293792559Z         "skip_trial": false,
2025-09-28T16:59:53.293795509Z         "quantity": 1,
2025-09-28T16:59:53.293798159Z         "subscription_preview": true,
2025-09-28T16:59:53.293800509Z         "locale": "en"
2025-09-28T16:59:53.293802839Z       },
2025-09-28T16:59:53.293805209Z       "checkout_data": {
2025-09-28T16:59:53.293807469Z         "email": "ziad321hussein@gmail.com",
2025-09-28T16:59:53.29380985Z         "name": "",
2025-09-28T16:59:53.293812299Z         "billing_address": [],
2025-09-28T16:59:53.2938152Z         "tax_number": "",
2025-09-28T16:59:53.29381771Z         "discount_code": "",
2025-09-28T16:59:53.29382008Z         "custom": {
2025-09-28T16:59:53.29382269Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-28T16:59:53.29382521Z         },
2025-09-28T16:59:53.2938278Z         "variant_quantities": []
2025-09-28T16:59:53.2938305Z       },
2025-09-28T16:59:53.29383292Z       "preview": false,
2025-09-28T16:59:53.29383526Z       "expires_at": null,
2025-09-28T16:59:53.29383791Z       "created_at": "2025-09-28T16:59:53.000000Z",
2025-09-28T16:59:53.29384057Z       "updated_at": "2025-09-28T16:59:53.000000Z",
2025-09-28T16:59:53.293842931Z       "test_mode": true,
2025-09-28T16:59:53.29384756Z       "url": "https://product-genie.lemonsqueezy.com/checkout/custom/ba9ef527-1226-4e3e-852c-722a3f3701fe?signature=c5444b5bb8dc5c1e9978d1b4c7340cb09b62015afd7ed5b17d5883c33e6ac91c"
2025-09-28T16:59:53.293850541Z     },
2025-09-28T16:59:53.293853311Z     "relationships": {
2025-09-28T16:59:53.293855961Z       "store": {
2025-09-28T16:59:53.293858511Z         "links": {
2025-09-28T16:59:53.293860961Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/ba9ef527-1226-4e3e-852c-722a3f3701fe/store",
2025-09-28T16:59:53.293864331Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/ba9ef527-1226-4e3e-852c-722a3f3701fe/relationships/store"
2025-09-28T16:59:53.293867051Z         }
2025-09-28T16:59:53.293869591Z       },
2025-09-28T16:59:53.293872581Z       "variant": {
2025-09-28T16:59:53.293875641Z         "links": {
2025-09-28T16:59:53.293878041Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/ba9ef527-1226-4e3e-852c-722a3f3701fe/variant",
2025-09-28T16:59:53.293880452Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/ba9ef527-1226-4e3e-852c-722a3f3701fe/relationships/variant"
2025-09-28T16:59:53.293883362Z         }
2025-09-28T16:59:53.293885992Z       }
2025-09-28T16:59:53.293888512Z     },
2025-09-28T16:59:53.293891042Z     "links": {
2025-09-28T16:59:53.293893632Z       "self": "https://api.lemonsqueezy.com/v1/checkouts/ba9ef527-1226-4e3e-852c-722a3f3701fe"
2025-09-28T16:59:53.293957084Z     }
2025-09-28T16:59:53.293961384Z   }
2025-09-28T16:59:53.293963854Z }
2025-09-28T16:59:53.293966534Z ✅ STEP 6 SUCCESS: Lemon Squeezy service call successful
2025-09-28T16:59:53.293971204Z Result: {'success': True, 'checkout_url': 'https://product-genie.lemonsqueezy.com/checkout/custom/ba9ef527-1226-4e3e-852c-722a3f3701fe?signature=c5444b5bb8dc5c1e9978d1b4c7340cb09b62015afd7ed5b17d5883c33e6ac91c', 'checkout_id': 'ba9ef527-1226-4e3e-852c-722a3f3701fe'}
2025-09-28T16:59:53.293974214Z INFO:     41.238.10.39:0 - "POST /api/payment/checkout HTTP/1.1" 200 OK
2025-09-28T16:59:53.343919075Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:53.81603977Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T16:59:53.818366939Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T16:59:53.820867593Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T16:59:53.941642743Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T16:59:55.774774333Z INFO:     connection closed
2025-09-28T17:00:30.700929095Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-28T17:00:30.700671+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-28T17:00:30.740558099Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-28T17:00:30.74057795Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '1997', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '9864cc238eae77be-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '6fe4d609-5d0d-49a0', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_payment_success', 'x-forwarded-for': '18.116.135.47, 104.23.197.55, 10.226.169.130', 'x-forwarded-proto': 'https', 'x-request-start': '1759078830697785', 'x-signature': '9b02dbb9f8f5173d50f90bef007adf197c535b07a9d6cb671f46a02811199a30'}
2025-09-28T17:00:30.7405981Z 🎯 BillingService: Processing webhook event_id=9b02dbb9f8f5173d50f90bef007adf197c535b07a9d6cb671f46a02811199a30
2025-09-28T17:00:30.740605421Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_payment_success', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': '7c247e9a-e15d-47e0-8969-9d34cf89362f'}, 'data': {'type': 'subscription-invoices', 'id': '4587819', 'attributes': {'store_id': 224253, 'subscription_id': 1521286, 'customer_id': 6829303, 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'billing_reason': 'initial', 'card_brand': 'visa', 'card_last_four': '4242', 'currency': 'USD', 'currency_rate': '1.00000000', 'status': 'paid', 'status_formatted': 'Paid', 'refunded': False, 'refunded_at': None, 'subtotal': 499, 'discount_total': 0, 'tax': 0, 'tax_inclusive': False, 'total': 499, 'refunded_amount': 0, 'subtotal_usd': 499, 'discount_total_usd': 0, 'tax_usd': 0, 'total_usd': 499, 'refunded_amount_usd': 0, 'subtotal_formatted': '$4.99', 'discount_total_formatted': '$0.00', 'tax_formatted': '$0.00', 'total_formatted': '$4.99', 'refunded_amount_formatted': '$0.00', 'urls': {'invoice_url': 'https://app.lemonsqueezy.com/my-orders/c44d6447-ab0a-4b65-9555-8203132281cd/subscription-invoice/4587819?expires=1759100430&signature=7d70aede83dd43da2b2ea7395691e31250b26304b9cef5a5c1d78fef650656a1'}, 'created_at': '2025-09-28T17:00:27.000000Z', 'updated_at': '2025-09-28T17:00:30.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4587819/store', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4587819/relationships/store'}}, 'subscription': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4587819/subscription', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4587819/relationships/subscription'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4587819/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4587819/relationships/customer'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4587819'}}}
2025-09-28T17:00:30.740620101Z 🎯 BillingService: Event 9b02dbb9f8f5173d50f90bef007adf197c535b07a9d6cb671f46a02811199a30 is new, processing...
2025-09-28T17:00:30.740623581Z 🎯 BillingService: Event type: subscription_payment_success
2025-09-28T17:00:30.740631112Z 🎯 BillingService: Attributes: {'store_id': 224253, 'subscription_id': 1521286, 'customer_id': 6829303, 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'billing_reason': 'initial', 'card_brand': 'visa', 'card_last_four': '4242', 'currency': 'USD', 'currency_rate': '1.00000000', 'status': 'paid', 'status_formatted': 'Paid', 'refunded': False, 'refunded_at': None, 'subtotal': 499, 'discount_total': 0, 'tax': 0, 'tax_inclusive': False, 'total': 499, 'refunded_amount': 0, 'subtotal_usd': 499, 'discount_total_usd': 0, 'tax_usd': 0, 'total_usd': 499, 'refunded_amount_usd': 0, 'subtotal_formatted': '$4.99', 'discount_total_formatted': '$0.00', 'tax_formatted': '$0.00', 'total_formatted': '$4.99', 'refunded_amount_formatted': '$0.00', 'urls': {'invoice_url': 'https://app.lemonsqueezy.com/my-orders/c44d6447-ab0a-4b65-9555-8203132281cd/subscription-invoice/4587819?expires=1759100430&signature=7d70aede83dd43da2b2ea7395691e31250b26304b9cef5a5c1d78fef650656a1'}, 'created_at': '2025-09-28T17:00:27.000000Z', 'updated_at': '2025-09-28T17:00:30.000000Z', 'test_mode': True}
2025-09-28T17:00:30.740634722Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T17:00:30.740637682Z 🎯 BillingService: Checking event type 'subscription_payment_success' against subscription events
2025-09-28T17:00:30.740641612Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=False
2025-09-28T17:00:30.740644062Z 🎯 Processing payment success event for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T17:00:30.740646382Z 🔧 Payment success: Using existing plan pro
2025-09-28T17:00:30.740648892Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-28T17:00:30.740651452Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-28T17:00:30.740654372Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-28T17:00:30.740656902Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-28T17:00:30.740659202Z ✅ Created new UserSubscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro
2025-09-28T17:00:30.740662833Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=active
2025-09-28T17:00:30.740665313Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-28T17:00:32.394560247Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-28T17:00:32.393500+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-28T17:00:32.418638511Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-28T17:00:32.418662092Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '3394', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '9864cc2e2af0d96e-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '000afce7-f18a-4dc9', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_created', 'x-forwarded-for': '18.116.135.47, 104.23.197.55, 10.226.169.130', 'x-forwarded-proto': 'https', 'x-request-start': '1759078832391737', 'x-signature': '31e02e324cff7ed9923bff29af7d45d5e0ced08ab52cd6e4b0e73e57534fb64b'}
2025-09-28T17:00:32.418665922Z 🎯 BillingService: Processing webhook event_id=31e02e324cff7ed9923bff29af7d45d5e0ced08ab52cd6e4b0e73e57534fb64b
2025-09-28T17:00:32.418685862Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_created', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': '5125867a-1bbe-45cd-801f-e75ed00c5375'}, 'data': {'type': 'subscriptions', 'id': '1521286', 'attributes': {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6492812, 'order_item_id': 6436647, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 28, 'first_subscription_item': {'id': 4515138, 'subscription_id': 1521286, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-28T17:00:32.000000Z', 'updated_at': '2025-09-28T17:00:32.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1521286/payment-details?expires=1759100432&signature=28cd8e52a9795c918278149bb5b4645f610f288a36e84622da4c701e4b4a27a7', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759100432&test_mode=1&user=5534177&signature=c944f6e21931d5a8ee7ceace5100865e16ab1bfc89e42b957a91f9bda24639d6', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1521286/update?expires=1759100432&user=5534177&signature=86d6c9e4021e4bba10498c90d4f971a02efd7b86b1e67ff5f33a732a5378624c'}, 'renews_at': '2025-10-28T17:00:22.000000Z', 'ends_at': None, 'created_at': '2025-09-28T17:00:24.000000Z', 'updated_at': '2025-09-28T17:00:29.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/store', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/store'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/customer'}}, 'order': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/order', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/order'}}, 'order-item': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/order-item', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/order-item'}}, 'product': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/product', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/product'}}, 'variant': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/variant', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/variant'}}, 'subscription-items': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/subscription-items', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/subscription-items'}}, 'subscription-invoices': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/subscription-invoices', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/subscription-invoices'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286'}}}
2025-09-28T17:00:32.418696453Z 🎯 BillingService: Event 31e02e324cff7ed9923bff29af7d45d5e0ced08ab52cd6e4b0e73e57534fb64b is new, processing...
2025-09-28T17:00:32.418699953Z 🎯 BillingService: Event type: subscription_created
2025-09-28T17:00:32.418705963Z 🎯 BillingService: Attributes: {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6492812, 'order_item_id': 6436647, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 28, 'first_subscription_item': {'id': 4515138, 'subscription_id': 1521286, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-28T17:00:32.000000Z', 'updated_at': '2025-09-28T17:00:32.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1521286/payment-details?expires=1759100432&signature=28cd8e52a9795c918278149bb5b4645f610f288a36e84622da4c701e4b4a27a7', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759100432&test_mode=1&user=5534177&signature=c944f6e21931d5a8ee7ceace5100865e16ab1bfc89e42b957a91f9bda24639d6', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1521286/update?expires=1759100432&user=5534177&signature=86d6c9e4021e4bba10498c90d4f971a02efd7b86b1e67ff5f33a732a5378624c'}, 'renews_at': '2025-10-28T17:00:22.000000Z', 'ends_at': None, 'created_at': '2025-09-28T17:00:24.000000Z', 'updated_at': '2025-09-28T17:00:29.000000Z', 'test_mode': True}
2025-09-28T17:00:32.418742304Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T17:00:32.418745294Z 🎯 BillingService: Checking event type 'subscription_created' against subscription events
2025-09-28T17:00:32.418748454Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=True
2025-09-28T17:00:32.418750804Z 🔧 Mapping variant_id: 1013286 (type: <class 'int'>)
2025-09-28T17:00:32.418753075Z 🔧 Available mappings: {'1013286': 'pro', '1013276': 'enterprise', '1013282': 'pro-yearly'}
2025-09-28T17:00:32.418755715Z 🔧 Mapped to plan: pro
2025-09-28T17:00:32.418758015Z 🔧 Mapped variant_id 1013286 to plan: pro
2025-09-28T17:00:32.418760395Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-28T17:00:32.418762615Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-28T17:00:32.418765485Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-28T17:00:32.418767775Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-28T17:00:32.418770165Z ✅ Updated UserSubscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro, status=active
2025-09-28T17:00:32.418772745Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-28T17:00:32.418775135Z ✅ Committed subscription update to database
2025-09-28T17:00:32.418777505Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-28T17:00:37.013541493Z INFO:     41.238.10.39:0 - "WebSocket /ws/payments" [accepted]
2025-09-28T17:00:37.013815291Z INFO:     connection open
2025-09-28T17:00:37.475815856Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:37.476521207Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T17:00:37.68579469Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:37.687440529Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T17:00:37.8993212Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:37.901525215Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T17:00:38.130306537Z ERROR:src.payments.endpoints:Error getting user subscription: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T17:00:38.130325067Z WARNING:src.database.deps:Rollback failed: Method 'rollback()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T17:00:38.130331287Z ERROR:src.database.deps:Database session error: 500: Failed to get user subscription: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T17:00:38.130334067Z WARNING:src.database.deps:Close failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T17:00:38.130347598Z WARNING:src.database.deps:Remove from registry failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T17:00:38.130866573Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 500 Internal Server Error
2025-09-28T17:00:38.143426145Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:38.333425307Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:38.509587489Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:42.644246507Z INFO:     41.238.10.39:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-28T17:00:42.793616005Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T17:00:42.962275445Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:43.250171888Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T17:00:43.301396177Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:43.78428612Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T17:00:43.939841491Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:45.444167642Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T17:00:45.555132851Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:00:45.833245315Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T17:00:45.944265396Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T17:01:02.312794963Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-28T17:01:02.311826+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-28T17:01:02.336369972Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-28T17:01:02.336393303Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '3394', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '9864cce94d5ecf5f-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '25512569-083b-4353', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_updated', 'x-forwarded-for': '18.116.135.47, 104.23.197.55, 10.226.169.130', 'x-forwarded-proto': 'https', 'x-request-start': '1759078862309015', 'x-signature': '7f6d88cecb87c35e12f02501b74442887b6904caf471d63fc05e23ee5cca0326'}
2025-09-28T17:01:02.336397293Z 🎯 BillingService: Processing webhook event_id=7f6d88cecb87c35e12f02501b74442887b6904caf471d63fc05e23ee5cca0326
2025-09-28T17:01:02.336404253Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_updated', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': 'aa5569e5-a505-46e8-8198-d126ec80c553'}, 'data': {'type': 'subscriptions', 'id': '1521286', 'attributes': {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6492812, 'order_item_id': 6436647, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 28, 'first_subscription_item': {'id': 4515138, 'subscription_id': 1521286, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-28T17:00:32.000000Z', 'updated_at': '2025-09-28T17:01:01.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1521286/payment-details?expires=1759100462&signature=a13a910b3aa4db22b9a4c77807aa577009e378e6a36b1a4dfbfab4bfa4f8d6d8', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759100462&test_mode=1&user=5534177&signature=2aeebdc6bd1eeb10e3bfacb629a2ecf5615cb9b3969e356677b07435b70c3f7f', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1521286/update?expires=1759100462&user=5534177&signature=07efd3245654b59e723f8885c73935fc21704a3ac3125bf10bcafe43f674321f'}, 'renews_at': '2025-10-28T17:00:22.000000Z', 'ends_at': None, 'created_at': '2025-09-28T17:00:24.000000Z', 'updated_at': '2025-09-28T17:00:29.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/store', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/store'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/customer'}}, 'order': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/order', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/order'}}, 'order-item': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/order-item', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/order-item'}}, 'product': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/product', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/product'}}, 'variant': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/variant', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/variant'}}, 'subscription-items': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/subscription-items', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/subscription-items'}}, 'subscription-invoices': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/subscription-invoices', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286/relationships/subscription-invoices'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1521286'}}}
2025-09-28T17:01:02.336419513Z 🎯 BillingService: Event 7f6d88cecb87c35e12f02501b74442887b6904caf471d63fc05e23ee5cca0326 is new, processing...
2025-09-28T17:01:02.336422643Z 🎯 BillingService: Event type: subscription_updated
2025-09-28T17:01:02.336437124Z 🎯 BillingService: Attributes: {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6492812, 'order_item_id': 6436647, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 28, 'first_subscription_item': {'id': 4515138, 'subscription_id': 1521286, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-28T17:00:32.000000Z', 'updated_at': '2025-09-28T17:01:01.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1521286/payment-details?expires=1759100462&signature=a13a910b3aa4db22b9a4c77807aa577009e378e6a36b1a4dfbfab4bfa4f8d6d8', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759100462&test_mode=1&user=5534177&signature=2aeebdc6bd1eeb10e3bfacb629a2ecf5615cb9b3969e356677b07435b70c3f7f', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1521286/update?expires=1759100462&user=5534177&signature=07efd3245654b59e723f8885c73935fc21704a3ac3125bf10bcafe43f674321f'}, 'renews_at': '2025-10-28T17:00:22.000000Z', 'ends_at': None, 'created_at': '2025-09-28T17:00:24.000000Z', 'updated_at': '2025-09-28T17:00:29.000000Z', 'test_mode': True}
2025-09-28T17:01:02.336441934Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T17:01:02.336444974Z 🎯 BillingService: Checking event type 'subscription_updated' against subscription events
2025-09-28T17:01:02.336450274Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=True
2025-09-28T17:01:02.336453524Z 🔧 Mapping variant_id: 1013286 (type: <class 'int'>)
2025-09-28T17:01:02.336456124Z 🔧 Available mappings: {'1013286': 'pro', '1013276': 'enterprise', '1013282': 'pro-yearly'}
2025-09-28T17:01:02.336459214Z 🔧 Mapped to plan: pro
2025-09-28T17:01:02.336462014Z 🔧 Mapped variant_id 1013286 to plan: pro
2025-09-28T17:01:02.336464895Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-28T17:01:02.336467735Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-28T17:01:02.336470785Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-28T17:01:02.336473625Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-28T17:01:02.336476475Z ✅ Updated UserSubscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro, status=active
2025-09-28T17:01:02.336478975Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-28T17:01:02.336481365Z ✅ Committed subscription update to database
2025-09-28T17:01:02.336483685Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK