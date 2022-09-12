#!/bin/bash
yes | python3 manage.py makemigrations movierama_app && yes | python3 manage.py migrate &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start migrations and user creation: $status"
  exit $status
fi

# Start the first process
uwsgi --ini uwsgi.ini &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start API server: $status"
  exit $status
fi

