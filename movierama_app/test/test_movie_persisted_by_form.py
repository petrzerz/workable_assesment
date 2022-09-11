from django.test import TestCase

from movierama_app.models import Movie, User


class MoviePersistTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testuserpassword'
        self.title = 'test_movie'
        self.description = 'test_movie_description'

        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.force_login(user=self.user)

    # test add movie page
    def test_add_movie_page_url(self):
        response = self.client.get("/add_movie/")
        self.assertEqual(response.status_code, 200)

    def test_add_movie_form(self):
        response = self.client.post('/add_movie/', data={
            'title': self.title,
            'description': self.password
        })
        # test if movie persisted to database
        movies = Movie.objects.all()
        self.assertEqual(movies.count(), 1)

    def test_redirection(self):
        response = self.client.post('/add_movie/', data={
            'title': self.title,
            'description': self.password
        })

        # test redirection to home
        self.assertRedirects(response, "/", status_code=302)

    def test_if_movie_registered_to_logged_in_user(self):
        response = self.client.post('/add_movie/', data={
            'title': self.title,
            'description': self.password
        })
        movies = Movie.objects.all()
        # test if movie registered to the logged in user
        self.assertEqual(movies.first().user.id, self.user.id)
