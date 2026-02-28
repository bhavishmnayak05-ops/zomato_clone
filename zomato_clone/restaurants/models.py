from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)  # ✅ only ONE dot
    location = models.CharField(max_length=200)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=255) 
