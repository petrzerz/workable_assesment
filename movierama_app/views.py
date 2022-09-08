from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostMovieForm, UpdateMovieForm
from .models import Movie


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'
    ordering = ['-timestamp']


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


class DeleteMovieView(DeleteView):
    # permission_classes = (IsAuthenticated,)
    model = Movie
    template_name = 'delete_movie.html'
    success_url = reverse_lazy('home')


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'category_list.html'
#
#     def get_queryset(self, **kwargs):
#        qs = super().get_queryset(**kwargs)
#        return qs.filter(brand_id=self.kwargs['pk'])
#
# And the url should look like this:
#
# path('category/<int:pk>/', CategoryListView.as_view())
