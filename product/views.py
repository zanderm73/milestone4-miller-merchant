from django.shortcuts import render, redirect
from .models import Product, Publisher, Author

# Create your views here.

# renders product/home page of the site
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"product": products})


# renders author page and displays all authors who currently have a book on the site
def all_authors(request):
    author = Product.objects.all()
    return render(request, "author.html", {"product": author})

# renders publisher page and displays all publishers who currently have a book on the site
def all_publishers(request):
    publisher = Product.objects.all()
    return render(request, "publisher.html", {"product": publisher})

# renders a unique product page using pk which shows a more in depth view of the book
def each_product(request, pk):
    eachproduct = Product.objects.filter(pk=pk)
    return render(request, "eachproduct.html", {"product": eachproduct})

# renders a unique author page using pk which shows a mroe in depth view of the author
def each_author(request, pk):
    eachauthor = Product.objects.filter(pk=pk)
    return render(request, "eachauthor.html", {"product": eachauthor})

