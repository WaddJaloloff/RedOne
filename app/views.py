from django.shortcuts import render, get_object_or_404
from .models import *
from .run_bot import send_order_to_group
from .models import Product, Categories
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, TopProduct
from .serializer import ProductSerializer, TopProductSerializer


@api_view(['GET'])
def index_api(request):
    top_products = TopProduct.objects.select_related('product').order_by('order')[:4]
    serializer = TopProductSerializer(top_products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def products_api(request):
    products = Product.objects.filter(is_active=True).select_related('category')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_products_api(request):
    products = Product.objects.select_related('category')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail_api(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Mahsulot topilmadi'}, status=404)
    
    serializer = ProductSerializer(product)
    return Response(serializer.data)



def index(request):
    last_products = Product.objects.filter(is_active=True).select_related('category').order_by('-id')[:4]
    top_products = TopProduct.objects.select_related('product').order_by('order')[:4]

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


# API viewla












# korzina    backend
@csrf_protect
def order_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_number = data.get('phone')
        order_items = data.get('items', [])
        send_order_to_group(phone_number, order_items)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Invalid method'}, status=405)
