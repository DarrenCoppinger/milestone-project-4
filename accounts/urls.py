from django.conf.urls import url, include
from accounts.views import login, logout

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
]