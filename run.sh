#!/bin/bash

cd "$(dirname "$0")"
python manage.py runserver &
xdg-open http://127.0.0.1:8000/
