from django.conf.urls import url, include
from accounts.views import login, logout, registration
from accounts import urls_reset

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', registration, name='register'),
    url(r'^password-reset/', include(urls_reset))
]
