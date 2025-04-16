from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    about = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
    