from django.test import TestCase
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages


class TestUserRegistrationForm(TestCase):
    def test_register_form_valid(self):
        form = UserRegistrationForm(
            {
                "email": "Test@Email.com",
                "username": "person",
                "password1": "test12345@_password",
                "password2": "test12345@_password"
            })
        self.assertTrue(form.is_valid())

    def test_register_form_for_mismatched_passwords(self):
        form = UserRegistrationForm(
            {
                "email": "Test@Email.com",
                "username": "person",
                "password1": "test12345@_password",
                "password2": "test@_password"
            })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], [u"Passwords must match"])


class TestUserLoginForm(TestCase):
    def test_login_using_UserLoginForm(self):
        login_form = UserLoginForm(
            {
                "username": 'person',
                "password": 'Jksdjfskdf1321@_password'})
        self.assertTrue(login_form.is_valid())
        self.assertRaisesMessage(
            messages.success,
            "You have successfully logged in!")

