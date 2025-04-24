from django.contrib import admin
from .models import Product, Categories
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'about_uz']
    search_fields = ['name1', 'price1', 'about_uz']

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_uz', 'category_ru']
    search_fields = ['category_uz', 'category_ru']

admin.site.register(Categories, CategoryAdmin)