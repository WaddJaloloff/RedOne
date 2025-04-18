from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    products = Product.objects.filter(is_active=True).select_related('category')[:4]  # tezroq ishlashi uchun
    categories = Categories.objects.filter(product__is_active=True).distinct()
    return render(request, 'home.html', {'products': products, 'categories': categories})


def products(request):
    products = Product.objects.filter(is_active=True).select_related('category')  # tezroq ishlashi uchun
    categories = Categories.objects.filter(product__is_active=True).distinct()
    return render(request, 'products.html', {
        'products': products,
        'categories': categories
    })


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product-detail.html', {'product': product})