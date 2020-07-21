from django.test import TestCase
from .models import Product


class TestProductModel(TestCase):
    def test_Product_as_a_string(self):
        product = Product(name="Create a Test")
        self.assertEqual("Create a Test", str(product))
