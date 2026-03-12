from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from restaurants.models import FoodItem

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    def get_subtotal(self):
        return self.food_item.price * self.quantity
