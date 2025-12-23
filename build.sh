#!/bin/bash

echo "Initialize project..."
python env_setup.py

echo "Building project packages..."
pip install -r requirements.txt
pip freeze > requirements.txt

echo "Migrating Database..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Remove setup files..."
rm -f env_setup.py README.md build.sh