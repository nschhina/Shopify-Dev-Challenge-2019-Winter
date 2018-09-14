#!/usr/bin/python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('products/', include('product.urls'))
]
