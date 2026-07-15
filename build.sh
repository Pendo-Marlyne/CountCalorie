#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit

pip install -r requirements.txt

cd countcalorie
python manage.py collectstatic --no-input
python manage.py migrate
