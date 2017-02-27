from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User)



