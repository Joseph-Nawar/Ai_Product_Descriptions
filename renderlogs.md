2025-09-28T07:27:11.81499304Z Using cached google_api_python_client-2.183.0-py3-none-any.whl (14.2 MB)
2025-09-28T07:27:11.826322996Z Using cached google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
2025-09-28T07:27:11.827477741Z Using cached httplib2-0.31.0-py3-none-any.whl (91 kB)
2025-09-28T07:27:11.828641697Z Using cached pyparsing-3.2.5-py3-none-any.whl (113 kB)
2025-09-28T07:27:11.829843579Z Using cached uritemplate-4.2.0-py3-none-any.whl (11 kB)
2025-09-28T07:27:11.830927173Z Using cached mako-1.3.10-py3-none-any.whl (78 kB)
2025-09-28T07:27:11.832058255Z Using cached markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
2025-09-28T07:27:11.833333577Z Using cached pycparser-2.23-py3-none-any.whl (118 kB)
2025-09-28T07:27:12.144571022Z Installing collected packages: pytz, wrapt, websockets, uvloop, urllib3, uritemplate, tzdata, typing-extensions, tqdm, tenacity, structlog, sniffio, six, rapidfuzz, pyyaml, python-multipart, python-dotenv, pyparsing, pymysql, pyjwt, pygments, pycparser, pyasn1, psycopg2-binary, psycopg-binary, psycopg, protobuf, pluggy, packaging, numpy, msgpack, MarkupSafe, iniconfig, idna, hyperframe, httptools, hpack, h11, greenlet, google-crc32c, coverage, click, charset_normalizer, certifi, cachetools, annotated-types, uvicorn, typing-inspection, sqlalchemy, sentry-sdk, rsa, requests, python-dateutil, pytest, pydantic-core, pyasn1-modules, proto-plus, Mako, httplib2, httpcore, h2, grpcio, googleapis-common-protos, google-resumable-media, deprecated, cffi, anyio, watchfiles, starlette, pytest-cov, pytest-asyncio, pydantic, pandas, limits, httpx, grpcio-status, google-auth, cryptography, cachecontrol, alembic, slowapi, google-auth-httplib2, google-api-core, fastapi, google-cloud-core, google-api-python-client, google-cloud-storage, google-cloud-firestore, google-ai-generativelanguage, google-generativeai, firebase-admin
2025-09-28T07:27:42.313228298Z 
2025-09-28T07:27:42.323441366Z Successfully installed Mako-1.3.10 MarkupSafe-3.0.3 alembic-1.16.5 annotated-types-0.7.0 anyio-4.11.0 cachecontrol-0.14.3 cachetools-5.5.2 certifi-2025.8.3 cffi-2.0.0 charset_normalizer-3.4.3 click-8.3.0 coverage-7.10.7 cryptography-46.0.1 deprecated-1.2.18 fastapi-0.117.1 firebase-admin-7.1.0 google-ai-generativelanguage-0.6.15 google-api-core-2.25.1 google-api-python-client-2.183.0 google-auth-2.40.3 google-auth-httplib2-0.2.0 google-cloud-core-2.4.3 google-cloud-firestore-2.21.0 google-cloud-storage-3.4.0 google-crc32c-1.7.1 google-generativeai-0.8.5 google-resumable-media-2.7.2 googleapis-common-protos-1.70.0 greenlet-3.2.4 grpcio-1.75.1 grpcio-status-1.71.2 h11-0.16.0 h2-4.3.0 hpack-4.1.0 httpcore-1.0.9 httplib2-0.31.0 httptools-0.6.4 httpx-0.28.1 hyperframe-6.1.0 idna-3.10 iniconfig-2.1.0 limits-5.5.0 msgpack-1.1.1 numpy-2.3.3 packaging-25.0 pandas-2.3.2 pluggy-1.6.0 proto-plus-1.26.1 protobuf-5.29.5 psycopg-3.2.10 psycopg-binary-3.2.10 psycopg2-binary-2.9.10 pyasn1-0.6.1 pyasn1-modules-0.4.2 pycparser-2.23 pydantic-2.11.9 pydantic-core-2.33.2 pygments-2.19.2 pyjwt-2.10.1 pymysql-1.1.2 pyparsing-3.2.5 pytest-8.4.2 pytest-asyncio-1.2.0 pytest-cov-7.0.0 python-dateutil-2.9.0.post0 python-dotenv-1.1.1 python-multipart-0.0.20 pytz-2025.2 pyyaml-6.0.3 rapidfuzz-3.14.1 requests-2.32.5 rsa-4.9.1 sentry-sdk-2.39.0 six-1.17.0 slowapi-0.1.9 sniffio-1.3.1 sqlalchemy-2.0.43 starlette-0.48.0 structlog-25.4.0 tenacity-9.1.2 tqdm-4.67.1 typing-extensions-4.15.0 typing-inspection-0.4.1 tzdata-2025.2 uritemplate-4.2.0 urllib3-2.5.0 uvicorn-0.37.0 uvloop-0.21.0 watchfiles-1.1.0 websockets-15.0.1 wrapt-1.17.3
2025-09-28T07:27:42.331674643Z 
2025-09-28T07:27:42.331687305Z [notice] A new release of pip is available: 25.1.1 -> 25.2
2025-09-28T07:27:42.331690675Z [notice] To update, run: pip install --upgrade pip
2025-09-28T07:27:50.347398523Z ==> Uploading build...
2025-09-28T07:28:10.139541069Z ==> Uploaded in 15.5s. Compression took 4.3s
2025-09-28T07:28:10.222844701Z ==> Build successful 🎉
2025-09-28T07:28:12.917216721Z ==> Deploying...
2025-09-28T07:28:54.75929923Z ==> Running '   cd backend && python init_db.py && uvicorn src.main:app --host 0.0.0.0 --port $PORT'
2025-09-28T07:29:02.401572928Z 🔄 Initializing database...
2025-09-28T07:29:02.401593558Z ✅ Database initialized successfully!
2025-09-28T07:29:18.901559216Z ==> No open ports detected, continuing to scan...
2025-09-28T07:29:19.121521293Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-28T07:29:33.526419712Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-28T07:29:33.526450913Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-28T07:29:33.526458213Z   warnings.warn(message, UserWarning)
2025-09-28T07:29:33.715233901Z INFO:     Started server process [57]
2025-09-28T07:29:33.715264212Z INFO:     Waiting for application startup.
2025-09-28T07:29:34.429571216Z INFO:     Application startup complete.
2025-09-28T07:29:34.43021057Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-28T07:29:35.216145745Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-28T07:29:35.216162975Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-28T07:29:35.216166715Z ✅ Gemini API key loaded successfully
2025-09-28T07:29:35.216169655Z 📊 Using model: gemini-1.5-pro, temperature: 0.8
2025-09-28T07:29:35.216172525Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-28T07:29:35.216175355Z ✅ AI Product Descriptions API started successfully
2025-09-28T07:29:35.216178266Z 🤖 Model: gemini-1.5-pro (Live mode)
2025-09-28T07:29:35.216181895Z 🌡️  Temperature: 0.8
2025-09-28T07:29:35.216185536Z ✅ API key configured - ready for AI generation
2025-09-28T07:29:35.216190056Z 💳 Credit service initialized - rate limiting enabled
2025-09-28T07:29:35.216194626Z 📋 Subscription plans initialized
2025-09-28T07:29:35.216198976Z INFO:     127.0.0.1:41260 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-28T07:29:43.665408631Z ==> Your service is live 🎉
2025-09-28T07:29:43.813816591Z ==> 
2025-09-28T07:29:43.88997044Z ==> ///////////////////////////////////////////////////////////
2025-09-28T07:29:43.96567944Z ==> 
2025-09-28T07:29:44.040689219Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-28T07:29:44.115983379Z ==> 
2025-09-28T07:29:44.192613639Z ==> ///////////////////////////////////////////////////////////
2025-09-28T07:29:45.626638766Z INFO:     34.82.80.145:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-28T07:33:55.546745576Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:33:55.547085374Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T07:33:55.547465692Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:33:55.548073826Z WARNING:root:Invalid auth header format
2025-09-28T07:33:55.548442925Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 401 Unauthorized
2025-09-28T07:33:55.712252602Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T07:33:56.077556647Z INFO:     41.238.10.39:0 - "WebSocket /ws/payments" [accepted]
2025-09-28T07:33:56.090990664Z INFO:     connection open
2025-09-28T07:33:56.144171441Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T07:33:56.419716094Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 500 Internal Server Error
2025-09-28T07:33:56.679586368Z ERROR:    Exception in ASGI application
2025-09-28T07:33:56.679603578Z   + Exception Group Traceback (most recent call last):
2025-09-28T07:33:56.679608988Z   |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 79, in collapse_excgroups
2025-09-28T07:33:56.679613488Z   |     yield
2025-09-28T07:33:56.679617958Z   |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 183, in __call__
2025-09-28T07:33:56.679712681Z   |     async with anyio.create_task_group() as task_group:
2025-09-28T07:33:56.679720301Z   |                ~~~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:33:56.679724961Z   |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 781, in __aexit__
2025-09-28T07:33:56.679739071Z   |     raise BaseExceptionGroup(
2025-09-28T07:33:56.679742201Z   |         "unhandled errors in a TaskGroup", self._exceptions
2025-09-28T07:33:56.679745391Z   |     ) from None
2025-09-28T07:33:56.679748351Z   | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
2025-09-28T07:33:56.679751631Z   +-+---------------- 1 ----------------
2025-09-28T07:33:56.679754311Z     | Traceback (most recent call last):
2025-09-28T07:33:56.679757431Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
2025-09-28T07:33:56.679760292Z     |     result = await app(  # type: ignore[func-returns-value]
2025-09-28T07:33:56.679763212Z     |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.679765952Z     |         self.scope, self.receive, self.send
2025-09-28T07:33:56.679768632Z     |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.679771812Z     |     )
2025-09-28T07:33:56.679774952Z     |     ^
2025-09-28T07:33:56.679777862Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T07:33:56.679780792Z     |     return await self.app(scope, receive, send)
2025-09-28T07:33:56.679783482Z     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.679786352Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T07:33:56.679789262Z     |     await super().__call__(scope, receive, send)
2025-09-28T07:33:56.679792172Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T07:33:56.679794803Z     |     await self.middleware_stack(scope, receive, send)
2025-09-28T07:33:56.679797663Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T07:33:56.679800563Z     |     raise exc
2025-09-28T07:33:56.679803333Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T07:33:56.679806063Z     |     await self.app(scope, receive, _send)
2025-09-28T07:33:56.679808913Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T07:33:56.679811653Z     |     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T07:33:56.679814343Z     |                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:33:56.679817393Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T07:33:56.679820763Z     |     self.gen.throw(value)
2025-09-28T07:33:56.679823423Z     |     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T07:33:56.679826053Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T07:33:56.679828673Z     |     raise exc
2025-09-28T07:33:56.679831403Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T07:33:56.679834263Z     |     response = await self.dispatch_func(request, call_next)
2025-09-28T07:33:56.679836963Z     |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.679840313Z     |   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T07:33:56.679843344Z     |     response = await call_next(request)
2025-09-28T07:33:56.679850914Z     |                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.679853844Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T07:33:56.679857004Z     |     raise app_exc
2025-09-28T07:33:56.679859544Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T07:33:56.679862234Z     |     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T07:33:56.679865114Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T07:33:56.679868054Z     |     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T07:33:56.679871004Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T07:33:56.679873654Z     |     await self.app(scope, receive, send)
2025-09-28T07:33:56.679876454Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T07:33:56.679882834Z     |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T07:33:56.679885874Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T07:33:56.679888594Z     |     raise exc
2025-09-28T07:33:56.679891625Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T07:33:56.679894545Z     |     await app(scope, receive, sender)
2025-09-28T07:33:56.679897385Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T07:33:56.679900645Z     |     await self.middleware_stack(scope, receive, send)
2025-09-28T07:33:56.679903575Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T07:33:56.679906385Z     |     await route.handle(scope, receive, send)
2025-09-28T07:33:56.679909245Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T07:33:56.679912125Z     |     await self.app(scope, receive, send)
2025-09-28T07:33:56.679915075Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T07:33:56.679917835Z     |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T07:33:56.679920415Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T07:33:56.679923255Z     |     raise exc
2025-09-28T07:33:56.679926206Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T07:33:56.679929146Z     |     await app(scope, receive, sender)
2025-09-28T07:33:56.679931795Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T07:33:56.679934656Z     |     response = await f(request)
2025-09-28T07:33:56.679937376Z     |                ^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.679939906Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 297, in app
2025-09-28T07:33:56.679942606Z     |     async with AsyncExitStack() as async_exit_stack:
2025-09-28T07:33:56.679945576Z     |                ~~~~~~~~~~~~~~^^
2025-09-28T07:33:56.679953546Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 768, in __aexit__
2025-09-28T07:33:56.679956496Z     |     raise exc
2025-09-28T07:33:56.679959556Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 751, in __aexit__
2025-09-28T07:33:56.679962216Z     |     cb_suppress = await cb(*exc_details)
2025-09-28T07:33:56.679964936Z     |                   ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.679967646Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 221, in __aexit__
2025-09-28T07:33:56.679970676Z     |     await anext(self.gen)
2025-09-28T07:33:56.679973496Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/concurrency.py", line 37, in contextmanager_in_threadpool
2025-09-28T07:33:56.679976376Z     |     await anyio.to_thread.run_sync(
2025-09-28T07:33:56.679979117Z     |         cm.__exit__, None, None, None, limiter=exit_limiter
2025-09-28T07:33:56.679982127Z     |     )
2025-09-28T07:33:56.679984877Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/to_thread.py", line 56, in run_sync
2025-09-28T07:33:56.679987907Z     |     return await get_async_backend().run_sync_in_worker_thread(
2025-09-28T07:33:56.679990737Z     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.679993827Z     |         func, args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
2025-09-28T07:33:56.679996577Z     |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.679999327Z     |     )
2025-09-28T07:33:56.680002137Z     |     ^
2025-09-28T07:33:56.680005107Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 2485, in run_sync_in_worker_thread
2025-09-28T07:33:56.680007847Z     |     return await future
2025-09-28T07:33:56.680010577Z     |            ^^^^^^^^^^^^
2025-09-28T07:33:56.680013497Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 976, in run
2025-09-28T07:33:56.680016568Z     |     result = context.run(func, *args)
2025-09-28T07:33:56.680019228Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 148, in __exit__
2025-09-28T07:33:56.680022018Z     |     next(self.gen)
2025-09-28T07:33:56.680024878Z     |     ~~~~^^^^^^^^^^
2025-09-28T07:33:56.680027728Z     |   File "/opt/render/project/src/backend/src/database/deps.py", line 82, in get_db
2025-09-28T07:33:56.680030318Z     |     session_factory.remove()
2025-09-28T07:33:56.680033108Z     |     ~~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:33:56.680035908Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/scoping.py", line 261, in remove
2025-09-28T07:33:56.680038978Z     |     self.registry().close()
2025-09-28T07:33:56.680041628Z     |     ~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:33:56.680044618Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2521, in close
2025-09-28T07:33:56.680047388Z     |     self._close_impl(invalidate=False)
2025-09-28T07:33:56.680050138Z     |     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.680055028Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2590, in _close_impl
2025-09-28T07:33:56.680057789Z     |     transaction.close(invalidate)
2025-09-28T07:33:56.680060549Z     |     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T07:33:56.680063249Z     |   File "<string>", line 2, in close
2025-09-28T07:33:56.680070849Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/state_changes.py", line 119, in _go
2025-09-28T07:33:56.680074039Z     |     raise sa_exc.IllegalStateChangeError(
2025-09-28T07:33:56.680076769Z     |     ...<5 lines>...
2025-09-28T07:33:56.680079419Z     |     )
2025-09-28T07:33:56.680082749Z     | sqlalchemy.exc.IllegalStateChangeError: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T07:33:56.680085579Z     +------------------------------------
2025-09-28T07:33:56.680088069Z 
2025-09-28T07:33:56.680091319Z During handling of the above exception, another exception occurred:
2025-09-28T07:33:56.680094089Z 
2025-09-28T07:33:56.680097279Z Traceback (most recent call last):
2025-09-28T07:33:56.680100179Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
2025-09-28T07:33:56.68010297Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T07:33:56.680105979Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.68010894Z         self.scope, self.receive, self.send
2025-09-28T07:33:56.68011157Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.68011416Z     )
2025-09-28T07:33:56.6801171Z     ^
2025-09-28T07:33:56.68012007Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T07:33:56.68012284Z     return await self.app(scope, receive, send)
2025-09-28T07:33:56.68012549Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.6801286Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T07:33:56.68013141Z     await super().__call__(scope, receive, send)
2025-09-28T07:33:56.68013428Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T07:33:56.68013695Z     await self.middleware_stack(scope, receive, send)
2025-09-28T07:33:56.68013986Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T07:33:56.68014256Z     raise exc
2025-09-28T07:33:56.6801453Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T07:33:56.680148051Z     await self.app(scope, receive, _send)
2025-09-28T07:33:56.680150931Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T07:33:56.680153731Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T07:33:56.680156541Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:33:56.680159111Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T07:33:56.680162131Z     self.gen.throw(value)
2025-09-28T07:33:56.680164761Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T07:33:56.680167631Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T07:33:56.680170201Z     raise exc
2025-09-28T07:33:56.680173161Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T07:33:56.680176011Z     response = await self.dispatch_func(request, call_next)
2025-09-28T07:33:56.680178751Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.680185971Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T07:33:56.680188781Z     response = await call_next(request)
2025-09-28T07:33:56.680191721Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.680194561Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T07:33:56.680197492Z     raise app_exc
2025-09-28T07:33:56.680200682Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T07:33:56.680203512Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T07:33:56.680206452Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T07:33:56.680209242Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T07:33:56.680211862Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T07:33:56.680214522Z     await self.app(scope, receive, send)
2025-09-28T07:33:56.680217132Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T07:33:56.680220062Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T07:33:56.680222872Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T07:33:56.680225712Z     raise exc
2025-09-28T07:33:56.680230593Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T07:33:56.680233522Z     await app(scope, receive, sender)
2025-09-28T07:33:56.680236313Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T07:33:56.680239023Z     await self.middleware_stack(scope, receive, send)
2025-09-28T07:33:56.680241923Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T07:33:56.680244803Z     await route.handle(scope, receive, send)
2025-09-28T07:33:56.680247523Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T07:33:56.680250093Z     await self.app(scope, receive, send)
2025-09-28T07:33:56.680252983Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T07:33:56.680255903Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T07:33:56.680258773Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T07:33:56.680261383Z     raise exc
2025-09-28T07:33:56.680264523Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T07:33:56.680267353Z     await app(scope, receive, sender)
2025-09-28T07:33:56.680270193Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T07:33:56.680272993Z     response = await f(request)
2025-09-28T07:33:56.680275934Z                ^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.680278763Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 297, in app
2025-09-28T07:33:56.680281714Z     async with AsyncExitStack() as async_exit_stack:
2025-09-28T07:33:56.680284304Z                ~~~~~~~~~~~~~~^^
2025-09-28T07:33:56.680291534Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 768, in __aexit__
2025-09-28T07:33:56.680294294Z     raise exc
2025-09-28T07:33:56.680297144Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 751, in __aexit__
2025-09-28T07:33:56.680300034Z     cb_suppress = await cb(*exc_details)
2025-09-28T07:33:56.680302944Z                   ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.680305784Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 221, in __aexit__
2025-09-28T07:33:56.680308464Z     await anext(self.gen)
2025-09-28T07:33:56.680311314Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/concurrency.py", line 37, in contextmanager_in_threadpool
2025-09-28T07:33:56.680314504Z     await anyio.to_thread.run_sync(
2025-09-28T07:33:56.680317484Z         cm.__exit__, None, None, None, limiter=exit_limiter
2025-09-28T07:33:56.680320195Z     )
2025-09-28T07:33:56.680323015Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/to_thread.py", line 56, in run_sync
2025-09-28T07:33:56.680325975Z     return await get_async_backend().run_sync_in_worker_thread(
2025-09-28T07:33:56.680328735Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.680331515Z         func, args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
2025-09-28T07:33:56.680334675Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.680337405Z     )
2025-09-28T07:33:56.680340055Z     ^
2025-09-28T07:33:56.680342855Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 2485, in run_sync_in_worker_thread
2025-09-28T07:33:56.680345885Z     return await future
2025-09-28T07:33:56.680348725Z            ^^^^^^^^^^^^
2025-09-28T07:33:56.680351805Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 976, in run
2025-09-28T07:33:56.680354585Z     result = context.run(func, *args)
2025-09-28T07:33:56.680357565Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 148, in __exit__
2025-09-28T07:33:56.680360335Z     next(self.gen)
2025-09-28T07:33:56.680363125Z     ~~~~^^^^^^^^^^
2025-09-28T07:33:56.680365945Z   File "/opt/render/project/src/backend/src/database/deps.py", line 82, in get_db
2025-09-28T07:33:56.680368945Z     session_factory.remove()
2025-09-28T07:33:56.680371846Z     ~~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:33:56.680374786Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/scoping.py", line 261, in remove
2025-09-28T07:33:56.680377586Z     self.registry().close()
2025-09-28T07:33:56.680380406Z     ~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:33:56.680383336Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2521, in close
2025-09-28T07:33:56.680386086Z     self._close_impl(invalidate=False)
2025-09-28T07:33:56.680388916Z     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
2025-09-28T07:33:56.680391876Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2590, in _close_impl
2025-09-28T07:33:56.680394606Z     transaction.close(invalidate)
2025-09-28T07:33:56.680397636Z     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T07:33:56.680400386Z   File "<string>", line 2, in close
2025-09-28T07:33:56.680403426Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/state_changes.py", line 119, in _go
2025-09-28T07:33:56.680406086Z     raise sa_exc.IllegalStateChangeError(
2025-09-28T07:33:56.680408766Z     ...<5 lines>...
2025-09-28T07:33:56.680416237Z     )
2025-09-28T07:33:56.680424607Z sqlalchemy.exc.IllegalStateChangeError: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T07:33:56.680469258Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:33:56.904989813Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T07:33:56.905380232Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:33:56.908481713Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T07:33:57.12039219Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:33:57.309791412Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:34:42.861562717Z ==> Detected service running on port 10000
2025-09-28T07:34:43.05570503Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding