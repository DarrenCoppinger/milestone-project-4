from django.test import TestCase, Client
from products.models import Product

# Create your tests here.


class TestCartViewLoggedOut(TestCase):
    """ Test for cart view when user is logged out """

    def setUp(self):
        self.client = Client()
        # product = Product()
        # product.id = 1
        # product.category = 'PINTS'
        # product.name = "Guiness"
        # product.description = "description"
        # product.price = 4.50
        # product.save()

    def test_search_view(self):
        """
        Check that the search url returns products.html page
        """

        response = self.client.get('/search/?q=')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")
