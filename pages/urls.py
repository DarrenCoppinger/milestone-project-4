from django.conf.urls import url
from .views import contact, about, contact_success, contact_error

urlpatterns = [
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
    url(r'^success/$', contact_success, name='contact_success'),
    url(r'^error/$', contact_error, name='contact_error'),
]
