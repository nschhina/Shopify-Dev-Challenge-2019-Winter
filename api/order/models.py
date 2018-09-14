from django.db import models
from product.models import Product

# Create your models here.

class LineItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.product.product_name

class Order(models.Model):
    line_items = models.ManyToManyField(LineItem)

    def get_order_items(self):
        return self.line_items.all()

    def get_order_total(self):
        return sum([item.product.product_price for item in self.items.all()])

    def __str__(self):
        return '{0}'.format(self.line_items)
