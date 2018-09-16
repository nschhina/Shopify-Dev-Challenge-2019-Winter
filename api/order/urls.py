#!/usr/bin/python

from django.contrib import admin
from django.urls import path, include
from .views import OrderList,OrderDetail
from django.conf.urls import url

urlpatterns = [
    path('', OrderList.as_view(), name= "orderview"),
    url(r'^(?P<order_name>[\w]+)/$', OrderDetail.as_view(), name='order_details'),
]
