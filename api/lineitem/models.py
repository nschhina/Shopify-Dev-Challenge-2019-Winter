from django.db import models
from product.models import Product
from order.models import Order

# Create your models here.

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, related_name="prod")
    quantity = models.IntegerField(default = 0)
    def product_total(self):
        return self.quantity * self.product.product_price
    total = property(product_total)
    # def return_set(product_name):
    #     return self.product.filter(product_name=product_name)


    class Meta:
        unique_together= ('order','product')
    def __str__(self):
        return '{} - {} - {} - CAD {}'.format(self.order.order_name,self.product.product_name, self.quantity , self.total)

    # def get_object(order_name):
    #     try:
    #         return Order.objects.get(order_name=order_name).lineall()
    #     except Order.DoesNotExist:
    #         raise Http404
    # def get_product(product_name):
    #     try:
    #         return Product.objects.get(produc_name=product_name).lineall()
    #     except Order.DoesNotExist:
    #         raise Http404
