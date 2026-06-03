from rest_framework import serializers
from .models import Order, OrderedItem

class OrderSeriailizer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = '__all__'

class OrderedItemSeriailizer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem 
        fields = '__all__'