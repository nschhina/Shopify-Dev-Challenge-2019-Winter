# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Model for Product
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()

    def __str__(self):
        return self.name

# Model for Shops
class Shop(models.Model):
    # Product Name
    pname = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    # Quantity
    qty = models.IntegerField(default=0)
    # Price of Item in Dollars
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    # Total Price of Item in Dollars
    def __str__(self):
        return self.pname.name

# Model for Order
class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    items = models.ManyToManyField(Shop)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.pname.rate for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.items, self.ref_code)
