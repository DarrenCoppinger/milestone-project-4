from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import ReservationForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags

@login_required()
def booking(request):
    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            user = User.objects.get(username=request.user.username)
            reservation.email = user.email
            reservation.save()
            subject = "Booking Request at BarTender - REQUEST"
            template = 'mail/request.txt'
            current_site = get_current_site(request)
            html_message = render_to_string(
                template,
                {
                    'reservation': reservation,
                    'user': user,
                    'site_name': current_site.name,
                }
                )
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email, settings.EMAIL_HOST_USER]
            send_mail(
                subject=subject,
                message=strip_tags(html_message),
                from_email=from_email,
                recipient_list=to_list,
                fail_silently=True,
                html_message=html_message)
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
