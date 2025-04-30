from django.shortcuts import render
from .models import *
from .run_bot import send_order_to_group
from .models import Product, Categories
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def index(request):
    last_products = Product.objects.filter(is_active=True).select_related('category').order_by('-id')[:4]
    top_products = Top_product.objects.filter(is_active=True)[:4]
    # Maxsus kesilgan nomlarni olish
    for product in last_products:
        product.name_uz = product.name_uz[:20].rsplit(' ', 1)[0] if len(product.name_uz) > 20 else product.name_uz
        product.name_ru = product.name_ru[:20].rsplit(' ', 1)[0] if len(product.name_ru) > 20 else product.name_ru

    return render(request, 'home.html', {'last_products': last_products, 'top_products': top_products})


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


# korzina    backend

def order_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_number = data.get('phone')
        order_items = data.get('items', [])
        send_order_to_group(phone_number, order_items)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Invalid method'}, status=405)
