2025-09-29T03:50:53.951185272Z ==> Uploading build...
2025-09-29T03:51:14.307852072Z ==> Uploaded in 16.4s. Compression took 4.0s
2025-09-29T03:51:14.545385562Z ==> Build successful 🎉
2025-09-29T03:51:20.700255103Z ==> Deploying...
2025-09-29T03:52:03.62754111Z ==> Running '  cd backend && python fix_database.py && python run_migrations.py && uvicorn src.main:app --host 0.0.0.0 --port $PORT'
2025-09-29T03:52:07.342087805Z 🔧 Database Fix Script
2025-09-29T03:52:07.342108896Z ==================================================
2025-09-29T03:52:07.342116636Z ✅ Found database URL: postgresql://ai_descriptions_db_user:ijlatK7LezNTw...
2025-09-29T03:52:07.342120046Z ✅ Database connection established
2025-09-29T03:52:07.342122566Z 🔄 Creating subscriptions table...
2025-09-29T03:52:07.342125586Z 🔄 Creating indexes...
2025-09-29T03:52:07.342128336Z 🔄 Creating webhook_events table...
2025-09-29T03:52:07.342131336Z 🔄 Creating transactions table...
2025-09-29T03:52:07.342134477Z 🔄 Creating usage table...
2025-09-29T03:52:07.342137606Z 🔄 Creating user_credits table...
2025-09-29T03:52:07.342140177Z ✅ All tables created successfully!
2025-09-29T03:52:07.342142627Z 🎉 Database fix completed successfully!
2025-09-29T03:52:13.741552287Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-29T03:52:13.741573758Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-29T03:52:13.741578538Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-29T03:52:13.741583248Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-29T03:52:13.926017296Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-29T03:52:13.926035996Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-29T03:52:13.926041367Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-29T03:52:13.926045667Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-29T03:52:13.979346751Z INFO  [alembic.runtime.migration] Running upgrade  -> 0001_initial, initial tables
2025-09-29T03:52:13.979388472Z INFO  [alembic.runtime.migration] Running upgrade  -> 0001_initial, initial tables
2025-09-29T03:52:14.584311704Z 🔄 Checking current database state...
2025-09-29T03:52:14.584327455Z 🔄 Running database migrations...
2025-09-29T03:52:14.584344675Z ⚠️ Migration error: (psycopg2.errors.DuplicateTable) relation "users" already exists
2025-09-29T03:52:14.584353015Z 
2025-09-29T03:52:14.584357176Z [SQL: 
2025-09-29T03:52:14.584361846Z CREATE TABLE users (
2025-09-29T03:52:14.584424497Z 	id VARCHAR NOT NULL, 
2025-09-29T03:52:14.584444188Z 	email VARCHAR, 
2025-09-29T03:52:14.584449538Z 	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
2025-09-29T03:52:14.584453348Z 	PRIMARY KEY (id)
2025-09-29T03:52:14.584457258Z )
2025-09-29T03:52:14.584460928Z 
2025-09-29T03:52:14.584464808Z ]
2025-09-29T03:52:14.584468819Z (Background on this error at: https://sqlalche.me/e/20/f405)
2025-09-29T03:52:14.584472768Z 🔄 Attempting to continue with existing schema...
2025-09-29T03:52:14.584476959Z ❌ Migration failed: cannot import name 'get_db' from 'src.database.connection' (/opt/render/project/src/backend/src/database/connection.py)
2025-09-29T03:52:14.584480889Z 🔄 Attempting to use simple database initialization...
2025-09-29T03:52:14.584485459Z 🔄 Initializing database...
2025-09-29T03:52:14.584489659Z ✅ Database initialized successfully!
2025-09-29T03:52:14.584493419Z ✅ Database initialized with simple script!
2025-09-29T03:52:24.199471747Z ==> No open ports detected, continuing to scan...
2025-09-29T03:52:24.373599851Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-29T03:52:45.477281357Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-29T03:52:45.477304908Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-29T03:52:45.477310568Z   warnings.warn(message, UserWarning)
2025-09-29T03:52:45.580390602Z INFO:     Started server process [55]
2025-09-29T03:52:45.580420033Z INFO:     Waiting for application startup.
2025-09-29T03:52:46.376602355Z INFO:     Application startup complete.
2025-09-29T03:52:46.377300394Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-29T03:52:46.774241049Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-29T03:52:46.77426558Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-29T03:52:46.77426989Z ✅ Gemini API key loaded successfully
2025-09-29T03:52:46.77427331Z 📊 Using model: gemini-flash-latest, temperature: 0.8
2025-09-29T03:52:46.77427611Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-29T03:52:46.77427903Z ✅ Gemini model 'gemini-flash-latest' configured successfully
2025-09-29T03:52:46.77428203Z ✅ AI Product Descriptions API started successfully
2025-09-29T03:52:46.77428522Z 🤖 Model: gemini-flash-latest (Live mode)
2025-09-29T03:52:46.77429102Z 🌡️  Temperature: 0.8
2025-09-29T03:52:46.774294801Z ✅ API key configured - ready for AI generation
2025-09-29T03:52:46.77429805Z 💳 Credit service initialized - rate limiting enabled
2025-09-29T03:52:46.774301201Z 📋 Subscription plans initialized
2025-09-29T03:52:46.774304671Z INFO:     127.0.0.1:43466 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-29T03:52:51.508054874Z ==> Your service is live 🎉
2025-09-29T03:52:51.611005143Z ==> 
2025-09-29T03:52:51.687755793Z ==> ///////////////////////////////////////////////////////////
2025-09-29T03:52:51.765650433Z ==> 
2025-09-29T03:52:51.841172642Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-29T03:52:51.917967852Z ==> 
2025-09-29T03:52:51.997751791Z ==> ///////////////////////////////////////////////////////////
2025-09-29T03:52:53.365951483Z INFO:     34.82.242.193:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-29T03:54:49.260128253Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:54:49.277115887Z INFO:     156.204.156.48:0 - "WebSocket /ws/payments" [accepted]
2025-09-29T03:54:49.277404815Z INFO:     connection open
2025-09-29T03:54:49.363402161Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:54:49.372178285Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:54:49.691852221Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:54:49.766394751Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:54:49.766568306Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:54:50.331204922Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:54:50.349342756Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:54:50.350123077Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:54:50.377443576Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:54:50.572538745Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:54:50.579485031Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:54:50.587076343Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:54:50.587450383Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:54:50.79966919Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:54:50.847306442Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:54:50.85397738Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:54:50.854324859Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:54:51.013980962Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:54:51.025630163Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:54:51.033963446Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:54:51.033991686Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:54:51.202989968Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:54:51.389514369Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:00.127867226Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/plans HTTP/1.1" 200 OK
2025-09-29T03:55:00.282542076Z INFO:     156.204.156.48:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-29T03:55:00.404000099Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:00.492188804Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:00.506356112Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:55:00.506679571Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:00.702728445Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:00.710337118Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:55:00.710695968Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:00.818437644Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:00.865140841Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:00.872350954Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:55:00.872675643Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:00.996674434Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:01.824742423Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/checkout HTTP/1.1" 200 OK
2025-09-29T03:55:02.397975958Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:02.410692018Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:55:02.411103159Z 🎯 STEP 1: CREATE_CHECKOUT ENDPOINT CALLED
2025-09-29T03:55:02.411114569Z Request data: variant_id='1013286' success_url='https://www.productgeniepro.com/billing?success=true' cancel_url='https://www.productgeniepro.com/pricing?cancelled=true'
2025-09-29T03:55:02.41111926Z Variant ID: 1013286
2025-09-29T03:55:02.41112344Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-29T03:55:02.41112711Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-29T03:55:02.41113105Z 🎯 STEP 2: GETTING CLIENT INFO
2025-09-29T03:55:02.41113588Z Client info: {'ip_address': '156.204.156.48', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36', 'correlation_id': 'c293891f-f49d-49fb-9824-722234048620'}
2025-09-29T03:55:02.411142Z 🎯 STEP 3: EXTRACTING AUTH DATA
2025-09-29T03:55:02.41114651Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:02.41115088Z User email: ziad321hussein@gmail.com
2025-09-29T03:55:02.411168051Z 🎯 STEP 4: VALIDATING USER
2025-09-29T03:55:02.411170741Z ✅ STEP 4 SUCCESS: User validated
2025-09-29T03:55:02.411173181Z 🎯 STEP 5: VALIDATING VARIANT ID
2025-09-29T03:55:02.411175311Z ✅ STEP 5 SUCCESS: Variant ID validated
2025-09-29T03:55:02.411177531Z 🎯 STEP 6: CALLING LEMON_SQUEEZY SERVICE
2025-09-29T03:55:02.411179561Z 🎯 LEMON SQUEEZY PAYLOAD DEBUG 🎯
2025-09-29T03:55:02.411181721Z === VARIABLES ===
2025-09-29T03:55:02.411184091Z Variant ID: 1013286
2025-09-29T03:55:02.411186371Z Store ID: 224253
2025-09-29T03:55:02.411188491Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:02.411190581Z User Email: ziad321hussein@gmail.com
2025-09-29T03:55:02.411192731Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-29T03:55:02.411194951Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-29T03:55:02.411197171Z Test Mode: True
2025-09-29T03:55:02.411199351Z === PAYLOAD BEING SENT ===
2025-09-29T03:55:02.411201442Z {
2025-09-29T03:55:02.411203552Z   "data": {
2025-09-29T03:55:02.411205692Z     "type": "checkouts",
2025-09-29T03:55:02.411207802Z     "attributes": {
2025-09-29T03:55:02.411209922Z       "checkout_options": {
2025-09-29T03:55:02.411212092Z         "embed": false,
2025-09-29T03:55:02.411214132Z         "media": false
2025-09-29T03:55:02.411216162Z       },
2025-09-29T03:55:02.411218322Z       "checkout_data": {
2025-09-29T03:55:02.411220432Z         "email": "ziad321hussein@gmail.com",
2025-09-29T03:55:02.411222522Z         "custom": {
2025-09-29T03:55:02.411224792Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-29T03:55:02.411226812Z         }
2025-09-29T03:55:02.411228992Z       },
2025-09-29T03:55:02.411231123Z       "product_options": {
2025-09-29T03:55:02.411233423Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true"
2025-09-29T03:55:02.411235583Z       }
2025-09-29T03:55:02.411237692Z     },
2025-09-29T03:55:02.411239953Z     "relationships": {
2025-09-29T03:55:02.411242003Z       "store": {
2025-09-29T03:55:02.411244013Z         "data": {
2025-09-29T03:55:02.411246103Z           "type": "stores",
2025-09-29T03:55:02.411250103Z           "id": "224253"
2025-09-29T03:55:02.411252493Z         }
2025-09-29T03:55:02.411254783Z       },
2025-09-29T03:55:02.411256923Z       "variant": {
2025-09-29T03:55:02.411259233Z         "data": {
2025-09-29T03:55:02.411261393Z           "type": "variants",
2025-09-29T03:55:02.411263603Z           "id": "1013286"
2025-09-29T03:55:02.411265853Z         }
2025-09-29T03:55:02.411268063Z       }
2025-09-29T03:55:02.411270224Z     }
2025-09-29T03:55:02.411272393Z   }
2025-09-29T03:55:02.411274693Z }
2025-09-29T03:55:02.411277114Z === HEADERS ===
2025-09-29T03:55:02.411279734Z {
2025-09-29T03:55:02.411284444Z   "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NGQ1OWNlZi1kYmI4LTRlYTUtYjE3OC1kMjU0MGZjZDY5MTkiLCJqdGkiOiJkOGY2NTljZjdhMzA3ZGNjM2RjNTk4ZjNiMzU4YTk3YTczYzdhNGJkNDg2ZDlkM2JhYTE4OGQ4Y2MxMGU1Zjc5YWQzODJkZTgyYjgxNjRiNiIsImlhdCI6MTc1ODgyNzU5MC41NzYwMjcsIm5iZiI6MTc1ODgyNzU5MC41NzYwMjksImV4cCI6MjA3NDM2MDM5MC41NjA2NzcsInN1YiI6IjU1NzE5NjQiLCJzY29wZXMiOltdfQ.v6DQ8CrPGAovPSiYrv6Y3GkQ3DWHPcC0aAiZ9mP5BsXCwXoz5Kf1OY-fLAHC4ikcmx2RYZuLbSrF_Xxa4mvw2exFnJMsODiiuzItzhdVGUwR89IzbFAD6hcto-w0ERT3gjP781BJ-lxa7pzC4tCADeRhAtMPM7MZ7h7g-0JsRjXyNDrM0ArKoN84kiGHojmPCBomBuXTQ-mC_VQEWn8PKxTbZEem7FoyP4ydK46xYQu-naukuPTOZHRQ44Mdz_16JQ7Cda2pbfJo2osSPGaLTYUKvH0-aF2jlZToxGCPPr8LbPsHo1-96W2D6CBkCF0kFd6BQd0PKw64X-2ywolNwyna51cLKvkZuOHrh2Z8XVG0GONxeo6b1mFzgs8PzSkaPJ5Er_vhcRQVhAolOVmBHcZ61FUUJ208hR1FUVzMHlrTWtcTAi6HUjthHZB2ZL0xrIkDcWQPxG38i8ArAslXFLytqDTU3tePixq0WDHHBnBq8XSbleFoLH8rdc0j4v5KEPoJyXUS7MrHkiJ602WwLFPuczEdkRPvnSNeRKhsSlPkO8SiQFdHZ6VLCGQoEWDvm7SL2U6lmOJ2T1imOAGiTveGoliycICl_HQo29Fk0VFMFVa_jei7HCgdsLArClUHceqfx5UTOsrWxcd8zr75ALBqDzIWT9tpG5ifdTappes",
2025-09-29T03:55:02.411294164Z   "Accept": "application/vnd.api+json",
2025-09-29T03:55:02.411296924Z   "Content-Type": "application/vnd.api+json",
2025-09-29T03:55:02.411299184Z   "Version": "2021-07-07"
2025-09-29T03:55:02.411301304Z }
2025-09-29T03:55:02.411303684Z === API ENDPOINT ===
2025-09-29T03:55:02.411306025Z POST https://api.lemonsqueezy.com/v1/checkouts
2025-09-29T03:55:02.411308574Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:02.522693228Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:02.787648513Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:02.801373289Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:55:02.802919811Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:02.803721352Z === RESPONSE ===
2025-09-29T03:55:02.803727842Z Status: Unknown
2025-09-29T03:55:02.803731242Z Response: {
2025-09-29T03:55:02.803734063Z   "jsonapi": {
2025-09-29T03:55:02.803737463Z     "version": "1.0"
2025-09-29T03:55:02.803740263Z   },
2025-09-29T03:55:02.803743263Z   "links": {
2025-09-29T03:55:02.803746553Z     "self": "https://api.lemonsqueezy.com/v1/checkouts/395c6fdb-222d-414d-996e-5621acac85b4"
2025-09-29T03:55:02.803749533Z   },
2025-09-29T03:55:02.803752313Z   "data": {
2025-09-29T03:55:02.803754763Z     "type": "checkouts",
2025-09-29T03:55:02.803758313Z     "id": "395c6fdb-222d-414d-996e-5621acac85b4",
2025-09-29T03:55:02.803760993Z     "attributes": {
2025-09-29T03:55:02.803764123Z       "store_id": 224253,
2025-09-29T03:55:02.803766643Z       "variant_id": 1013286,
2025-09-29T03:55:02.803768993Z       "custom_price": null,
2025-09-29T03:55:02.803771513Z       "product_options": {
2025-09-29T03:55:02.803774124Z         "name": "",
2025-09-29T03:55:02.803777024Z         "description": "",
2025-09-29T03:55:02.803782944Z         "media": [],
2025-09-29T03:55:02.803786444Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true",
2025-09-29T03:55:02.803790794Z         "receipt_button_text": "",
2025-09-29T03:55:02.803793324Z         "receipt_link_url": "",
2025-09-29T03:55:02.803796124Z         "receipt_thank_you_note": "",
2025-09-29T03:55:02.803798744Z         "enabled_variants": [],
2025-09-29T03:55:02.803801374Z         "confirmation_title": "",
2025-09-29T03:55:02.803803894Z         "confirmation_message": "",
2025-09-29T03:55:02.803806374Z         "confirmation_button_text": ""
2025-09-29T03:55:02.803809214Z       },
2025-09-29T03:55:02.803811785Z       "checkout_options": {
2025-09-29T03:55:02.803814454Z         "embed": false,
2025-09-29T03:55:02.803816835Z         "media": false,
2025-09-29T03:55:02.803819405Z         "logo": true,
2025-09-29T03:55:02.803821775Z         "desc": true,
2025-09-29T03:55:02.803824135Z         "discount": true,
2025-09-29T03:55:02.803826565Z         "skip_trial": false,
2025-09-29T03:55:02.803829285Z         "quantity": 1,
2025-09-29T03:55:02.803832105Z         "subscription_preview": true,
2025-09-29T03:55:02.803835255Z         "locale": "en"
2025-09-29T03:55:02.803837565Z       },
2025-09-29T03:55:02.803839225Z       "checkout_data": {
2025-09-29T03:55:02.803851546Z         "email": "ziad321hussein@gmail.com",
2025-09-29T03:55:02.803854926Z         "name": "",
2025-09-29T03:55:02.803857736Z         "billing_address": [],
2025-09-29T03:55:02.803860446Z         "tax_number": "",
2025-09-29T03:55:02.803863136Z         "discount_code": "",
2025-09-29T03:55:02.803866206Z         "custom": {
2025-09-29T03:55:02.803868716Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-29T03:55:02.803871196Z         },
2025-09-29T03:55:02.803873646Z         "variant_quantities": []
2025-09-29T03:55:02.803876186Z       },
2025-09-29T03:55:02.803878746Z       "preview": false,
2025-09-29T03:55:02.803881416Z       "expires_at": null,
2025-09-29T03:55:02.803885976Z       "created_at": "2025-09-29T03:55:02.000000Z",
2025-09-29T03:55:02.803887747Z       "updated_at": "2025-09-29T03:55:02.000000Z",
2025-09-29T03:55:02.803889487Z       "test_mode": true,
2025-09-29T03:55:02.803928958Z       "url": "https://product-genie.lemonsqueezy.com/checkout/custom/395c6fdb-222d-414d-996e-5621acac85b4?signature=730493b477bb89dba20114e9aa5865e372c4d3a06f3a79264ab51789b0bb453a"
2025-09-29T03:55:02.803932078Z     },
2025-09-29T03:55:02.803934848Z     "relationships": {
2025-09-29T03:55:02.803937478Z       "store": {
2025-09-29T03:55:02.803939838Z         "links": {
2025-09-29T03:55:02.803942698Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/395c6fdb-222d-414d-996e-5621acac85b4/store",
2025-09-29T03:55:02.803945648Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/395c6fdb-222d-414d-996e-5621acac85b4/relationships/store"
2025-09-29T03:55:02.803948468Z         }
2025-09-29T03:55:02.803950978Z       },
2025-09-29T03:55:02.803953318Z       "variant": {
2025-09-29T03:55:02.803955838Z         "links": {
2025-09-29T03:55:02.803958558Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/395c6fdb-222d-414d-996e-5621acac85b4/variant",
2025-09-29T03:55:02.803961498Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/395c6fdb-222d-414d-996e-5621acac85b4/relationships/variant"
2025-09-29T03:55:02.803964549Z         }
2025-09-29T03:55:02.803966619Z       }
2025-09-29T03:55:02.803968289Z     },
2025-09-29T03:55:02.803969999Z     "links": {
2025-09-29T03:55:02.803971889Z       "self": "https://api.lemonsqueezy.com/v1/checkouts/395c6fdb-222d-414d-996e-5621acac85b4"
2025-09-29T03:55:02.803973569Z     }
2025-09-29T03:55:02.803975229Z   }
2025-09-29T03:55:02.803976929Z }
2025-09-29T03:55:02.803978809Z ✅ STEP 6 SUCCESS: Lemon Squeezy service call successful
2025-09-29T03:55:02.803981419Z Result: {'success': True, 'checkout_url': 'https://product-genie.lemonsqueezy.com/checkout/custom/395c6fdb-222d-414d-996e-5621acac85b4?signature=730493b477bb89dba20114e9aa5865e372c4d3a06f3a79264ab51789b0bb453a', 'checkout_id': '395c6fdb-222d-414d-996e-5621acac85b4'}
2025-09-29T03:55:02.803983859Z INFO:     156.204.156.48:0 - "POST /api/payment/checkout HTTP/1.1" 200 OK
2025-09-29T03:55:03.049179556Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:05.516177705Z INFO:     connection closed
2025-09-29T03:55:44.138538602Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-29T03:55:44.138271+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-29T03:55:44.176935617Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-29T03:55:44.176958227Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '1997', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '98688bf08dfd5094-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '19676165-13d8-45fd', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_payment_success', 'x-forwarded-for': '18.116.135.47, 104.23.243.80, 10.226.170.195', 'x-forwarded-proto': 'https', 'x-request-start': '1759118144135130', 'x-signature': '4d56d0072cf5e09676283192e3710f054ed816571d4e30c176fa8158568402b7'}
2025-09-29T03:55:44.176982078Z 🎯 BillingService: Processing webhook event_id=4d56d0072cf5e09676283192e3710f054ed816571d4e30c176fa8158568402b7
2025-09-29T03:55:44.176989298Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_payment_success', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': '82215a0d-412c-4f60-88b7-24c710f64f3a'}, 'data': {'type': 'subscription-invoices', 'id': '4591820', 'attributes': {'store_id': 224253, 'subscription_id': 1522272, 'customer_id': 6829303, 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'billing_reason': 'initial', 'card_brand': 'visa', 'card_last_four': '4242', 'currency': 'USD', 'currency_rate': '1.00000000', 'status': 'paid', 'status_formatted': 'Paid', 'refunded': False, 'refunded_at': None, 'subtotal': 499, 'discount_total': 0, 'tax': 0, 'tax_inclusive': False, 'total': 499, 'refunded_amount': 0, 'subtotal_usd': 499, 'discount_total_usd': 0, 'tax_usd': 0, 'total_usd': 499, 'refunded_amount_usd': 0, 'subtotal_formatted': '$4.99', 'discount_total_formatted': '$0.00', 'tax_formatted': '$0.00', 'total_formatted': '$4.99', 'refunded_amount_formatted': '$0.00', 'urls': {'invoice_url': 'https://app.lemonsqueezy.com/my-orders/2a6a2b01-74da-4b74-a00f-a88e7189b7e3/subscription-invoice/4591820?expires=1759139744&signature=81c098d1f135fdc90162bdf5a1e39069fdb913be1887c7de71921357d814451a'}, 'created_at': '2025-09-29T03:55:40.000000Z', 'updated_at': '2025-09-29T03:55:43.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591820/store', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591820/relationships/store'}}, 'subscription': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591820/subscription', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591820/relationships/subscription'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591820/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591820/relationships/customer'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591820'}}}
2025-09-29T03:55:44.176992878Z 🎯 BillingService: Event 4d56d0072cf5e09676283192e3710f054ed816571d4e30c176fa8158568402b7 is new, processing...
2025-09-29T03:55:44.176996318Z 🎯 BillingService: Event type: subscription_payment_success
2025-09-29T03:55:44.177018269Z 🎯 BillingService: Attributes: {'store_id': 224253, 'subscription_id': 1522272, 'customer_id': 6829303, 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'billing_reason': 'initial', 'card_brand': 'visa', 'card_last_four': '4242', 'currency': 'USD', 'currency_rate': '1.00000000', 'status': 'paid', 'status_formatted': 'Paid', 'refunded': False, 'refunded_at': None, 'subtotal': 499, 'discount_total': 0, 'tax': 0, 'tax_inclusive': False, 'total': 499, 'refunded_amount': 0, 'subtotal_usd': 499, 'discount_total_usd': 0, 'tax_usd': 0, 'total_usd': 499, 'refunded_amount_usd': 0, 'subtotal_formatted': '$4.99', 'discount_total_formatted': '$0.00', 'tax_formatted': '$0.00', 'total_formatted': '$4.99', 'refunded_amount_formatted': '$0.00', 'urls': {'invoice_url': 'https://app.lemonsqueezy.com/my-orders/2a6a2b01-74da-4b74-a00f-a88e7189b7e3/subscription-invoice/4591820?expires=1759139744&signature=81c098d1f135fdc90162bdf5a1e39069fdb913be1887c7de71921357d814451a'}, 'created_at': '2025-09-29T03:55:40.000000Z', 'updated_at': '2025-09-29T03:55:43.000000Z', 'test_mode': True}
2025-09-29T03:55:44.177031269Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:44.17703551Z 🎯 BillingService: Checking event type 'subscription_payment_success' against subscription events
2025-09-29T03:55:44.17703993Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=False
2025-09-29T03:55:44.17704359Z 🎯 Processing payment success event for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:44.17704668Z 🔧 Payment success: Using existing plan pro
2025-09-29T03:55:44.17704978Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-29T03:55:44.17705338Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-29T03:55:44.17705682Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:55:44.17706016Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-29T03:55:44.17706364Z ✅ Created new UserSubscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro
2025-09-29T03:55:44.17706713Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=active
2025-09-29T03:55:44.17707058Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-29T03:55:44.862658405Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-29T03:55:44.862381+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-29T03:55:44.887821947Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-29T03:55:44.887849908Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '3394', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '98688bf51e36addf-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '1b0b51ff-e87f-4fa8', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_created', 'x-forwarded-for': '18.116.135.47, 104.23.197.55, 10.226.170.195', 'x-forwarded-proto': 'https', 'x-request-start': '1759118144860202', 'x-signature': 'cffb5aed7efb2af38a22e4c560ff80551272634bc540f8d75bae11af5ed62750'}
2025-09-29T03:55:44.887854168Z 🎯 BillingService: Processing webhook event_id=cffb5aed7efb2af38a22e4c560ff80551272634bc540f8d75bae11af5ed62750
2025-09-29T03:55:44.887862618Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_created', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': 'b98a2d73-ae26-4a7b-9d73-3cbe508a0ecd'}, 'data': {'type': 'subscriptions', 'id': '1522272', 'attributes': {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495491, 'order_item_id': 6439314, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4540753, 'subscription_id': 1522272, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:55:44.000000Z', 'updated_at': '2025-09-29T03:55:44.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522272/payment-details?expires=1759139744&signature=5b0c5356ea19faa969a3c0e7308158ad34de34e19f6583607199f1fccab1a152', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759139744&test_mode=1&user=5534177&signature=98dce7879449af6a72b70a33063dff01fb7ddc6a2e987b24e75e3265e4bbe89f', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522272/update?expires=1759139744&user=5534177&signature=0433693a71749598b539c26fd8048513f72e4dd821f7f2e2ad1a65c4f65b1d2f'}, 'renews_at': '2025-10-29T03:55:35.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:55:37.000000Z', 'updated_at': '2025-09-29T03:55:42.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/store', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/store'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/customer'}}, 'order': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/order', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/order'}}, 'order-item': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/order-item', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/order-item'}}, 'product': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/product', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/product'}}, 'variant': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/variant', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/variant'}}, 'subscription-items': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/subscription-items', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/subscription-items'}}, 'subscription-invoices': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/subscription-invoices', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/subscription-invoices'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272'}}}
2025-09-29T03:55:44.887883989Z 🎯 BillingService: Event cffb5aed7efb2af38a22e4c560ff80551272634bc540f8d75bae11af5ed62750 is new, processing...
2025-09-29T03:55:44.887887459Z 🎯 BillingService: Event type: subscription_created
2025-09-29T03:55:44.88792061Z 🎯 BillingService: Attributes: {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495491, 'order_item_id': 6439314, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4540753, 'subscription_id': 1522272, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:55:44.000000Z', 'updated_at': '2025-09-29T03:55:44.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522272/payment-details?expires=1759139744&signature=5b0c5356ea19faa969a3c0e7308158ad34de34e19f6583607199f1fccab1a152', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759139744&test_mode=1&user=5534177&signature=98dce7879449af6a72b70a33063dff01fb7ddc6a2e987b24e75e3265e4bbe89f', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522272/update?expires=1759139744&user=5534177&signature=0433693a71749598b539c26fd8048513f72e4dd821f7f2e2ad1a65c4f65b1d2f'}, 'renews_at': '2025-10-29T03:55:35.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:55:37.000000Z', 'updated_at': '2025-09-29T03:55:42.000000Z', 'test_mode': True}
2025-09-29T03:55:44.88793377Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:55:44.88793637Z 🎯 BillingService: Checking event type 'subscription_created' against subscription events
2025-09-29T03:55:44.88793945Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=True
2025-09-29T03:55:44.887941711Z 🔧 Mapping variant_id: 1013286 (type: <class 'int'>)
2025-09-29T03:55:44.887944011Z 🔧 Available mappings: {'1013286': 'pro', '1013276': 'enterprise', '1013282': 'pro-yearly'}
2025-09-29T03:55:44.88794684Z 🔧 Mapped to plan: pro
2025-09-29T03:55:44.887949291Z 🔧 Mapped variant_id 1013286 to plan: pro
2025-09-29T03:55:44.887952051Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-29T03:55:44.887954571Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-29T03:55:44.887957631Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:55:44.887960071Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-29T03:55:44.887962571Z ✅ Updated UserSubscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro, status=active
2025-09-29T03:55:44.887964661Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:55:44.887966881Z ✅ Committed subscription update to database
2025-09-29T03:55:44.887968921Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-29T03:55:46.122818701Z INFO:     156.204.156.48:0 - "WebSocket /ws/payments" [accepted]
2025-09-29T03:55:46.123105159Z INFO:     connection open
2025-09-29T03:55:46.27521346Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:46.292703237Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:46.482935716Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:46.542488236Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:46.887315013Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:47.07857731Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:47.090915389Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:47.279856534Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:47.470113744Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:47.660539528Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:53.353037954Z INFO:     156.204.156.48:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-29T03:55:53.524545993Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:53.743372346Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:55:53.9128082Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:55:54.077442926Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:56:14.70461492Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-29T03:56:14.704374+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-29T03:56:14.735410622Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-29T03:56:14.735444173Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '3394', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '98688cafbe653488-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '76a869a5-d0f8-46bd', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_updated', 'x-forwarded-for': '18.116.135.47, 104.23.243.80, 10.226.170.195', 'x-forwarded-proto': 'https', 'x-request-start': '1759118174701238', 'x-signature': '9f9d3e70360090c42f241bf8913e7b5995da980a25ff04b6b1a50b00aa37d209'}
2025-09-29T03:56:14.735449023Z 🎯 BillingService: Processing webhook event_id=9f9d3e70360090c42f241bf8913e7b5995da980a25ff04b6b1a50b00aa37d209
2025-09-29T03:56:14.735458484Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_updated', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': '9002feff-b690-478d-b329-94d7cd54528e'}, 'data': {'type': 'subscriptions', 'id': '1522272', 'attributes': {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495491, 'order_item_id': 6439314, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4540753, 'subscription_id': 1522272, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:55:44.000000Z', 'updated_at': '2025-09-29T03:56:14.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522272/payment-details?expires=1759139774&signature=013c4175c6adc142c1307d99c468b2e06c2aea511095735137c4ceddb98c08d0', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759139774&test_mode=1&user=5534177&signature=c2db5d5805f85fc6a4cb4384794403a1f1f6cacc3d88888c1b9d888cdcf1dd1c', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522272/update?expires=1759139774&user=5534177&signature=4278d4d134fb4e88a7ac6b37e20f62ec215cfc754a7d69a38f5a0da128d2e130'}, 'renews_at': '2025-10-29T03:55:35.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:55:37.000000Z', 'updated_at': '2025-09-29T03:55:42.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/store', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/store'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/customer'}}, 'order': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/order', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/order'}}, 'order-item': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/order-item', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/order-item'}}, 'product': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/product', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/product'}}, 'variant': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/variant', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/variant'}}, 'subscription-items': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/subscription-items', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/subscription-items'}}, 'subscription-invoices': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/subscription-invoices', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272/relationships/subscription-invoices'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522272'}}}
2025-09-29T03:56:14.735479774Z 🎯 BillingService: Event 9f9d3e70360090c42f241bf8913e7b5995da980a25ff04b6b1a50b00aa37d209 is new, processing...
2025-09-29T03:56:14.735484064Z 🎯 BillingService: Event type: subscription_updated
2025-09-29T03:56:14.735501265Z 🎯 BillingService: Attributes: {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495491, 'order_item_id': 6439314, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4540753, 'subscription_id': 1522272, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:55:44.000000Z', 'updated_at': '2025-09-29T03:56:14.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522272/payment-details?expires=1759139774&signature=013c4175c6adc142c1307d99c468b2e06c2aea511095735137c4ceddb98c08d0', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759139774&test_mode=1&user=5534177&signature=c2db5d5805f85fc6a4cb4384794403a1f1f6cacc3d88888c1b9d888cdcf1dd1c', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522272/update?expires=1759139774&user=5534177&signature=4278d4d134fb4e88a7ac6b37e20f62ec215cfc754a7d69a38f5a0da128d2e130'}, 'renews_at': '2025-10-29T03:55:35.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:55:37.000000Z', 'updated_at': '2025-09-29T03:55:42.000000Z', 'test_mode': True}
2025-09-29T03:56:14.735506265Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:56:14.735510465Z 🎯 BillingService: Checking event type 'subscription_updated' against subscription events
2025-09-29T03:56:14.735514955Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=True
2025-09-29T03:56:14.735518125Z 🔧 Mapping variant_id: 1013286 (type: <class 'int'>)
2025-09-29T03:56:14.735521805Z 🔧 Available mappings: {'1013286': 'pro', '1013276': 'enterprise', '1013282': 'pro-yearly'}
2025-09-29T03:56:14.735526025Z 🔧 Mapped to plan: pro
2025-09-29T03:56:14.735529445Z 🔧 Mapped variant_id 1013286 to plan: pro
2025-09-29T03:56:14.735532875Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-29T03:56:14.735539456Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-29T03:56:14.735542456Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:56:14.735544576Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-29T03:56:14.735546636Z ✅ Updated UserSubscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro, status=active
2025-09-29T03:56:14.735548756Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:56:14.735550906Z ✅ Committed subscription update to database
2025-09-29T03:56:14.735553106Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-29T03:56:18.483075043Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:56:18.58858537Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:56:18.977934695Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:56:19.003137898Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:57:51.688292423Z ==> Detected service running on port 10000
2025-09-29T03:57:51.878278468Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding