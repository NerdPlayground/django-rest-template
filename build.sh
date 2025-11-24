#!/bin/bash

echo "Building project packages..."
pip install -r requirements.txt

echo "Add Database URL..."
python database_setup.py

echo "Migrating Database..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Updating packages..."
cat requirements.txt | cut -f1 -d= | xargs pip install -U
pip freeze > requirements.txt