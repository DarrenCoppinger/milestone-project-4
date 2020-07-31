from django import forms
from .models import Reservation
from django.utils import timezone
from datetime import datetime, date, time
from django.utils.dateparse import parse_time


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = ('time')


class NumberInput(forms.NumberInput):
    input_type = ('number')


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
            'phone_number': NumberInput,
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

    def clean_date(self):
        booking_date = self.cleaned_data.get('date')
        now = date.today()
        if booking_date < now:
            raise forms.ValidationError(u'Invalid date - selected date passed')
        return booking_date

    def clean_booking_start_time(self):
        booking_start_time = self.cleaned_data.get('booking_start_time')
        opening_time = parse_time('12:30:00')
        if booking_start_time < opening_time:
            raise forms.ValidationError(
                u'Booking must be during bar opening hours 12:30 - 00:00.'
                )
        return booking_start_time

    def clean_booking_end_time(self):
        booking_start_time = self.cleaned_data.get('booking_start_time')
        booking_end_time = self.cleaned_data.get('booking_end_time')
        opening_time = parse_time('12:30:00')
        if booking_end_time < opening_time:
            raise forms.ValidationError(
                u'Booking must be during bar opening hours 12:30 - 00:00.'
                )
        if booking_end_time < booking_start_time:
            raise forms.ValidationError(
                u'Booking can not end before it starts'
                )
        return booking_end_time
