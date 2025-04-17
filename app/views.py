from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    products = Product.objects.filter(is_active=True)
    categories = Categories.objects.filter(product__is_active=True).distinct()
    return render(request, 'home.html', {'products': products, 'categories': categories})
def products(request):
    categories = Categories.objects.filter(product__is_active=True).distinct()  # faqat aktiv kategoriyalar
    return render(request, 'products.html', {'categories': categories})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product-detail.html', {'product': product})