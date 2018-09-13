# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import ShopA,ShopB
from .serializers import ShoppingListSerializerA,ShoppingListSerializerB

# Create your views here


class ListShoppingCartAView(generics.ListAPIView):

    queryset = ShopA.objects.all()
    serializer_class = ShoppingListSerializerA

class ListShoppingCartBView(generics.ListAPIView):

    queryset = ShopB.objects.all()
    serializer_class = ShoppingListSerializerB
