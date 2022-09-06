from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_details.html'
