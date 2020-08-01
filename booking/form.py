from django import forms
from .models import Reservation
from datetime import date, time
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

    def clean(self):
        """
            Clean the date, booking_start_time and booking_end_time
            fields of the ReservationForm
        """
        cleaned_data = super().clean()
        # ------ Date ------
        booking_date = self.cleaned_data.get('date')
        now = date.today()
        if booking_date < now:
            msg = "Invalid date - selected date passed"
            self.add_error('date', msg)

        # ------ booking_start_time ------
        booking_start_time = self.cleaned_data.get('booking_start_time')
        opening_time = parse_time('12:30:00')
        print('booking_start_time= ' + str(booking_start_time))
        if booking_start_time < opening_time:
            msg = "Booking must start during bar opening hours 12:30 - 00:00."
            self.add_error('booking_start_time', msg)

        # ------ booking_end_time ------
        booking_end_time = self.cleaned_data.get('booking_end_time')
        opening_time = parse_time('12:30:00')
        print('booking_start_time= ' + str(booking_start_time))
        print('booking_end_time= ' + str(booking_end_time))
        if booking_end_time < opening_time:
            msg = "Booking must end during bar opening hours 12:30 - 00:00."
            self.add_error('booking_end_time', msg)
        if booking_end_time < booking_start_time:
            msg = "Booking can not end before it starts"
            self.add_error('booking_end_time', msg)
        return cleaned_data
