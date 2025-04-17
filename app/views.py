from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    products = Product.objects.all() #.filter(category__category='wax')
    return render(request, 'home.html', {'products': products})

def products(request):
    products = Product.objects.all() 
    return render(request, 'products.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product-detail.html', {'product': product})