from django.shortcuts import render
from .models import Product


def all_products(request):
    """ Display all products in Products dataset """
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})
