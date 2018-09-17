from rest_framework import serializers
from .models import LineItem
from product.serializers import ProductSerializer
from order.serializers import OrderSerializer


class LineItemSerializer(serializers.ModelSerializer):
    productname = ProductSerializer(many=True, read_only=True)
    ordername = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = LineItem
        fields = ['productname','ordername']
