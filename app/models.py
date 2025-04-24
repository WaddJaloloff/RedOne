from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category
    

class Product(models.Model):
    name_uz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    size1 = models.CharField(max_length=10)
    price1 = models.IntegerField()
    size2 = models.CharField(max_length=10, null=True, blank=True)
    price2 = models.IntegerField(null=True, blank=True)
    about_uz = models.TextField(null=True, blank=True)
    about_ru = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_uz
    
    @property
    def formatted_price1(self):
        return f"{self.price1:,}".replace(",", " ")

    @property
    def formatted_price2(self):
        if self.price2:
            return f"{self.price2:,}".replace(",", " ")
        return ""