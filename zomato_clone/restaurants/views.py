from django.shortcuts import render
from .models import Restaurant

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

    from .models import Restaurant, FoodItem

def restaurant_detail(request, id):
    restaurant = Restaurant.objects.get(id=id)
    food_items = Food_items.objects.filter(restaurant=restaurant)
    
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'food_items': food_items
    })