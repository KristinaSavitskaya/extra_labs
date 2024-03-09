from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 255)

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE)
    is_active = models.BooleanField(default = True)

class User(models.Model):
    username = models.CharField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    credit_card = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)

class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)