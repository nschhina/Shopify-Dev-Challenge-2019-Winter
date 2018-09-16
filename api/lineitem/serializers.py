from rest_framework import serializers
from .models import LineItem


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = '__all__'
