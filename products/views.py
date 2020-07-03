from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ Display all products in Products dataset """
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})


def product_desc(request, id):
    product = get_object_or_404(Product, pk=id)
    print('product name= ', str(product.name))
    return render(request, 'listing.html', {"product": product})
