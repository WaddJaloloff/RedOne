from django.contrib import admin
from .models import Product, Categories, TopProduct

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name_uz', 'about_uz']
    search_fields = ['name_uz', 'price1', 'about_uz']

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_uz', 'category_ru']
    search_fields = ['category_uz', 'category_ru']

admin.site.register(Categories, CategoryAdmin)


@admin.register(TopProduct)
class TopProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'order']