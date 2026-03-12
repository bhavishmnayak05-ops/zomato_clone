from django.shortcuts import render
from .models import Restaurant, FoodItem

def home(request):
    restaurants = Restaurant.objects.all()
    food_items = FoodItem.objects.all()[:12]  # Get first 12 food items
    return render(request, 'home.html', {
        'restaurants': restaurants,
        'food_items': food_items
    })

def restaurant_detail(request, id):
    restaurant = Restaurant.objects.get(id=id)
    food_items = FoodItem.objects.filter(restaurant=restaurant)
    
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'food_items': food_items
    })