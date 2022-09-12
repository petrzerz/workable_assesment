import os

import django
from init_data import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movierama.settings')
django.setup()
from movierama_app.models import *

for username, password in zip(usernames, passwords):
    try:
        User.objects.get(username=username)
    except Exception as e:
        user = User.objects.create_user(username=username, password=password)

for title, description, username in zip(titles, descriptions, usernames):
    Movie.objects.get_or_create(title=title, description=description, user=User.objects.get(username=username))
