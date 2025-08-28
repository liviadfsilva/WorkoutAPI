migrate:
	docker compose run --rm app alembic revision --autogenerate -m "$(m)"

upgrade:
	docker compose run --rm app alembic upgrade head

downgrade:
	docker compose run --rm app alembic downgrade -1