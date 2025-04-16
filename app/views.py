from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    products = Product.objects.all() #.filter(category__category='wax')
    return render(request, 'home.html', {'products': products})