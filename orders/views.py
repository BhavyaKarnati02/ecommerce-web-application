from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from carts.models import Cart, CartItem
from .models import Order, OrderItem


@login_required
def checkout(request):

    cart = Cart.objects.get(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart)

    total = sum(item.total_price() for item in cart_items)

    if request.method == 'POST':

        address = request.POST['address']

        order = Order.objects.create(
            user=request.user,
            address=address,
            total_price=total
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()

        return redirect('my_orders')

    return render(request, 'checkout.html', {
        'items': cart_items,
        'total': total
    })


@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'my_orders.html', {
        'orders': orders
    })