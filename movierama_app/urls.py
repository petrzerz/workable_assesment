from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

from .views import HomeView, MovieDetailView, AddMovieView, UpdateMovieView, DeleteMovieView, MovieListByUserView, \
    LikeView, HateView, HomeByLikesView, HomeByHatesView

urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('movie/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
                  path('add_movie/', AddMovieView.as_view(), name='add_movie'),
                  path('movie/edit/<int:pk>', UpdateMovieView.as_view(), name='update_movie'),
                  path('movie/delete/<int:pk>', DeleteMovieView.as_view(), name='delete_movie'),
                  path('user_movie/<int:pk>/', MovieListByUserView.as_view(), name='movie_list_by_user'),
                  path('like/<int:pk>', LikeView, name='like_movie'),
                  path('hate/<int:pk>', HateView, name='hate_movie'),
                  path('home_by_likes/', HomeByLikesView.as_view(), name='home_likes'),
                  path('home_by_hates/', HomeByHatesView.as_view(), name='home_hates')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
