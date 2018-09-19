from rest_framework import serializers
from .models import Order
from lineitem.serializers import LineItemSerializer
from lineitem.models import LineItem


class OrderSerializer(serializers.ModelSerializer):
    line_items = LineItemSerializer(many=True, source='lineitem_set')
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
        items = validated_data.pop('product')
        #items = validated_data.get('instance.lineitem_set', None)
        for item in items:
            item_name=item.get('product')
            if item_name:
                line_item = LineItem.objects.get(product=product)
                line_item.quantity = item.get('product', line_item.product)
            else:
                pass
            return instance
