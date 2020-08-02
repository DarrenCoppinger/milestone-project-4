from django.test import TestCase
from .models import Reservation
from django.contrib.auth.models import User


class Testviews(TestCase):
    def test_post_create_a_booking(self):
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='test12345@_password',
            )
        self.client.login(
            username='person',
            password='test12345@_password')
        # self.client.post("/booking/", {
        #     "seat_type": 1,
        #     "full_name": "Test Name",
        #     "phone_number": "12345678910",
        #     "date": '2021-01-01',
        #     "booking_start_time": '20:10',
        #     "booking_end_time": '21:10',
        #     "status": 1,
        #     "email": 'fake@email.com',
        # })
        booking = Reservation.objects.create(
            seat_type=1,
            full_name="Test Name",
            phone_number="12345678910",
            date='2021-01-01',
            booking_start_time='20:10',
            booking_end_time='21:10',
            status=1,
            email='fake@email.com')

        booking = Reservation.objects.get(pk=1)
        self.assertEqual(booking.full_name, "Test Name")

    def test_get_booking_page(self):
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='Jksdjfskdf1321@_password',
            )
        self.client.login(
            username='person',
            password='Jksdjfskdf1321@_password')
        page = self.client.get("/booking/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "booking.html")
    