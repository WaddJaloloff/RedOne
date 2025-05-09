from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Categories(models.Model):
    category_uz = models.CharField(max_length=30)
    category_ru = models.CharField(max_length=30)
    def __str__(self):
        return self.category_uz
    

class Product(models.Model):
    name_uz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200, blank=True)
    size1 = models.CharField(max_length=10)
    price1 = models.IntegerField()
    size2 = models.CharField(max_length=10, null=True, blank=True)
    price2 = models.IntegerField(null=True, blank=True)
    about_uz = models.TextField(null=True, blank=True)
    about_ru = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_uz
    
    def save(self, *args, **kwargs):
        if not self.name_ru:
            self.name_ru = self.name_uz
        super().save(*args, **kwargs)

    @property
    def formatted_price1(self):
        return f"{self.price1:,}".replace(",", " ")

    @property
    def formatted_price2(self):
        if self.price2:
            return f"{self.price2:,}".replace(",", " ")
        return ""
    from django.core.exceptions import ValidationError

class TopProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Qaysi tartibda chiqishini belgilang")
    def __str__(self):
        return f"Top: {self.product.name_uz}"

