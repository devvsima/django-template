-include .env

run:
	python3 manage.py collectstatic && \
	python3 manage.py makemigrations && \
	python3 manage.py migrate && \
	gunicorn -b 0.0.0.0:$(server_port) app.wsgi