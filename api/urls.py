from django.urls import path
from . import views

urlpatterns = [

    path('products/',
         views.product_list_api,
         name='product_api'),

    path('orders/',
         views.order_list_api,
         name='order_api'),
]