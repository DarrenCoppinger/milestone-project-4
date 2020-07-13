from django.contrib import admin
from .models import Reservation
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'status')
    readonly_fields = ('full_name', 'phone_number', 'email')

    def save_model(self, request, obj, form, change):
        current_site = get_current_site(request)
        user = User.objects.get(username=request.user.username)
        if change:
            print('Inside check loop 1')
            print(obj)
            if(obj.status == 1):
                subject = "Booking Request at BarTender - REQUEST ALTERED"
                template = 'mail/request.txt'
            elif(obj.status == 2):
                subject = "Booking Request at BarTender - ACCEPTED"
                template = 'mail/accepted.txt'
            elif(obj.status == 3):
                subject = "Booking Request at BarTender - DENIED"
                template = 'mail/denied.txt'
            html_message = render_to_string(
                template,
                {
                    'reservation': obj,
                    'user': user,
                    'site_name': current_site.name,
                }
                )
            from_email = settings.EMAIL_HOST_USER
            to_list = [obj.email, settings.EMAIL_HOST_USER]
            send_mail(
                subject=subject,
                message=strip_tags(html_message),
                from_email=from_email,
                recipient_list=to_list,
                fail_silently=True,
                html_message=html_message)
        return super().save_model(request, obj, form, change)


admin.site.register(Reservation, ReservationAdmin)
