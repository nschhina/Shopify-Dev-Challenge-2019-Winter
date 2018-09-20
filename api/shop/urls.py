#!/usr/bin/python

from django.contrib import admin
from django.urls import path, include
from .views import login
from django.conf.urls import url

urlpatterns = [
    path('products/', include('product.urls')),
    path('login/', login),
    path('orders/', include('order.urls')),
    path('lineitem/', include('lineitem.urls')),
]
