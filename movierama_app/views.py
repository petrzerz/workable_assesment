from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import PostMovieForm, UpdateMovieForm
from .models import Movie


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_details.html'


class AddMovieView(CreateView):
    model = Movie
    form_class = PostMovieForm
    template_name = 'add_movie.html'


class UpdateMovieView(UpdateView):
    model = Movie
    form_class = UpdateMovieForm
    template_name = 'update_movie.html'
