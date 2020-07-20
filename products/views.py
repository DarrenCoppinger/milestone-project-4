from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required


@login_required
def all_products(request):
    """ Display all products in Products dataset """
    products = Product.objects.order_by('category')
    return render(request, 'products.html', {"products": products})


@login_required
def filtered_products(request, category_name):
    products = Product.objects.filter(category=category_name)
    return render(request, 'products.html', {"products": products})


@login_required
def product_desc(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'listing.html', {"product": product})
