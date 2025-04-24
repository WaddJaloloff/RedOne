from django.shortcuts import render
from .models import *
from .models import Product, Categories



# Create your views here.
def index(request):
    products = Product.objects.filter(is_active=True).select_related('category')[:4]
    categories = Categories.objects.filter(product__is_active=True).distinct()
    
    # Maxsus kesilgan nomlarni olish
    for product in products:
        product.name_uz = product.name_uz[:20].rsplit(' ', 1)[0] if len(product.name_uz) > 20 else product.name_uz
        product.name_ru = product.name_ru[:20].rsplit(' ', 1)[0] if len(product.name_ru) > 20 else product.name_ru

    return render(request, 'home.html', {'products': products, 'categories': categories})


def products(request):
    products = Product.objects.filter(is_active=True).select_related('category')
    categories = Categories.objects.filter(product__is_active=True).distinct()

    # Maxsus kesilgan nomlarni olish
    for product in products:
        product.name_uz = product.name_uz[:18].rsplit(' ', 1)[0] if len(product.name_uz) > 18 else product.name_uz
        product.name_ru = product.name_ru[:18].rsplit(' ', 1)[0] if len(product.name_ru) > 18 else product.name_ru

    return render(request, 'products.html', {
        'products': products,
        'categories': categories
    })


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product-detail.html', {'product': product})
