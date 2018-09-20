from rest_framework import serializers
from .models import LineItem
from order.models import Order
from product.serializers import ProductSerializer

class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        depth =1
        fields = ('product', 'quantity', 'product_total')
