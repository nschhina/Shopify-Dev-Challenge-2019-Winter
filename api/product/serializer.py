from rest_framework import serializers
from .models import Shop


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("product_name","product_price")
