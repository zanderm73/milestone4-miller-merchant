from django.shortcuts import render
from product.models import Product, Author, Publisher

# Create your views here.
def do_search(request):
    products = Product.objects.filter(title__icontains=request.GET['q'])
    return render(request, "products.html", {"product": products})
