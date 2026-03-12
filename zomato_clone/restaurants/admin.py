
from django.contrib import admin
from django.utils.html import format_html
from .models import Restaurant, FoodItem

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'rating', 'image_preview')
    search_fields = ('name', 'location')
    list_filter = ('rating',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="border-radius: 5px; object-fit: cover;" />',
                obj.image.url
            )
        return 'No Image'
    image_preview.short_description = 'Image Preview'

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price', 'image_preview')
    search_fields = ('name', 'restaurant__name')
    list_filter = ('restaurant', 'price')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="border-radius: 5px; object-fit: cover;" />',
                obj.image.url
            )
        return 'No Image'
    image_preview.short_description = 'Image Preview'
