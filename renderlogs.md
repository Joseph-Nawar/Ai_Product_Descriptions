2025-09-28T06:59:18.285778233Z Using cached google_api_python_client-2.183.0-py3-none-any.whl (14.2 MB)
2025-09-28T06:59:18.300951933Z Using cached google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
2025-09-28T06:59:18.302155782Z Using cached httplib2-0.31.0-py3-none-any.whl (91 kB)
2025-09-28T06:59:18.303595266Z Using cached pyparsing-3.2.5-py3-none-any.whl (113 kB)
2025-09-28T06:59:18.30502601Z Using cached uritemplate-4.2.0-py3-none-any.whl (11 kB)
2025-09-28T06:59:18.306167597Z Using cached mako-1.3.10-py3-none-any.whl (78 kB)
2025-09-28T06:59:18.307419987Z Using cached markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
2025-09-28T06:59:18.308584114Z Using cached pycparser-2.23-py3-none-any.whl (118 kB)
2025-09-28T06:59:18.705470243Z Installing collected packages: pytz, wrapt, websockets, uvloop, urllib3, uritemplate, tzdata, typing-extensions, tqdm, tenacity, structlog, sniffio, six, rapidfuzz, pyyaml, python-multipart, python-dotenv, pyparsing, pymysql, pyjwt, pygments, pycparser, pyasn1, psycopg2-binary, psycopg-binary, psycopg, protobuf, pluggy, packaging, numpy, msgpack, MarkupSafe, iniconfig, idna, hyperframe, httptools, hpack, h11, greenlet, google-crc32c, coverage, click, charset_normalizer, certifi, cachetools, annotated-types, uvicorn, typing-inspection, sqlalchemy, sentry-sdk, rsa, requests, python-dateutil, pytest, pydantic-core, pyasn1-modules, proto-plus, Mako, httplib2, httpcore, h2, grpcio, googleapis-common-protos, google-resumable-media, deprecated, cffi, anyio, watchfiles, starlette, pytest-cov, pytest-asyncio, pydantic, pandas, limits, httpx, grpcio-status, google-auth, cryptography, cachecontrol, alembic, slowapi, google-auth-httplib2, google-api-core, fastapi, google-cloud-core, google-api-python-client, google-cloud-storage, google-cloud-firestore, google-ai-generativelanguage, google-generativeai, firebase-admin
2025-09-28T06:59:55.240919282Z 
2025-09-28T06:59:55.253500901Z Successfully installed Mako-1.3.10 MarkupSafe-3.0.3 alembic-1.16.5 annotated-types-0.7.0 anyio-4.11.0 cachecontrol-0.14.3 cachetools-5.5.2 certifi-2025.8.3 cffi-2.0.0 charset_normalizer-3.4.3 click-8.3.0 coverage-7.10.7 cryptography-46.0.1 deprecated-1.2.18 fastapi-0.117.1 firebase-admin-7.1.0 google-ai-generativelanguage-0.6.15 google-api-core-2.25.1 google-api-python-client-2.183.0 google-auth-2.40.3 google-auth-httplib2-0.2.0 google-cloud-core-2.4.3 google-cloud-firestore-2.21.0 google-cloud-storage-3.4.0 google-crc32c-1.7.1 google-generativeai-0.8.5 google-resumable-media-2.7.2 googleapis-common-protos-1.70.0 greenlet-3.2.4 grpcio-1.75.1 grpcio-status-1.71.2 h11-0.16.0 h2-4.3.0 hpack-4.1.0 httpcore-1.0.9 httplib2-0.31.0 httptools-0.6.4 httpx-0.28.1 hyperframe-6.1.0 idna-3.10 iniconfig-2.1.0 limits-5.5.0 msgpack-1.1.1 numpy-2.3.3 packaging-25.0 pandas-2.3.2 pluggy-1.6.0 proto-plus-1.26.1 protobuf-5.29.5 psycopg-3.2.10 psycopg-binary-3.2.10 psycopg2-binary-2.9.10 pyasn1-0.6.1 pyasn1-modules-0.4.2 pycparser-2.23 pydantic-2.11.9 pydantic-core-2.33.2 pygments-2.19.2 pyjwt-2.10.1 pymysql-1.1.2 pyparsing-3.2.5 pytest-8.4.2 pytest-asyncio-1.2.0 pytest-cov-7.0.0 python-dateutil-2.9.0.post0 python-dotenv-1.1.1 python-multipart-0.0.20 pytz-2025.2 pyyaml-6.0.3 rapidfuzz-3.14.1 requests-2.32.5 rsa-4.9.1 sentry-sdk-2.39.0 six-1.17.0 slowapi-0.1.9 sniffio-1.3.1 sqlalchemy-2.0.43 starlette-0.48.0 structlog-25.4.0 tenacity-9.1.2 tqdm-4.67.1 typing-extensions-4.15.0 typing-inspection-0.4.1 tzdata-2025.2 uritemplate-4.2.0 urllib3-2.5.0 uvicorn-0.37.0 uvloop-0.21.0 watchfiles-1.1.0 websockets-15.0.1 wrapt-1.17.3
2025-09-28T06:59:55.262355271Z 
2025-09-28T06:59:55.262372602Z [notice] A new release of pip is available: 25.1.1 -> 25.2
2025-09-28T06:59:55.262376762Z [notice] To update, run: pip install --upgrade pip
2025-09-28T07:00:22.822141872Z ==> Uploading build...
2025-09-28T07:00:43.398134747Z ==> Uploaded in 15.2s. Compression took 5.4s
2025-09-28T07:00:43.500245903Z ==> Build successful 🎉
2025-09-28T07:00:45.761699472Z ==> Deploying...
2025-09-28T07:01:25.238472952Z ==> Running '   cd backend && python init_db.py && uvicorn src.main:app --host 0.0.0.0 --port $PORT'
2025-09-28T07:01:34.593247143Z 🔄 Initializing database...
2025-09-28T07:01:34.593270944Z ✅ Database initialized successfully!
2025-09-28T07:01:47.864473708Z ==> No open ports detected, continuing to scan...
2025-09-28T07:01:48.179276924Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-28T07:01:53.748365147Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-28T07:01:53.748392968Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-28T07:01:53.748399008Z   warnings.warn(message, UserWarning)
2025-09-28T07:01:53.934747062Z INFO:     Started server process [56]
2025-09-28T07:01:53.934779273Z INFO:     Waiting for application startup.
2025-09-28T07:01:54.547255341Z INFO:     Application startup complete.
2025-09-28T07:01:54.548020381Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-28T07:01:54.839617828Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-28T07:01:54.839649069Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-28T07:01:54.839656309Z ✅ Gemini API key loaded successfully
2025-09-28T07:01:54.839661489Z 📊 Using model: gemini-1.5-pro, temperature: 0.8
2025-09-28T07:01:54.839666539Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-28T07:01:54.839671509Z ✅ AI Product Descriptions API started successfully
2025-09-28T07:01:54.83967626Z 🤖 Model: gemini-1.5-pro (Live mode)
2025-09-28T07:01:54.8396817Z 🌡️  Temperature: 0.8
2025-09-28T07:01:54.8397077Z ✅ API key configured - ready for AI generation
2025-09-28T07:01:54.839716221Z 💳 Credit service initialized - rate limiting enabled
2025-09-28T07:01:54.839721561Z 📋 Subscription plans initialized
2025-09-28T07:01:54.839727221Z INFO:     127.0.0.1:36554 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-28T07:01:56.466076888Z ==> Your service is live 🎉
2025-09-28T07:01:56.566311447Z ==> 
2025-09-28T07:01:56.641961147Z ==> ///////////////////////////////////////////////////////////
2025-09-28T07:01:56.717226296Z ==> 
2025-09-28T07:01:56.828939286Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-28T07:01:56.904050205Z ==> 
2025-09-28T07:01:56.982952905Z ==> ///////////////////////////////////////////////////////////
2025-09-28T07:01:58.553514981Z INFO:     35.247.111.159:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-28T07:02:30.43531444Z WARNING:root:Invalid auth header format
2025-09-28T07:02:30.435671549Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 401 Unauthorized
2025-09-28T07:02:31.269151243Z INFO:     41.238.10.39:0 - "WebSocket /ws/payments" [accepted]
2025-09-28T07:02:31.269780219Z INFO:     connection open
2025-09-28T07:02:31.271636466Z ERROR:src.auth.deps:❌ Error in get_authed_user_db: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T07:02:31.274027417Z ERROR:src.auth.deps:❌ Full traceback: Traceback (most recent call last):
2025-09-28T07:02:31.274043537Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 27, in get_authed_user_db
2025-09-28T07:02:31.274048858Z     db.execute(text("SELECT 1"))
2025-09-28T07:02:31.274053148Z     ~~~~~~~~~~^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.274059808Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T07:02:31.274066178Z     return self._execute_internal(
2025-09-28T07:02:31.274071388Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T07:02:31.274089039Z         statement,
2025-09-28T07:02:31.274094009Z         ^^^^^^^^^^
2025-09-28T07:02:31.274099289Z     ...<4 lines>...
2025-09-28T07:02:31.274104439Z         _add_event=_add_event,
2025-09-28T07:02:31.274110039Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.274115229Z     )
2025-09-28T07:02:31.274120359Z     ^
2025-09-28T07:02:31.27412577Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2241, in _execute_internal
2025-09-28T07:02:31.27413099Z     conn = self._connection_for_bind(bind)
2025-09-28T07:02:31.27413727Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2110, in _connection_for_bind
2025-09-28T07:02:31.2741578Z     return trans._connection_for_bind(engine, execution_options)
2025-09-28T07:02:31.274160071Z            ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.274162191Z   File "<string>", line 2, in _connection_for_bind
2025-09-28T07:02:31.274164341Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/state_changes.py", line 101, in _go
2025-09-28T07:02:31.274166471Z     self._raise_for_prerequisite_state(fn.__name__, current_state)
2025-09-28T07:02:31.274168601Z     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.274171441Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 996, in _raise_for_prerequisite_state
2025-09-28T07:02:31.274173571Z     raise sa_exc.InvalidRequestError(
2025-09-28T07:02:31.274175701Z     ...<2 lines>...
2025-09-28T07:02:31.274177771Z     )
2025-09-28T07:02:31.274181601Z sqlalchemy.exc.InvalidRequestError: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T07:02:31.274184981Z 
2025-09-28T07:02:31.274238522Z ERROR:src.database.deps:Database session error, rolling back: This session is in 'prepared' state; no further SQL can be emitted within this transaction.
2025-09-28T07:02:31.274777646Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 500 Internal Server Error
2025-09-28T07:02:31.3465709Z ERROR:    Exception in ASGI application
2025-09-28T07:02:31.346595261Z   + Exception Group Traceback (most recent call last):
2025-09-28T07:02:31.346599881Z   |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 79, in collapse_excgroups
2025-09-28T07:02:31.346602971Z   |     yield
2025-09-28T07:02:31.346605791Z   |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 183, in __call__
2025-09-28T07:02:31.346608401Z   |     async with anyio.create_task_group() as task_group:
2025-09-28T07:02:31.346611291Z   |                ~~~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:02:31.346613871Z   |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 781, in __aexit__
2025-09-28T07:02:31.346616441Z   |     raise BaseExceptionGroup(
2025-09-28T07:02:31.346619061Z   |         "unhandled errors in a TaskGroup", self._exceptions
2025-09-28T07:02:31.346622281Z   |     ) from None
2025-09-28T07:02:31.346625601Z   | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
2025-09-28T07:02:31.346628201Z   +-+---------------- 1 ----------------
2025-09-28T07:02:31.346630692Z     | Traceback (most recent call last):
2025-09-28T07:02:31.346634101Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
2025-09-28T07:02:31.346637012Z     |     result = await app(  # type: ignore[func-returns-value]
2025-09-28T07:02:31.346639842Z     |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.346642682Z     |         self.scope, self.receive, self.send
2025-09-28T07:02:31.346645152Z     |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.346647662Z     |     )
2025-09-28T07:02:31.346650262Z     |     ^
2025-09-28T07:02:31.346652872Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T07:02:31.346655702Z     |     return await self.app(scope, receive, send)
2025-09-28T07:02:31.346658302Z     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.346675223Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T07:02:31.346678123Z     |     await super().__call__(scope, receive, send)
2025-09-28T07:02:31.346680783Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T07:02:31.346683383Z     |     await self.middleware_stack(scope, receive, send)
2025-09-28T07:02:31.346685943Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T07:02:31.346714094Z     |     raise exc
2025-09-28T07:02:31.346717044Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T07:02:31.346719934Z     |     await self.app(scope, receive, _send)
2025-09-28T07:02:31.346722734Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T07:02:31.346725644Z     |     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T07:02:31.346728124Z     |                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:02:31.346731634Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T07:02:31.346734644Z     |     self.gen.throw(value)
2025-09-28T07:02:31.346737094Z     |     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T07:02:31.346739864Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T07:02:31.346742674Z     |     raise exc
2025-09-28T07:02:31.346745224Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T07:02:31.346747835Z     |     response = await self.dispatch_func(request, call_next)
2025-09-28T07:02:31.346750315Z     |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.346753345Z     |   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T07:02:31.346756005Z     |     response = await call_next(request)
2025-09-28T07:02:31.346758545Z     |                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.346761285Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T07:02:31.346763815Z     |     raise app_exc
2025-09-28T07:02:31.346766385Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T07:02:31.346769035Z     |     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T07:02:31.346774435Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T07:02:31.346777115Z     |     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T07:02:31.346779795Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T07:02:31.346782285Z     |     await self.app(scope, receive, send)
2025-09-28T07:02:31.346784845Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T07:02:31.346799846Z     |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T07:02:31.346802836Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T07:02:31.346812196Z     |     raise exc
2025-09-28T07:02:31.346815026Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T07:02:31.346817746Z     |     await app(scope, receive, sender)
2025-09-28T07:02:31.346820506Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T07:02:31.346823336Z     |     await self.middleware_stack(scope, receive, send)
2025-09-28T07:02:31.346826137Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T07:02:31.346828817Z     |     await route.handle(scope, receive, send)
2025-09-28T07:02:31.346831487Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T07:02:31.346834137Z     |     await self.app(scope, receive, send)
2025-09-28T07:02:31.346836647Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T07:02:31.346839227Z     |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T07:02:31.346842027Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T07:02:31.346844657Z     |     raise exc
2025-09-28T07:02:31.346847387Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T07:02:31.346849897Z     |     await app(scope, receive, sender)
2025-09-28T07:02:31.346852477Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T07:02:31.346855187Z     |     response = await f(request)
2025-09-28T07:02:31.346858007Z     |                ^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.346860547Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 297, in app
2025-09-28T07:02:31.346863217Z     |     async with AsyncExitStack() as async_exit_stack:
2025-09-28T07:02:31.346866178Z     |                ~~~~~~~~~~~~~~^^
2025-09-28T07:02:31.346868827Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 768, in __aexit__
2025-09-28T07:02:31.346871468Z     |     raise exc
2025-09-28T07:02:31.346874218Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 751, in __aexit__
2025-09-28T07:02:31.346876758Z     |     cb_suppress = await cb(*exc_details)
2025-09-28T07:02:31.346879548Z     |                   ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.346882138Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 235, in __aexit__
2025-09-28T07:02:31.346884638Z     |     await self.gen.athrow(value)
2025-09-28T07:02:31.346887408Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/concurrency.py", line 30, in contextmanager_in_threadpool
2025-09-28T07:02:31.346890158Z     |     await anyio.to_thread.run_sync(
2025-09-28T07:02:31.346892808Z     |         cm.__exit__, type(e), e, e.__traceback__, limiter=exit_limiter
2025-09-28T07:02:31.346895498Z     |     )
2025-09-28T07:02:31.346897978Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/to_thread.py", line 56, in run_sync
2025-09-28T07:02:31.346900428Z     |     return await get_async_backend().run_sync_in_worker_thread(
2025-09-28T07:02:31.346902948Z     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.346910519Z     |         func, args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
2025-09-28T07:02:31.346913499Z     |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.346916089Z     |     )
2025-09-28T07:02:31.346918819Z     |     ^
2025-09-28T07:02:31.346921789Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 2485, in run_sync_in_worker_thread
2025-09-28T07:02:31.346924509Z     |     return await future
2025-09-28T07:02:31.346926979Z     |            ^^^^^^^^^^^^
2025-09-28T07:02:31.346929509Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 976, in run
2025-09-28T07:02:31.346932169Z     |     result = context.run(func, *args)
2025-09-28T07:02:31.346934739Z     |   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T07:02:31.346937399Z     |     self.gen.throw(value)
2025-09-28T07:02:31.346942249Z     |     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T07:02:31.346945069Z     |   File "/opt/render/project/src/backend/src/database/deps.py", line 82, in get_db
2025-09-28T07:02:31.346947649Z     |     session_factory.remove()
2025-09-28T07:02:31.34695025Z     |     ~~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:02:31.34695312Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/scoping.py", line 261, in remove
2025-09-28T07:02:31.34695579Z     |     self.registry().close()
2025-09-28T07:02:31.34695849Z     |     ~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:02:31.3469612Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2521, in close
2025-09-28T07:02:31.34696386Z     |     self._close_impl(invalidate=False)
2025-09-28T07:02:31.34697513Z     |     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.34697795Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2590, in _close_impl
2025-09-28T07:02:31.34698029Z     |     transaction.close(invalidate)
2025-09-28T07:02:31.34698255Z     |     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T07:02:31.34698471Z     |   File "<string>", line 2, in close
2025-09-28T07:02:31.34698697Z     |   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/state_changes.py", line 119, in _go
2025-09-28T07:02:31.346989191Z     |     raise sa_exc.IllegalStateChangeError(
2025-09-28T07:02:31.346991411Z     |     ...<5 lines>...
2025-09-28T07:02:31.346993611Z     |     )
2025-09-28T07:02:31.346998081Z     | sqlalchemy.exc.IllegalStateChangeError: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T07:02:31.347000721Z     +------------------------------------
2025-09-28T07:02:31.347002971Z 
2025-09-28T07:02:31.347005521Z During handling of the above exception, another exception occurred:
2025-09-28T07:02:31.347007791Z 
2025-09-28T07:02:31.347010271Z Traceback (most recent call last):
2025-09-28T07:02:31.347012921Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
2025-09-28T07:02:31.347015371Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T07:02:31.347017891Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347020361Z         self.scope, self.receive, self.send
2025-09-28T07:02:31.347022682Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347030042Z     )
2025-09-28T07:02:31.347032612Z     ^
2025-09-28T07:02:31.347035152Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T07:02:31.347037482Z     return await self.app(scope, receive, send)
2025-09-28T07:02:31.347039832Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347042392Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T07:02:31.347044762Z     await super().__call__(scope, receive, send)
2025-09-28T07:02:31.347047212Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T07:02:31.347049652Z     await self.middleware_stack(scope, receive, send)
2025-09-28T07:02:31.347051972Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T07:02:31.347054372Z     raise exc
2025-09-28T07:02:31.347056712Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T07:02:31.347059102Z     await self.app(scope, receive, _send)
2025-09-28T07:02:31.347061463Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T07:02:31.347063812Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T07:02:31.347066163Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:02:31.347068783Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T07:02:31.347071183Z     self.gen.throw(value)
2025-09-28T07:02:31.347073443Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T07:02:31.347075973Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T07:02:31.347078293Z     raise exc
2025-09-28T07:02:31.347080553Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T07:02:31.347082983Z     response = await self.dispatch_func(request, call_next)
2025-09-28T07:02:31.347085373Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347088213Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T07:02:31.347090593Z     response = await call_next(request)
2025-09-28T07:02:31.347093013Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347095403Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T07:02:31.347097803Z     raise app_exc
2025-09-28T07:02:31.347100244Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T07:02:31.347102624Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T07:02:31.347104993Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T07:02:31.347107524Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T07:02:31.347109894Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T07:02:31.347110114Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:02:31.347112324Z     await self.app(scope, receive, send)
2025-09-28T07:02:31.347124594Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T07:02:31.347138665Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T07:02:31.347141965Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T07:02:31.347144994Z     raise exc
2025-09-28T07:02:31.347150875Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T07:02:31.347154755Z     await app(scope, receive, sender)
2025-09-28T07:02:31.347158145Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T07:02:31.347161545Z     await self.middleware_stack(scope, receive, send)
2025-09-28T07:02:31.347164355Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T07:02:31.347167055Z     await route.handle(scope, receive, send)
2025-09-28T07:02:31.347170095Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T07:02:31.347172825Z     await self.app(scope, receive, send)
2025-09-28T07:02:31.347176045Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T07:02:31.347179026Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T07:02:31.347181946Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T07:02:31.347184995Z     raise exc
2025-09-28T07:02:31.347187956Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T07:02:31.347190606Z     await app(scope, receive, sender)
2025-09-28T07:02:31.347193516Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T07:02:31.347196836Z     response = await f(request)
2025-09-28T07:02:31.347199336Z                ^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347202076Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 297, in app
2025-09-28T07:02:31.347204436Z     async with AsyncExitStack() as async_exit_stack:
2025-09-28T07:02:31.347206866Z                ~~~~~~~~~~~~~~^^
2025-09-28T07:02:31.347209506Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 768, in __aexit__
2025-09-28T07:02:31.347212356Z     raise exc
2025-09-28T07:02:31.347215066Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 751, in __aexit__
2025-09-28T07:02:31.347218056Z     cb_suppress = await cb(*exc_details)
2025-09-28T07:02:31.347220767Z                   ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347223196Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 235, in __aexit__
2025-09-28T07:02:31.347225627Z     await self.gen.athrow(value)
2025-09-28T07:02:31.347229217Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/concurrency.py", line 30, in contextmanager_in_threadpool
2025-09-28T07:02:31.347234477Z     await anyio.to_thread.run_sync(
2025-09-28T07:02:31.347237387Z         cm.__exit__, type(e), e, e.__traceback__, limiter=exit_limiter
2025-09-28T07:02:31.347240447Z     )
2025-09-28T07:02:31.347243377Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/to_thread.py", line 56, in run_sync
2025-09-28T07:02:31.347246267Z     return await get_async_backend().run_sync_in_worker_thread(
2025-09-28T07:02:31.347248957Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347258637Z         func, args, abandon_on_cancel=abandon_on_cancel, limiter=limiter
2025-09-28T07:02:31.347261517Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347263978Z     )
2025-09-28T07:02:31.347266328Z     ^
2025-09-28T07:02:31.347269038Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 2485, in run_sync_in_worker_thread
2025-09-28T07:02:31.347271938Z     return await future
2025-09-28T07:02:31.347274288Z            ^^^^^^^^^^^^
2025-09-28T07:02:31.347277068Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/anyio/_backends/_asyncio.py", line 976, in run
2025-09-28T07:02:31.347279538Z     result = context.run(func, *args)
2025-09-28T07:02:31.347282378Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T07:02:31.347285248Z     self.gen.throw(value)
2025-09-28T07:02:31.347287948Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T07:02:31.347291448Z   File "/opt/render/project/src/backend/src/database/deps.py", line 82, in get_db
2025-09-28T07:02:31.347294158Z     session_factory.remove()
2025-09-28T07:02:31.347296878Z     ~~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:02:31.347299749Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/scoping.py", line 261, in remove
2025-09-28T07:02:31.347302258Z     self.registry().close()
2025-09-28T07:02:31.347305129Z     ~~~~~~~~~~~~~~~~~~~~~^^
2025-09-28T07:02:31.347308039Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2521, in close
2025-09-28T07:02:31.347310639Z     self._close_impl(invalidate=False)
2025-09-28T07:02:31.347313189Z     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
2025-09-28T07:02:31.347315789Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2590, in _close_impl
2025-09-28T07:02:31.347318219Z     transaction.close(invalidate)
2025-09-28T07:02:31.347320679Z     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T07:02:31.347322989Z   File "<string>", line 2, in close
2025-09-28T07:02:31.347325169Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/state_changes.py", line 119, in _go
2025-09-28T07:02:31.347327679Z     raise sa_exc.IllegalStateChangeError(
2025-09-28T07:02:31.347330379Z     ...<5 lines>...
2025-09-28T07:02:31.347333039Z     )
2025-09-28T07:02:31.34735246Z sqlalchemy.exc.IllegalStateChangeError: Method 'close()' can't be called here; method 'commit()' is already in progress and this would cause an unexpected state change to <SessionTransactionState.CLOSED: 5> (Background on this error at: https://sqlalche.me/e/20/isce)
2025-09-28T07:02:31.779628552Z WARNING:src.payments.endpoints:User bpR6MB3823T20EK7BEa3cs2y22u2 has no subscription record, returning free tier
2025-09-28T07:02:31.780398881Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:02:31.782376002Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T07:02:31.958429174Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T07:02:32.146678687Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 200 OK