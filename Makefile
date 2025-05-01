web-dev:
	docker-compose run --service-ports --rm dev-web-app fastapi run /app/src/main.py --port 80

web-dev-build:
	docker-compose build dev-web-app