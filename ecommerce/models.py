# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Model for Shops
class ShopA(models.Model):
    # Product Name
    pname = models.CharField(max_length=255, null=False)
    # Quantity
    qty = models.IntegerField(default=0)
    # Price of Item in Dollars
    rate = models.IntegerField(default=0)
    # Total Price of Item in Dollars
    price = {% widthratio A 1 B %}
    def __str__(self):
        return "{} - {} - {} - {}".format(self.pname, self.qty, self.rate, self.price)

class ShopB(models.Model):
    # Product Name
    pname = models.CharField(max_length=255, null=False)
    # Quantity
    qty = models.IntegerField(default=0)
    # Price of Item in Dollars
    rate = models.IntegerField(default=0)
    # Total Price of Item in Dollars
    def getPrice(qty,rate):
        return qty*rate

    def __str__(self):
        return "{} - {} - {} - {}".format(self.pname, self.qty, self.rate, self.getPrice(self.rate,self.qty))
