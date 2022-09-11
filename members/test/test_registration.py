from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase


class SignUpTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testuserpassword'

    # test registration page
    def test_signup_page_url(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        })

        # test if user persisted to database
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    def test_redirection(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        })

        # test redirection to /members/login/
        self.assertRedirects(response, "/members/login/", status_code=302)
