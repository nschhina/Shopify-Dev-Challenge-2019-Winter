#!/usr/bin/python

from django.contrib import admin
from django.urls import path, include
from .views import ProductList

urlpatterns = [
    path('', ProductList.as_view(), name= "productview"),
]
