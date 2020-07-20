from django.test import TestCase
from django.contrib.auth.models import User


class TestProductViewsLoggedOut(TestCase):
    """ Test for cart view when user is logged out """

    def test_all_products_view_logged_out(self):
        """
        Check that the products url redirects when logged out
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/products/")


class TestProductViewsLoggedIn(TestCase):
    """ Test for cart view when user is logged out """

    def setUp(self):
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='test12345@_password',
        )
        self.client.login(
            username='person',
            password='test12345@_password')

    def test_all_products_view_logged_in(self):
        """
        Check that the products url returns products.html page
        """

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")
