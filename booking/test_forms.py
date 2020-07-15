from django.test import TestCase
from .form import ReservationForm


class TestReservationForm(TestCase):

    def test_can_create_a_reservation_(self):
        reservation_form = ReservationForm({
            'seat_type': '1',
            'full_name': 'Test Name',
            'phone_number': '12345678910',
            'date': '1/1/21',
            'reserved_start_time': '20:10',
            'reserved_end_time': '21:10'})
        self.assertTrue(reservation_form.is_valid())

    def test_correct_message_for_missing_name(self):
        reservation_form = ReservationForm({
            'seat_type': '1',
            'full_name': '',
            'phone_number': '12345678910',
            'date': '1/1/21',
            'reserved_start_time': '20:10',
            'reserved_end_time': '21:10'})
        self.assertFalse(reservation_form.is_valid())
        self.assertEqual(
            reservation_form.errors['full_name'], [u'This field is required.'])
