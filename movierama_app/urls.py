from django.urls import path

from .views import HomeView, MovieDetailView, AddMovieView, UpdateMovieView, DeleteMovieView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('add_movie/', AddMovieView.as_view(), name='add_movie'),
    path('movie/edit/<int:pk>', UpdateMovieView.as_view(), name='update_movie'),
    path('movie/delete/<int:pk>', DeleteMovieView.as_view(), name='delete_movie')
]
