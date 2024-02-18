from rest_framework import serializers
from .models import Category, Product, User, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'quantity', 'category', 'is_active')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'credit_card', 'is_active')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('product_id', 'user_id', 'date')