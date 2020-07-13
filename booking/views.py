from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import ReservationForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site


@login_required()
def booking(request):
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.save()
            subject = "Booking Request at BarTender"
            template = 'mail/request.txt'
            current_site = get_current_site(request)
            user = User.objects.get(username=request.user.username)
            html_message = render_to_string(
                template,
                {
                    'reservation': reservation,
                    'user': user,
                    'site_name': current_site.name,
                }
                )
            # html_message = message
            from_email = settings.EMAIL_HOST_USER
            to_list = [reservation.email, settings.EMAIL_HOST_USER]
            send_mail(
                subject,
                html_message,
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
