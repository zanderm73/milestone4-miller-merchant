from django.shortcuts import render

# Create your views here.

# renders index.html page
def index(request):
    return render(request, "index.html")