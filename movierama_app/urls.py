from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie-detail')
]
