from django.urls import path

from api.views import *

urlpatterns = [
    path('api/products/', index),
    path('api/login/', user_login),
    path('api/register/', user_register),
    path('api/products/<int:product_id>/', product_detail),
    path('api/categories/', category_list),
    path('api/categories/<int:category_id>/products/', category_products),
    path('api/products/<int:product_id>/buy/', product_buy),
    path('api/users/<int:user_id>/orders/', user_orders)
]
