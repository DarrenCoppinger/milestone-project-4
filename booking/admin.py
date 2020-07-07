from django.contrib import admin
from .models import Reservation
from .form import ReservationForm
from django.core.mail import send_mail
from django.conf import settings


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'status')
    readonly_fields = ('full_name', 'phone_number', 'email')

    def save_model(self, request, obj, form, change):
        if change:
            print('Inside check loop 1')
            print(obj)
            if(obj.status == 2):
                subject = "Status Changed - ACCEPTED"
                message = "Status Changed - ACCEPTED"
            elif(obj.status == 3):
                subject = "Status Changed - DENIED"
                message = "Status Changed - DENIED"
            from_email = settings.EMAIL_HOST_USER
            to_list = [obj.email, settings.EMAIL_HOST_USER]
            send_mail(
                subject,
                message,
                from_email,
                to_list,
                fail_silently=False)
        return super().save_model(request, obj, form, change)


admin.site.register(Reservation, ReservationAdmin)
