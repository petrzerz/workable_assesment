from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostMovieForm, UpdateMovieForm
from .models import Movie


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'
    ordering = ['-timestamp']

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        timestamp = self.request.GET.get('order_by')
        likes = self.request.GET.get('order_by')
        hates = self.request.GET.get('order_by')

        if timestamp is not None:
            queryset = queryset.order_by('-timestamp')
        # if likes is not None:
        #     queryset = queryset.order_by('likes.all().count')
        # if hates is not None:
        #     queryset = queryset.order_by('likes.all().count')

        return queryset


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_details.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data()
        print(context)
        stuff = get_object_or_404(Movie, id=self.kwargs['pk'])

        total_likes = stuff.total_likes()
        liked = False

        total_hates = stuff.total_hates()
        hated = False

        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
            hated = False
        elif stuff.hates.filter(id=self.request.user.id).exists():
            hated = True
            liked = False

        context['total_likes'] = total_likes
        context['liked'] = liked

        context['total_hates'] = total_hates
        context['hated'] = hated
        return context


class AddMovieView(CreateView):
    model = Movie
    form_class = PostMovieForm
    template_name = 'add_movie.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateMovieView(UpdateView):
    model = Movie
    form_class = UpdateMovieForm
    template_name = 'update_movie.html'


class DeleteMovieView(DeleteView):
    model = Movie
    template_name = 'delete_movie.html'
    success_url = reverse_lazy('home')


class MovieListByUserView(ListView):
    model = Movie
    template_name = 'movie_list_by_user.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(user_id=self.kwargs['pk'])


def LikeView(request, pk):
    movie = get_object_or_404(Movie, id=request.POST.get('movie_id'))
    liked = False
    if movie.likes.filter(id=request.user.id).exists():
        movie.likes.remove(request.user)
        liked = False
    else:
        movie.likes.add(request.user)
        liked = True
        movie.hates.remove(request.user)
        hated = False

    return HttpResponseRedirect(reverse('movie-detail', args=[str(pk)]))


def HateView(request, pk):
    movie = get_object_or_404(Movie, id=request.POST.get('movie_id'))
    hated = False
    if movie.hates.filter(id=request.user.id).exists():
        movie.hates.remove(request.user)
        hated = False
    else:
        movie.hates.add(request.user)
        hated = True
        movie.likes.remove(request.user)
        liked = False
    return HttpResponseRedirect(reverse('movie-detail', args=[str(pk)]))
