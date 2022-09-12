from django.test import TestCase

from movierama_app.models import Movie, User


class MoviePersistTest(TestCase):
    def setUp(self):
        self.username1 = 'testuser1'
        self.password1 = 'testuserpassword1'

        self.username2 = 'testuser2'
        self.password2 = 'testuserpassword2'

        self.title = 'test_movie'
        self.description = 'test_movie_description'

        self.user1 = User.objects.create_user(username=self.username1, password=self.password1)
        # login user
        self.client.force_login(user=self.user1)

        self.user2 = User.objects.create_user(username=self.username2, password=self.password2)
        self.movie = Movie.objects.create(title=self.title, description=self.description, user=self.user1)

    # test if user can like a movie
    def test_like_a_movie(self):
        self.movie.likes.add(self.user2)
        self.assertEqual(self.movie.likes.count(), 1)

    # test if user can hate a movie
    def test_hate_a_movie(self):
        self.movie.hates.add(self.user1)
        self.assertEqual(self.movie.hates.count(), 1)

    # test if movie can be liked from multiple users
    def test_movie_liked_from_more_than_one_user(self):
        self.movie.likes.add(self.user1)
        self.movie.likes.add(self.user2)
        self.assertEqual(self.movie.likes.count(), 2)

    # test if movie can be hated from multiple users
    def test_movie_hated_from_more_than_one_user(self):
        self.movie.hates.add(self.user1)
        self.movie.hates.add(self.user2)
        self.assertEqual(self.movie.hates.count(), 2)

    # test if movie can be liked more tha once from the same user
    def test_movie_multiple_likes_times_same_user(self):
        self.movie.likes.add(self.user1)
        self.movie.likes.add(self.user1)
        self.assertEqual(self.movie.likes.count(), 1)

    # test if movie can be hated more tha once from the same user
    def test_movie_multiple_hates_times_same_user(self):
        self.movie.hates.add(self.user1)
        self.movie.hates.add(self.user1)
        self.assertEqual(self.movie.hates.count(), 1)
