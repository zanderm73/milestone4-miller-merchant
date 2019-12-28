from django.shortcuts import render
from product.models import Product, Author, Publisher

# Create your views here.

# function that filters objects in products based on their title, allows search funstion to be used
def do_search(request):
    products = Product.objects.filter(title__icontains=request.GET['q'])
    return render(request, "products.html", {"product": products})
