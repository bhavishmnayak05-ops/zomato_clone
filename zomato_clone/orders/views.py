from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order
from restaurants.models import FoodItem

@login_required(login_url='login')
def add_to_order(request, food_item_id):
    food_item = FoodItem.objects.get(id=food_item_id)
    quantity = int(request.POST.get('quantity', 1))
    
    order = Order.objects.create(
        user=request.user,
        food_item=food_item,
        quantity=quantity
    )
    messages.success(request, f'{food_item.name} added to cart!')
    return redirect('restaurant_detail', id=food_item.restaurant.id)

@login_required(login_url='login')
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    total_price = sum(order.get_subtotal() for order in orders)
    
    return render(request, 'orders/my_orders.html', {
        'orders': orders,
        'total_price': total_price
    })

@login_required(login_url='login')
def checkout(request):
    orders = Order.objects.filter(user=request.user)
    if not orders.exists():
        messages.warning(request, 'Your cart is empty!')
        return redirect('home')
    
    total_price = sum(order.get_subtotal() for order in orders)
    delivery_fee = 50
    tax = round((total_price + delivery_fee) * 0.05, 2)
    final_total = total_price + delivery_fee + tax
    
    if request.method == 'POST':
        orders.delete()
        messages.success(request, 'Order placed successfully!')
        return redirect('home')
    
    return render(request, 'orders/checkout.html', {
        'orders': orders,
        'total_price': total_price,
        'delivery_fee': delivery_fee,
        'tax': tax,
        'final_total': final_total
    })

@login_required(login_url='login')
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if order.user == request.user:
        order.delete()
        messages.success(request, 'Item removed from cart!')
    return redirect('my_orders')
