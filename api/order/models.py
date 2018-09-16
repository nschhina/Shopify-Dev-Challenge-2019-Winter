from django.db import models
from product.models import Product

# Create your models here.

class Order(models.Model):
    #line_items = models.ManyToManyField(LineItem)
    order_name = models.CharField(max_length=10,unique = True, default = "")
    # def get_order_items(self):
    #     return self.line_items.all()
    #
    # def get_order_total(self):
    #     return sum([item.product.product_price for item in self.items.all()])
    #
    # def __str__(self):
    def __str__(self):
        return '{0}'.format(self.order_name)
