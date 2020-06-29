from django.conf.urls import url, include
from accounts.views import login, logout, registration

urlpatterns = [
    # url(r'^index/$', index, name='index'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', registration, name='register'),
]
