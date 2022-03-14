from django.contrib import admin
from .models import CarPart, Order, ShoppingCartItem

admin.site.register(CarPart)
admin.site.register(ShoppingCartItem)
admin.site.register(Order)
