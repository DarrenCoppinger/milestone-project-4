from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'table_number',
            'full_name',
            'phone_number'
            )
        labels = {
            'table_number': 'Table Number',
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
        }
        exclude = ['date', 'time']


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2040)]

    credit_card_number = forms.CharField(
        label="Credit card number",
        required=False)
    cvc = forms.CharField(
        label="Security Code (CVC)",
        required=False)
    expiry_month = forms.ChoiceField(
        label="Expiry Month",
        choices=MONTH_CHOICES,
        required=False)
    expiry_year = forms.ChoiceField(
        label="Expiry Year",
        choices=YEAR_CHOICES,
        required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
