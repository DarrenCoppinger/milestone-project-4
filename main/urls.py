from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from booking import urls as urls_booking
from django.views import static
from .settings import MEDIA_ROOT
from accounts.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^booking/', include(urls_booking)),
    url(r'media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
