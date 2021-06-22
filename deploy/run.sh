# run.sh
# Run all the commands required to start Django in production.
#!/bin/sh

python manage.py collectstatic --noinput

python manage.py migrate

# For Production:
gunicorn project.wsgi --reload --workers=2 --threads=4 --worker-tmp-dir=/dev/shm --bind=0.0.0.0:8080 --log-file=- --worker-class=gthread
