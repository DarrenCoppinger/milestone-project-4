from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import OrderForm, MakePaymentForm


class TestOrderFormLoggedIn(TestCase):
    """ Test for Checkout view when user is logged out """

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

    def test_order_form(self):
        order_form = OrderForm({
            'table_number': 1,
            'full_name': 'Test Name',
            'phone_number': '+353861234567',
            'date': '2020-07-21',
            'time': '21:10'
            })
        self.assertTrue(order_form.is_valid())

    def test_MakePaymentForm_form(self):
        payment_form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvc': '111',
            'expiry_month': '6',
            'expiry_year': '2020',
            'stripe_id': 'tok_visa'
            })
        self.assertTrue(payment_form.is_valid())
