#!/bin/bash

set -e
set -o errexit
set -o nounset

python manage.py makemigrations
python ./manage.py migrate
python ./manage.py collectstatic --no-input

exec "$@"
