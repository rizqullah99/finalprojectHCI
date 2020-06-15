from django.http import HttpResponse
from django.shortcuts import render
from .models import Product as P

def index (request):
    products = P.objects.all() 
    return render(request, 'katalog.html', {'products' : products})

def payment(request):
    products = P.objects.all()
    return render(request, 'checkout.html', {'products' : products})


