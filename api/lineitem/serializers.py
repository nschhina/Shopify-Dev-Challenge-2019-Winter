from rest_framework import serializers
from .models import LineItem
from order.models import Order
from product.serializers import ProductSerializer

class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        depth =1
        fields = ('product', 'quantity', 'product_total')
    # def create(self, validated_data):
    #     list = LineItem.objects.create(**validated_data)
    #     return list
    def update(self, instance, validated_data):
        for orders in instance.order:
            if orders.order_name == validated_data.get("product_name"):
                pass
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
