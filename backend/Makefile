migrate:
	alembic upgrade head

makemigration:
	alembic revision --autogenerate -m "$(m)"

seed:
	python -m app.scripts.seed
