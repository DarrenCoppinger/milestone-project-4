from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    REQUESTED = 1
    ACCEPTED = 2
    DENIED = 3
    STATUS = (
        (REQUESTED, "Requested"),
        (ACCEPTED, "Accepted"),
        (DENIED, "Denied"),
    )
    STOOL = 1
    WINDOW = 2
    BOOTH = 3
    TABLE = 4
    SEAT_TYPE = (
        (STOOL, "Bar Stool"),
        (WINDOW, "Window Seat"),
        (BOOTH, "Booth"),
        (TABLE, "Table"),
    )

    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()
    seat_type = models.SmallIntegerField(choices=SEAT_TYPE, default=STOOL)
    reserved_start_time = models.TimeField()
    reserved_end_time = models.TimeField()
    status = models.SmallIntegerField(choices=STATUS, default=REQUESTED)
    email = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return "{0} for {1}  ({2} to {3})".format(
            self.status,
            self.date,
            self.reserved_start_time.strftime("%H:%M"),
            self.reserved_end_time.strftime("%H:%M"),
        )
