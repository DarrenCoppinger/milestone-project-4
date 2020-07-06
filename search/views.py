from django.shortcuts import render
from products.models import Product


def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    query = request.GET['q']
    print('serach query= '+str(query))
    return render(request, "products.html", {"products": products})
