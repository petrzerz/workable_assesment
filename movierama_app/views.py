from datetime import datetime
from urllib import request

from django.views.generic import ListView, DetailView, CreateView

from .models import Movie


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_details.html'


class AddMovieView(CreateView):
    model = Movie
    template_name = 'add_movie.html'
    fields = 'title', 'description', 'user'
