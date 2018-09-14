# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Order,LineItem
from .serializers import OrderSerializer

class ListOrderView(generics.ListAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
