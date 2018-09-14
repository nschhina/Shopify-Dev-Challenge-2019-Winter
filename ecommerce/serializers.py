from rest_framework import serializers
from .models import Shop


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("pname","qty","rate")
