from django.conf.urls import url
from .views import all_products, product_desc

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^listing/(?P<id>\d+)', product_desc, name='product_desc'),
    
]
