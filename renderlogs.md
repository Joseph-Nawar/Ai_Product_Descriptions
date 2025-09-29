2025-09-29T03:38:48.517134897Z ==> Uploading build...
2025-09-29T03:39:11.301769517Z ==> Uploaded in 18.3s. Compression took 4.5s
2025-09-29T03:39:11.396019272Z ==> Build successful 🎉
2025-09-29T03:39:14.574591883Z ==> Deploying...
2025-09-29T03:39:51.814396099Z ==> Running '  cd backend && python fix_database.py && python run_migrations.py && uvicorn src.main:app --host 0.0.0.0 --port $PORT'
2025-09-29T03:39:54.421844137Z 🔧 Database Fix Script
2025-09-29T03:39:54.421870148Z ==================================================
2025-09-29T03:39:54.421874618Z ✅ Found database URL: postgresql://ai_descriptions_db_user:ijlatK7LezNTw...
2025-09-29T03:39:54.421878768Z ✅ Database connection established
2025-09-29T03:39:54.421882228Z 🔄 Creating subscriptions table...
2025-09-29T03:39:54.421885698Z 🔄 Creating indexes...
2025-09-29T03:39:54.421889308Z 🔄 Creating webhook_events table...
2025-09-29T03:39:54.421892758Z 🔄 Creating transactions table...
2025-09-29T03:39:54.421896739Z 🔄 Creating usage table...
2025-09-29T03:39:54.421900329Z 🔄 Creating user_credits table...
2025-09-29T03:39:54.421903839Z ✅ All tables created successfully!
2025-09-29T03:39:54.421907339Z 🎉 Database fix completed successfully!
2025-09-29T03:39:59.585685326Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-29T03:39:59.585731527Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-29T03:39:59.585739697Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-29T03:39:59.585744188Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-29T03:39:59.767131512Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-29T03:39:59.767158793Z INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2025-09-29T03:39:59.767163743Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-29T03:39:59.767168043Z INFO  [alembic.runtime.migration] Will assume transactional DDL.
2025-09-29T03:39:59.778914666Z INFO  [alembic.runtime.migration] Running upgrade  -> 0001_initial, initial tables
2025-09-29T03:39:59.778932336Z INFO  [alembic.runtime.migration] Running upgrade  -> 0001_initial, initial tables
2025-09-29T03:40:00.195094841Z 🔄 Checking current database state...
2025-09-29T03:40:00.195122832Z 🔄 Running database migrations...
2025-09-29T03:40:00.195131912Z ⚠️ Migration error: (psycopg2.errors.DuplicateTable) relation "users" already exists
2025-09-29T03:40:00.195137842Z 
2025-09-29T03:40:00.195142732Z [SQL: 
2025-09-29T03:40:00.195147833Z CREATE TABLE users (
2025-09-29T03:40:00.195152173Z 	id VARCHAR NOT NULL, 
2025-09-29T03:40:00.195156753Z 	email VARCHAR, 
2025-09-29T03:40:00.195161963Z 	created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL, 
2025-09-29T03:40:00.195166903Z 	PRIMARY KEY (id)
2025-09-29T03:40:00.195171533Z )
2025-09-29T03:40:00.195175773Z 
2025-09-29T03:40:00.195180164Z ]
2025-09-29T03:40:00.195184614Z (Background on this error at: https://sqlalche.me/e/20/f405)
2025-09-29T03:40:00.195189314Z 🔄 Attempting to continue with existing schema...
2025-09-29T03:40:00.195194454Z ❌ Migration failed: cannot import name 'get_db' from 'src.database.connection' (/opt/render/project/src/backend/src/database/connection.py)
2025-09-29T03:40:00.195199294Z 🔄 Attempting to use simple database initialization...
2025-09-29T03:40:00.195205044Z 🔄 Initializing database...
2025-09-29T03:40:00.195209605Z ✅ Database initialized successfully!
2025-09-29T03:40:00.195214134Z ✅ Database initialized with simple script!
2025-09-29T03:40:16.240212513Z ==> No open ports detected, continuing to scan...
2025-09-29T03:40:16.448973806Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-29T03:40:30.82841467Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-29T03:40:30.828458471Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-29T03:40:30.828465031Z   warnings.warn(message, UserWarning)
2025-09-29T03:40:31.017915151Z INFO:     Started server process [56]
2025-09-29T03:40:31.017948272Z INFO:     Waiting for application startup.
2025-09-29T03:40:31.620027015Z INFO:     Application startup complete.
2025-09-29T03:40:31.620602072Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-29T03:40:32.815854038Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-29T03:40:32.815880819Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-29T03:40:32.815886979Z ✅ Gemini API key loaded successfully
2025-09-29T03:40:32.815891139Z 📊 Using model: gemini-flash-latest, temperature: 0.8
2025-09-29T03:40:32.81589591Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-29T03:40:32.815900919Z ✅ Gemini model 'gemini-flash-latest' configured successfully
2025-09-29T03:40:32.81590491Z ✅ AI Product Descriptions API started successfully
2025-09-29T03:40:32.81590938Z 🤖 Model: gemini-flash-latest (Live mode)
2025-09-29T03:40:32.81591425Z 🌡️  Temperature: 0.8
2025-09-29T03:40:32.81591839Z ✅ API key configured - ready for AI generation
2025-09-29T03:40:32.81592272Z 💳 Credit service initialized - rate limiting enabled
2025-09-29T03:40:32.81592691Z 📋 Subscription plans initialized
2025-09-29T03:40:32.81593086Z INFO:     127.0.0.1:47350 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-29T03:40:35.377594312Z ==> Your service is live 🎉
2025-09-29T03:40:35.483684351Z ==> 
2025-09-29T03:40:35.56208775Z ==> ///////////////////////////////////////////////////////////
2025-09-29T03:40:35.65649822Z ==> 
2025-09-29T03:40:35.735864169Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-29T03:40:35.899821809Z ==> 
2025-09-29T03:40:35.979868678Z ==> ///////////////////////////////////////////////////////////
2025-09-29T03:40:50.826813729Z INFO:     71.163.80.157:0 - "WebSocket /ws/payments" [accepted]
2025-09-29T03:40:50.82718788Z INFO:     connection open
2025-09-29T03:40:52.697956611Z INFO:     34.168.108.203:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-29T03:40:52.793479284Z INFO:     71.163.80.157:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:40:53.763842989Z INFO:     71.163.80.157:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:40:57.017261429Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:40:57.065853315Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:40:57.065902517Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:40:58.987804569Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:40:59.766251592Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:40:59.793703301Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:40:59.819860823Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:40:59.819894595Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:00.769084423Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:00.811063396Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:00.818654587Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:00.819235984Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:01.779725772Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:01.813597089Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:01.822345254Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:01.822364444Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:02.765751894Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:02.808500529Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:02.815203644Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:02.815591676Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:03.753605488Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:03.794888671Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:03.813475623Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:03.813850174Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:04.762064194Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:04.795784047Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:04.80206804Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:04.802448491Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:05.762481065Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:05.80483741Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:05.811808543Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:05.812106182Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:06.756412948Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:06.804761617Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:06.810934707Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:06.811255016Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:07.774873625Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:07.801917783Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:07.80798969Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:07.80830793Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:08.791637523Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:08.814007605Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:08.820634568Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:08.821020139Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:09.793845857Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:09.817795905Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:09.823846951Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:09.824187571Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:10.783055322Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:10.811082029Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:10.817772294Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:10.818087633Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:11.774511803Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:11.806858695Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:11.813429606Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:11.813818168Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:12.820818232Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:12.99545433Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:13.004207905Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:13.004676399Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:13.791131816Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:13.809928354Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:13.818308408Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:13.81869793Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:14.768503037Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:14.817101023Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:14.826102585Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:14.826533088Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:15.780863047Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:15.805879846Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:15.814824957Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:15.815242978Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:16.773004998Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:16.798160891Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:16.815843976Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:16.816633159Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:17.770778233Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:17.801384385Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:17.823364925Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:17.823738276Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:18.786224202Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:18.816903576Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:18.877271376Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:18.877655727Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:19.771666468Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:19.814056353Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:19.822467619Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:19.822902541Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:20.770907726Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:20.805251177Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:20.815105004Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:20.815425033Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:21.770060171Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:21.803871927Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:21.812511778Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:21.812879969Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:22.767779855Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:22.796960575Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:22.807695308Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:22.808127301Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:23.775595563Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:23.801508518Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:23.816613678Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:23.816997109Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:24.782571377Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:24.808242825Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:24.816751362Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:24.817125093Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:25.786672266Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:25.804360462Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:25.816455094Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:25.816870276Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:26.766287563Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:26.802767136Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:26.810742518Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:26.811059747Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:27.768655452Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:27.80942922Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:27.818874705Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:27.818875396Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:28.884607752Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:28.895426117Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:28.903635666Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:28.904082229Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:29.769043484Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:29.813305754Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:29.821575715Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:29.821902745Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:30.765132971Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:30.806303841Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:30.816282902Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:30.816755205Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:31.774063452Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:31.807118085Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:31.817350803Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:31.818005462Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:32.766601615Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:32.799305738Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:32.807672442Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:32.808107875Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:33.766317808Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:33.805131419Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:33.81649562Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:33.816879881Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:34.77356926Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:34.808034544Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:34.816581433Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:34.816971454Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:35.77628019Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:35.813760022Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:35.822354902Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:35.822788455Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:36.769615086Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:36.791314239Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:41:36.800225928Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:41:36.800600899Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:38.750028538Z WARNING:root:Invalid auth header format
2025-09-29T03:41:38.750279615Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 401 Unauthorized
2025-09-29T03:41:58.825306634Z INFO:     156.204.156.48:0 - "WebSocket /ws/payments" [accepted]
2025-09-29T03:41:58.825462779Z INFO:     connection open
2025-09-29T03:41:58.866236477Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:58.934580049Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:59.068356197Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:59.089119842Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:59.091560834Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:59.194767981Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:59.202092675Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:59.288176223Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:41:59.294835797Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:59.296078324Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:59.296081184Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:41:59.414081963Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:59.457061745Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:41:59.493175568Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:59.493406564Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:41:59.608843028Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:59.644382994Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:41:59.693376352Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:41:59.693385362Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:41:59.809454585Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:41:59.86213615Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:41:59.868075393Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:41:59.868357921Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:42:00.032586567Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:42:00.260378086Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:42:03.332898696Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/plans HTTP/1.1" 200 OK
2025-09-29T03:42:03.488829911Z INFO:     156.204.156.48:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-29T03:42:03.497473103Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:42:03.503686844Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:42:03.504271401Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:42:03.625162264Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:42:03.899226801Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:42:03.907116551Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:42:03.907479601Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:42:03.988252935Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:42:20.883286908Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/checkout HTTP/1.1" 200 OK
2025-09-29T03:42:21.461634883Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:42:21.471549082Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:42:21.471935093Z 🎯 STEP 1: CREATE_CHECKOUT ENDPOINT CALLED
2025-09-29T03:42:21.471954014Z Request data: variant_id='1013286' success_url='https://www.productgeniepro.com/billing?success=true' cancel_url='https://www.productgeniepro.com/pricing?cancelled=true'
2025-09-29T03:42:21.471960244Z Variant ID: 1013286
2025-09-29T03:42:21.471965494Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-29T03:42:21.471970594Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-29T03:42:21.471976214Z 🎯 STEP 2: GETTING CLIENT INFO
2025-09-29T03:42:21.471983084Z Client info: {'ip_address': '156.204.156.48', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36', 'correlation_id': 'f22569d4-6bb0-4ed7-b319-a96c628dbf76'}
2025-09-29T03:42:21.472005435Z 🎯 STEP 3: EXTRACTING AUTH DATA
2025-09-29T03:42:21.472008635Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:42:21.472011505Z User email: ziad321hussein@gmail.com
2025-09-29T03:42:21.472014185Z 🎯 STEP 4: VALIDATING USER
2025-09-29T03:42:21.472016716Z ✅ STEP 4 SUCCESS: User validated
2025-09-29T03:42:21.472019336Z 🎯 STEP 5: VALIDATING VARIANT ID
2025-09-29T03:42:21.472021856Z ✅ STEP 5 SUCCESS: Variant ID validated
2025-09-29T03:42:21.472024656Z 🎯 STEP 6: CALLING LEMON_SQUEEZY SERVICE
2025-09-29T03:42:21.472027236Z 🎯 LEMON SQUEEZY PAYLOAD DEBUG 🎯
2025-09-29T03:42:21.472030066Z === VARIABLES ===
2025-09-29T03:42:21.472032846Z Variant ID: 1013286
2025-09-29T03:42:21.472035646Z Store ID: 224253
2025-09-29T03:42:21.472038386Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:42:21.472041336Z User Email: ziad321hussein@gmail.com
2025-09-29T03:42:21.472044566Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-29T03:42:21.472047466Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-29T03:42:21.472050626Z Test Mode: True
2025-09-29T03:42:21.472053617Z === PAYLOAD BEING SENT ===
2025-09-29T03:42:21.472056477Z {
2025-09-29T03:42:21.472061597Z   "data": {
2025-09-29T03:42:21.472064197Z     "type": "checkouts",
2025-09-29T03:42:21.472066777Z     "attributes": {
2025-09-29T03:42:21.472069097Z       "checkout_options": {
2025-09-29T03:42:21.472071797Z         "embed": false,
2025-09-29T03:42:21.472074467Z         "media": false
2025-09-29T03:42:21.472077117Z       },
2025-09-29T03:42:21.472080097Z       "checkout_data": {
2025-09-29T03:42:21.472083207Z         "email": "ziad321hussein@gmail.com",
2025-09-29T03:42:21.472085918Z         "custom": {
2025-09-29T03:42:21.472089007Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-29T03:42:21.472091548Z         }
2025-09-29T03:42:21.472094248Z       },
2025-09-29T03:42:21.472097028Z       "product_options": {
2025-09-29T03:42:21.472099718Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true"
2025-09-29T03:42:21.472102328Z       }
2025-09-29T03:42:21.472104988Z     },
2025-09-29T03:42:21.472107948Z     "relationships": {
2025-09-29T03:42:21.472110978Z       "store": {
2025-09-29T03:42:21.472113968Z         "data": {
2025-09-29T03:42:21.472116848Z           "type": "stores",
2025-09-29T03:42:21.472119588Z           "id": "224253"
2025-09-29T03:42:21.472122168Z         }
2025-09-29T03:42:21.472124899Z       },
2025-09-29T03:42:21.472127639Z       "variant": {
2025-09-29T03:42:21.472130269Z         "data": {
2025-09-29T03:42:21.472132789Z           "type": "variants",
2025-09-29T03:42:21.472135209Z           "id": "1013286"
2025-09-29T03:42:21.472137659Z         }
2025-09-29T03:42:21.472140089Z       }
2025-09-29T03:42:21.472142599Z     }
2025-09-29T03:42:21.472145089Z   }
2025-09-29T03:42:21.472147749Z }
2025-09-29T03:42:21.472152489Z === HEADERS ===
2025-09-29T03:42:21.47215562Z {
2025-09-29T03:42:21.47216047Z   "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NGQ1OWNlZi1kYmI4LTRlYTUtYjE3OC1kMjU0MGZjZDY5MTkiLCJqdGkiOiJkOGY2NTljZjdhMzA3ZGNjM2RjNTk4ZjNiMzU4YTk3YTczYzdhNGJkNDg2ZDlkM2JhYTE4OGQ4Y2MxMGU1Zjc5YWQzODJkZTgyYjgxNjRiNiIsImlhdCI6MTc1ODgyNzU5MC41NzYwMjcsIm5iZiI6MTc1ODgyNzU5MC41NzYwMjksImV4cCI6MjA3NDM2MDM5MC41NjA2NzcsInN1YiI6IjU1NzE5NjQiLCJzY29wZXMiOltdfQ.v6DQ8CrPGAovPSiYrv6Y3GkQ3DWHPcC0aAiZ9mP5BsXCwXoz5Kf1OY-fLAHC4ikcmx2RYZuLbSrF_Xxa4mvw2exFnJMsODiiuzItzhdVGUwR89IzbFAD6hcto-w0ERT3gjP781BJ-lxa7pzC4tCADeRhAtMPM7MZ7h7g-0JsRjXyNDrM0ArKoN84kiGHojmPCBomBuXTQ-mC_VQEWn8PKxTbZEem7FoyP4ydK46xYQu-naukuPTOZHRQ44Mdz_16JQ7Cda2pbfJo2osSPGaLTYUKvH0-aF2jlZToxGCPPr8LbPsHo1-96W2D6CBkCF0kFd6BQd0PKw64X-2ywolNwyna51cLKvkZuOHrh2Z8XVG0GONxeo6b1mFzgs8PzSkaPJ5Er_vhcRQVhAolOVmBHcZ61FUUJ208hR1FUVzMHlrTWtcTAi6HUjthHZB2ZL0xrIkDcWQPxG38i8ArAslXFLytqDTU3tePixq0WDHHBnBq8XSbleFoLH8rdc0j4v5KEPoJyXUS7MrHkiJ602WwLFPuczEdkRPvnSNeRKhsSlPkO8SiQFdHZ6VLCGQoEWDvm7SL2U6lmOJ2T1imOAGiTveGoliycICl_HQo29Fk0VFMFVa_jei7HCgdsLArClUHceqfx5UTOsrWxcd8zr75ALBqDzIWT9tpG5ifdTappes",
2025-09-29T03:42:21.47217109Z   "Accept": "application/vnd.api+json",
2025-09-29T03:42:21.47217399Z   "Content-Type": "application/vnd.api+json",
2025-09-29T03:42:21.47217694Z   "Version": "2021-07-07"
2025-09-29T03:42:21.47217982Z }
2025-09-29T03:42:21.47218274Z === API ENDPOINT ===
2025-09-29T03:42:21.47218493Z POST https://api.lemonsqueezy.com/v1/checkouts
2025-09-29T03:42:21.47218717Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:42:21.492202094Z === RESPONSE ===
2025-09-29T03:42:21.492222544Z Status: Unknown
2025-09-29T03:42:21.492226165Z Response: {
2025-09-29T03:42:21.492229025Z   "jsonapi": {
2025-09-29T03:42:21.492232725Z     "version": "1.0"
2025-09-29T03:42:21.492235465Z   },
2025-09-29T03:42:21.492238085Z   "links": {
2025-09-29T03:42:21.492241665Z     "self": "https://api.lemonsqueezy.com/v1/checkouts/367f4ad6-ec0a-4d90-93cb-6c60bb33f700"
2025-09-29T03:42:21.492244825Z   },
2025-09-29T03:42:21.492248075Z   "data": {
2025-09-29T03:42:21.492250995Z     "type": "checkouts",
2025-09-29T03:42:21.492254595Z     "id": "367f4ad6-ec0a-4d90-93cb-6c60bb33f700",
2025-09-29T03:42:21.492257595Z     "attributes": {
2025-09-29T03:42:21.492261426Z       "store_id": 224253,
2025-09-29T03:42:21.492264106Z       "variant_id": 1013286,
2025-09-29T03:42:21.492266826Z       "custom_price": null,
2025-09-29T03:42:21.492269716Z       "product_options": {
2025-09-29T03:42:21.492272476Z         "name": "",
2025-09-29T03:42:21.492275236Z         "description": "",
2025-09-29T03:42:21.492278066Z         "media": [],
2025-09-29T03:42:21.492281446Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true",
2025-09-29T03:42:21.492284846Z         "receipt_button_text": "",
2025-09-29T03:42:21.492287536Z         "receipt_link_url": "",
2025-09-29T03:42:21.492290136Z         "receipt_thank_you_note": "",
2025-09-29T03:42:21.492292546Z         "enabled_variants": [],
2025-09-29T03:42:21.492295287Z         "confirmation_title": "",
2025-09-29T03:42:21.492297787Z         "confirmation_message": "",
2025-09-29T03:42:21.492301007Z         "confirmation_button_text": ""
2025-09-29T03:42:21.492303987Z       },
2025-09-29T03:42:21.492306507Z       "checkout_options": {
2025-09-29T03:42:21.492309727Z         "embed": false,
2025-09-29T03:42:21.492312567Z         "media": false,
2025-09-29T03:42:21.492315517Z         "logo": true,
2025-09-29T03:42:21.492318257Z         "desc": true,
2025-09-29T03:42:21.492320947Z         "discount": true,
2025-09-29T03:42:21.492323877Z         "skip_trial": false,
2025-09-29T03:42:21.492326737Z         "quantity": 1,
2025-09-29T03:42:21.492329648Z         "subscription_preview": true,
2025-09-29T03:42:21.492332617Z         "locale": "en"
2025-09-29T03:42:21.492335398Z       },
2025-09-29T03:42:21.492338008Z       "checkout_data": {
2025-09-29T03:42:21.492341008Z         "email": "ziad321hussein@gmail.com",
2025-09-29T03:42:21.492343948Z         "name": "",
2025-09-29T03:42:21.492346678Z         "billing_address": [],
2025-09-29T03:42:21.492349368Z         "tax_number": "",
2025-09-29T03:42:21.492364898Z         "discount_code": "",
2025-09-29T03:42:21.492367709Z         "custom": {
2025-09-29T03:42:21.492370679Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-29T03:42:21.492373529Z         },
2025-09-29T03:42:21.492376329Z         "variant_quantities": []
2025-09-29T03:42:21.492378929Z       },
2025-09-29T03:42:21.492381549Z       "preview": false,
2025-09-29T03:42:21.492384319Z       "expires_at": null,
2025-09-29T03:42:21.492390359Z       "created_at": "2025-09-29T03:42:21.000000Z",
2025-09-29T03:42:21.492393379Z       "updated_at": "2025-09-29T03:42:21.000000Z",
2025-09-29T03:42:21.492395079Z       "test_mode": true,
2025-09-29T03:42:21.492398059Z       "url": "https://product-genie.lemonsqueezy.com/checkout/custom/367f4ad6-ec0a-4d90-93cb-6c60bb33f700?signature=cac553d1af8417651648260c33f3c563f7402ada125069114e08dd54d9019250"
2025-09-29T03:42:21.492399819Z     },
2025-09-29T03:42:21.492401539Z     "relationships": {
2025-09-29T03:42:21.49240321Z       "store": {
2025-09-29T03:42:21.49240493Z         "links": {
2025-09-29T03:42:21.49240762Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/367f4ad6-ec0a-4d90-93cb-6c60bb33f700/store",
2025-09-29T03:42:21.49240981Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/367f4ad6-ec0a-4d90-93cb-6c60bb33f700/relationships/store"
2025-09-29T03:42:21.49241146Z         }
2025-09-29T03:42:21.4924131Z       },
2025-09-29T03:42:21.49241482Z       "variant": {
2025-09-29T03:42:21.49241646Z         "links": {
2025-09-29T03:42:21.4924181Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/367f4ad6-ec0a-4d90-93cb-6c60bb33f700/variant",
2025-09-29T03:42:21.49241989Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/367f4ad6-ec0a-4d90-93cb-6c60bb33f700/relationships/variant"
2025-09-29T03:42:21.49242163Z         }
2025-09-29T03:42:21.49242402Z       }
2025-09-29T03:42:21.49242663Z     },
2025-09-29T03:42:21.4924296Z     "links": {
2025-09-29T03:42:21.49243252Z       "self": "https://api.lemonsqueezy.com/v1/checkouts/367f4ad6-ec0a-4d90-93cb-6c60bb33f700"
2025-09-29T03:42:21.49243498Z     }
2025-09-29T03:42:21.492437511Z   }
2025-09-29T03:42:21.492440041Z }
2025-09-29T03:42:21.492442911Z ✅ STEP 6 SUCCESS: Lemon Squeezy service call successful
2025-09-29T03:42:21.492447481Z Result: {'success': True, 'checkout_url': 'https://product-genie.lemonsqueezy.com/checkout/custom/367f4ad6-ec0a-4d90-93cb-6c60bb33f700?signature=cac553d1af8417651648260c33f3c563f7402ada125069114e08dd54d9019250', 'checkout_id': '367f4ad6-ec0a-4d90-93cb-6c60bb33f700'}
2025-09-29T03:42:21.492450411Z INFO:     156.204.156.48:0 - "POST /api/payment/checkout HTTP/1.1" 200 OK
2025-09-29T03:42:21.587831791Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:42:21.789825067Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:42:21.798111559Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:42:21.798741017Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:42:21.923818583Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:42:23.931338259Z INFO:     connection closed
2025-09-29T03:44:10.80476038Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-29T03:44:10.804474+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-29T03:44:10.851052499Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-29T03:44:10.85107414Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '1997', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '98687b033a1370f3-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '480b6296-c19d-40c1', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_payment_success', 'x-forwarded-for': '18.116.135.47, 104.23.243.81, 10.226.151.1', 'x-forwarded-proto': 'https', 'x-request-start': '1759117450801923', 'x-signature': '2bcefc1311263ec17ffa1254b7a7f0f9a208494040e6c80594d8b0e400df027b'}
2025-09-29T03:44:10.85107813Z 🎯 BillingService: Processing webhook event_id=2bcefc1311263ec17ffa1254b7a7f0f9a208494040e6c80594d8b0e400df027b
2025-09-29T03:44:10.85108405Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_payment_success', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': '05d18b9c-2973-4adf-b345-2b642afa42c0'}, 'data': {'type': 'subscription-invoices', 'id': '4591773', 'attributes': {'store_id': 224253, 'subscription_id': 1522258, 'customer_id': 6829303, 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'billing_reason': 'initial', 'card_brand': 'visa', 'card_last_four': '4242', 'currency': 'USD', 'currency_rate': '1.00000000', 'status': 'paid', 'status_formatted': 'Paid', 'refunded': False, 'refunded_at': None, 'subtotal': 499, 'discount_total': 0, 'tax': 0, 'tax_inclusive': False, 'total': 499, 'refunded_amount': 0, 'subtotal_usd': 499, 'discount_total_usd': 0, 'tax_usd': 0, 'total_usd': 499, 'refunded_amount_usd': 0, 'subtotal_formatted': '$4.99', 'discount_total_formatted': '$0.00', 'tax_formatted': '$0.00', 'total_formatted': '$4.99', 'refunded_amount_formatted': '$0.00', 'urls': {'invoice_url': 'https://app.lemonsqueezy.com/my-orders/668826ab-9fe1-435b-800a-b3cbf3613673/subscription-invoice/4591773?expires=1759139050&signature=afe7748d9802fd89ffb44624e27a83c89043d5989140c9b9989bbeb46c0a6b0f'}, 'created_at': '2025-09-29T03:44:06.000000Z', 'updated_at': '2025-09-29T03:44:10.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591773/store', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591773/relationships/store'}}, 'subscription': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591773/subscription', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591773/relationships/subscription'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591773/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591773/relationships/customer'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591773'}}}
2025-09-29T03:44:10.85108826Z 🎯 BillingService: Event 2bcefc1311263ec17ffa1254b7a7f0f9a208494040e6c80594d8b0e400df027b is new, processing...
2025-09-29T03:44:10.85109178Z 🎯 BillingService: Event type: subscription_payment_success
2025-09-29T03:44:10.851102861Z 🎯 BillingService: Attributes: {'store_id': 224253, 'subscription_id': 1522258, 'customer_id': 6829303, 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'billing_reason': 'initial', 'card_brand': 'visa', 'card_last_four': '4242', 'currency': 'USD', 'currency_rate': '1.00000000', 'status': 'paid', 'status_formatted': 'Paid', 'refunded': False, 'refunded_at': None, 'subtotal': 499, 'discount_total': 0, 'tax': 0, 'tax_inclusive': False, 'total': 499, 'refunded_amount': 0, 'subtotal_usd': 499, 'discount_total_usd': 0, 'tax_usd': 0, 'total_usd': 499, 'refunded_amount_usd': 0, 'subtotal_formatted': '$4.99', 'discount_total_formatted': '$0.00', 'tax_formatted': '$0.00', 'total_formatted': '$4.99', 'refunded_amount_formatted': '$0.00', 'urls': {'invoice_url': 'https://app.lemonsqueezy.com/my-orders/668826ab-9fe1-435b-800a-b3cbf3613673/subscription-invoice/4591773?expires=1759139050&signature=afe7748d9802fd89ffb44624e27a83c89043d5989140c9b9989bbeb46c0a6b0f'}, 'created_at': '2025-09-29T03:44:06.000000Z', 'updated_at': '2025-09-29T03:44:10.000000Z', 'test_mode': True}
2025-09-29T03:44:10.851119991Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:44:10.851123321Z 🎯 BillingService: Checking event type 'subscription_payment_success' against subscription events
2025-09-29T03:44:10.851126161Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=False
2025-09-29T03:44:10.851128502Z 🎯 Processing payment success event for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:44:10.851131052Z 🔧 Payment success: Using existing plan pro
2025-09-29T03:44:10.851133632Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-29T03:44:10.851136262Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-29T03:44:10.851138692Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:44:10.851141072Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-29T03:44:10.851143482Z ✅ Created new UserSubscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro
2025-09-29T03:44:10.851145862Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=active
2025-09-29T03:44:10.851148242Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-29T03:44:12.243008115Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-29T03:44:12.241957+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-29T03:44:12.279248111Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-29T03:44:12.279300952Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '3394', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '98687b0c68f3f4d4-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': 'ab1d672a-2dd1-45d8', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_created', 'x-forwarded-for': '18.116.135.47, 104.23.243.81, 10.226.151.1', 'x-forwarded-proto': 'https', 'x-request-start': '1759117452238681', 'x-signature': 'a70a31ae99c16d1ddc52d8b50fe651b4306277d5d903a76d10301309b557289a'}
2025-09-29T03:44:12.279305643Z 🎯 BillingService: Processing webhook event_id=a70a31ae99c16d1ddc52d8b50fe651b4306277d5d903a76d10301309b557289a
2025-09-29T03:44:12.279312263Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_created', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': '80844ff1-2ce8-4649-9a50-344b388d78bd'}, 'data': {'type': 'subscriptions', 'id': '1522258', 'attributes': {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495453, 'order_item_id': 6439277, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4540317, 'subscription_id': 1522258, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:44:12.000000Z', 'updated_at': '2025-09-29T03:44:12.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522258/payment-details?expires=1759139052&signature=2e35affd29887d14d82949f37a30444b83ee9a3b80d74038165c73e059b8c361', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759139052&test_mode=1&user=5534177&signature=077e504cb29a0f90f62829e89de802faf5023a378c38d5cc3002d08bf62015f3', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522258/update?expires=1759139052&user=5534177&signature=30da95b11d61642f56554e8a1be84c11986e5e05176fe74edf3ea35cddff6c1e'}, 'renews_at': '2025-10-29T03:44:01.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:44:03.000000Z', 'updated_at': '2025-09-29T03:44:09.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/store', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/store'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/customer'}}, 'order': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/order', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/order'}}, 'order-item': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/order-item', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/order-item'}}, 'product': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/product', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/product'}}, 'variant': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/variant', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/variant'}}, 'subscription-items': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/subscription-items', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/subscription-items'}}, 'subscription-invoices': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/subscription-invoices', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/subscription-invoices'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258'}}}
2025-09-29T03:44:12.279331424Z 🎯 BillingService: Event a70a31ae99c16d1ddc52d8b50fe651b4306277d5d903a76d10301309b557289a is new, processing...
2025-09-29T03:44:12.279334613Z 🎯 BillingService: Event type: subscription_created
2025-09-29T03:44:12.279389775Z 🎯 BillingService: Attributes: {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495453, 'order_item_id': 6439277, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4540317, 'subscription_id': 1522258, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:44:12.000000Z', 'updated_at': '2025-09-29T03:44:12.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522258/payment-details?expires=1759139052&signature=2e35affd29887d14d82949f37a30444b83ee9a3b80d74038165c73e059b8c361', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759139052&test_mode=1&user=5534177&signature=077e504cb29a0f90f62829e89de802faf5023a378c38d5cc3002d08bf62015f3', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522258/update?expires=1759139052&user=5534177&signature=30da95b11d61642f56554e8a1be84c11986e5e05176fe74edf3ea35cddff6c1e'}, 'renews_at': '2025-10-29T03:44:01.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:44:03.000000Z', 'updated_at': '2025-09-29T03:44:09.000000Z', 'test_mode': True}
2025-09-29T03:44:12.279399666Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:44:12.279402275Z 🎯 BillingService: Checking event type 'subscription_created' against subscription events
2025-09-29T03:44:12.279405055Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=True
2025-09-29T03:44:12.279407226Z 🔧 Mapping variant_id: 1013286 (type: <class 'int'>)
2025-09-29T03:44:12.279409676Z 🔧 Available mappings: {'1013286': 'pro', '1013276': 'enterprise', '1013282': 'pro-yearly'}
2025-09-29T03:44:12.279412596Z 🔧 Mapped to plan: pro
2025-09-29T03:44:12.279414896Z 🔧 Mapped variant_id 1013286 to plan: pro
2025-09-29T03:44:12.279417286Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-29T03:44:12.279419676Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-29T03:44:12.279422536Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:44:12.279424936Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-29T03:44:12.279427236Z ✅ Updated UserSubscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro, status=active
2025-09-29T03:44:12.279447317Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:44:12.279450217Z ✅ Committed subscription update to database
2025-09-29T03:44:12.279452907Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-29T03:44:16.338833848Z INFO:     156.204.156.48:0 - "WebSocket /ws/payments" [accepted]
2025-09-29T03:44:16.339129527Z INFO:     connection open
2025-09-29T03:44:16.532205455Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:44:16.532455423Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:44:16.693833327Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:44:16.73580031Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:44:16.874984757Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:44:17.09668466Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:44:17.276318116Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:44:17.482116955Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:44:19.139058895Z INFO:     156.204.156.48:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-29T03:44:19.328046604Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:44:19.459503616Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:44:19.736858401Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:44:19.815237146Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:44:19.937642564Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:44:20.011036473Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:44:41.910598125Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-29T03:44:41.909446+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-29T03:44:41.937480219Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-29T03:44:41.937506329Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '3394', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '98687bc5ca7122ce-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': 'a3a1c65d-6943-4bf4', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_updated', 'x-forwarded-for': '18.116.135.47, 104.23.243.81, 10.226.151.1', 'x-forwarded-proto': 'https', 'x-request-start': '1759117481906786', 'x-signature': 'e328f3586eee84263e30faf99643ddc648ca4f89bcac1d5c12fc5506dbb47579'}
2025-09-29T03:44:41.93751202Z 🎯 BillingService: Processing webhook event_id=e328f3586eee84263e30faf99643ddc648ca4f89bcac1d5c12fc5506dbb47579
2025-09-29T03:44:41.93752084Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_updated', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': '758ce461-e53b-46ab-ad6f-1c5cca90afe4'}, 'data': {'type': 'subscriptions', 'id': '1522258', 'attributes': {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495453, 'order_item_id': 6439277, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4540317, 'subscription_id': 1522258, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:44:12.000000Z', 'updated_at': '2025-09-29T03:44:41.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522258/payment-details?expires=1759139081&signature=64cb9d0c5e64d3b5aca2f61c5de1791b4908bb72538a50ebc506d0c95a2e7908', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759139081&test_mode=1&user=5534177&signature=66d92524861ef4f941d02b2a6451291db480f798277a19ba8160ab263fe3f920', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522258/update?expires=1759139081&user=5534177&signature=486ff62be72187c06f6df190e69ac33422f4bdb9be09aff5cdecb23d05172af7'}, 'renews_at': '2025-10-29T03:44:01.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:44:03.000000Z', 'updated_at': '2025-09-29T03:44:09.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/store', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/store'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/customer'}}, 'order': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/order', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/order'}}, 'order-item': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/order-item', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/order-item'}}, 'product': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/product', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/product'}}, 'variant': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/variant', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/variant'}}, 'subscription-items': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/subscription-items', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/subscription-items'}}, 'subscription-invoices': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/subscription-invoices', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258/relationships/subscription-invoices'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522258'}}}
2025-09-29T03:44:41.937540581Z 🎯 BillingService: Event e328f3586eee84263e30faf99643ddc648ca4f89bcac1d5c12fc5506dbb47579 is new, processing...
2025-09-29T03:44:41.937543831Z 🎯 BillingService: Event type: subscription_updated
2025-09-29T03:44:41.937549571Z 🎯 BillingService: Attributes: {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495453, 'order_item_id': 6439277, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4540317, 'subscription_id': 1522258, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:44:12.000000Z', 'updated_at': '2025-09-29T03:44:41.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522258/payment-details?expires=1759139081&signature=64cb9d0c5e64d3b5aca2f61c5de1791b4908bb72538a50ebc506d0c95a2e7908', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759139081&test_mode=1&user=5534177&signature=66d92524861ef4f941d02b2a6451291db480f798277a19ba8160ab263fe3f920', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522258/update?expires=1759139081&user=5534177&signature=486ff62be72187c06f6df190e69ac33422f4bdb9be09aff5cdecb23d05172af7'}, 'renews_at': '2025-10-29T03:44:01.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:44:03.000000Z', 'updated_at': '2025-09-29T03:44:09.000000Z', 'test_mode': True}
2025-09-29T03:44:41.937552821Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:44:41.937555511Z 🎯 BillingService: Checking event type 'subscription_updated' against subscription events
2025-09-29T03:44:41.937558731Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=True
2025-09-29T03:44:41.937561041Z 🔧 Mapping variant_id: 1013286 (type: <class 'int'>)
2025-09-29T03:44:41.937563571Z 🔧 Available mappings: {'1013286': 'pro', '1013276': 'enterprise', '1013282': 'pro-yearly'}
2025-09-29T03:44:41.937566531Z 🔧 Mapped to plan: pro
2025-09-29T03:44:41.937568951Z 🔧 Mapped variant_id 1013286 to plan: pro
2025-09-29T03:44:41.937571402Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-29T03:44:41.937573791Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-29T03:44:41.937577072Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:44:41.937579542Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-29T03:44:41.937582082Z ✅ Updated UserSubscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro, status=active
2025-09-29T03:44:41.937584962Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:44:41.937592842Z ✅ Committed subscription update to database
2025-09-29T03:44:41.937595572Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-29T03:45:39.136895961Z ==> Detected service running on port 10000
2025-09-29T03:45:39.355655687Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding