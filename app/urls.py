from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('api/order/', order_create, name='order-create')
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)