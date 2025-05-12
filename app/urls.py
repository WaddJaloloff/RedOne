from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('api/order/', order_create, name='order-create'),
    path('api/index/', index_api, name='index_api'),
    path('api/products/', products_api, name='products_api'),
    path('api/products-all/', all_products_api, name='all_products_api'),
    path('api/product/<int:pk>/', product_detail_api, name='product_detail_api'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)