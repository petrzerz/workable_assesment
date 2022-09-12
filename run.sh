#!/bin/bash
python3 manage.py makemigrations movierama_app && python3 manage.py migrate && python3 movierama_init.py && python3 manage.py test && python3 manage.py runserver 0.0.0.0:8000
