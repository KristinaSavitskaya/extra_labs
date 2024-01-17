import json
from django.http import HttpRequest, JsonResponse

from models import Product

def index(request: HttpRequest):

    products = Product.objects.filter(is_active = True, quantity__gt = 0)

    json_data = [{
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "quantity": product.quantity,
        "category_id": product.category_id,
        "is_active": product.is_active,
    } for product in products]

    return JsonResponse(json_data, safe=False)
