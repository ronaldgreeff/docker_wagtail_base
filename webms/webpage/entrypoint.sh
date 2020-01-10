#!/bin/sh

./wait-for-it.sh -t 0 db:5432

echo "PostgreSQL started"

cd webpage;
python manage.py makemigrations;
python manage.py migrate --noinput;

exec "$@"
