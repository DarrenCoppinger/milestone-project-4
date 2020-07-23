from django.conf.urls import url
from .views import contact, about

urlpatterns = [
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
]