#!/bin/sh

./wait-for-it.sh -t 0 db:5432

echo "PostgreSQL started"

python manage.py makemigrations;
python manage.py migrate --noinput;
python manage.py collectstatic --noinput;

exec "$@"
