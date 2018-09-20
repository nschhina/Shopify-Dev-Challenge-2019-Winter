#!/usr/bin/python

from django.contrib import admin
from django.urls import path, include
from .views import ProductList,ProductDetail
from django.conf.urls import url

urlpatterns = [
    path('', ProductList.as_view(), name= "productview"),
    url(r'^(?P<product_name>[\w]+)/$', ProductDetail.as_view(), name='prodview'),
]
