from django.db import models
from product.models import Product

# Create your models here.

class Order(models.Model):
    order_name = models.CharField(max_length=10,unique = True, default = "")
    def get_order_total(self):
        return sum([item.total for item in self.lineitem_set.all()])
    cart_total = property(get_order_total)
    # def __str__(self):
    def __str__(self):
        return '{} - {}'.format(self.order_name,self.cart_total)
