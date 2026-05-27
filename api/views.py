from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from orders.models import Order

from .serializers import (
    ProductSerializer,
    OrderSerializer
)


@api_view(['GET'])
def product_list_api(request):

    products = Product.objects.all()

    serializer = ProductSerializer(
        products,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
def order_list_api(request):

    orders = Order.objects.all()

    serializer = OrderSerializer(
        orders,
        many=True
    )

    return Response(serializer.data)