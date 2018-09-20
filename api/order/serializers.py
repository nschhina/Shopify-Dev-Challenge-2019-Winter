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
    # def create(self, validated_data):
    #     list = LineItem.objects.create(**validated_data)
    #     return list
    def update(self, instance, validated_data):
        #listitems = instance.items.product.get(product_name = validated_data.get("product_name"))
        # items = instance.items.return_set(validated_data.get("product_name"))

        # items = instance.objects.items.all().select_related('product').select_related('product_name')
        # items = items.product_name
        # instance.save()
        #a = items.get('product_name'= validated_data.get("product_name")

        #asper= key.get(product_name=validated_data.get("product_name"))

        # items.product.get(produc_name=validated_data.get("product_name")
        # for prod in items.product.all():
        #     if prod.product_name==validated_data.get("product_name"):
        #         prod.quantity = validated_data.get("quantity")
        #         prod.save()
        return instance
