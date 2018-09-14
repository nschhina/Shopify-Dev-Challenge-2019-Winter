# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Shop
from .serializers import ShoppingListSerializer

# Create your views here


class ListShoppingCartView(generics.ListAPIView):

    queryset = Shop.objects.all()
    serializer_class = ShoppingListSerializer
