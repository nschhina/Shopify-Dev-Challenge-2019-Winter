from django.db import models
from product.models import Product

# Create your models here.

class Order(models.Model):
    order_name = models.CharField(max_length=10,unique = True, default = "")
    def get_order_total(self):
        try:
            return sum([item.total for item in self.items.all()])
        except:
            return 0

    cart_total = property(get_order_total)
    def __str__(self):
        return '{} - CAD {}'.format(self.order_name,self.cart_total)
