2025-09-28T06:33:22.412865048Z Using cached typing_inspection-0.4.1-py3-none-any.whl (14 kB)
2025-09-28T06:33:22.413982825Z Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
2025-09-28T06:33:22.415376018Z Using cached google_api_python_client-2.183.0-py3-none-any.whl (14.2 MB)
2025-09-28T06:33:22.426682908Z Using cached google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
2025-09-28T06:33:22.427832506Z Using cached httplib2-0.31.0-py3-none-any.whl (91 kB)
2025-09-28T06:33:22.428987523Z Using cached pyparsing-3.2.5-py3-none-any.whl (113 kB)
2025-09-28T06:33:22.430171811Z Using cached uritemplate-4.2.0-py3-none-any.whl (11 kB)
2025-09-28T06:33:22.431282898Z Using cached mako-1.3.10-py3-none-any.whl (78 kB)
2025-09-28T06:33:22.432509897Z Using cached markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
2025-09-28T06:33:22.47785511Z Using cached pycparser-2.23-py3-none-any.whl (118 kB)
2025-09-28T06:33:22.863725998Z Installing collected packages: pytz, wrapt, urllib3, uritemplate, tzdata, typing-extensions, tqdm, tenacity, structlog, sniffio, six, rapidfuzz, python-multipart, python-dotenv, pyparsing, pymysql, pyjwt, pygments, pycparser, pyasn1, psycopg2-binary, psycopg-binary, psycopg, protobuf, pluggy, packaging, numpy, msgpack, MarkupSafe, iniconfig, idna, hyperframe, hpack, h11, greenlet, google-crc32c, coverage, click, charset_normalizer, certifi, cachetools, annotated-types, uvicorn, typing-inspection, sqlalchemy, sentry-sdk, rsa, requests, python-dateutil, pytest, pydantic-core, pyasn1-modules, proto-plus, Mako, httplib2, httpcore, h2, grpcio, googleapis-common-protos, google-resumable-media, deprecated, cffi, anyio, starlette, pytest-cov, pytest-asyncio, pydantic, pandas, limits, httpx, grpcio-status, google-auth, cryptography, cachecontrol, alembic, slowapi, google-auth-httplib2, google-api-core, fastapi, google-cloud-core, google-api-python-client, google-cloud-storage, google-cloud-firestore, google-ai-generativelanguage, google-generativeai, firebase-admin
2025-09-28T06:34:00.555816826Z 
2025-09-28T06:34:00.564844192Z Successfully installed Mako-1.3.10 MarkupSafe-3.0.3 alembic-1.16.5 annotated-types-0.7.0 anyio-4.11.0 cachecontrol-0.14.3 cachetools-5.5.2 certifi-2025.8.3 cffi-2.0.0 charset_normalizer-3.4.3 click-8.3.0 coverage-7.10.7 cryptography-46.0.1 deprecated-1.2.18 fastapi-0.117.1 firebase-admin-7.1.0 google-ai-generativelanguage-0.6.15 google-api-core-2.25.1 google-api-python-client-2.183.0 google-auth-2.40.3 google-auth-httplib2-0.2.0 google-cloud-core-2.4.3 google-cloud-firestore-2.21.0 google-cloud-storage-3.4.0 google-crc32c-1.7.1 google-generativeai-0.8.5 google-resumable-media-2.7.2 googleapis-common-protos-1.70.0 greenlet-3.2.4 grpcio-1.75.1 grpcio-status-1.71.2 h11-0.16.0 h2-4.3.0 hpack-4.1.0 httpcore-1.0.9 httplib2-0.31.0 httpx-0.28.1 hyperframe-6.1.0 idna-3.10 iniconfig-2.1.0 limits-5.5.0 msgpack-1.1.1 numpy-2.3.3 packaging-25.0 pandas-2.3.2 pluggy-1.6.0 proto-plus-1.26.1 protobuf-5.29.5 psycopg-3.2.10 psycopg-binary-3.2.10 psycopg2-binary-2.9.10 pyasn1-0.6.1 pyasn1-modules-0.4.2 pycparser-2.23 pydantic-2.11.9 pydantic-core-2.33.2 pygments-2.19.2 pyjwt-2.10.1 pymysql-1.1.2 pyparsing-3.2.5 pytest-8.4.2 pytest-asyncio-1.2.0 pytest-cov-7.0.0 python-dateutil-2.9.0.post0 python-dotenv-1.1.1 python-multipart-0.0.20 pytz-2025.2 rapidfuzz-3.14.1 requests-2.32.5 rsa-4.9.1 sentry-sdk-2.39.0 six-1.17.0 slowapi-0.1.9 sniffio-1.3.1 sqlalchemy-2.0.43 starlette-0.48.0 structlog-25.4.0 tenacity-9.1.2 tqdm-4.67.1 typing-extensions-4.15.0 typing-inspection-0.4.1 tzdata-2025.2 uritemplate-4.2.0 urllib3-2.5.0 uvicorn-0.37.0 wrapt-1.17.3
2025-09-28T06:34:00.571814938Z 
2025-09-28T06:34:00.571831879Z [notice] A new release of pip is available: 25.1.1 -> 25.2
2025-09-28T06:34:00.571834309Z [notice] To update, run: pip install --upgrade pip
2025-09-28T06:34:46.823323315Z ==> Uploading build...
2025-09-28T06:35:10.246577436Z ==> Uploaded in 18.3s. Compression took 5.2s
2025-09-28T06:35:10.342567749Z ==> Build successful 🎉
2025-09-28T06:35:17.761008773Z ==> Deploying...
2025-09-28T06:35:48.39435364Z ==> Running '   cd backend && python init_db.py && uvicorn src.main:app --host 0.0.0.0 --port $PORT'
2025-09-28T06:35:56.194704849Z 🔄 Initializing database...
2025-09-28T06:35:56.19474127Z ✅ Database initialized successfully!
2025-09-28T06:36:15.492975187Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-28T06:36:15.493000377Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-28T06:36:15.493006247Z   warnings.warn(message, UserWarning)
2025-09-28T06:36:15.591704558Z INFO:     Started server process [56]
2025-09-28T06:36:15.591731258Z INFO:     Waiting for application startup.
2025-09-28T06:36:16.218177961Z INFO:     Application startup complete.
2025-09-28T06:36:16.218403554Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-28T06:36:16.789054835Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-28T06:36:16.789071325Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-28T06:36:16.789075465Z ✅ Gemini API key loaded successfully
2025-09-28T06:36:16.789079175Z 📊 Using model: gemini-1.5-pro, temperature: 0.8
2025-09-28T06:36:16.789082655Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-28T06:36:16.789086115Z ✅ AI Product Descriptions API started successfully
2025-09-28T06:36:16.789089535Z 🤖 Model: gemini-1.5-pro (Live mode)
2025-09-28T06:36:16.789093035Z 🌡️  Temperature: 0.8
2025-09-28T06:36:16.789096515Z ✅ API key configured - ready for AI generation
2025-09-28T06:36:16.789100035Z 💳 Credit service initialized - rate limiting enabled
2025-09-28T06:36:16.789103746Z 📋 Subscription plans initialized
2025-09-28T06:36:16.789108375Z INFO:     127.0.0.1:51038 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-28T06:36:18.504950282Z ==> Your service is live 🎉
2025-09-28T06:36:18.585493031Z ==> 
2025-09-28T06:36:18.661070791Z ==> ///////////////////////////////////////////////////////////
2025-09-28T06:36:18.73688031Z ==> 
2025-09-28T06:36:18.81598398Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-28T06:36:18.89284902Z ==> 
2025-09-28T06:36:18.969481949Z ==> ///////////////////////////////////////////////////////////
2025-09-28T06:36:20.252534373Z INFO:     35.230.74.10:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-28T06:41:22.76984Z ==> Detected service running on port 10000
2025-09-28T06:41:22.956835149Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-28T06:41:22.76984Z ==> Detected service running on port 10000
2025-09-28T06:41:22.956835149Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-28T06:52:13.833526223Z ==> Running '   cd backend && python init_db.py && uvicorn src.main:app --host 0.0.0.0 --port $PORT'
2025-09-28T06:52:21.207820397Z 🔄 Initializing database...
2025-09-28T06:52:21.207861437Z ✅ Database initialized successfully!
2025-09-28T06:52:29.485996718Z INFO:     Shutting down
2025-09-28T06:52:29.586519951Z INFO:     Waiting for application shutdown.
2025-09-28T06:52:29.586697194Z INFO:     Application shutdown complete.
2025-09-28T06:52:29.586731144Z INFO:     Finished server process [56]
2025-09-28T06:52:40.938499952Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-28T06:52:40.938539323Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-28T06:52:40.938547713Z   warnings.warn(message, UserWarning)
2025-09-28T06:52:41.034726943Z INFO:     Started server process [38]
2025-09-28T06:52:41.034749163Z INFO:     Waiting for application startup.
2025-09-28T06:52:41.617659687Z INFO:     Application startup complete.
2025-09-28T06:52:41.617957761Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-28T06:52:47.443147013Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-28T06:52:47.443172473Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-28T06:52:47.443179264Z ✅ Gemini API key loaded successfully
2025-09-28T06:52:47.443188564Z 📊 Using model: gemini-1.5-pro, temperature: 0.8
2025-09-28T06:52:47.443193954Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-28T06:52:47.443199884Z ✅ AI Product Descriptions API started successfully
2025-09-28T06:52:47.443206614Z 🤖 Model: gemini-1.5-pro (Live mode)
2025-09-28T06:52:47.443212944Z 🌡️  Temperature: 0.8
2025-09-28T06:52:47.443218234Z ✅ API key configured - ready for AI generation
2025-09-28T06:52:47.443223574Z 💳 Credit service initialized - rate limiting enabled
2025-09-28T06:52:47.443229114Z 📋 Subscription plans initialized
2025-09-28T06:52:47.443235454Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T06:52:47.531164434Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:47.531360166Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:47.531987226Z WARNING:  Unsupported upgrade request.
2025-09-28T06:52:47.531995766Z WARNING:  No supported WebSocket library detected. Please use "pip install 'uvicorn[standard]'", or install 'websockets' or 'wsproto' manually.
2025-09-28T06:52:47.53232908Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:47.533322675Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:47.533529648Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:47.533720901Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T06:52:47.533906074Z INFO:     41.238.10.39:0 - "GET /ws/payments HTTP/1.1" 404 Not Found
2025-09-28T06:52:47.946057566Z ERROR:src.payments.endpoints:Error getting user subscription: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T06:52:47.946553704Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 500 Internal Server Error
2025-09-28T06:52:48.034338241Z ERROR:    Exception in ASGI application
2025-09-28T06:52:48.034356631Z   + Exception Group Traceback (most recent call last):
2025-09-28T06:52:48.034361451Z   |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 79, in collapse_excgroups
2025-09-28T06:52:48.034365251Z   |     yield
2025-09-28T06:52:48.034368871Z   |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 183, in __call__
2025-09-28T06:52:48.034372331Z   |     async with anyio.create_task_group() as task_group:
2025-09-28T06:52:48.034385652Z   |                ~~~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:52:48.034388001Z   |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 781, in __aexit__
2025-09-28T06:52:48.034390361Z   |     raise BaseExceptionGroup(
2025-09-28T06:52:48.034392501Z   |         "unhandled errors in a TaskGroup", self._exceptions
2025-09-28T06:52:48.034395152Z   |     ) from None
2025-09-28T06:52:48.034398012Z   | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
2025-09-28T06:52:48.034400122Z   +-+---------------- 1 ----------------
2025-09-28T06:52:48.034402152Z     | Traceback (most recent call last):
2025-09-28T06:52:48.034405232Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:52:48.034407432Z     |     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:52:48.034409552Z     |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034411622Z     |         self.scope, self.receive, self.send
2025-09-28T06:52:48.034413672Z     |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034415742Z     |     )
2025-09-28T06:52:48.034417832Z     |     ^
2025-09-28T06:52:48.034419912Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:52:48.034422032Z     |     return await self.app(scope, receive, send)
2025-09-28T06:52:48.034424062Z     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034426202Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:52:48.034428312Z     |     await super().__call__(scope, receive, send)
2025-09-28T06:52:48.034430412Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:52:48.034432462Z     |     await self.middleware_stack(scope, receive, send)
2025-09-28T06:52:48.034434562Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:52:48.034436642Z     |     raise exc
2025-09-28T06:52:48.034438792Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:52:48.034440872Z     |     await self.app(scope, receive, _send)
2025-09-28T06:52:48.034442982Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:52:48.034445062Z     |     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:52:48.034447122Z     |                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:52:48.034449762Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:52:48.034452442Z     |     self.gen.throw(value)
2025-09-28T06:52:48.034454482Z     |     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:52:48.034456542Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:52:48.034476293Z     |     raise exc
2025-09-28T06:52:48.034481223Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:52:48.034485173Z     |     response = await self.dispatch_func(request, call_next)
2025-09-28T06:52:48.034488493Z     |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034498513Z     |   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:52:48.034501873Z     |     response = await call_next(request)
2025-09-28T06:52:48.034505453Z     |                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034508913Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:52:48.034512233Z     |     raise app_exc
2025-09-28T06:52:48.034515453Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:52:48.034518653Z     |     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:52:48.034522043Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:52:48.034525174Z     |     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:52:48.034528303Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:52:48.034545454Z     |     await self.app(scope, receive, send)
2025-09-28T06:52:48.034549154Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:52:48.034565124Z     |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:52:48.034567634Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:52:48.034569854Z     |     raise exc
2025-09-28T06:52:48.034572034Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:52:48.034574174Z     |     await app(scope, receive, sender)
2025-09-28T06:52:48.034576294Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:52:48.034578344Z     |     await self.middleware_stack(scope, receive, send)
2025-09-28T06:52:48.034580374Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:52:48.034582474Z     |     await route.handle(scope, receive, send)
2025-09-28T06:52:48.034584804Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:52:48.034586844Z     |     await self.app(scope, receive, send)
2025-09-28T06:52:48.034588924Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:52:48.034590955Z     |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:52:48.034593124Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:52:48.034595215Z     |     raise exc
2025-09-28T06:52:48.034597315Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:52:48.034599395Z     |     await app(scope, receive, sender)
2025-09-28T06:52:48.034601444Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:52:48.034603475Z     |     response = await f(request)
2025-09-28T06:52:48.034605535Z     |                ^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034607605Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 297, in app
2025-09-28T06:52:48.034614105Z     |     async with AsyncExitStack() as async_exit_stack:
2025-09-28T06:52:48.034616255Z     |                ~~~~~~~~~~~~~~^^
2025-09-28T06:52:48.034618275Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 768, in __aexit__
2025-09-28T06:52:48.034620385Z     |     raise exc
2025-09-28T06:52:48.034622425Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 751, in __aexit__
2025-09-28T06:52:48.034624475Z     |     cb_suppress = await cb(*exc_details)
2025-09-28T06:52:48.034626535Z     |                   ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034628605Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 235, in __aexit__
2025-09-28T06:52:48.034630675Z     |     await self.gen.athrow(value)
2025-09-28T06:52:48.034632755Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/concurrency.py", line 30, in contextmanager_in_threadpool
2025-09-28T06:52:48.034634825Z     |     await anyio.to_thread.run_sync(
2025-09-28T06:52:48.034636965Z     |         cm.__exit__, type(e), e, e.__traceback__, limiter=exit_limiter
2025-09-28T06:52:48.034639045Z     |     )
2025-09-28T06:52:48.034641155Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/to_thread.py", line 56, in run_sync
2025-09-28T06:52:48.034645855Z     |     return await get_async_backend().run_sync_in_worker_thread(
2025-09-28T06:52:48.034648105Z     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034650215Z     |         func, args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
2025-09-28T06:52:48.034652305Z     |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034654355Z     |     )
2025-09-28T06:52:48.034656545Z     |     ^
2025-09-28T06:52:48.034658695Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 2485, in run_sync_in_worker_thread
2025-09-28T06:52:48.034660845Z     |     return await future
2025-09-28T06:52:48.034662976Z     |            ^^^^^^^^^^^^
2025-09-28T06:52:48.034665085Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 976, in run
2025-09-28T06:52:48.034667145Z     |     result = context.run(func, *args)
2025-09-28T06:52:48.034669236Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:52:48.034671305Z     |     self.gen.throw(value)
2025-09-28T06:52:48.034673396Z     |     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:52:48.034675476Z     |   File "/opt/render/project/src/backend/src/database/deps.py", line 73, in get_db
2025-09-28T06:52:48.034680166Z     |     db.close()
2025-09-28T06:52:48.034682336Z     |     ~~~~~~~~^^
2025-09-28T06:52:48.034684506Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2521, in close
2025-09-28T06:52:48.034686586Z     |     self._close_impl(invalidate=False)
2025-09-28T06:52:48.034688676Z     |     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034690816Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2590, in _close_impl
2025-09-28T06:52:48.034693266Z     |     transaction.close(invalidate)
2025-09-28T06:52:48.034702346Z     |     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:52:48.034704666Z     |   File "<string>", line 2, in close
2025-09-28T06:52:48.034706826Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/state_changes.py", line 119, in _go
2025-09-28T06:52:48.034713276Z     |     raise sa_exc.IllegalStateChangeError(
2025-09-28T06:52:48.034715436Z     |     ...<5 lines>...
2025-09-28T06:52:48.034717616Z     |     )
2025-09-28T06:52:48.034720406Z     | sqlalchemy.exc.IllegalStateChangeError: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T06:52:48.034722596Z     +------------------------------------
2025-09-28T06:52:48.034724506Z 
2025-09-28T06:52:48.034726746Z During handling of the above exception, another exception occurred:
2025-09-28T06:52:48.034728726Z 
2025-09-28T06:52:48.034730766Z Traceback (most recent call last):
2025-09-28T06:52:48.034732866Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:52:48.034734946Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:52:48.034737057Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034739117Z         self.scope, self.receive, self.send
2025-09-28T06:52:48.034741167Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034743277Z     )
2025-09-28T06:52:48.034745407Z     ^
2025-09-28T06:52:48.034747587Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:52:48.034749637Z     return await self.app(scope, receive, send)
2025-09-28T06:52:48.034751707Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034753897Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:52:48.034755967Z     await super().__call__(scope, receive, send)
2025-09-28T06:52:48.034758047Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:52:48.034760157Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:52:48.034762227Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:52:48.034764307Z     raise exc
2025-09-28T06:52:48.034766387Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:52:48.034768457Z     await self.app(scope, receive, _send)
2025-09-28T06:52:48.034770567Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:52:48.034772647Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:52:48.034774677Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:52:48.034776807Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:52:48.034778887Z     self.gen.throw(value)
2025-09-28T06:52:48.034780927Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:52:48.034782977Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:52:48.034785027Z     raise exc
2025-09-28T06:52:48.034787127Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:52:48.034789227Z     response = await self.dispatch_func(request, call_next)
2025-09-28T06:52:48.034791267Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034793377Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:52:48.034802607Z     response = await call_next(request)
2025-09-28T06:52:48.034804767Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034806878Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:52:48.034808987Z     raise app_exc
2025-09-28T06:52:48.034811068Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:52:48.034813128Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:52:48.034815188Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:52:48.034817328Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:52:48.034819368Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:52:48.034821418Z     await self.app(scope, receive, send)
2025-09-28T06:52:48.034823478Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:52:48.034825558Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:52:48.034827668Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:52:48.034829748Z     raise exc
2025-09-28T06:52:48.034831848Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:52:48.034833938Z     await app(scope, receive, sender)
2025-09-28T06:52:48.034844768Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:52:48.034848378Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:52:48.034852188Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:52:48.034855378Z     await route.handle(scope, receive, send)
2025-09-28T06:52:48.034858688Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:52:48.034861748Z     await self.app(scope, receive, send)
2025-09-28T06:52:48.034864608Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:48.034865318Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:52:48.034869588Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:52:48.034873079Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:52:48.034881679Z     raise exc
2025-09-28T06:52:48.034886249Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:52:48.034889999Z     await app(scope, receive, sender)
2025-09-28T06:52:48.034893649Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:52:48.034897169Z     response = await f(request)
2025-09-28T06:52:48.034899429Z                ^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034901589Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 297, in app
2025-09-28T06:52:48.034905069Z     async with AsyncExitStack() as async_exit_stack:
2025-09-28T06:52:48.034907159Z                ~~~~~~~~~~~~~~^^
2025-09-28T06:52:48.034918469Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 768, in __aexit__
2025-09-28T06:52:48.034920779Z     raise exc
2025-09-28T06:52:48.034922919Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 751, in __aexit__
2025-09-28T06:52:48.034925029Z     cb_suppress = await cb(*exc_details)
2025-09-28T06:52:48.034927129Z                   ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.034929219Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 235, in __aexit__
2025-09-28T06:52:48.034931309Z     await self.gen.athrow(value)
2025-09-28T06:52:48.03493532Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/concurrency.py", line 30, in contextmanager_in_threadpool
2025-09-28T06:52:48.0349391Z     await anyio.to_thread.run_sync(
2025-09-28T06:52:48.034943Z         cm.__exit__, type(e), e, e.__traceback__, limiter=exit_limiter
2025-09-28T06:52:48.03494626Z     )
2025-09-28T06:52:48.03494958Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/to_thread.py", line 56, in run_sync
2025-09-28T06:52:48.03495274Z     return await get_async_backend().run_sync_in_worker_thread(
2025-09-28T06:52:48.03495632Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.03495967Z         func, args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
2025-09-28T06:52:48.03496342Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.0349669Z     )
2025-09-28T06:52:48.03497016Z     ^
2025-09-28T06:52:48.03497338Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 2485, in run_sync_in_worker_thread
2025-09-28T06:52:48.0349768Z     return await future
2025-09-28T06:52:48.03497982Z            ^^^^^^^^^^^^
2025-09-28T06:52:48.03498291Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 976, in run
2025-09-28T06:52:48.03498636Z     result = context.run(func, *args)
2025-09-28T06:52:48.03498967Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:52:48.03499287Z     self.gen.throw(value)
2025-09-28T06:52:48.03499587Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:52:48.03499938Z   File "/opt/render/project/src/backend/src/database/deps.py", line 73, in get_db
2025-09-28T06:52:48.03500263Z     db.close()
2025-09-28T06:52:48.035005841Z     ~~~~~~~~^^
2025-09-28T06:52:48.03500885Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2521, in close
2025-09-28T06:52:48.03501213Z     self._close_impl(invalidate=False)
2025-09-28T06:52:48.03501581Z     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
2025-09-28T06:52:48.035019451Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2590, in _close_impl
2025-09-28T06:52:48.035022581Z     transaction.close(invalidate)
2025-09-28T06:52:48.035025551Z     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:52:48.035028371Z   File "<string>", line 2, in close
2025-09-28T06:52:48.035031421Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/state_changes.py", line 119, in _go
2025-09-28T06:52:48.035034591Z     raise sa_exc.IllegalStateChangeError(
2025-09-28T06:52:48.035037561Z     ...<5 lines>...
2025-09-28T06:52:48.035040631Z     )
2025-09-28T06:52:48.035045631Z sqlalchemy.exc.IllegalStateChangeError: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T06:52:48.135719497Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T06:52:48.137733066Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T06:52:48.200250453Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:48.367730418Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:48.537188272Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:48.887124993Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:52:53.000118156Z WARNING:  Unsupported upgrade request.
2025-09-28T06:52:53.000142716Z WARNING:  No supported WebSocket library detected. Please use "pip install 'uvicorn[standard]'", or install 'websockets' or 'wsproto' manually.
2025-09-28T06:52:53.000782985Z INFO:     41.238.10.39:0 - "GET /ws/payments HTTP/1.1" 404 Not Found
2025-09-28T06:53:03.462364843Z WARNING:  Unsupported upgrade request.
2025-09-28T06:53:03.462393234Z WARNING:  No supported WebSocket library detected. Please use "pip install 'uvicorn[standard]'", or install 'websockets' or 'wsproto' manually.
2025-09-28T06:53:03.463055253Z INFO:     41.238.10.39:0 - "GET /ws/payments HTTP/1.1" 404 Not Found
2025-09-28T06:53:23.930827472Z WARNING:  Unsupported upgrade request.
2025-09-28T06:53:23.930863303Z WARNING:  No supported WebSocket library detected. Please use "pip install 'uvicorn[standard]'", or install 'websockets' or 'wsproto' manually.
2025-09-28T06:53:23.931439961Z INFO:     41.238.10.39:0 - "GET /ws/payments HTTP/1.1" 404 Not Found
2025-09-28T06:54:05.321117511Z WARNING:  Unsupported upgrade request.
2025-09-28T06:54:05.321138241Z WARNING:  No supported WebSocket library detected. Please use "pip install 'uvicorn[standard]'", or install 'websockets' or 'wsproto' manually.
2025-09-28T06:54:05.321785991Z INFO:     41.238.10.39:0 - "GET /ws/payments HTTP/1.1" 404 Not Found