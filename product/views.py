from django.shortcuts import render
from .models import Product, Publisher, Author

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"product": products})

def all_authors(request):
    author = Author.objects.all()
    return render(request, "author.html", {"product": author})

def all_publishers(request):
    publisher = Publisher.objects.all()
    return render(request, "publisher.html", {"product": publisher})

def each_product(request):
    eachproduct = Product.objects.get(pk=this_object_id)
    return render(request, "eachproduct.html", {"product": eachproduct})