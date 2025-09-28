2025-09-28T09:33:48.812472281Z Using cached google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
2025-09-28T09:33:48.813824631Z Using cached httplib2-0.31.0-py3-none-any.whl (91 kB)
2025-09-28T09:33:48.815186932Z Using cached pyparsing-3.2.5-py3-none-any.whl (113 kB)
2025-09-28T09:33:48.816561312Z Using cached uritemplate-4.2.0-py3-none-any.whl (11 kB)
2025-09-28T09:33:48.817747008Z Using cached mako-1.3.10-py3-none-any.whl (78 kB)
2025-09-28T09:33:48.819198581Z Using cached markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
2025-09-28T09:33:48.820681114Z Using cached pycparser-2.23-py3-none-any.whl (118 kB)
2025-09-28T09:33:49.141723725Z Installing collected packages: pytz, wrapt, websockets, uvloop, urllib3, uritemplate, tzdata, typing-extensions, tqdm, tenacity, structlog, sniffio, six, rapidfuzz, pyyaml, python-multipart, python-dotenv, pyparsing, pymysql, pyjwt, pygments, pycparser, pyasn1, psycopg2-binary, psycopg-binary, psycopg, protobuf, pluggy, packaging, numpy, msgpack, MarkupSafe, iniconfig, idna, hyperframe, httptools, hpack, h11, greenlet, google-crc32c, coverage, click, charset_normalizer, certifi, cachetools, annotated-types, uvicorn, typing-inspection, sqlalchemy, sentry-sdk, rsa, requests, python-dateutil, pytest, pydantic-core, pyasn1-modules, proto-plus, Mako, httplib2, httpcore, h2, grpcio, googleapis-common-protos, google-resumable-media, deprecated, cffi, anyio, watchfiles, starlette, pytest-cov, pytest-asyncio, pydantic, pandas, limits, httpx, grpcio-status, google-auth, cryptography, cachecontrol, alembic, slowapi, google-auth-httplib2, google-api-core, fastapi, google-cloud-core, google-api-python-client, google-cloud-storage, google-cloud-firestore, google-ai-generativelanguage, google-generativeai, firebase-admin
2025-09-28T09:34:07.508976451Z 
2025-09-28T09:34:07.518096642Z Successfully installed Mako-1.3.10 MarkupSafe-3.0.3 alembic-1.16.5 annotated-types-0.7.0 anyio-4.11.0 cachecontrol-0.14.3 cachetools-5.5.2 certifi-2025.8.3 cffi-2.0.0 charset_normalizer-3.4.3 click-8.3.0 coverage-7.10.7 cryptography-46.0.1 deprecated-1.2.18 fastapi-0.117.1 firebase-admin-7.1.0 google-ai-generativelanguage-0.6.15 google-api-core-2.25.1 google-api-python-client-2.183.0 google-auth-2.40.3 google-auth-httplib2-0.2.0 google-cloud-core-2.4.3 google-cloud-firestore-2.21.0 google-cloud-storage-3.4.0 google-crc32c-1.7.1 google-generativeai-0.8.5 google-resumable-media-2.7.2 googleapis-common-protos-1.70.0 greenlet-3.2.4 grpcio-1.75.1 grpcio-status-1.71.2 h11-0.16.0 h2-4.3.0 hpack-4.1.0 httpcore-1.0.9 httplib2-0.31.0 httptools-0.6.4 httpx-0.28.1 hyperframe-6.1.0 idna-3.10 iniconfig-2.1.0 limits-5.5.0 msgpack-1.1.1 numpy-2.3.3 packaging-25.0 pandas-2.3.2 pluggy-1.6.0 proto-plus-1.26.1 protobuf-5.29.5 psycopg-3.2.10 psycopg-binary-3.2.10 psycopg2-binary-2.9.10 pyasn1-0.6.1 pyasn1-modules-0.4.2 pycparser-2.23 pydantic-2.11.9 pydantic-core-2.33.2 pygments-2.19.2 pyjwt-2.10.1 pymysql-1.1.2 pyparsing-3.2.5 pytest-8.4.2 pytest-asyncio-1.2.0 pytest-cov-7.0.0 python-dateutil-2.9.0.post0 python-dotenv-1.1.1 python-multipart-0.0.20 pytz-2025.2 pyyaml-6.0.3 rapidfuzz-3.14.1 requests-2.32.5 rsa-4.9.1 sentry-sdk-2.39.0 six-1.17.0 slowapi-0.1.9 sniffio-1.3.1 sqlalchemy-2.0.43 starlette-0.48.0 structlog-25.4.0 tenacity-9.1.2 tqdm-4.67.1 typing-extensions-4.15.0 typing-inspection-0.4.1 tzdata-2025.2 uritemplate-4.2.0 urllib3-2.5.0 uvicorn-0.37.0 uvloop-0.21.0 watchfiles-1.1.0 websockets-15.0.1 wrapt-1.17.3
2025-09-28T09:34:07.52476747Z 
2025-09-28T09:34:07.524783101Z [notice] A new release of pip is available: 25.1.1 -> 25.2
2025-09-28T09:34:07.524787821Z [notice] To update, run: pip install --upgrade pip
2025-09-28T09:34:38.753145478Z ==> Uploading build...
2025-09-28T09:34:58.986284809Z ==> Uploaded in 15.8s. Compression took 4.4s
2025-09-28T09:34:59.08306411Z ==> Build successful 🎉
2025-09-28T09:35:22.388436219Z ==> Deploying...
2025-09-28T09:35:55.589145206Z ==> Running '   cd backend && python init_db.py && uvicorn src.main:app --host 0.0.0.0 --port $PORT'
2025-09-28T09:35:59.278725136Z 🔄 Initializing database...
2025-09-28T09:35:59.278745016Z ✅ Database initialized successfully!
2025-09-28T09:36:26.586949711Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-28T09:36:26.586974171Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-28T09:36:26.586978411Z   warnings.warn(message, UserWarning)
2025-09-28T09:36:26.686768545Z INFO:     Started server process [56]
2025-09-28T09:36:26.686794716Z INFO:     Waiting for application startup.
2025-09-28T09:36:27.312043115Z INFO:     Application startup complete.
2025-09-28T09:36:27.312566088Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-28T09:36:28.056688345Z ==> No open ports detected, continuing to scan...
2025-09-28T09:36:28.192462963Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-28T09:36:28.192488423Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-28T09:36:28.192496153Z ✅ Gemini API key loaded successfully
2025-09-28T09:36:28.192502084Z 📊 Using model: gemini-flash-latest, temperature: 0.8
2025-09-28T09:36:28.192561215Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-28T09:36:28.192567035Z ✅ Gemini model 'gemini-flash-latest' configured successfully
2025-09-28T09:36:28.192570635Z ✅ AI Product Descriptions API started successfully
2025-09-28T09:36:28.192574315Z 🤖 Model: gemini-flash-latest (Live mode)
2025-09-28T09:36:28.192578286Z 🌡️  Temperature: 0.8
2025-09-28T09:36:28.192581796Z ✅ API key configured - ready for AI generation
2025-09-28T09:36:28.192586526Z 💳 Credit service initialized - rate limiting enabled
2025-09-28T09:36:28.192592686Z 📋 Subscription plans initialized
2025-09-28T09:36:28.192597536Z INFO:     127.0.0.1:55408 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-28T09:36:28.273060257Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-28T09:36:33.044656711Z ==> Your service is live 🎉
2025-09-28T09:36:33.318244548Z ==> 
2025-09-28T09:36:33.392935927Z ==> ///////////////////////////////////////////////////////////
2025-09-28T09:36:33.467110687Z ==> 
2025-09-28T09:36:33.544630566Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-28T09:36:33.620611425Z ==> 
2025-09-28T09:36:33.695054605Z ==> ///////////////////////////////////////////////////////////
2025-09-28T09:36:35.085554243Z INFO:     35.197.37.4:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-28T09:39:09.213741823Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:09.29310868Z INFO:     41.238.10.39:0 - "WebSocket /ws/payments" [accepted]
2025-09-28T09:39:09.293440678Z INFO:     connection open
2025-09-28T09:39:09.388331592Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:09.541799386Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:09.544369034Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:39:09.986935927Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:39:09.98780058Z ERROR:src.payments.endpoints:Error getting user subscription: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T09:39:09.988122209Z WARNING:src.database.deps:Rollback failed: Method 'rollback()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T09:39:09.98816571Z ERROR:src.database.deps:Database session error: 500: Failed to get user subscription: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T09:39:09.988262652Z WARNING:src.database.deps:Close failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T09:39:09.988344335Z WARNING:src.database.deps:Remove from registry failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T09:39:09.988653192Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 500 Internal Server Error
2025-09-28T09:39:09.990395898Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:10.365839487Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:39:10.366431103Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:10.3693542Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:39:10.57326533Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:39:10.573874666Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:10.576928646Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:39:10.790962592Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:10.798946262Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:39:10.802086814Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:39:11.003061177Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:11.199272465Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:11.413835045Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:23.528188659Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/plans HTTP/1.1" 200 OK
2025-09-28T09:39:23.72149575Z INFO:     41.238.10.39:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-28T09:39:24.068296526Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:39:24.071135001Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:39:24.223501476Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:24.753661572Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:39:24.756493196Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:39:24.866002245Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:27.888166834Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/checkout HTTP/1.1" 200 OK
2025-09-28T09:39:28.473281593Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:39:28.478129771Z 🎯 STEP 1: CREATE_CHECKOUT ENDPOINT CALLED
2025-09-28T09:39:28.478150021Z Request data: variant_id='1013286' success_url='https://www.productgeniepro.com/billing?success=true' cancel_url='https://www.productgeniepro.com/pricing?cancelled=true'
2025-09-28T09:39:28.478155432Z Variant ID: 1013286
2025-09-28T09:39:28.478160112Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-28T09:39:28.478163852Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-28T09:39:28.478168322Z 🎯 STEP 2: GETTING CLIENT INFO
2025-09-28T09:39:28.478172812Z Client info: {'ip_address': '41.238.10.39', 'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36', 'correlation_id': 'd495c168-33d2-442b-bd7d-554a9462555f'}
2025-09-28T09:39:28.478191403Z 🎯 STEP 3: EXTRACTING AUTH DATA
2025-09-28T09:39:28.478194523Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T09:39:28.478196933Z User email: ziad321hussein@gmail.com
2025-09-28T09:39:28.478199313Z 🎯 STEP 4: VALIDATING USER
2025-09-28T09:39:28.478201473Z ✅ STEP 4 SUCCESS: User validated
2025-09-28T09:39:28.478203763Z 🎯 STEP 5: VALIDATING VARIANT ID
2025-09-28T09:39:28.478206033Z ✅ STEP 5 SUCCESS: Variant ID validated
2025-09-28T09:39:28.478208313Z 🎯 STEP 6: CALLING LEMON_SQUEEZY SERVICE
2025-09-28T09:39:28.478210463Z 🎯 LEMON SQUEEZY PAYLOAD DEBUG 🎯
2025-09-28T09:39:28.478212803Z === VARIABLES ===
2025-09-28T09:39:28.478215083Z Variant ID: 1013286
2025-09-28T09:39:28.478217373Z Store ID: 224253
2025-09-28T09:39:28.478219623Z User ID: bpR6MB3823T20EK7BEa3cs2y22u2
2025-09-28T09:39:28.478221914Z User Email: ziad321hussein@gmail.com
2025-09-28T09:39:28.478224214Z Success URL: https://www.productgeniepro.com/billing?success=true
2025-09-28T09:39:28.478226383Z Cancel URL: https://www.productgeniepro.com/pricing?cancelled=true
2025-09-28T09:39:28.478228804Z Test Mode: True
2025-09-28T09:39:28.478231084Z === PAYLOAD BEING SENT ===
2025-09-28T09:39:28.478233314Z {
2025-09-28T09:39:28.478235594Z   "data": {
2025-09-28T09:39:28.478237824Z     "type": "checkouts",
2025-09-28T09:39:28.478240014Z     "attributes": {
2025-09-28T09:39:28.478242154Z       "checkout_options": {
2025-09-28T09:39:28.478244244Z         "embed": false,
2025-09-28T09:39:28.478246764Z         "media": false
2025-09-28T09:39:28.478249024Z       },
2025-09-28T09:39:28.478251414Z       "checkout_data": {
2025-09-28T09:39:28.478253704Z         "email": "ziad321hussein@gmail.com",
2025-09-28T09:39:28.478256004Z         "custom": {
2025-09-28T09:39:28.478258824Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-28T09:39:28.478261095Z         }
2025-09-28T09:39:28.478263255Z       },
2025-09-28T09:39:28.478265535Z       "product_options": {
2025-09-28T09:39:28.478267805Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true"
2025-09-28T09:39:28.478270135Z       }
2025-09-28T09:39:28.478272395Z     },
2025-09-28T09:39:28.478274585Z     "relationships": {
2025-09-28T09:39:28.478276925Z       "store": {
2025-09-28T09:39:28.478279155Z         "data": {
2025-09-28T09:39:28.478281345Z           "type": "stores",
2025-09-28T09:39:28.478283665Z           "id": "224253"
2025-09-28T09:39:28.478285865Z         }
2025-09-28T09:39:28.478288155Z       },
2025-09-28T09:39:28.478290425Z       "variant": {
2025-09-28T09:39:28.478292715Z         "data": {
2025-09-28T09:39:28.478294975Z           "type": "variants",
2025-09-28T09:39:28.478297235Z           "id": "1013286"
2025-09-28T09:39:28.478299485Z         }
2025-09-28T09:39:28.478304236Z       }
2025-09-28T09:39:28.478306596Z     }
2025-09-28T09:39:28.478308976Z   }
2025-09-28T09:39:28.478311356Z }
2025-09-28T09:39:28.478313606Z === HEADERS ===
2025-09-28T09:39:28.478316046Z {
2025-09-28T09:39:28.478321176Z   "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NGQ1OWNlZi1kYmI4LTRlYTUtYjE3OC1kMjU0MGZjZDY5MTkiLCJqdGkiOiJkOGY2NTljZjdhMzA3ZGNjM2RjNTk4ZjNiMzU4YTk3YTczYzdhNGJkNDg2ZDlkM2JhYTE4OGQ4Y2MxMGU1Zjc5YWQzODJkZTgyYjgxNjRiNiIsImlhdCI6MTc1ODgyNzU5MC41NzYwMjcsIm5iZiI6MTc1ODgyNzU5MC41NzYwMjksImV4cCI6MjA3NDM2MDM5MC41NjA2NzcsInN1YiI6IjU1NzE5NjQiLCJzY29wZXMiOltdfQ.v6DQ8CrPGAovPSiYrv6Y3GkQ3DWHPcC0aAiZ9mP5BsXCwXoz5Kf1OY-fLAHC4ikcmx2RYZuLbSrF_Xxa4mvw2exFnJMsODiiuzItzhdVGUwR89IzbFAD6hcto-w0ERT3gjP781BJ-lxa7pzC4tCADeRhAtMPM7MZ7h7g-0JsRjXyNDrM0ArKoN84kiGHojmPCBomBuXTQ-mC_VQEWn8PKxTbZEem7FoyP4ydK46xYQu-naukuPTOZHRQ44Mdz_16JQ7Cda2pbfJo2osSPGaLTYUKvH0-aF2jlZToxGCPPr8LbPsHo1-96W2D6CBkCF0kFd6BQd0PKw64X-2ywolNwyna51cLKvkZuOHrh2Z8XVG0GONxeo6b1mFzgs8PzSkaPJ5Er_vhcRQVhAolOVmBHcZ61FUUJ208hR1FUVzMHlrTWtcTAi6HUjthHZB2ZL0xrIkDcWQPxG38i8ArAslXFLytqDTU3tePixq0WDHHBnBq8XSbleFoLH8rdc0j4v5KEPoJyXUS7MrHkiJ602WwLFPuczEdkRPvnSNeRKhsSlPkO8SiQFdHZ6VLCGQoEWDvm7SL2U6lmOJ2T1imOAGiTveGoliycICl_HQo29Fk0VFMFVa_jei7HCgdsLArClUHceqfx5UTOsrWxcd8zr75ALBqDzIWT9tpG5ifdTappes",
2025-09-28T09:39:28.478329006Z   "Accept": "application/vnd.api+json",
2025-09-28T09:39:28.478331456Z   "Content-Type": "application/vnd.api+json",
2025-09-28T09:39:28.478333866Z   "Version": "2021-07-07"
2025-09-28T09:39:28.478336046Z }
2025-09-28T09:39:28.478338297Z === API ENDPOINT ===
2025-09-28T09:39:28.478340597Z POST https://api.lemonsqueezy.com/v1/checkouts
2025-09-28T09:39:28.478343117Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:39:28.583386798Z === RESPONSE ===
2025-09-28T09:39:28.583412338Z Status: Unknown
2025-09-28T09:39:28.583415499Z Response: {
2025-09-28T09:39:28.583418048Z   "jsonapi": {
2025-09-28T09:39:28.583421109Z     "version": "1.0"
2025-09-28T09:39:28.583423299Z   },
2025-09-28T09:39:28.583425559Z   "links": {
2025-09-28T09:39:28.583428699Z     "self": "https://api.lemonsqueezy.com/v1/checkouts/f2ffaa91-43d8-4587-9603-7090943f63c1"
2025-09-28T09:39:28.583430929Z   },
2025-09-28T09:39:28.583433199Z   "data": {
2025-09-28T09:39:28.583435379Z     "type": "checkouts",
2025-09-28T09:39:28.583438229Z     "id": "f2ffaa91-43d8-4587-9603-7090943f63c1",
2025-09-28T09:39:28.583440609Z     "attributes": {
2025-09-28T09:39:28.583443629Z       "store_id": 224253,
2025-09-28T09:39:28.583446219Z       "variant_id": 1013286,
2025-09-28T09:39:28.583448719Z       "custom_price": null,
2025-09-28T09:39:28.583450969Z       "product_options": {
2025-09-28T09:39:28.58345334Z         "name": "",
2025-09-28T09:39:28.5834556Z         "description": "",
2025-09-28T09:39:28.58345778Z         "media": [],
2025-09-28T09:39:28.58346064Z         "redirect_url": "https://www.productgeniepro.com/billing?success=true",
2025-09-28T09:39:28.58346336Z         "receipt_button_text": "",
2025-09-28T09:39:28.58346545Z         "receipt_link_url": "",
2025-09-28T09:39:28.58346764Z         "receipt_thank_you_note": "",
2025-09-28T09:39:28.58346989Z         "enabled_variants": [],
2025-09-28T09:39:28.58347205Z         "confirmation_title": "",
2025-09-28T09:39:28.58347416Z         "confirmation_message": "",
2025-09-28T09:39:28.58347629Z         "confirmation_button_text": ""
2025-09-28T09:39:28.58347837Z       },
2025-09-28T09:39:28.58348037Z       "checkout_options": {
2025-09-28T09:39:28.58348248Z         "embed": false,
2025-09-28T09:39:28.58348464Z         "media": false,
2025-09-28T09:39:28.58348674Z         "logo": true,
2025-09-28T09:39:28.58348874Z         "desc": true,
2025-09-28T09:39:28.583490741Z         "discount": true,
2025-09-28T09:39:28.583492701Z         "skip_trial": false,
2025-09-28T09:39:28.58349529Z         "quantity": 1,
2025-09-28T09:39:28.583497491Z         "subscription_preview": true,
2025-09-28T09:39:28.583499661Z         "locale": "en"
2025-09-28T09:39:28.583501741Z       },
2025-09-28T09:39:28.583503851Z       "checkout_data": {
2025-09-28T09:39:28.583505911Z         "email": "ziad321hussein@gmail.com",
2025-09-28T09:39:28.583507961Z         "name": "",
2025-09-28T09:39:28.583510551Z         "billing_address": [],
2025-09-28T09:39:28.583527762Z         "tax_number": "",
2025-09-28T09:39:28.583530251Z         "discount_code": "",
2025-09-28T09:39:28.583532331Z         "custom": {
2025-09-28T09:39:28.583534522Z           "user_id": "bpR6MB3823T20EK7BEa3cs2y22u2"
2025-09-28T09:39:28.583536632Z         },
2025-09-28T09:39:28.583538752Z         "variant_quantities": []
2025-09-28T09:39:28.583540902Z       },
2025-09-28T09:39:28.583543032Z       "preview": false,
2025-09-28T09:39:28.583545862Z       "expires_at": null,
2025-09-28T09:39:28.583547982Z       "created_at": "2025-09-28T09:39:28.000000Z",
2025-09-28T09:39:28.583550072Z       "updated_at": "2025-09-28T09:39:28.000000Z",
2025-09-28T09:39:28.583552372Z       "test_mode": true,
2025-09-28T09:39:28.583555202Z       "url": "https://product-genie.lemonsqueezy.com/checkout/custom/f2ffaa91-43d8-4587-9603-7090943f63c1?signature=d625701e529d1252923cd458cf8cb9d3cf818ec34c61919863d7a7c7ca6eb9c3"
2025-09-28T09:39:28.583557212Z     },
2025-09-28T09:39:28.583559362Z     "relationships": {
2025-09-28T09:39:28.583561492Z       "store": {
2025-09-28T09:39:28.583563612Z         "links": {
2025-09-28T09:39:28.583566283Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/f2ffaa91-43d8-4587-9603-7090943f63c1/store",
2025-09-28T09:39:28.583569063Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/f2ffaa91-43d8-4587-9603-7090943f63c1/relationships/store"
2025-09-28T09:39:28.583571083Z         }
2025-09-28T09:39:28.583573313Z       },
2025-09-28T09:39:28.583575373Z       "variant": {
2025-09-28T09:39:28.583577483Z         "links": {
2025-09-28T09:39:28.583579643Z           "related": "https://api.lemonsqueezy.com/v1/checkouts/f2ffaa91-43d8-4587-9603-7090943f63c1/variant",
2025-09-28T09:39:28.583581763Z           "self": "https://api.lemonsqueezy.com/v1/checkouts/f2ffaa91-43d8-4587-9603-7090943f63c1/relationships/variant"
2025-09-28T09:39:28.583583973Z         }
2025-09-28T09:39:28.583585953Z       }
2025-09-28T09:39:28.583587973Z     },
2025-09-28T09:39:28.583589973Z     "links": {
2025-09-28T09:39:28.583592303Z       "self": "https://api.lemonsqueezy.com/v1/checkouts/f2ffaa91-43d8-4587-9603-7090943f63c1"
2025-09-28T09:39:28.583594423Z     }
2025-09-28T09:39:28.583596493Z   }
2025-09-28T09:39:28.583598563Z }
2025-09-28T09:39:28.583600653Z ✅ STEP 6 SUCCESS: Lemon Squeezy service call successful
2025-09-28T09:39:28.583603423Z Result: {'success': True, 'checkout_url': 'https://product-genie.lemonsqueezy.com/checkout/custom/f2ffaa91-43d8-4587-9603-7090943f63c1?signature=d625701e529d1252923cd458cf8cb9d3cf818ec34c61919863d7a7c7ca6eb9c3', 'checkout_id': 'f2ffaa91-43d8-4587-9603-7090943f63c1'}
2025-09-28T09:39:28.583605724Z INFO:     41.238.10.39:0 - "POST /api/payment/checkout HTTP/1.1" 200 OK
2025-09-28T09:39:28.678695293Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:28.888410585Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:39:28.891946078Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:39:28.981826101Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:39:31.101541908Z INFO:     connection closed
2025-09-28T09:40:13.549962926Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-28T09:40:13.549687+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-28T09:40:13.560019001Z ERROR:src.payments.lemon_squeezy:No user_id found in custom data for order 6490824
2025-09-28T09:40:13.560527174Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK
2025-09-28T09:40:21.330810106Z INFO:     41.238.10.39:0 - "WebSocket /ws/payments" [accepted]
2025-09-28T09:40:21.331020181Z INFO:     connection open
2025-09-28T09:40:21.604664854Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:40:21.60491742Z WARNING:src.database.deps:Commit failed (may be expected): Method 'commit()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T09:40:21.604974072Z WARNING:src.database.deps:Close failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T09:40:21.605052914Z WARNING:src.database.deps:Remove from registry failed: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T09:40:21.605333241Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:40:21.607023296Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:21.793489346Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:40:21.817466317Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:40:21.820412354Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:22.003074875Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:40:22.003551308Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:22.00666476Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:40:22.189753292Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:22.371019966Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:26.742726501Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:27.272372242Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:40:27.277006173Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:40:27.394631895Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:27.868764367Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:40:27.871719414Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:40:27.975832441Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:30.064010235Z INFO:     41.238.10.39:0 - "GET /api/payment/plans HTTP/1.1" 200 OK
2025-09-28T09:40:30.575507159Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:40:30.578487677Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:40:30.744074219Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:30.969638498Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T09:40:30.974099825Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T09:40:31.055697009Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T09:40:45.532868633Z WARNING:security:{"event_type": "webhook_received", "user_id": null, "timestamp": "2025-09-28T09:40:45.532628+00:00", "ip_address": null, "user_agent": null, "event_data": {"signature_provided": true, "signature_valid": true}, "security_level": "high", "success": true, "error_message": null, "session_id": null, "correlation_id": null}
2025-09-28T09:40:45.540868663Z WARNING:src.payments.lemon_squeezy:Unknown variant_id: 1013286
2025-09-28T09:40:45.540911995Z ERROR:src.payments.lemon_squeezy:Unknown variant_id 1013286 in subscription update
2025-09-28T09:40:45.541443128Z INFO:     18.116.135.47:0 - "POST /api/payment/webhook HTTP/1.1" 200 OK