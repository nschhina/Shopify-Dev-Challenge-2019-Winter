# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Model for Shopping Cart
class ShoppingList(models.Model):
    # Product ID
    pid = models.CharField(max_length=255, null=False)
    # Product Name
    pname = models.CharField(max_length=255, null=False)
    # Quantity
    qty = models.IntegerField(default=0)
    # Price of Item in Dollars
    price = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.pid, self.pname, self.qty, self.price)
