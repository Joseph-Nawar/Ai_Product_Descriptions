2025-09-29T03:28:19.659125418Z ==> Uploading build...
2025-09-29T03:28:39.598098358Z ==> Uploaded in 15.6s. Compression took 4.3s
2025-09-29T03:28:39.692207493Z ==> Build successful 🎉
2025-09-29T03:28:44.245166312Z ==> Deploying...
2025-09-29T03:29:34.241277484Z 🔄 Attempting to use simple database initialization...
2025-09-29T03:29:34.241280233Z 🔄 Initializing database...
2025-09-29T03:29:34.241282464Z ✅ Database initialized successfully!
2025-09-29T03:29:34.241284704Z ✅ Database initialized with simple script!
2025-09-29T03:29:50.708377724Z ==> No open ports detected, continuing to scan...
2025-09-29T03:29:50.908675305Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-29T03:30:00.745701116Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-29T03:30:00.745744367Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-29T03:30:00.745749838Z   warnings.warn(message, UserWarning)
2025-09-29T03:30:00.848222126Z INFO:     Started server process [56]
2025-09-29T03:30:00.848240407Z INFO:     Waiting for application startup.
2025-09-29T03:30:01.611403671Z INFO:     Application startup complete.
2025-09-29T03:30:01.640567997Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-29T03:30:02.253680866Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-29T03:30:02.253700546Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-29T03:30:02.253703896Z ✅ Gemini API key loaded successfully
2025-09-29T03:30:02.253722217Z 📊 Using model: gemini-flash-latest, temperature: 0.8
2025-09-29T03:30:02.253727467Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-29T03:30:02.253729917Z ✅ Gemini model 'gemini-flash-latest' configured successfully
2025-09-29T03:30:02.253732197Z ✅ AI Product Descriptions API started successfully
2025-09-29T03:30:02.253734717Z 🤖 Model: gemini-flash-latest (Live mode)
2025-09-29T03:30:02.253737297Z 🌡️  Temperature: 0.8
2025-09-29T03:30:02.253740327Z ✅ API key configured - ready for AI generation
2025-09-29T03:30:02.253742628Z 💳 Credit service initialized - rate limiting enabled
2025-09-29T03:30:02.253745077Z 📋 Subscription plans initialized
2025-09-29T03:30:02.253747658Z INFO:     127.0.0.1:47410 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-29T03:30:05.054404734Z ==> Your service is live 🎉
2025-09-29T03:30:05.133354334Z ==> 
2025-09-29T03:30:05.208281704Z ==> ///////////////////////////////////////////////////////////
2025-09-29T03:30:05.283762375Z ==> 
2025-09-29T03:30:05.359114665Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-29T03:30:05.434490096Z ==> 
2025-09-29T03:30:05.509611886Z ==> ///////////////////////////////////////////////////////////
2025-09-29T03:30:19.824945261Z INFO:     71.163.80.157:0 - "WebSocket /ws/payments" [accepted]
2025-09-29T03:30:19.824972042Z INFO:     connection open
2025-09-29T03:30:20.453048131Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:30:20.463299072Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:30:20.463317162Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:30:20.811728061Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:30:20.843492663Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:30:20.889810933Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:30:20.896349895Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:30:20.896365995Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:30:20.943613392Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:30:20.946210419Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:31:27.265109173Z INFO:     35.197.118.178:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-29T03:31:35.615912085Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:31:35.848449363Z WARNING:src.payments.endpoints:🔍 No subscription found for user FFngpbGhKWcpByg5j2kT83fsdEj1
2025-09-29T03:31:35.854885962Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:31:35.854903412Z WARNING:src.payments.endpoints:User FFngpbGhKWcpByg5j2kT83fsdEj1 has no subscription record, returning free tier
2025-09-29T03:31:35.857869499Z INFO:     71.163.80.157:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:31:35.960970306Z INFO:     71.163.80.157:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:31:56.267518476Z WARNING:root:Invalid auth header format
2025-09-29T03:31:56.267870126Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 401 Unauthorized
2025-09-29T03:31:56.751038503Z INFO:     156.204.156.48:0 - "WebSocket /ws/payments" [accepted]
2025-09-29T03:31:56.751215198Z INFO:     connection open
2025-09-29T03:31:56.885958964Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:31:56.892816276Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:31:56.892906668Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:31:56.896473613Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:31:57.082794424Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:31:57.248354245Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:31:57.255794433Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:31:57.255961768Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:31:57.259129471Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:31:57.340075308Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:31:57.434574293Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:31:57.441026492Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:31:57.441040002Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:31:57.445336539Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:31:57.51215111Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:31:57.728619476Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:31:57.832025072Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:31:57.838245675Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:31:57.838265805Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:31:57.841315155Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:31:57.911740003Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:31:58.142763316Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:32:06.290101444Z INFO:     156.204.156.48:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-29T03:32:06.435004239Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:06.44048546Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:32:06.440498151Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:32:06.444660783Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:32:06.571885748Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:32:06.805467987Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:06.811467603Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:32:06.811503094Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:32:06.814765449Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:32:06.950266878Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:32:07.990079469Z INFO:     156.204.156.48:0 - "OPTIONS /api/payment/checkout HTTP/1.1" 200 OK
2025-09-29T03:32:08.545095965Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:08.551472792Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:32:08.551491933Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:32:08.554517732Z 🎯 STEP 1: CREATE_CHECKOUT ENDPOINT CALLED
2025-09-29T03:32:08.554608954Z Request data: variant_id='1013286' success_url='https://www.productgeniepro.com/billing?success=true' cancel_url='https://www.productgeniepro.com/pricing?cancelled=true'
2025-09-29T03:32:08.554615115Z Variant ID: 1013286
2025-09-29T03:32:08.554618445Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-29T03:32:08.554621025Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-29T03:32:08.554623985Z 🎯 STEP 2: GETTING CLIENT INFO
2025-09-29T03:32:08.554628635Z Client info: {'ip_address': '156.204.156.48', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36', 'correlation_id': 'b7f600ae-2023-463d-b9a1-b937c875ff93'}
2025-09-29T03:32:08.554633925Z 🎯 STEP 3: EXTRACTING AUTH DATA
2025-09-29T03:32:08.554636645Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:08.554639415Z User email: ziad321hussein@gmail.com
2025-09-29T03:32:08.554642235Z 🎯 STEP 4: VALIDATING USER
2025-09-29T03:32:08.554644775Z ✅ STEP 4 SUCCESS: User validated
2025-09-29T03:32:08.554647195Z 🎯 STEP 5: VALIDATING VARIANT ID
2025-09-29T03:32:08.554649666Z ✅ STEP 5 SUCCESS: Variant ID validated
2025-09-29T03:32:08.554652196Z 🎯 STEP 6: CALLING LEMON_SQUEEZY SERVICE
2025-09-29T03:32:08.554654516Z 🎯 LEMON SQUEEZY PAYLOAD DEBUG 🎯
2025-09-29T03:32:08.554657026Z === VARIABLES ===
2025-09-29T03:32:08.554662316Z Variant ID: 1013286
2025-09-29T03:32:08.554664716Z Store ID: 224253
2025-09-29T03:32:08.554667136Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:08.554669756Z User Email: ziad321hussein@gmail.com
2025-09-29T03:32:08.554672816Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-29T03:32:08.554675446Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-29T03:32:08.554678207Z Test Mode: True
2025-09-29T03:32:08.554680867Z === PAYLOAD BEING SENT ===
2025-09-29T03:32:08.554683467Z {
2025-09-29T03:32:08.554686107Z   "data": {
2025-09-29T03:32:08.554688657Z     "type": "checkouts",
2025-09-29T03:32:08.554691017Z     "attributes": {
2025-09-29T03:32:08.554693397Z       "checkout_options": {
2025-09-29T03:32:08.554695787Z         "embed": false,
2025-09-29T03:32:08.554698267Z         "media": false
2025-09-29T03:32:08.554741468Z       },
2025-09-29T03:32:08.554748058Z       "checkout_data": {
2025-09-29T03:32:08.554751009Z         "email": "ziad321hussein@gmail.com",
2025-09-29T03:32:08.554753689Z         "custom": {
2025-09-29T03:32:08.554756619Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-29T03:32:08.554760239Z         }
2025-09-29T03:32:08.554762829Z       },
2025-09-29T03:32:08.554765419Z       "product_options": {
2025-09-29T03:32:08.554767859Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true"
2025-09-29T03:32:08.55479741Z       }
2025-09-29T03:32:08.55480071Z     },
2025-09-29T03:32:08.55480322Z     "relationships": {
2025-09-29T03:32:08.55480563Z       "store": {
2025-09-29T03:32:08.55480845Z         "data": {
2025-09-29T03:32:08.55481105Z           "type": "stores",
2025-09-29T03:32:08.554813791Z           "id": "224253"
2025-09-29T03:32:08.554816331Z         }
2025-09-29T03:32:08.554818671Z       },
2025-09-29T03:32:08.554821481Z       "variant": {
2025-09-29T03:32:08.554824091Z         "data": {
2025-09-29T03:32:08.554826671Z           "type": "variants",
2025-09-29T03:32:08.554829051Z           "id": "1013286"
2025-09-29T03:32:08.554831471Z         }
2025-09-29T03:32:08.554834001Z       }
2025-09-29T03:32:08.554836551Z     }
2025-09-29T03:32:08.554838861Z   }
2025-09-29T03:32:08.554841291Z }
2025-09-29T03:32:08.554871562Z === HEADERS ===
2025-09-29T03:32:08.554874112Z {
2025-09-29T03:32:08.554877722Z   "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NGQ1OWNlZi1kYmI4LTRlYTUtYjE3OC1kMjU0MGZjZDY5MTkiLCJqdGkiOiJkOGY2NTljZjdhMzA3ZGNjM2RjNTk4ZjNiMzU4YTk3YTczYzdhNGJkNDg2ZDlkM2JhYTE4OGQ4Y2MxMGU1Zjc5YWQzODJkZTgyYjgxNjRiNiIsImlhdCI6MTc1ODgyNzU5MC41NzYwMjcsIm5iZiI6MTc1ODgyNzU5MC41NzYwMjksImV4cCI6MjA3NDM2MDM5MC41NjA2NzcsInN1YiI6IjU1NzE5NjQiLCJzY29wZXMiOltdfQ.v6DQ8CrPGAovPSiYrv6Y3GkQ3DWHPcC0aAiZ9mP5BsXCwXoz5Kf1OY-fLAHC4ikcmx2RYZuLbSrF_Xxa4mvw2exFnJMsODiiuzItzhdVGUwR89IzbFAD6hcto-w0ERT3gjP781BJ-lxa7pzC4tCADeRhAtMPM7MZ7h7g-0JsRjXyNDrM0ArKoN84kiGHojmPCBomBuXTQ-mC_VQEWn8PKxTbZEem7FoyP4ydK46xYQu-naukuPTOZHRQ44Mdz_16JQ7Cda2pbfJo2osSPGaLTYUKvH0-aF2jlZToxGCPPr8LbPsHo1-96W2D6CBkCF0kFd6BQd0PKw64X-2ywolNwyna51cLKvkZuOHrh2Z8XVG0GONxeo6b1mFzgs8PzSkaPJ5Er_vhcRQVhAolOVmBHcZ61FUUJ208hR1FUVzMHlrTWtcTAi6HUjthHZB2ZL0xrIkDcWQPxG38i8ArAslXFLytqDTU3tePixq0WDHHBnBq8XSbleFoLH8rdc0j4v5KEPoJyXUS7MrHkiJ602WwLFPuczEdkRPvnSNeRKhsSlPkO8SiQFdHZ6VLCGQoEWDvm7SL2U6lmOJ2T1imOAGiTveGoliycICl_HQo29Fk0VFMFVa_jei7HCgdsLArClUHceqfx5UTOsrWxcd8zr75ALBqDzIWT9tpG5ifdTappes",
2025-09-29T03:32:08.554883222Z   "Accept": "application/vnd.api+json",
2025-09-29T03:32:08.554885822Z   "Content-Type": "application/vnd.api+json",
2025-09-29T03:32:08.554888343Z   "Version": "2021-07-07"
2025-09-29T03:32:08.554890943Z }
2025-09-29T03:32:08.554893443Z === API ENDPOINT ===
2025-09-29T03:32:08.554896203Z POST https://api.lemonsqueezy.com/v1/checkouts
2025-09-29T03:32:08.554899243Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:32:08.617335186Z === RESPONSE ===
2025-09-29T03:32:08.617354467Z Status: Unknown
2025-09-29T03:32:08.617357607Z Response: {
2025-09-29T03:32:08.617360287Z   "jsonapi": {
2025-09-29T03:32:08.617363637Z     "version": "1.0"
2025-09-29T03:32:08.617366257Z   },
2025-09-29T03:32:08.617369087Z   "links": {
2025-09-29T03:32:08.617372027Z     "self": "https://api.lemonsqueezy.com/v1/checkouts/236c3283-1073-42ab-8cf5-1466b898f9fd"
2025-09-29T03:32:08.617374577Z   },
2025-09-29T03:32:08.617377268Z   "data": {
2025-09-29T03:32:08.617379717Z     "type": "checkouts",
2025-09-29T03:32:08.617382748Z     "id": "236c3283-1073-42ab-8cf5-1466b898f9fd",
2025-09-29T03:32:08.617397828Z     "attributes": {
2025-09-29T03:32:08.617401568Z       "store_id": 224253,
2025-09-29T03:32:08.617404128Z       "variant_id": 1013286,
2025-09-29T03:32:08.617406708Z       "custom_price": null,
2025-09-29T03:32:08.617409189Z       "product_options": {
2025-09-29T03:32:08.617412009Z         "name": "",
2025-09-29T03:32:08.617414678Z         "description": "",
2025-09-29T03:32:08.617417269Z         "media": [],
2025-09-29T03:32:08.617420179Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true",
2025-09-29T03:32:08.617423649Z         "receipt_button_text": "",
2025-09-29T03:32:08.617426269Z         "receipt_link_url": "",
2025-09-29T03:32:08.617428759Z         "receipt_thank_you_note": "",
2025-09-29T03:32:08.617431319Z         "enabled_variants": [],
2025-09-29T03:32:08.617433989Z         "confirmation_title": "",
2025-09-29T03:32:08.617436329Z         "confirmation_message": "",
2025-09-29T03:32:08.617438749Z         "confirmation_button_text": ""
2025-09-29T03:32:08.617441229Z       },
2025-09-29T03:32:08.61744361Z       "checkout_options": {
2025-09-29T03:32:08.617446079Z         "embed": false,
2025-09-29T03:32:08.617448979Z         "media": false,
2025-09-29T03:32:08.61745148Z         "logo": true,
2025-09-29T03:32:08.61745411Z         "desc": true,
2025-09-29T03:32:08.61745675Z         "discount": true,
2025-09-29T03:32:08.61745909Z         "skip_trial": false,
2025-09-29T03:32:08.61746178Z         "quantity": 1,
2025-09-29T03:32:08.61746439Z         "subscription_preview": true,
2025-09-29T03:32:08.61746691Z         "locale": "en"
2025-09-29T03:32:08.61746948Z       },
2025-09-29T03:32:08.61747209Z       "checkout_data": {
2025-09-29T03:32:08.61747481Z         "email": "ziad321hussein@gmail.com",
2025-09-29T03:32:08.617477331Z         "name": "",
2025-09-29T03:32:08.617479931Z         "billing_address": [],
2025-09-29T03:32:08.61748244Z         "tax_number": "",
2025-09-29T03:32:08.617485071Z         "discount_code": "",
2025-09-29T03:32:08.617487801Z         "custom": {
2025-09-29T03:32:08.617490151Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-29T03:32:08.617492671Z         },
2025-09-29T03:32:08.617495281Z         "variant_quantities": []
2025-09-29T03:32:08.617497841Z       },
2025-09-29T03:32:08.617500331Z       "preview": false,
2025-09-29T03:32:08.617502731Z       "expires_at": null,
2025-09-29T03:32:08.617505381Z       "created_at": "2025-09-29T03:32:08.000000Z",
2025-09-29T03:32:08.617507921Z       "updated_at": "2025-09-29T03:32:08.000000Z",
2025-09-29T03:32:08.617510511Z       "test_mode": true,
2025-09-29T03:32:08.617513721Z       "url": "https://product-genie.lemonsqueezy.com/checkout/custom/236c3283-1073-42ab-8cf5-1466b898f9fd?signature=80727830459785aa7983435c4c9382efe6dddf18e246e6c459f0d125d3f9ae91"
2025-09-29T03:32:08.617516341Z     },
2025-09-29T03:32:08.617518842Z     "relationships": {
2025-09-29T03:32:08.617521362Z       "store": {
2025-09-29T03:32:08.617523762Z         "links": {
2025-09-29T03:32:08.617527212Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/236c3283-1073-42ab-8cf5-1466b898f9fd/store",
2025-09-29T03:32:08.617530292Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/236c3283-1073-42ab-8cf5-1466b898f9fd/relationships/store"
2025-09-29T03:32:08.617532872Z         }
2025-09-29T03:32:08.617535542Z       },
2025-09-29T03:32:08.617538012Z       "variant": {
2025-09-29T03:32:08.617540272Z         "links": {
2025-09-29T03:32:08.617542792Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/236c3283-1073-42ab-8cf5-1466b898f9fd/variant",
2025-09-29T03:32:08.617550773Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/236c3283-1073-42ab-8cf5-1466b898f9fd/relationships/variant"
2025-09-29T03:32:08.617553493Z         }
2025-09-29T03:32:08.617556373Z       }
2025-09-29T03:32:08.617558923Z     },
2025-09-29T03:32:08.617561633Z     "links": {
2025-09-29T03:32:08.617564453Z       "self": "https://api.lemonsqueezy.com/v1/checkouts/236c3283-1073-42ab-8cf5-1466b898f9fd"
2025-09-29T03:32:08.617566893Z     }
2025-09-29T03:32:08.617569323Z   }
2025-09-29T03:32:08.617572023Z }
2025-09-29T03:32:08.617574683Z ✅ STEP 6 SUCCESS: Lemon Squeezy service call successful
2025-09-29T03:32:08.617578233Z Result: {'success': True, 'checkout_url': 'https://product-genie.lemonsqueezy.com/checkout/custom/236c3283-1073-42ab-8cf5-1466b898f9fd?signature=80727830459785aa7983435c4c9382efe6dddf18e246e6c459f0d125d3f9ae91', 'checkout_id': '236c3283-1073-42ab-8cf5-1466b898f9fd'}
2025-09-29T03:32:08.617594994Z INFO:     156.204.156.48:0 - "POST /api/payment/checkout HTTP/1.1" 200 OK
2025-09-29T03:32:08.700648462Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:32:08.985106045Z WARNING:src.payments.endpoints:🔍 No subscription found for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:08.990970127Z ERROR:src.payments.endpoints:🔍 Database connection error: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-29T03:32:08.990999988Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-29T03:32:08.994247773Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:32:09.041085328Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:32:11.035185429Z INFO:     connection closed
2025-09-29T03:32:50.753827913Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-29T03:32:50.753564+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-29T03:32:50.843874447Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-29T03:32:50.843901818Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '1997', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '98686a68ee6d8a31-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '57ec2bb2-c4af-4d3a', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_payment_success', 'x-forwarded-for': '18.116.135.47, 104.23.197.55, 10.226.170.195', 'x-forwarded-proto': 'https', 'x-request-start': '1759116770749929', 'x-signature': '3aad7d9a264b322a7d8cc06929435c65ccd80a16b22c089723b5176ee7cf2ab0'}
2025-09-29T03:32:50.843907658Z 🎯 BillingService: Processing webhook event_id=3aad7d9a264b322a7d8cc06929435c65ccd80a16b22c089723b5176ee7cf2ab0
2025-09-29T03:32:50.843915208Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_payment_success', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': '52fd3792-2e7b-440d-a3b5-d7c28c0fa8d0'}, 'data': {'type': 'subscription-invoices', 'id': '4591720', 'attributes': {'store_id': 224253, 'subscription_id': 1522249, 'customer_id': 6829303, 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'billing_reason': 'initial', 'card_brand': 'visa', 'card_last_four': '4242', 'currency': 'USD', 'currency_rate': '1.00000000', 'status': 'paid', 'status_formatted': 'Paid', 'refunded': False, 'refunded_at': None, 'subtotal': 499, 'discount_total': 0, 'tax': 0, 'tax_inclusive': False, 'total': 499, 'refunded_amount': 0, 'subtotal_usd': 499, 'discount_total_usd': 0, 'tax_usd': 0, 'total_usd': 499, 'refunded_amount_usd': 0, 'subtotal_formatted': '$4.99', 'discount_total_formatted': '$0.00', 'tax_formatted': '$0.00', 'total_formatted': '$4.99', 'refunded_amount_formatted': '$0.00', 'urls': {'invoice_url': 'https://app.lemonsqueezy.com/my-orders/ead152f1-e8d6-44ca-9930-891c70eea318/subscription-invoice/4591720?expires=1759138370&signature=5cd6f4b24127c02a742ce38661e206796e8fac45c49b2d0e2eac6cc99577c33b'}, 'created_at': '2025-09-29T03:32:46.000000Z', 'updated_at': '2025-09-29T03:32:50.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591720/store', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591720/relationships/store'}}, 'subscription': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591720/subscription', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591720/relationships/subscription'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591720/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591720/relationships/customer'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscription-invoices/4591720'}}}
2025-09-29T03:32:50.843935409Z 🎯 BillingService: Event 3aad7d9a264b322a7d8cc06929435c65ccd80a16b22c089723b5176ee7cf2ab0 is new, processing...
2025-09-29T03:32:50.843939349Z 🎯 BillingService: Event type: subscription_payment_success
2025-09-29T03:32:50.843950399Z 🎯 BillingService: Attributes: {'store_id': 224253, 'subscription_id': 1522249, 'customer_id': 6829303, 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'billing_reason': 'initial', 'card_brand': 'visa', 'card_last_four': '4242', 'currency': 'USD', 'currency_rate': '1.00000000', 'status': 'paid', 'status_formatted': 'Paid', 'refunded': False, 'refunded_at': None, 'subtotal': 499, 'discount_total': 0, 'tax': 0, 'tax_inclusive': False, 'total': 499, 'refunded_amount': 0, 'subtotal_usd': 499, 'discount_total_usd': 0, 'tax_usd': 0, 'total_usd': 499, 'refunded_amount_usd': 0, 'subtotal_formatted': '$4.99', 'discount_total_formatted': '$0.00', 'tax_formatted': '$0.00', 'total_formatted': '$4.99', 'refunded_amount_formatted': '$0.00', 'urls': {'invoice_url': 'https://app.lemonsqueezy.com/my-orders/ead152f1-e8d6-44ca-9930-891c70eea318/subscription-invoice/4591720?expires=1759138370&signature=5cd6f4b24127c02a742ce38661e206796e8fac45c49b2d0e2eac6cc99577c33b'}, 'created_at': '2025-09-29T03:32:46.000000Z', 'updated_at': '2025-09-29T03:32:50.000000Z', 'test_mode': True}
2025-09-29T03:32:50.843954289Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:50.84395979Z 🎯 BillingService: Checking event type 'subscription_payment_success' against subscription events
2025-09-29T03:32:50.84396359Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=False
2025-09-29T03:32:50.84396617Z 🎯 Processing payment success event for user bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:50.84396849Z 🔧 Payment success: Using existing plan pro
2025-09-29T03:32:50.84397087Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-29T03:32:50.84397323Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-29T03:32:50.84397579Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:32:50.84397843Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-29T03:32:50.84398128Z ✅ Created new UserSubscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro
2025-09-29T03:32:50.84399045Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=active
2025-09-29T03:32:50.843993471Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-29T03:32:52.317683243Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-29T03:32:52.317465+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-29T03:32:52.348502308Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-29T03:32:52.348522249Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '3394', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '98686a72a8c21e9f-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '47ed4958-96a3-4ac0', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_created', 'x-forwarded-for': '18.116.135.47, 104.23.243.81, 10.226.151.1', 'x-forwarded-proto': 'https', 'x-request-start': '1759116772316496', 'x-signature': '11e3daeff84e410505d09be7bfac1062ed1c901b0d1599585bc118a096443f35'}
2025-09-29T03:32:52.348527859Z 🎯 BillingService: Processing webhook event_id=11e3daeff84e410505d09be7bfac1062ed1c901b0d1599585bc118a096443f35
2025-09-29T03:32:52.348536959Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_created', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': 'c36ba444-4336-4a9a-8327-f126fe762069'}, 'data': {'type': 'subscriptions', 'id': '1522249', 'attributes': {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495424, 'order_item_id': 6439248, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4539886, 'subscription_id': 1522249, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:32:52.000000Z', 'updated_at': '2025-09-29T03:32:52.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522249/payment-details?expires=1759138372&signature=8bb86f75025ffe4d66f367905f5e46d9b06cc1a84dbf31ffed7cf9b7d48a167c', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759138372&test_mode=1&user=5534177&signature=7180a9769db099aacbf9ee423e08816d4af3ffb3753235946e77c56880e595b5', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522249/update?expires=1759138372&user=5534177&signature=9d1c77e6e5b91f9e785077acee5a27d045a5e2bcec5479b3f077e44e81d82632'}, 'renews_at': '2025-10-29T03:32:43.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:32:44.000000Z', 'updated_at': '2025-09-29T03:32:50.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/store', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/store'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/customer'}}, 'order': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/order', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/order'}}, 'order-item': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/order-item', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/order-item'}}, 'product': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/product', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/product'}}, 'variant': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/variant', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/variant'}}, 'subscription-items': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/subscription-items', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/subscription-items'}}, 'subscription-invoices': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/subscription-invoices', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/subscription-invoices'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249'}}}
2025-09-29T03:32:52.34855865Z 🎯 BillingService: Event 11e3daeff84e410505d09be7bfac1062ed1c901b0d1599585bc118a096443f35 is new, processing...
2025-09-29T03:32:52.34856325Z 🎯 BillingService: Event type: subscription_created
2025-09-29T03:32:52.3485791Z 🎯 BillingService: Attributes: {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495424, 'order_item_id': 6439248, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4539886, 'subscription_id': 1522249, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:32:52.000000Z', 'updated_at': '2025-09-29T03:32:52.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522249/payment-details?expires=1759138372&signature=8bb86f75025ffe4d66f367905f5e46d9b06cc1a84dbf31ffed7cf9b7d48a167c', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759138372&test_mode=1&user=5534177&signature=7180a9769db099aacbf9ee423e08816d4af3ffb3753235946e77c56880e595b5', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522249/update?expires=1759138372&user=5534177&signature=9d1c77e6e5b91f9e785077acee5a27d045a5e2bcec5479b3f077e44e81d82632'}, 'renews_at': '2025-10-29T03:32:43.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:32:44.000000Z', 'updated_at': '2025-09-29T03:32:50.000000Z', 'test_mode': True}
2025-09-29T03:32:52.3485848Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:52.34858764Z 🎯 BillingService: Checking event type 'subscription_created' against subscription events
2025-09-29T03:32:52.34859318Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=True
2025-09-29T03:32:52.348596511Z 🔧 Mapping variant_id: 1013286 (type: <class 'int'>)
2025-09-29T03:32:52.348600171Z 🔧 Available mappings: {'1013286': 'pro', '1013276': 'enterprise', '1013282': 'pro-yearly'}
2025-09-29T03:32:52.348605171Z 🔧 Mapped to plan: pro
2025-09-29T03:32:52.348608391Z 🔧 Mapped variant_id 1013286 to plan: pro
2025-09-29T03:32:52.348621481Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-29T03:32:52.348625052Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-29T03:32:52.348628472Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:32:52.348630602Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-29T03:32:52.348638322Z ✅ Updated UserSubscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro, status=active
2025-09-29T03:32:52.348640332Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:32:52.348642592Z ✅ Committed subscription update to database
2025-09-29T03:32:52.348644332Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-29T03:32:52.835055985Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-29T03:32:52.834804+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-29T03:32:52.871067252Z 🎯 WEBHOOK RECEIVED: POST https://ai-product-descriptions.onrender.com/api/payment/webhook
2025-09-29T03:32:52.871092183Z 🎯 WEBHOOK HEADERS: {'host': 'ai-product-descriptions.onrender.com', 'user-agent': 'LemonSqueezy-Hookshot', 'content-length': '3394', 'accept-encoding': 'gzip, br', 'cdn-loop': 'cloudflare; loops=1', 'cf-connecting-ip': '18.116.135.47', 'cf-ipcountry': 'US', 'cf-ray': '98686a760a9bcf3a-CMH', 'cf-visitor': '{"scheme":"https"}', 'content-type': 'application/json', 'render-proxy-ttl': '4', 'rndr-id': '5cbe62f5-cd8a-4107', 'true-client-ip': '18.116.135.47', 'x-event-name': 'subscription_updated', 'x-forwarded-for': '18.116.135.47, 104.23.197.55, 10.226.170.195', 'x-forwarded-proto': 'https', 'x-request-start': '1759116772831481', 'x-signature': 'c50b72bdcc580fc768ec25eef088b52373c9706f1c69bb44f1bf48489de964ed'}
2025-09-29T03:32:52.871096483Z 🎯 BillingService: Processing webhook event_id=c50b72bdcc580fc768ec25eef088b52373c9706f1c69bb44f1bf48489de964ed
2025-09-29T03:32:52.871102863Z 🎯 BillingService: Event data: {'meta': {'test_mode': True, 'event_name': 'subscription_updated', 'custom_data': {'user_id': 'bpR6MB3823T20EK7BEa3cs2y22u2'}, 'webhook_id': '8ec2f586-9393-4164-9bcf-8582f99623ce'}, 'data': {'type': 'subscriptions', 'id': '1522249', 'attributes': {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495424, 'order_item_id': 6439248, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4539886, 'subscription_id': 1522249, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:32:52.000000Z', 'updated_at': '2025-09-29T03:32:52.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522249/payment-details?expires=1759138372&signature=8bb86f75025ffe4d66f367905f5e46d9b06cc1a84dbf31ffed7cf9b7d48a167c', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759138372&test_mode=1&user=5534177&signature=7180a9769db099aacbf9ee423e08816d4af3ffb3753235946e77c56880e595b5', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522249/update?expires=1759138372&user=5534177&signature=9d1c77e6e5b91f9e785077acee5a27d045a5e2bcec5479b3f077e44e81d82632'}, 'renews_at': '2025-10-29T03:32:43.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:32:44.000000Z', 'updated_at': '2025-09-29T03:32:50.000000Z', 'test_mode': True}, 'relationships': {'store': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/store', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/store'}}, 'customer': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/customer', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/customer'}}, 'order': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/order', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/order'}}, 'order-item': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/order-item', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/order-item'}}, 'product': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/product', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/product'}}, 'variant': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/variant', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/variant'}}, 'subscription-items': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/subscription-items', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/subscription-items'}}, 'subscription-invoices': {'links': {'related': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/subscription-invoices', 'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249/relationships/subscription-invoices'}}}, 'links': {'self': 'https://api.lemonsqueezy.com/v1/subscriptions/1522249'}}}
2025-09-29T03:32:52.871125844Z 🎯 BillingService: Event c50b72bdcc580fc768ec25eef088b52373c9706f1c69bb44f1bf48489de964ed is new, processing...
2025-09-29T03:32:52.871129214Z 🎯 BillingService: Event type: subscription_updated
2025-09-29T03:32:52.871134134Z 🎯 BillingService: Attributes: {'store_id': 224253, 'customer_id': 6829303, 'order_id': 6495424, 'order_item_id': 6439248, 'product_id': 645534, 'variant_id': 1013286, 'product_name': 'Get Extra Product Descriptions', 'variant_name': 'Pro Plan', 'user_name': 'Zeyad Sherif', 'user_email': 'ziad321hussein@gmail.com', 'status': 'active', 'status_formatted': 'Active', 'card_brand': 'visa', 'card_last_four': '4242', 'payment_processor': 'stripe', 'pause': None, 'cancelled': False, 'trial_ends_at': None, 'billing_anchor': 29, 'first_subscription_item': {'id': 4539886, 'subscription_id': 1522249, 'price_id': 1608947, 'quantity': 1, 'is_usage_based': False, 'created_at': '2025-09-29T03:32:52.000000Z', 'updated_at': '2025-09-29T03:32:52.000000Z'}, 'urls': {'update_payment_method': 'https://product-genie.lemonsqueezy.com/subscription/1522249/payment-details?expires=1759138372&signature=8bb86f75025ffe4d66f367905f5e46d9b06cc1a84dbf31ffed7cf9b7d48a167c', 'customer_portal': 'https://product-genie.lemonsqueezy.com/billing?expires=1759138372&test_mode=1&user=5534177&signature=7180a9769db099aacbf9ee423e08816d4af3ffb3753235946e77c56880e595b5', 'customer_portal_update_subscription': 'https://product-genie.lemonsqueezy.com/billing/1522249/update?expires=1759138372&user=5534177&signature=9d1c77e6e5b91f9e785077acee5a27d045a5e2bcec5479b3f077e44e81d82632'}, 'renews_at': '2025-10-29T03:32:43.000000Z', 'ends_at': None, 'created_at': '2025-09-29T03:32:44.000000Z', 'updated_at': '2025-09-29T03:32:50.000000Z', 'test_mode': True}
2025-09-29T03:32:52.871137244Z ✅ Using user_id: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-29T03:32:52.871139515Z 🎯 BillingService: Checking event type 'subscription_updated' against subscription events
2025-09-29T03:32:52.871142804Z 🎯 BillingService: is_subscription_event=True, has_subscription_data=True
2025-09-29T03:32:52.871145235Z 🔧 Mapping variant_id: 1013286 (type: <class 'int'>)
2025-09-29T03:32:52.871147555Z 🔧 Available mappings: {'1013286': 'pro', '1013276': 'enterprise', '1013282': 'pro-yearly'}
2025-09-29T03:32:52.871150595Z 🔧 Mapped to plan: pro
2025-09-29T03:32:52.871152935Z 🔧 Mapped variant_id 1013286 to plan: pro
2025-09-29T03:32:52.871155405Z ✅ Ensured user bpR6MB3823T20EK7BEa3cs2y22u2 exists in users table
2025-09-29T03:32:52.871157705Z 🔄 Updating existing subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: pro -> pro
2025-09-29T03:32:52.871165405Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:32:52.871167985Z ✅ Updated Subscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro
2025-09-29T03:32:52.871170585Z ✅ Updated UserSubscription table for user bpR6MB3823T20EK7BEa3cs2y22u2: plan_id=pro, status=active
2025-09-29T03:32:52.871172976Z ✅ Updated subscription for user bpR6MB3823T20EK7BEa3cs2y22u2: plan=pro, status=SubscriptionStatus.active
2025-09-29T03:32:52.871175496Z ✅ Committed subscription update to database
2025-09-29T03:32:52.871177856Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-29T03:32:53.429784528Z INFO:     156.204.156.48:0 - "WebSocket /ws/payments" [accepted]
2025-09-29T03:32:53.429937203Z INFO:     connection open
2025-09-29T03:32:53.63760579Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:32:53.780027293Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:32:53.849475772Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:32:53.958324128Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:32:54.041953234Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:32:54.190759893Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:32:54.25809534Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:32:54.485035864Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:33:10.501303793Z INFO:     156.204.156.48:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-29T03:33:10.662963031Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:33:10.817320433Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:33:11.011026521Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:33:11.302792439Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:33:12.032731043Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:33:12.176933467Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:33:12.474635019Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:33:12.58979597Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-29T03:33:12.820592797Z INFO:     156.204.156.48:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-29T03:33:12.944002871Z INFO:     156.204.156.48:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK