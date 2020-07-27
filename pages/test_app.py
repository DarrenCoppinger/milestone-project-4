from django.apps import apps
from django.test import TestCase
from .apps import PagesConfig


class TestPagesConfig(TestCase):

    def test_app(self):
        self.assertEqual("pages", PagesConfig.name)
        self.assertEqual("pages", apps.get_app_config("pages").name)
