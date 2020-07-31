from django import forms
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = ('time')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = (
            'seat_type',
            'full_name',
            'phone_number',
            'date',
            'booking_start_time',
            'booking_end_time'
            )
        widgets = {
            'date': DateInput(),
            'booking_start_time': TimeInput(),
            'booking_end_time': TimeInput()
            }
        labels = {
            'seat_type': 'Seat Type',
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'booking_start_time': 'Booking Start Time',
            'booking_end_time': 'Booking End Time',
        }
        exclude = ['status']
