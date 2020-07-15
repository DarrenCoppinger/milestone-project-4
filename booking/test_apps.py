from django.apps import apps
from django.test import TestCase
from .apps import BookingConfig


class TestBookingConfig(TestCase):

    def test_app(self):
        self.assertEqual("booking", BookingConfig.name)
        self.assertEqual("booking", apps.get_app_config("booking").name)
