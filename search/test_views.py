from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestSearchView(TestCase):
    """ Test for cart view when user is logged out """

    def setUp(self):
        self.client = Client()

    def test_search_view_when_user_logged_out(self):
        """
        Check that the search url redirects to login page
        """

        response = self.client.get('/search/?q=')
        self.assertEqual(response.status_code, 302)
        redirect = self.client.get("/accounts/login/?next=/search/?q=")
        self.assertEqual(redirect.status_code, 200)

    def test_search_view_when_user_logged_in(self):
        """
        Check that the search url returns products.html page
        """
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='test12345@_password',
            )
        self.client.login(
            username='person',
            password='test12345@_password')

        response = self.client.get('/search/?q=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")
