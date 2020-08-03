from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestCartViewLoggedOut(TestCase):
    """ Test for cart view when user is logged out """

    def setUp(self):
        self.client = Client()

    def test_cart_redirect(self):
        """
        Check that the when not logged in the user
         is redirected to the login page
        """

        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/cart/")


class TestCartViewLoggedIn(TestCase):
    """ Test for cart view when user is logged out """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='test12345@_password',
        )
        self.client.login(
            username='person',
            password='test12345@_password')

    def test_cart_redirect(self):
        """
        Check that the when logged in the user
         is directed to the cart page
        """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html")
