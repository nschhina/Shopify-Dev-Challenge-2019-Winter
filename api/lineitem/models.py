from django.db import models
from product.models import Product
from order.models import Order

# Create your models here.

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default = 0)
    def product_total(self):
        return self.quantity * self.product.product_price
    total = property(product_total)

    class Meta:
        unique_together= ('order','product')
    def __str__(self):
        return '{} - {}'.format(self.order.order_name,self.product.product_name)

    def get_object(order_name):
        try:
            return Order.objects.get(order_name=order_name).lineall()
        except Order.DoesNotExist:
            raise Http404
