from rest_framework import serializers
from .models import LineItem
from product.serializers import ProductSerializer

class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ('id', 'product', 'quantity', 'product_total')
