from django.test import TestCase
from .models import Reservation


class TestReservationModel(TestCase):
    def test_seat_type_defaults_to_STOOL(self):
        reservation = Reservation(
            full_name="Test Name",
            phone_number='12345678910',
            date='2021-01-01',
            booking_start_time='20:10',
            booking_end_time='21:10'
            )
        reservation.save()
        self.assertEqual(reservation.full_name, "Test Name")
        self.assertEqual(reservation.seat_type, 1)

    def test_status_defaults_to_REQUEST(self):
        reservation = Reservation(
            full_name="Test Name",
            phone_number='12345678910',
            date='2021-01-01',
            booking_start_time='20:10',
            booking_end_time='21:10'
            )
        reservation.save()
        self.assertEqual(reservation.full_name, "Test Name")
        self.assertEqual(reservation.status, 1)

    def test_reservation_details_as_string(self):
        reservation = Reservation(
            status=1,
            full_name="Test Name",
            phone_number='12345678910',
            date='2021-01-01',
            booking_start_time='20:10',
            booking_end_time='21:10',
        )
        self.assertEqual(
            "1 for 2021-01-01  (20:10 to 21:10)",
            str(reservation))
