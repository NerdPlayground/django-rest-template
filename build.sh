#!/bin/bash

echo "Add Database URL..."
python env_setup.py.py

echo "Building project packages..."
pip install -r requirements.txt
pip freeze > requirements.txt

echo "Migrating Database..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Remove setup files..."
rm -f env_setup.py.py README.md build.sh