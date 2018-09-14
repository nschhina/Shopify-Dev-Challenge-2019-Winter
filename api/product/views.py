# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ListProductiew(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
