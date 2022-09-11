from django.contrib.auth.models import User
from django.test import TestCase


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    # test login page
    def test_login_page_url(self):
        response = self.client.get("/members/login/")
        self.assertEqual(response.status_code, 200)

    # test if user is active after login
    def test_login(self):
        # send login data
        response = self.client.post('/members/login/', self.credentials, follow=True)
        # should be logged in now
        print(response)
        self.assertTrue(response.context['user'].is_active)
