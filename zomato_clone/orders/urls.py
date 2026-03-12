from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order/<int:food_item_id>/', views.add_to_order, name='add_to_order'),
    path('my-orders/', views.view_orders, name='my_orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
]
