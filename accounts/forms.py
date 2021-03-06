from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    """Form to log users in """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register new users"""
    email = forms.CharField(widget=forms.EmailInput)
    password1 = forms.CharField(
            label="Password",
            widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {
            'email': None,
            'username': None,
        }

    def clean_email(self):
        """validate email field"""
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique.')
        return email

    def clean_password2(self):
        """ validate confirm password field field """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError(u'Passwords must match.')

        return password2

    def __init__(self, *args, **kwargs):
        """ Make email field required """
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
