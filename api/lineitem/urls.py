#!/usr/bin/python

from django.contrib import admin
from django.urls import path, include
from .views import LineItemList,LineItemDetail
from django.conf.urls import url

urlpatterns = [
    path('', OrderList.as_view(), name= "orderview"),
    url(r'^(?P<order_name>[\w]+)/$', LineItemDetail.as_view(), name='order_details'),
]
