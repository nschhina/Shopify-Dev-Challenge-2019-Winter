from django.db import models
from product.models import Product
from order.models import Order

# Create your models here.

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together= ('order','product')
    def __str__(self):
        return self.product.product_name

    def get_object(order_name):
        try:
            return LineItem.objects.filter(order_name=order_name)
        except Order.DoesNotExist:
            raise Http404
