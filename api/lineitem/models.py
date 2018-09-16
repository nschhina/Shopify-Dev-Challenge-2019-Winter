from django.db import models
from product.models import Product
from order.models import Order

# Create your models here.

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.product.product_name
