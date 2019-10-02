from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def mineralwool(request):
    mineralwool = Product.objects.all()
    return render(request, "mineralwool.html", {"products": mineralwool})

def plasterboard(request):
    plasterboard = Product.objects.all()
    return render(request, "plasterboard.html", {"products": plasterboard})

def pir(request):
    pir = Product.objects.all()
    return render(request, "pir.html", {"products": pir})

def thermallaminate(request):
    thermallaminate = Product.objects.all()
    return render(request, "thermallaminate.html", {"products": thermallaminate})

