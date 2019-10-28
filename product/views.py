from django.shortcuts import render, redirect
from .models import Product, Publisher, Author

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"product": products})

def all_authors(request):
    author = Product.objects.all()
    return render(request, "author.html", {"product": author})

def all_publishers(request):
    publisher = Product.objects.all()
    return render(request, "publisher.html", {"product": publisher})

def each_product(request, pk):
    eachproduct = Product.objects.filter(pk=pk)
    return render(request, "eachproduct.html", {"product": eachproduct})

def each_author(request, pk):
    eachauthor = Product.objects.filter(pk=pk)
    return render(request, "eachauthor.html", {"product": eachauthor})

