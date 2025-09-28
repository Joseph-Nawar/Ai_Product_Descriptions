2025-09-28T06:21:30.872201837Z Using cached google_api_python_client-2.183.0-py3-none-any.whl (14.2 MB)
2025-09-28T06:21:30.890090724Z Using cached google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
2025-09-28T06:21:30.891751414Z Using cached httplib2-0.31.0-py3-none-any.whl (91 kB)
2025-09-28T06:21:30.893462485Z Using cached pyparsing-3.2.5-py3-none-any.whl (113 kB)
2025-09-28T06:21:30.895201177Z Using cached uritemplate-4.2.0-py3-none-any.whl (11 kB)
2025-09-28T06:21:30.917191602Z Using cached mako-1.3.10-py3-none-any.whl (78 kB)
2025-09-28T06:21:30.918530274Z Using cached markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
2025-09-28T06:21:30.919923657Z Using cached pycparser-2.23-py3-none-any.whl (118 kB)
2025-09-28T06:21:31.30746019Z Installing collected packages: pytz, wrapt, urllib3, uritemplate, tzdata, typing-extensions, tqdm, tenacity, structlog, sniffio, six, rapidfuzz, python-multipart, python-dotenv, pyparsing, pymysql, pyjwt, pygments, pycparser, pyasn1, psycopg2-binary, psycopg-binary, psycopg, protobuf, pluggy, packaging, numpy, msgpack, MarkupSafe, iniconfig, idna, hyperframe, hpack, h11, greenlet, google-crc32c, coverage, click, charset_normalizer, certifi, cachetools, annotated-types, uvicorn, typing-inspection, sqlalchemy, sentry-sdk, rsa, requests, python-dateutil, pytest, pydantic-core, pyasn1-modules, proto-plus, Mako, httplib2, httpcore, h2, grpcio, googleapis-common-protos, google-resumable-media, deprecated, cffi, anyio, starlette, pytest-cov, pytest-asyncio, pydantic, pandas, limits, httpx, grpcio-status, google-auth, cryptography, cachecontrol, alembic, slowapi, google-auth-httplib2, google-api-core, fastapi, google-cloud-core, google-api-python-client, google-cloud-storage, google-cloud-firestore, google-ai-generativelanguage, google-generativeai, firebase-admin
2025-09-28T06:22:03.650059555Z 
2025-09-28T06:22:03.658692941Z Successfully installed Mako-1.3.10 MarkupSafe-3.0.3 alembic-1.16.5 annotated-types-0.7.0 anyio-4.11.0 cachecontrol-0.14.3 cachetools-5.5.2 certifi-2025.8.3 cffi-2.0.0 charset_normalizer-3.4.3 click-8.3.0 coverage-7.10.7 cryptography-46.0.1 deprecated-1.2.18 fastapi-0.117.1 firebase-admin-7.1.0 google-ai-generativelanguage-0.6.15 google-api-core-2.25.1 google-api-python-client-2.183.0 google-auth-2.40.3 google-auth-httplib2-0.2.0 google-cloud-core-2.4.3 google-cloud-firestore-2.21.0 google-cloud-storage-3.4.0 google-crc32c-1.7.1 google-generativeai-0.8.5 google-resumable-media-2.7.2 googleapis-common-protos-1.70.0 greenlet-3.2.4 grpcio-1.75.1 grpcio-status-1.71.2 h11-0.16.0 h2-4.3.0 hpack-4.1.0 httpcore-1.0.9 httplib2-0.31.0 httpx-0.28.1 hyperframe-6.1.0 idna-3.10 iniconfig-2.1.0 limits-5.5.0 msgpack-1.1.1 numpy-2.3.3 packaging-25.0 pandas-2.3.2 pluggy-1.6.0 proto-plus-1.26.1 protobuf-5.29.5 psycopg-3.2.10 psycopg-binary-3.2.10 psycopg2-binary-2.9.10 pyasn1-0.6.1 pyasn1-modules-0.4.2 pycparser-2.23 pydantic-2.11.9 pydantic-core-2.33.2 pygments-2.19.2 pyjwt-2.10.1 pymysql-1.1.2 pyparsing-3.2.5 pytest-8.4.2 pytest-asyncio-1.2.0 pytest-cov-7.0.0 python-dateutil-2.9.0.post0 python-dotenv-1.1.1 python-multipart-0.0.20 pytz-2025.2 rapidfuzz-3.14.1 requests-2.32.5 rsa-4.9.1 sentry-sdk-2.39.0 six-1.17.0 slowapi-0.1.9 sniffio-1.3.1 sqlalchemy-2.0.43 starlette-0.48.0 structlog-25.4.0 tenacity-9.1.2 tqdm-4.67.1 typing-extensions-4.15.0 typing-inspection-0.4.1 tzdata-2025.2 uritemplate-4.2.0 urllib3-2.5.0 uvicorn-0.37.0 wrapt-1.17.3
2025-09-28T06:22:03.666071217Z 
2025-09-28T06:22:03.666096578Z [notice] A new release of pip is available: 25.1.1 -> 25.2
2025-09-28T06:22:03.666100427Z [notice] To update, run: pip install --upgrade pip
2025-09-28T06:22:06.697800235Z ==> Uploading build...
2025-09-28T06:22:28.121868582Z ==> Uploaded in 15.5s. Compression took 5.9s
2025-09-28T06:22:28.336513737Z ==> Build successful 🎉
2025-09-28T06:22:56.33888226Z ==> Deploying...
2025-09-28T06:23:29.370467023Z ==> Running '   cd backend && python init_db.py && uvicorn src.main:app --host 0.0.0.0 --port $PORT'
2025-09-28T06:23:32.891302984Z 🔄 Initializing database...
2025-09-28T06:23:32.891341775Z ✅ Database initialized successfully!
2025-09-28T06:24:00.2959701Z ==> No open ports detected, continuing to scan...
2025-09-28T06:24:00.687797605Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2025-09-28T06:24:04.383065701Z /opt/render/project/src/.venv/lib/python3.13/site-packages/pydantic/_internal/_config.py:373: UserWarning: Valid config keys have changed in V2:
2025-09-28T06:24:04.383086302Z * 'schema_extra' has been renamed to 'json_schema_extra'
2025-09-28T06:24:04.383090412Z   warnings.warn(message, UserWarning)
2025-09-28T06:24:04.575026737Z INFO:     Started server process [57]
2025-09-28T06:24:04.575050658Z INFO:     Waiting for application startup.
2025-09-28T06:24:05.353083621Z INFO:     Application startup complete.
2025-09-28T06:24:05.353455071Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2025-09-28T06:24:05.539065173Z No .env file found at: /opt/render/project/src/backend/.env
2025-09-28T06:24:05.539083234Z Make sure to create a .env file with your GEMINI_API_KEY
2025-09-28T06:24:05.539088504Z ✅ Gemini API key loaded successfully
2025-09-28T06:24:05.539092814Z 📊 Using model: gemini-1.5-pro, temperature: 0.8
2025-09-28T06:24:05.539110295Z 💰 Daily cost limit: $1.0, Monthly: $10.0
2025-09-28T06:24:05.539115885Z ✅ AI Product Descriptions API started successfully
2025-09-28T06:24:05.539120425Z 🤖 Model: gemini-1.5-pro (Live mode)
2025-09-28T06:24:05.539126045Z 🌡️  Temperature: 0.8
2025-09-28T06:24:05.539130525Z ✅ API key configured - ready for AI generation
2025-09-28T06:24:05.539134895Z 💳 Credit service initialized - rate limiting enabled
2025-09-28T06:24:05.539139525Z 📋 Subscription plans initialized
2025-09-28T06:24:05.539144225Z INFO:     127.0.0.1:45124 - "HEAD / HTTP/1.1" 404 Not Found
2025-09-28T06:24:07.017398185Z ==> Your service is live 🎉
2025-09-28T06:24:07.134740534Z ==> 
2025-09-28T06:24:07.212984624Z ==> ///////////////////////////////////////////////////////////
2025-09-28T06:24:07.289611593Z ==> 
2025-09-28T06:24:07.367962442Z ==> Available at your primary URL https://ai-product-descriptions.onrender.com
2025-09-28T06:24:07.445126302Z ==> 
2025-09-28T06:24:07.524120992Z ==> ///////////////////////////////////////////////////////////
2025-09-28T06:24:08.80322173Z INFO:     34.168.108.203:0 - "GET / HTTP/1.1" 404 Not Found
2025-09-28T06:24:53.771284944Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:24:53.771563621Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T06:24:53.773233844Z WARNING:root:Invalid auth header format
2025-09-28T06:24:53.773516691Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:24:53.773954882Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 401 Unauthorized
2025-09-28T06:24:53.775225365Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:24:53.7769857Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/subscription HTTP/1.1" 200 OK
2025-09-28T06:24:53.936874763Z INFO:     41.238.10.39:0 - "OPTIONS /api/payment/user/credits HTTP/1.1" 200 OK
2025-09-28T06:24:54.180300789Z ERROR:src.auth.deps:❌ Error in get_authed_user_db: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.185987995Z ERROR:src.auth.deps:❌ Full traceback: Traceback (most recent call last):
2025-09-28T06:24:54.186005835Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.186011345Z     db.execute("SELECT 1")
2025-09-28T06:24:54.186015916Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.186021156Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.186026406Z     return self._execute_internal(
2025-09-28T06:24:54.186031046Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.186036136Z         statement,
2025-09-28T06:24:54.186040656Z         ^^^^^^^^^^
2025-09-28T06:24:54.186045366Z     ...<4 lines>...
2025-09-28T06:24:54.186063467Z         _add_event=_add_event,
2025-09-28T06:24:54.186066617Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.186069467Z     )
2025-09-28T06:24:54.186072607Z     ^
2025-09-28T06:24:54.186075517Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.186078747Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.186081697Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.186084687Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.186087907Z         element, argname=argname, **kw
2025-09-28T06:24:54.186090457Z     )
2025-09-28T06:24:54.186092778Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.186095327Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.186098018Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.186100938Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.186103388Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.186106128Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.186109268Z     raise exc_cls(
2025-09-28T06:24:54.186112138Z     ...<7 lines>...
2025-09-28T06:24:54.186114648Z     ) from err
2025-09-28T06:24:54.186117328Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.186119798Z 
2025-09-28T06:24:54.263835472Z ERROR:src.auth.deps:❌ Error in get_authed_user_db: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.26413183Z ERROR:src.database.deps:Database session error, rolling back: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.26609418Z ERROR:src.auth.deps:❌ Full traceback: Traceback (most recent call last):
2025-09-28T06:24:54.266109511Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.266113231Z     db.execute("SELECT 1")
2025-09-28T06:24:54.266116151Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.266120071Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.266123511Z     return self._execute_internal(
2025-09-28T06:24:54.266126221Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.266129401Z         statement,
2025-09-28T06:24:54.266132301Z         ^^^^^^^^^^
2025-09-28T06:24:54.266135281Z     ...<4 lines>...
2025-09-28T06:24:54.266137691Z         _add_event=_add_event,
2025-09-28T06:24:54.266140441Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.266143312Z     )
2025-09-28T06:24:54.266146001Z     ^
2025-09-28T06:24:54.266148882Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.266152522Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.266155302Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.266158252Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.266161162Z         element, argname=argname, **kw
2025-09-28T06:24:54.266206393Z     )
2025-09-28T06:24:54.266213013Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.266215653Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.266218054Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.266220863Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.266223683Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.266226634Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.266229294Z     raise exc_cls(
2025-09-28T06:24:54.266232224Z     ...<7 lines>...
2025-09-28T06:24:54.266234914Z     ) from err
2025-09-28T06:24:54.266237504Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.266239764Z 
2025-09-28T06:24:54.266655555Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 500 Internal Server Error
2025-09-28T06:24:54.2668723Z ERROR:src.database.deps:Database session error, rolling back: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.288108955Z ERROR:    Exception in ASGI application
2025-09-28T06:24:54.288144366Z Traceback (most recent call last):
2025-09-28T06:24:54.288148116Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:24:54.288150946Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:24:54.288153156Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288155326Z         self.scope, self.receive, self.send
2025-09-28T06:24:54.288157497Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288159946Z     )
2025-09-28T06:24:54.288162037Z     ^
2025-09-28T06:24:54.288164486Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:24:54.288166757Z     return await self.app(scope, receive, send)
2025-09-28T06:24:54.288168797Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288170867Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:24:54.288173037Z     await super().__call__(scope, receive, send)
2025-09-28T06:24:54.288175017Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:24:54.288177147Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.288196287Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:24:54.288198627Z     raise exc
2025-09-28T06:24:54.288200798Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:24:54.288202827Z     await self.app(scope, receive, _send)
2025-09-28T06:24:54.288204948Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:24:54.288207008Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:24:54.288209168Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:24:54.288211998Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:24:54.288227738Z     self.gen.throw(value)
2025-09-28T06:24:54.288230168Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:24:54.288232318Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:24:54.288234378Z     raise exc
2025-09-28T06:24:54.288236799Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:24:54.288238879Z     response = await self.dispatch_func(request, call_next)
2025-09-28T06:24:54.288241099Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288243939Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:24:54.288246049Z     response = await call_next(request)
2025-09-28T06:24:54.288248049Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288250429Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:24:54.288253029Z     raise app_exc
2025-09-28T06:24:54.288255139Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:24:54.288257129Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:24:54.288259189Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:24:54.288264589Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:24:54.288266979Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:24:54.288269009Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.288270999Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:24:54.288273139Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:24:54.288275229Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.288277329Z     raise exc
2025-09-28T06:24:54.28827942Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.28828181Z     await app(scope, receive, sender)
2025-09-28T06:24:54.28828399Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:24:54.28828618Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.28828823Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:24:54.28829025Z     await route.handle(scope, receive, send)
2025-09-28T06:24:54.28829221Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:24:54.28829431Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.28829623Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:24:54.28829841Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:24:54.28831507Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.28831765Z     raise exc
2025-09-28T06:24:54.288319921Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.288322101Z     await app(scope, receive, sender)
2025-09-28T06:24:54.288329141Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:24:54.288331581Z     response = await f(request)
2025-09-28T06:24:54.288333791Z                ^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288335931Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 298, in app
2025-09-28T06:24:54.288338221Z     solved_result = await solve_dependencies(
2025-09-28T06:24:54.288340441Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288342741Z     ...<6 lines>...
2025-09-28T06:24:54.288344871Z     )
2025-09-28T06:24:54.288347061Z     ^
2025-09-28T06:24:54.288349881Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/dependencies/utils.py", line 646, in solve_dependencies
2025-09-28T06:24:54.288352222Z     solved = await call(**solved_result.values)
2025-09-28T06:24:54.288354551Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288357131Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.288359522Z     db.execute("SELECT 1")
2025-09-28T06:24:54.288361942Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.288364332Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.288366562Z     return self._execute_internal(
2025-09-28T06:24:54.288368792Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.288370922Z         statement,
2025-09-28T06:24:54.288373282Z         ^^^^^^^^^^
2025-09-28T06:24:54.288375932Z     ...<4 lines>...
2025-09-28T06:24:54.288378332Z         _add_event=_add_event,
2025-09-28T06:24:54.288380602Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288382772Z     )
2025-09-28T06:24:54.288384892Z     ^
2025-09-28T06:24:54.288387182Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.288389542Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.288392132Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.288394383Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.288396563Z         element, argname=argname, **kw
2025-09-28T06:24:54.288398893Z     )
2025-09-28T06:24:54.288401363Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.288404153Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.288406563Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.288408903Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.288411263Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.288413503Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.288416153Z     raise exc_cls(
2025-09-28T06:24:54.288418293Z     ...<7 lines>...
2025-09-28T06:24:54.288420743Z     ) from err
2025-09-28T06:24:54.288423383Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.28869586Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 500 Internal Server Error
2025-09-28T06:24:54.292097558Z ERROR:    Exception in ASGI application
2025-09-28T06:24:54.292119468Z Traceback (most recent call last):
2025-09-28T06:24:54.292123218Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:24:54.292127488Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:24:54.292131528Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292134908Z         self.scope, self.receive, self.send
2025-09-28T06:24:54.292138989Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292142489Z     )
2025-09-28T06:24:54.292145739Z     ^
2025-09-28T06:24:54.292149129Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:24:54.292152599Z     return await self.app(scope, receive, send)
2025-09-28T06:24:54.292156569Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292159249Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:24:54.292161569Z     await super().__call__(scope, receive, send)
2025-09-28T06:24:54.292163849Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:24:54.292166019Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.292168179Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:24:54.292170289Z     raise exc
2025-09-28T06:24:54.292172469Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:24:54.29217462Z     await self.app(scope, receive, _send)
2025-09-28T06:24:54.29217679Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:24:54.29220031Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:24:54.29220394Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:24:54.29220799Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:24:54.292211761Z     self.gen.throw(value)
2025-09-28T06:24:54.292215891Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:24:54.292219531Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:24:54.292221961Z     raise exc
2025-09-28T06:24:54.292224071Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:24:54.292226171Z     response = await self.dispatch_func(request, call_next)
2025-09-28T06:24:54.292228351Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292231011Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:24:54.292233251Z     response = await call_next(request)
2025-09-28T06:24:54.292235571Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292237641Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:24:54.292240231Z     raise app_exc
2025-09-28T06:24:54.292242391Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:24:54.292244541Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:24:54.292246702Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:24:54.292254312Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:24:54.292256582Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:24:54.292258712Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.292260902Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:24:54.292263222Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:24:54.292265342Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.292267482Z     raise exc
2025-09-28T06:24:54.292269682Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.292271752Z     await app(scope, receive, sender)
2025-09-28T06:24:54.292273892Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:24:54.292276312Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.292279892Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:24:54.292283692Z     await route.handle(scope, receive, send)
2025-09-28T06:24:54.292287172Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:24:54.292290392Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.292294483Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:24:54.292298093Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:24:54.292312243Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.292315793Z     raise exc
2025-09-28T06:24:54.292319103Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.292322783Z     await app(scope, receive, sender)
2025-09-28T06:24:54.292326964Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:24:54.292329433Z     response = await f(request)
2025-09-28T06:24:54.292331584Z                ^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292336074Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 298, in app
2025-09-28T06:24:54.292338304Z     solved_result = await solve_dependencies(
2025-09-28T06:24:54.292340414Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292342564Z     ...<6 lines>...
2025-09-28T06:24:54.292344654Z     )
2025-09-28T06:24:54.292346794Z     ^
2025-09-28T06:24:54.292349634Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/dependencies/utils.py", line 646, in solve_dependencies
2025-09-28T06:24:54.292351744Z     solved = await call(**solved_result.values)
2025-09-28T06:24:54.292353864Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292356094Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.292358204Z     db.execute("SELECT 1")
2025-09-28T06:24:54.292360264Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.292362394Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.292370554Z     return self._execute_internal(
2025-09-28T06:24:54.292372765Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.292374875Z         statement,
2025-09-28T06:24:54.292376985Z         ^^^^^^^^^^
2025-09-28T06:24:54.292379015Z     ...<4 lines>...
2025-09-28T06:24:54.292381105Z         _add_event=_add_event,
2025-09-28T06:24:54.292383145Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292385275Z     )
2025-09-28T06:24:54.292387555Z     ^
2025-09-28T06:24:54.292389715Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.292391905Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.292394045Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.292396185Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.292398235Z         element, argname=argname, **kw
2025-09-28T06:24:54.292400335Z     )
2025-09-28T06:24:54.292402405Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.292404546Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.292406706Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.292408815Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.292410916Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.292412956Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.292415036Z     raise exc_cls(
2025-09-28T06:24:54.292417096Z     ...<7 lines>...
2025-09-28T06:24:54.292419206Z     ) from err
2025-09-28T06:24:54.292421346Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.459347479Z ERROR:src.auth.deps:❌ Error in get_authed_user_db: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.460441137Z ERROR:src.auth.deps:❌ Full traceback: Traceback (most recent call last):
2025-09-28T06:24:54.460453578Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.460457218Z     db.execute("SELECT 1")
2025-09-28T06:24:54.460459878Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.460463118Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.460466748Z     return self._execute_internal(
2025-09-28T06:24:54.460469248Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.460472178Z         statement,
2025-09-28T06:24:54.460475038Z         ^^^^^^^^^^
2025-09-28T06:24:54.460477858Z     ...<4 lines>...
2025-09-28T06:24:54.460479908Z         _add_event=_add_event,
2025-09-28T06:24:54.460481568Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.460483258Z     )
2025-09-28T06:24:54.460486298Z     ^
2025-09-28T06:24:54.460489818Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.460493899Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.460496688Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.460499619Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.460512139Z         element, argname=argname, **kw
2025-09-28T06:24:54.460514639Z     )
2025-09-28T06:24:54.460517049Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.460519309Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.460521549Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.460523959Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.460526319Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.460528569Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.46053084Z     raise exc_cls(
2025-09-28T06:24:54.4605333Z     ...<7 lines>...
2025-09-28T06:24:54.46053604Z     ) from err
2025-09-28T06:24:54.46053878Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.46054118Z 
2025-09-28T06:24:54.460642202Z ERROR:src.database.deps:Database session error, rolling back: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.461051963Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 500 Internal Server Error
2025-09-28T06:24:54.464972003Z ERROR:    Exception in ASGI application
2025-09-28T06:24:54.464983874Z Traceback (most recent call last):
2025-09-28T06:24:54.464988144Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:24:54.464991794Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:24:54.464994744Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.464997394Z         self.scope, self.receive, self.send
2025-09-28T06:24:54.464999734Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.465002054Z     )
2025-09-28T06:24:54.465004464Z     ^
2025-09-28T06:24:54.465006924Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:24:54.465009814Z     return await self.app(scope, receive, send)
2025-09-28T06:24:54.465012515Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.465015195Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:24:54.465017715Z     await super().__call__(scope, receive, send)
2025-09-28T06:24:54.465020345Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:24:54.465022955Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.465025695Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:24:54.465028625Z     raise exc
2025-09-28T06:24:54.465031235Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:24:54.465033905Z     await self.app(scope, receive, _send)
2025-09-28T06:24:54.465036815Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:24:54.465039545Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:24:54.465042165Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:24:54.465045465Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:24:54.465060696Z     self.gen.throw(value)
2025-09-28T06:24:54.465064046Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:24:54.465066336Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:24:54.465068096Z     raise exc
2025-09-28T06:24:54.465070226Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:24:54.465071976Z     response = await self.dispatch_func(request, call_next)
2025-09-28T06:24:54.465073766Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.465076046Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:24:54.465077806Z     response = await call_next(request)
2025-09-28T06:24:54.465079456Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.465081126Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:24:54.465083396Z     raise app_exc
2025-09-28T06:24:54.465085186Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:24:54.465087026Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:24:54.465088746Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:24:54.465091186Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:24:54.465092926Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:24:54.465094737Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.465096437Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:24:54.465098217Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:24:54.465099897Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.465101557Z     raise exc
2025-09-28T06:24:54.465103257Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.465104957Z     await app(scope, receive, sender)
2025-09-28T06:24:54.465106687Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:24:54.465108347Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.465109997Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:24:54.465111687Z     await route.handle(scope, receive, send)
2025-09-28T06:24:54.465114057Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:24:54.465116887Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.465119877Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:24:54.465122927Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:24:54.465136428Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.465139338Z     raise exc
2025-09-28T06:24:54.465142088Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.465149178Z     await app(scope, receive, sender)
2025-09-28T06:24:54.465151078Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:24:54.465152798Z     response = await f(request)
2025-09-28T06:24:54.465154488Z                ^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.465156198Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 298, in app
2025-09-28T06:24:54.465157928Z     solved_result = await solve_dependencies(
2025-09-28T06:24:54.465159588Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.465161288Z     ...<6 lines>...
2025-09-28T06:24:54.465162998Z     )
2025-09-28T06:24:54.465164668Z     ^
2025-09-28T06:24:54.465166998Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/dependencies/utils.py", line 646, in solve_dependencies
2025-09-28T06:24:54.465168679Z     solved = await call(**solved_result.values)
2025-09-28T06:24:54.465170419Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.465172239Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.465173879Z     db.execute("SELECT 1")
2025-09-28T06:24:54.465175569Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.465177309Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.46521294Z     return self._execute_internal(
2025-09-28T06:24:54.4652151Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.46521681Z         statement,
2025-09-28T06:24:54.46521849Z         ^^^^^^^^^^
2025-09-28T06:24:54.46522023Z     ...<4 lines>...
2025-09-28T06:24:54.46522194Z         _add_event=_add_event,
2025-09-28T06:24:54.46522369Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.46522544Z     )
2025-09-28T06:24:54.46522712Z     ^
2025-09-28T06:24:54.46522888Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.46523064Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.46523434Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.4652361Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.46523775Z         element, argname=argname, **kw
2025-09-28T06:24:54.46523952Z     )
2025-09-28T06:24:54.46524362Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.465245381Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.465247101Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.465248821Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.465250541Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.465252251Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.465253961Z     raise exc_cls(
2025-09-28T06:24:54.465255651Z     ...<7 lines>...
2025-09-28T06:24:54.465257371Z     ) from err
2025-09-28T06:24:54.465259121Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.542994805Z ERROR:src.auth.deps:❌ Error in get_authed_user_db: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.544460983Z ERROR:src.auth.deps:❌ Full traceback: Traceback (most recent call last):
2025-09-28T06:24:54.544475223Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.544479743Z     db.execute("SELECT 1")
2025-09-28T06:24:54.544482704Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.544486124Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.544489844Z     return self._execute_internal(
2025-09-28T06:24:54.544493304Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.544497504Z         statement,
2025-09-28T06:24:54.544500604Z         ^^^^^^^^^^
2025-09-28T06:24:54.544503594Z     ...<4 lines>...
2025-09-28T06:24:54.544507054Z         _add_event=_add_event,
2025-09-28T06:24:54.544510504Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.544513955Z     )
2025-09-28T06:24:54.544517295Z     ^
2025-09-28T06:24:54.544520625Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.544524295Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.544528005Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.544531645Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.544535475Z         element, argname=argname, **kw
2025-09-28T06:24:54.544537705Z     )
2025-09-28T06:24:54.544539895Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.544542115Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.544544285Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.544546395Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.544548475Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.544550525Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.544552725Z     raise exc_cls(
2025-09-28T06:24:54.544554885Z     ...<7 lines>...
2025-09-28T06:24:54.544557125Z     ) from err
2025-09-28T06:24:54.544559276Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.544561286Z 
2025-09-28T06:24:54.544658468Z ERROR:src.database.deps:Database session error, rolling back: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.545146201Z INFO:     41.238.10.39:0 - "GET /api/payment/user/subscription HTTP/1.1" 500 Internal Server Error
2025-09-28T06:24:54.550008485Z ERROR:    Exception in ASGI application
2025-09-28T06:24:54.550024846Z Traceback (most recent call last):
2025-09-28T06:24:54.550028636Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:24:54.550031826Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:24:54.550034236Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.550036766Z         self.scope, self.receive, self.send
2025-09-28T06:24:54.550039166Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.550041446Z     )
2025-09-28T06:24:54.550044006Z     ^
2025-09-28T06:24:54.550046586Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:24:54.550061247Z     return await self.app(scope, receive, send)
2025-09-28T06:24:54.550063867Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.550066397Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:24:54.550068727Z     await super().__call__(scope, receive, send)
2025-09-28T06:24:54.550071167Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:24:54.550073647Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.550076197Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:24:54.550078457Z     raise exc
2025-09-28T06:24:54.550080897Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:24:54.550083347Z     await self.app(scope, receive, _send)
2025-09-28T06:24:54.550085627Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:24:54.550088027Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:24:54.550090607Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:24:54.550237841Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:24:54.550247202Z     self.gen.throw(value)
2025-09-28T06:24:54.550249792Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:24:54.550252702Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:24:54.550254942Z     raise exc
2025-09-28T06:24:54.550257282Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:24:54.550259862Z     response = await self.dispatch_func(request, call_next)
2025-09-28T06:24:54.550262162Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.550264862Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:24:54.550267192Z     response = await call_next(request)
2025-09-28T06:24:54.550269402Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.550271702Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:24:54.550274372Z     raise app_exc
2025-09-28T06:24:54.550276672Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:24:54.550366475Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:24:54.550369895Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:24:54.550372735Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:24:54.550375065Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:24:54.550377545Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.550379975Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:24:54.550382405Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:24:54.550384695Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.550394305Z     raise exc
2025-09-28T06:24:54.550396775Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.550399235Z     await app(scope, receive, sender)
2025-09-28T06:24:54.550401715Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:24:54.550403986Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.550406216Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:24:54.550408446Z     await route.handle(scope, receive, send)
2025-09-28T06:24:54.550410716Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:24:54.550413096Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.550415286Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:24:54.550417606Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:24:54.550476908Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.550480828Z     raise exc
2025-09-28T06:24:54.550483548Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.550485928Z     await app(scope, receive, sender)
2025-09-28T06:24:54.550488368Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:24:54.550490738Z     response = await f(request)
2025-09-28T06:24:54.550493228Z                ^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.550495418Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 298, in app
2025-09-28T06:24:54.550497848Z     solved_result = await solve_dependencies(
2025-09-28T06:24:54.550499998Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.550502458Z     ...<6 lines>...
2025-09-28T06:24:54.550504838Z     )
2025-09-28T06:24:54.550507088Z     ^
2025-09-28T06:24:54.550510068Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/dependencies/utils.py", line 646, in solve_dependencies
2025-09-28T06:24:54.550512318Z     solved = await call(**solved_result.values)
2025-09-28T06:24:54.550538129Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.550541679Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.550544069Z     db.execute("SELECT 1")
2025-09-28T06:24:54.550546399Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.550548889Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.550551179Z     return self._execute_internal(
2025-09-28T06:24:54.55055341Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.55055571Z         statement,
2025-09-28T06:24:54.550558039Z         ^^^^^^^^^^
2025-09-28T06:24:54.55056315Z     ...<4 lines>...
2025-09-28T06:24:54.55056548Z         _add_event=_add_event,
2025-09-28T06:24:54.55056769Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.55057Z     )
2025-09-28T06:24:54.55057235Z     ^
2025-09-28T06:24:54.55057474Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.5505775Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.55058672Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.55058928Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.55059166Z         element, argname=argname, **kw
2025-09-28T06:24:54.55059392Z     )
2025-09-28T06:24:54.5505964Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.550598831Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.550619321Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.550622181Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.550626811Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.550629261Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.550631841Z     raise exc_cls(
2025-09-28T06:24:54.550634201Z     ...<7 lines>...
2025-09-28T06:24:54.550636481Z     ) from err
2025-09-28T06:24:54.550638852Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.706421119Z ERROR:src.auth.deps:❌ Error in get_authed_user_db: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.707457025Z ERROR:src.auth.deps:❌ Full traceback: Traceback (most recent call last):
2025-09-28T06:24:54.707465786Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.707468536Z     db.execute("SELECT 1")
2025-09-28T06:24:54.707470336Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.707472566Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.707474806Z     return self._execute_internal(
2025-09-28T06:24:54.707476616Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.707478986Z         statement,
2025-09-28T06:24:54.707480696Z         ^^^^^^^^^^
2025-09-28T06:24:54.707482446Z     ...<4 lines>...
2025-09-28T06:24:54.707484116Z         _add_event=_add_event,
2025-09-28T06:24:54.707485846Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.707487566Z     )
2025-09-28T06:24:54.707489286Z     ^
2025-09-28T06:24:54.707491086Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.707493297Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.707495077Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.707497006Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.707498707Z         element, argname=argname, **kw
2025-09-28T06:24:54.707500357Z     )
2025-09-28T06:24:54.707502057Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.707504047Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.707507037Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.707510087Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.707512947Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.707515517Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.707531587Z     raise exc_cls(
2025-09-28T06:24:54.707534798Z     ...<7 lines>...
2025-09-28T06:24:54.707537198Z     ) from err
2025-09-28T06:24:54.707539328Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.707540958Z 
2025-09-28T06:24:54.707659101Z ERROR:src.database.deps:Database session error, rolling back: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.708064431Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 500 Internal Server Error
2025-09-28T06:24:54.712370612Z ERROR:    Exception in ASGI application
2025-09-28T06:24:54.712398312Z Traceback (most recent call last):
2025-09-28T06:24:54.712402772Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:24:54.712406063Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:24:54.712408883Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712411743Z         self.scope, self.receive, self.send
2025-09-28T06:24:54.712414833Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712417643Z     )
2025-09-28T06:24:54.712420283Z     ^
2025-09-28T06:24:54.712423023Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:24:54.712425683Z     return await self.app(scope, receive, send)
2025-09-28T06:24:54.712428403Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712431103Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:24:54.712434153Z     await super().__call__(scope, receive, send)
2025-09-28T06:24:54.712436873Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:24:54.712438823Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.712440553Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:24:54.712442284Z     raise exc
2025-09-28T06:24:54.712443964Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:24:54.712445664Z     await self.app(scope, receive, _send)
2025-09-28T06:24:54.712447324Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:24:54.712449344Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:24:54.712451104Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:24:54.712453574Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:24:54.712455744Z     self.gen.throw(value)
2025-09-28T06:24:54.712457434Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:24:54.712459084Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:24:54.712460754Z     raise exc
2025-09-28T06:24:54.712462424Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:24:54.712464084Z     response = await self.dispatch_func(request, call_next)
2025-09-28T06:24:54.712465774Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712468284Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:24:54.712477734Z     response = await call_next(request)
2025-09-28T06:24:54.712479774Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712481434Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:24:54.712483885Z     raise app_exc
2025-09-28T06:24:54.712485575Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:24:54.712487355Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:24:54.712489155Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:24:54.712491595Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:24:54.712493305Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:24:54.712495035Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.712496705Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:24:54.712498425Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:24:54.712500075Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.712501795Z     raise exc
2025-09-28T06:24:54.712503465Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.712505115Z     await app(scope, receive, sender)
2025-09-28T06:24:54.712506835Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:24:54.712508495Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.712510145Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:24:54.712512015Z     await route.handle(scope, receive, send)
2025-09-28T06:24:54.712513665Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:24:54.712515435Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.712517075Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:24:54.712518775Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:24:54.712530426Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.712532346Z     raise exc
2025-09-28T06:24:54.712534086Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.712535826Z     await app(scope, receive, sender)
2025-09-28T06:24:54.712541056Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:24:54.712542796Z     response = await f(request)
2025-09-28T06:24:54.712544476Z                ^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712546156Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 298, in app
2025-09-28T06:24:54.712547856Z     solved_result = await solve_dependencies(
2025-09-28T06:24:54.712549576Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712552026Z     ...<6 lines>...
2025-09-28T06:24:54.712557016Z     )
2025-09-28T06:24:54.712558827Z     ^
2025-09-28T06:24:54.712561096Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/dependencies/utils.py", line 646, in solve_dependencies
2025-09-28T06:24:54.712562907Z     solved = await call(**solved_result.values)
2025-09-28T06:24:54.712564627Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712566327Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.712567987Z     db.execute("SELECT 1")
2025-09-28T06:24:54.712569647Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.712571327Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.712573097Z     return self._execute_internal(
2025-09-28T06:24:54.712574807Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.712576477Z         statement,
2025-09-28T06:24:54.712578167Z         ^^^^^^^^^^
2025-09-28T06:24:54.712579807Z     ...<4 lines>...
2025-09-28T06:24:54.712581447Z         _add_event=_add_event,
2025-09-28T06:24:54.712583147Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712584797Z     )
2025-09-28T06:24:54.712586467Z     ^
2025-09-28T06:24:54.712588187Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.712589927Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.712591647Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.712593377Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.712595037Z         element, argname=argname, **kw
2025-09-28T06:24:54.712596677Z     )
2025-09-28T06:24:54.712598437Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.712600157Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.712601857Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.712603508Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.712605168Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.712606818Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.712608548Z     raise exc_cls(
2025-09-28T06:24:54.712610218Z     ...<7 lines>...
2025-09-28T06:24:54.712611888Z     ) from err
2025-09-28T06:24:54.712613648Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.967388305Z ERROR:src.auth.deps:❌ Error in get_authed_user_db: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.968905074Z ERROR:src.auth.deps:❌ Full traceback: Traceback (most recent call last):
2025-09-28T06:24:54.968915705Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.968920285Z     db.execute("SELECT 1")
2025-09-28T06:24:54.968923545Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.968927565Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.968931455Z     return self._execute_internal(
2025-09-28T06:24:54.968935015Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.968939695Z         statement,
2025-09-28T06:24:54.968941905Z         ^^^^^^^^^^
2025-09-28T06:24:54.968958826Z     ...<4 lines>...
2025-09-28T06:24:54.968962776Z         _add_event=_add_event,
2025-09-28T06:24:54.968966076Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.968969556Z     )
2025-09-28T06:24:54.968972906Z     ^
2025-09-28T06:24:54.968976536Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.968981696Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.968984236Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.968986416Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.968988596Z         element, argname=argname, **kw
2025-09-28T06:24:54.968990696Z     )
2025-09-28T06:24:54.968992936Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.968995136Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.968997277Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.968999457Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.969001607Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.969003687Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.969005847Z     raise exc_cls(
2025-09-28T06:24:54.969007937Z     ...<7 lines>...
2025-09-28T06:24:54.969010157Z     ) from err
2025-09-28T06:24:54.969012357Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.969014347Z 
2025-09-28T06:24:54.969098019Z ERROR:src.database.deps:Database session error, rolling back: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:54.969593372Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 500 Internal Server Error
2025-09-28T06:24:54.975083853Z ERROR:    Exception in ASGI application
2025-09-28T06:24:54.975094513Z Traceback (most recent call last):
2025-09-28T06:24:54.975097733Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:24:54.975100523Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:24:54.975102583Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.975104703Z         self.scope, self.receive, self.send
2025-09-28T06:24:54.975108063Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.975111904Z     )
2025-09-28T06:24:54.975115453Z     ^
2025-09-28T06:24:54.975118714Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:24:54.975122014Z     return await self.app(scope, receive, send)
2025-09-28T06:24:54.975125274Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.975128874Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:24:54.975132344Z     await super().__call__(scope, receive, send)
2025-09-28T06:24:54.975136224Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:24:54.975139844Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.975143214Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:24:54.975157925Z     raise exc
2025-09-28T06:24:54.975162125Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:24:54.975166185Z     await self.app(scope, receive, _send)
2025-09-28T06:24:54.975169335Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:24:54.975172885Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:24:54.975176355Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:24:54.975205646Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:24:54.975210436Z     self.gen.throw(value)
2025-09-28T06:24:54.975213686Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:24:54.975217166Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:24:54.975220466Z     raise exc
2025-09-28T06:24:54.975223666Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:24:54.975227347Z     response = await self.dispatch_func(request, call_next)
2025-09-28T06:24:54.975230967Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.975234877Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:24:54.975238477Z     response = await call_next(request)
2025-09-28T06:24:54.975241717Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.975245267Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:24:54.975249407Z     raise app_exc
2025-09-28T06:24:54.975252857Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:24:54.975256247Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:24:54.975259907Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:24:54.975264227Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:24:54.975267968Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:24:54.975270188Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.975272378Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:24:54.975274508Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:24:54.975276628Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.975278708Z     raise exc
2025-09-28T06:24:54.975281338Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.975283468Z     await app(scope, receive, sender)
2025-09-28T06:24:54.975285608Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:24:54.975287658Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:54.975289818Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:24:54.975291908Z     await route.handle(scope, receive, send)
2025-09-28T06:24:54.975299688Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:24:54.975301928Z     await self.app(scope, receive, send)
2025-09-28T06:24:54.975304038Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:24:54.975306158Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:24:54.975319399Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:54.975321879Z     raise exc
2025-09-28T06:24:54.975324069Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:54.975326189Z     await app(scope, receive, sender)
2025-09-28T06:24:54.975328289Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:24:54.975330389Z     response = await f(request)
2025-09-28T06:24:54.975332419Z                ^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.975334499Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 298, in app
2025-09-28T06:24:54.975336609Z     solved_result = await solve_dependencies(
2025-09-28T06:24:54.975338709Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.975340789Z     ...<6 lines>...
2025-09-28T06:24:54.975342939Z     )
2025-09-28T06:24:54.975345039Z     ^
2025-09-28T06:24:54.975347819Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/dependencies/utils.py", line 646, in solve_dependencies
2025-09-28T06:24:54.975349899Z     solved = await call(**solved_result.values)
2025-09-28T06:24:54.97535201Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.97535419Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:54.97535631Z     db.execute("SELECT 1")
2025-09-28T06:24:54.97535843Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:54.9753605Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:54.97536261Z     return self._execute_internal(
2025-09-28T06:24:54.97536468Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:54.97536672Z         statement,
2025-09-28T06:24:54.97536876Z         ^^^^^^^^^^
2025-09-28T06:24:54.97537078Z     ...<4 lines>...
2025-09-28T06:24:54.97537294Z         _add_event=_add_event,
2025-09-28T06:24:54.97537508Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.97537713Z     )
2025-09-28T06:24:54.97537918Z     ^
2025-09-28T06:24:54.97538138Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:54.975383531Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:54.975385591Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:54.97538764Z     resolved = impl._literal_coercion(
2025-09-28T06:24:54.975389731Z         element, argname=argname, **kw
2025-09-28T06:24:54.975391871Z     )
2025-09-28T06:24:54.975394001Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:54.975396141Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:54.975398251Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:54.975400281Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:54.975406261Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:54.975408421Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:54.975410561Z     raise exc_cls(
2025-09-28T06:24:54.975412681Z     ...<7 lines>...
2025-09-28T06:24:54.975414801Z     ) from err
2025-09-28T06:24:54.975419731Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:56.588528057Z ERROR:src.auth.deps:❌ Error in get_authed_user_db: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:56.589589014Z ERROR:src.auth.deps:❌ Full traceback: Traceback (most recent call last):
2025-09-28T06:24:56.589597704Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:56.589601664Z     db.execute("SELECT 1")
2025-09-28T06:24:56.589604384Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:56.589607764Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:56.589611084Z     return self._execute_internal(
2025-09-28T06:24:56.589612784Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:56.589614984Z         statement,
2025-09-28T06:24:56.589616655Z         ^^^^^^^^^^
2025-09-28T06:24:56.589618465Z     ...<4 lines>...
2025-09-28T06:24:56.589621295Z         _add_event=_add_event,
2025-09-28T06:24:56.589623365Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.589625825Z     )
2025-09-28T06:24:56.589627955Z     ^
2025-09-28T06:24:56.589630145Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:56.589633685Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:56.589635895Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:56.589638115Z     resolved = impl._literal_coercion(
2025-09-28T06:24:56.589640195Z         element, argname=argname, **kw
2025-09-28T06:24:56.589642265Z     )
2025-09-28T06:24:56.589644445Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:56.589646595Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:56.589648745Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.589650885Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:56.589652965Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:56.589655125Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:56.589657246Z     raise exc_cls(
2025-09-28T06:24:56.589659356Z     ...<7 lines>...
2025-09-28T06:24:56.589661476Z     ) from err
2025-09-28T06:24:56.589664726Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:56.589668136Z 
2025-09-28T06:24:56.589765478Z ERROR:src.database.deps:Database session error, rolling back: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:56.590154228Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 500 Internal Server Error
2025-09-28T06:24:56.59371052Z ERROR:    Exception in ASGI application
2025-09-28T06:24:56.59373529Z Traceback (most recent call last):
2025-09-28T06:24:56.59373974Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:24:56.593743421Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:24:56.59374677Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.593750291Z         self.scope, self.receive, self.send
2025-09-28T06:24:56.593753881Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.593757141Z     )
2025-09-28T06:24:56.593759361Z     ^
2025-09-28T06:24:56.593761581Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:24:56.593763701Z     return await self.app(scope, receive, send)
2025-09-28T06:24:56.593765811Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.593767931Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:24:56.593770011Z     await super().__call__(scope, receive, send)
2025-09-28T06:24:56.593772211Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:24:56.593776661Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:56.593778841Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:24:56.593780991Z     raise exc
2025-09-28T06:24:56.593783562Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:24:56.593786911Z     await self.app(scope, receive, _send)
2025-09-28T06:24:56.593790612Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:24:56.593794012Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:24:56.593797732Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:24:56.593801902Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:24:56.593805742Z     self.gen.throw(value)
2025-09-28T06:24:56.593809052Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:24:56.593812872Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:24:56.593816792Z     raise exc
2025-09-28T06:24:56.593820732Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:24:56.593824072Z     response = await self.dispatch_func(request, call_next)
2025-09-28T06:24:56.593827153Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.593830763Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:24:56.593834073Z     response = await call_next(request)
2025-09-28T06:24:56.593838013Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.593841223Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:24:56.593845213Z     raise app_exc
2025-09-28T06:24:56.593848993Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:24:56.593851343Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:24:56.593853523Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:24:56.593861464Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:24:56.593863744Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:24:56.593865864Z     await self.app(scope, receive, send)
2025-09-28T06:24:56.593867994Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:24:56.593870094Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:24:56.593872164Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:56.593874674Z     raise exc
2025-09-28T06:24:56.593878234Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:56.593881854Z     await app(scope, receive, sender)
2025-09-28T06:24:56.593885554Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:24:56.593889124Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:56.593892604Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:24:56.593895884Z     await route.handle(scope, receive, send)
2025-09-28T06:24:56.593899125Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:24:56.593902425Z     await self.app(scope, receive, send)
2025-09-28T06:24:56.593906015Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:24:56.593908845Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:24:56.593923255Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:56.593926785Z     raise exc
2025-09-28T06:24:56.593930165Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:56.593933305Z     await app(scope, receive, sender)
2025-09-28T06:24:56.593936926Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:24:56.593939886Z     response = await f(request)
2025-09-28T06:24:56.593942046Z                ^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.593944146Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 298, in app
2025-09-28T06:24:56.593946226Z     solved_result = await solve_dependencies(
2025-09-28T06:24:56.593948346Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.593950486Z     ...<6 lines>...
2025-09-28T06:24:56.593952556Z     )
2025-09-28T06:24:56.593954636Z     ^
2025-09-28T06:24:56.593956806Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/dependencies/utils.py", line 646, in solve_dependencies
2025-09-28T06:24:56.593959026Z     solved = await call(**solved_result.values)
2025-09-28T06:24:56.593961086Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.593963256Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:56.593965736Z     db.execute("SELECT 1")
2025-09-28T06:24:56.593969186Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:56.593973176Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:56.593989207Z     return self._execute_internal(
2025-09-28T06:24:56.593992957Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:56.593996837Z         statement,
2025-09-28T06:24:56.593999027Z         ^^^^^^^^^^
2025-09-28T06:24:56.594001217Z     ...<4 lines>...
2025-09-28T06:24:56.594003347Z         _add_event=_add_event,
2025-09-28T06:24:56.594005437Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.594007507Z     )
2025-09-28T06:24:56.594009577Z     ^
2025-09-28T06:24:56.594011677Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:56.594013897Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:56.594016017Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:56.594018108Z     resolved = impl._literal_coercion(
2025-09-28T06:24:56.594020208Z         element, argname=argname, **kw
2025-09-28T06:24:56.594022288Z     )
2025-09-28T06:24:56.594024468Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:56.594026598Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:56.594028678Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:56.594030888Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:56.594032988Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:56.594035048Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:56.594037138Z     raise exc_cls(
2025-09-28T06:24:56.594039198Z     ...<7 lines>...
2025-09-28T06:24:56.594041308Z     ) from err
2025-09-28T06:24:56.594043438Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:57.644850171Z ERROR:src.auth.deps:❌ Error in get_authed_user_db: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:57.64634498Z ERROR:src.auth.deps:❌ Full traceback: Traceback (most recent call last):
2025-09-28T06:24:57.64637422Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:57.646377921Z     db.execute("SELECT 1")
2025-09-28T06:24:57.646380511Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:57.646383251Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:57.646410601Z     return self._execute_internal(
2025-09-28T06:24:57.646414882Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:57.646417932Z         statement,
2025-09-28T06:24:57.646420472Z         ^^^^^^^^^^
2025-09-28T06:24:57.646422952Z     ...<4 lines>...
2025-09-28T06:24:57.646425372Z         _add_event=_add_event,
2025-09-28T06:24:57.646427972Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.646430562Z     )
2025-09-28T06:24:57.646433152Z     ^
2025-09-28T06:24:57.646435852Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:57.646439302Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:57.646441762Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:57.646444462Z     resolved = impl._literal_coercion(
2025-09-28T06:24:57.646458793Z         element, argname=argname, **kw
2025-09-28T06:24:57.646461503Z     )
2025-09-28T06:24:57.646463983Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:57.646466503Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:57.646469153Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.646471603Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:57.646486034Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:57.646491263Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:57.646494004Z     raise exc_cls(
2025-09-28T06:24:57.646496424Z     ...<7 lines>...
2025-09-28T06:24:57.646499014Z     ) from err
2025-09-28T06:24:57.646501804Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:57.646504294Z 
2025-09-28T06:24:57.646675048Z ERROR:src.database.deps:Database session error, rolling back: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
2025-09-28T06:24:57.647059948Z INFO:     41.238.10.39:0 - "GET /api/payment/user/credits HTTP/1.1" 500 Internal Server Error
2025-09-28T06:24:57.653075792Z ERROR:    Exception in ASGI application
2025-09-28T06:24:57.653088083Z Traceback (most recent call last):
2025-09-28T06:24:57.653091993Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
2025-09-28T06:24:57.653095293Z     result = await app(  # type: ignore[func-returns-value]
2025-09-28T06:24:57.653098293Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.653101493Z         self.scope, self.receive, self.send
2025-09-28T06:24:57.653103983Z         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.653105703Z     )
2025-09-28T06:24:57.653107983Z     ^
2025-09-28T06:24:57.653111073Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-09-28T06:24:57.653113933Z     return await self.app(scope, receive, send)
2025-09-28T06:24:57.653116593Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.653119333Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/applications.py", line 1082, in __call__
2025-09-28T06:24:57.653121994Z     await super().__call__(scope, receive, send)
2025-09-28T06:24:57.653124944Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/applications.py", line 113, in __call__
2025-09-28T06:24:57.653127994Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:57.653130894Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-09-28T06:24:57.653133554Z     raise exc
2025-09-28T06:24:57.653136104Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-09-28T06:24:57.653138854Z     await self.app(scope, receive, _send)
2025-09-28T06:24:57.653141394Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 182, in __call__
2025-09-28T06:24:57.653143974Z     with recv_stream, send_stream, collapse_excgroups():
2025-09-28T06:24:57.653146734Z                                    ~~~~~~~~~~~~~~~~~~^^
2025-09-28T06:24:57.653151074Z   File "/opt/render/project/python/Python-3.13.4/lib/python3.13/contextlib.py", line 162, in __exit__
2025-09-28T06:24:57.653162575Z     self.gen.throw(value)
2025-09-28T06:24:57.653165305Z     ~~~~~~~~~~~~~~^^^^^^^
2025-09-28T06:24:57.653167875Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-09-28T06:24:57.653170485Z     raise exc
2025-09-28T06:24:57.653173195Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 184, in __call__
2025-09-28T06:24:57.653175775Z     response = await self.dispatch_func(request, call_next)
2025-09-28T06:24:57.653209016Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.653216066Z   File "/opt/render/project/src/backend/src/main.py", line 90, in add_security_headers
2025-09-28T06:24:57.653218696Z     response = await call_next(request)
2025-09-28T06:24:57.653221316Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.653223936Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 159, in call_next
2025-09-28T06:24:57.653227096Z     raise app_exc
2025-09-28T06:24:57.653229976Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/base.py", line 144, in coro
2025-09-28T06:24:57.653233047Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-09-28T06:24:57.653234956Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-09-28T06:24:57.653236876Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-09-28T06:24:57.653238607Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-09-28T06:24:57.653240257Z     await self.app(scope, receive, send)
2025-09-28T06:24:57.653241917Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-09-28T06:24:57.653244737Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-09-28T06:24:57.653247787Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:57.653250627Z     raise exc
2025-09-28T06:24:57.653253287Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:57.653256047Z     await app(scope, receive, sender)
2025-09-28T06:24:57.653258657Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 716, in __call__
2025-09-28T06:24:57.653261227Z     await self.middleware_stack(scope, receive, send)
2025-09-28T06:24:57.653264227Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 736, in app
2025-09-28T06:24:57.653266887Z     await route.handle(scope, receive, send)
2025-09-28T06:24:57.653269608Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 290, in handle
2025-09-28T06:24:57.653272248Z     await self.app(scope, receive, send)
2025-09-28T06:24:57.653275188Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 78, in app
2025-09-28T06:24:57.653277728Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-09-28T06:24:57.653283518Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-09-28T06:24:57.653286318Z     raise exc
2025-09-28T06:24:57.653288988Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-09-28T06:24:57.653296418Z     await app(scope, receive, sender)
2025-09-28T06:24:57.653298178Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/starlette/routing.py", line 75, in app
2025-09-28T06:24:57.653299918Z     response = await f(request)
2025-09-28T06:24:57.653301548Z                ^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.653303178Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 298, in app
2025-09-28T06:24:57.653304808Z     solved_result = await solve_dependencies(
2025-09-28T06:24:57.653306438Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.653308069Z     ...<6 lines>...
2025-09-28T06:24:57.653309789Z     )
2025-09-28T06:24:57.653311469Z     ^
2025-09-28T06:24:57.653313429Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/fastapi/dependencies/utils.py", line 646, in solve_dependencies
2025-09-28T06:24:57.653315109Z     solved = await call(**solved_result.values)
2025-09-28T06:24:57.653316789Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.653318509Z   File "/opt/render/project/src/backend/src/auth/deps.py", line 26, in get_authed_user_db
2025-09-28T06:24:57.653320139Z     db.execute("SELECT 1")
2025-09-28T06:24:57.653321799Z     ~~~~~~~~~~^^^^^^^^^^^^
2025-09-28T06:24:57.653323509Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2365, in execute
2025-09-28T06:24:57.653325129Z     return self._execute_internal(
2025-09-28T06:24:57.653326799Z            ~~~~~~~~~~~~~~~~~~~~~~^
2025-09-28T06:24:57.653328749Z         statement,
2025-09-28T06:24:57.653330559Z         ^^^^^^^^^^
2025-09-28T06:24:57.653332199Z     ...<4 lines>...
2025-09-28T06:24:57.653333839Z         _add_event=_add_event,
2025-09-28T06:24:57.653335549Z         ^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.653337229Z     )
2025-09-28T06:24:57.653338879Z     ^
2025-09-28T06:24:57.653340549Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 2149, in _execute_internal
2025-09-28T06:24:57.653342259Z     statement = coercions.expect(roles.StatementRole, statement)
2025-09-28T06:24:57.653344459Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 395, in expect
2025-09-28T06:24:57.653347159Z     resolved = impl._literal_coercion(
2025-09-28T06:24:57.653350219Z         element, argname=argname, **kw
2025-09-28T06:24:57.65335299Z     )
2025-09-28T06:24:57.65335562Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 621, in _literal_coercion
2025-09-28T06:24:57.6533587Z     return self._text_coercion(element, argname, **kw)
2025-09-28T06:24:57.65336161Z            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
2025-09-28T06:24:57.65336431Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 614, in _text_coercion
2025-09-28T06:24:57.65336691Z     return _no_text_coercion(element, argname)
2025-09-28T06:24:57.65336944Z   File "/opt/render/project/src/.venv/lib/python3.13/site-packages/sqlalchemy/sql/coercions.py", line 584, in _no_text_coercion
2025-09-28T06:24:57.65337193Z     raise exc_cls(
2025-09-28T06:24:57.65337442Z     ...<7 lines>...
2025-09-28T06:24:57.65337714Z     ) from err
2025-09-28T06:24:57.65338014Z sqlalchemy.exc.ArgumentError: Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')