from rest_framework import serializers
from .models import ShopA,ShopB


class ShoppingListSerializerA(serializers.ModelSerializer):
    class Meta:
        model = ShopA
        fields = ("pname","qty","rate")
class ShoppingListSerializerB(serializers.ModelSerializer):
    class Meta:
        model = ShopA
        fields = ("pname","qty","rate")
