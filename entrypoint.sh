#!/usr/bin/env bash
# exit on error
set -o errexit

# prepare backend stuff, think of running collect static and compilemessages in build step
python manage.py collectstatic --no-input
python manage.py migrate

# run web server
python manage.py runserver