from django.contrib import admin
from .models import Product, Categories
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'about_uz']
    search_fields = ['name', 'price', 'about']

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    search_fields = ['category']

admin.site.register(Categories, CategoryAdmin)