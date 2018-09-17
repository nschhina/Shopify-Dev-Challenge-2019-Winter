from rest_framework import serializers
from .models import Order
from lineitem.serializers import LineItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    line_items = LineItemSerializer(many=True, source='lineitem_set')
    class Meta:
        model = Order
        fields = ['order_name', 'line_items']
