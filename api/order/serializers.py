from rest_framework import serializers
from .models import Order
from lineitem.serializers import LineItemSerializer
from lineitem.models import LineItem
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    line_items = LineItemSerializer(many=True, source='items')
    class Meta:
        model = Order
        fields = ['order_name', 'line_items', 'cart_total']
    def create(self, request):
        serialized = self.serializer_class(data=request.DATA)
        if serialized.is_valid():
            serialized.save()
            return Response(status=HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, instance, validated_data):
        instance.order_name = validated_data.get("order_name")
        return instance
    def delete(self, instance, validated_data):
        for order in instance.order_name:
            if order == validated_data.get("order_name"):
                snippet = Order.objects.get(order_name=order_name)
                snippet.delete()
                return
