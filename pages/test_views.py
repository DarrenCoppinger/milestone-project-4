from django.test import TestCase
from django.contrib.auth.models import User
from .forms import ContactForm


class TestPageViewsLoggedOut(TestCase):
    def test_get_about_page_logged_out(self):
        page = self.client.get("/pages/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_get_contact_page(self):
        page = self.client.get("/pages/contact/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contact.html")


class TestPageViewsLoggedIn(TestCase):
    def test_get_contact_page_logged_in(self):
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='Jksdjfskdf1321@_password',
        )
        self.client.login(
            username='person',
            password='test12345@_password')
        page = self.client.get("/pages/contact/")

        form = page.context['contact_form']
        form_type = type(form)
        self.assertEqual(form_type, ContactForm)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contact.html")
