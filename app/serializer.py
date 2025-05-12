from rest_framework import serializers
from .models import Product, Categories, TopProduct


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class TopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProduct
        fields = '__all__'
