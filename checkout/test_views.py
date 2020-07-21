from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import Order


# Create your tests here.
class TestCheckoutViewLoggedOut(TestCase):
    """ Test for Checkout view when user is logged out """

    def setUp(self):
        self.client = Client()

    def test_checkout_redirect_logged_out(self):
        """
        Check that the when not logged in the user
         is redirected to the login page
        """

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/checkout/")


class TestCheckoutViewLoggedIn(TestCase):
    """ Test for Checkout view when user is logged In """
    def test_checkout_redirect_logged_in(self):
        """
        Check that the when not logged in the user
         is redirected to the login page
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='test12345@_password',
        )
        self.client.login(
            username='person',
            password='test12345@_password')

        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout.html")


class TestCheckoutOrderAccepted(TestCase):
    def test_card_order_accepted(self):
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='test12345@_password',
            )
        self.client.login(
            username='person',
            password='test12345@_password')
        self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '100',
            'expiry_month': '6',
            'expiry_year': '2021',
            'stripe_id': 'tok_visa'
            })

        self.assertRaisesMessage(
            messages.success,
            "Your have successfully paid")

        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")

    def test_card_order_declined(self):
        self.client.post('/checkout', {
            'credit_card_number': '4242424242424242',
            'cvv': '100',
            'expiry_month': '6',
            'expiry_year': '2020',
            'stripe_id': 'tok_chargeDeclined',
            })
