from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product


class TestProductViewsLoggedOut(TestCase):
    """ Test for cart view when user is logged out """

    def test_all_products_view_logged_out(self):
        """
        Check that the all products view redirects to
        login page when logged out
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/products/")

    def test_filtered_products_view_logged_out(self):
        """
        Check that the filter products views redirects to
        login page when logged out
        """
        response = self.client.get('/products/Pints/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            "/accounts/login/?next=/products/Pints/"
            )

    def test_product_desc_view_logged_out(self):
        """
        Check that the product_desc views redirects to
        login page when logged out
        """

        response = self.client.get('/products/listing/1')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            "/accounts/login/?next=/products/listing/1"
            )


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
        Check that the all products view returns products.html
        page when logged in.
        """

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")

    def test_filtered_products_view_logged_in(self):
        """
        Check that the filter products view returns products.html
        page when logged in.
        """
        response = self.client.get('/products/Pints/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")

    def test_product_desc_view_logged_in(self):
        """
        Check that the product_desc views returns products.html
        page when logged in.
        """
        product = Product()
        product.id = 1
        product.category = 'PINTS'
        product.name = "Guinness"
        product.description = "description"
        product.price = 4.50
        product.save()

        response = self.client.get('/products/listing/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listing.html")
