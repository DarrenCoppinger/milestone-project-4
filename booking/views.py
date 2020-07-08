from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import ReservationForm
from django.conf import settings
from django.core.mail import send_mail


@login_required()
def booking(request):
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.save()
            subject = "Thank you for requesting a booking at Barstool"
            message = "Welcome to barstool. We appreciate your business. /n We will be in touch soon!"
            from_email = settings.EMAIL_HOST_USER
            to_list = [reservation.email, settings.EMAIL_HOST_USER]
            send_mail(
                subject,
                message,
                from_email,
                to_list,
                fail_silently=True)
            messages.success(
                request,
                "Your have requested a booking. A member of our staff will be in touch shortly to confirm your booking."
                )
            return redirect(reverse('index'))
        else:
            messages.error(request, "We were unable to make this reservation")
    else:
        reservation_form = ReservationForm()
    return render(
        request,
        "booking.html",
        {'reservation_form': reservation_form}
        )
