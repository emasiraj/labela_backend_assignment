from .models import CarPart, ShoppingCartItem, Order
from .serializers import CarPartSerializer, OrderSerializer, ShoppingCartItemSerializer
from rest_framework import generics


class CarPartList(generics.ListCreateAPIView):
    queryset = CarPart.objects.all()
    serializer_class = CarPartSerializer


class CarPartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarPart.objects.all()
    serializer_class = CarPartSerializer

class ShoppingCartItemsView(generics.ListCreateAPIView):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
