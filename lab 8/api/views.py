from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ProductSerializer, CategorySerializer, UserSerializer, OrderSerializer

from .models import Product, Category, User, Order

def index(request: HttpRequest):

    products = Product.objects.filter(is_active = True, quantity__gt=0)

    json_data = [{
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "quantity": product.quantity,
        "category_id": product.category_id,
        "is_active": product.is_active,
    } for product in products]

    return JsonResponse(json_data, safe = False)

@api_view(['POST'])
def user_login(request):

    pass

@api_view(['POST'])
def user_register(request):

    pass

@api_view(['GET'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(product_id = product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_products(request, category_id):
    try:
        products = Product.objects.filter(category_id = category_id)
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def product_buy(request, product_id):

    pass

@api_view(['POST'])
def user_orders(request, user_id):

    pass
