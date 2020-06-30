from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from django.views import static
from .settings import MEDIA_ROOT
from accounts.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
