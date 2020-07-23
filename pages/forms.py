from django import forms


class ContactForm(forms.Form):
    """ Contact Form used with EmailJS """

    username = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 10,
            },
        ),
    )

    class Meta:
        fields = [
            'username',
            'email',
            'message',
        ]
