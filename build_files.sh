#!/bin/bash
set -x

pip install -r requirements.txt
python manage.py collectstatic --noinput
