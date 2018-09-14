from rest_framework import serializers
from .models import LineItem,Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
