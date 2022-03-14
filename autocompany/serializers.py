from rest_framework import serializers
from .models import CarPart, Order, ShoppingCartItem

class CarPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPart
        fields = ['id', 'name', 'price', 'description', 'stock']

    def create(self, validated_data):
        return CarPart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    sub_total = serializers.CharField(source="get_sub_total_price", read_only=True)
    class Meta:
        model = ShoppingCartItem
        fields = ['item', 'quantity', 'item_name', 'sub_total']

class OrderSerializer(serializers.ModelSerializer):
    items = ShoppingCartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['items', 'delivery_datetime']