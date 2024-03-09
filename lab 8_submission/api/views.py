from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

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

class UserLoginAPIView(TokenObtainPairView):
    serializer_class = UserSerializer

class UserRegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    user = request.user
    try:
        product = Product.objects.get(product_id = product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if product.quantity <= 0:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    order = Order.objects.create(user = user, product = product)

    product.quantity -= 1
    product.save()

    serializer = OrderSerializer(order)
    
    return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['POST'])
def user_orders(request, user_id):

    if request.user.id != user_id:
        return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    orders = Order.objects.filter(user_id = user_id)

    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)


