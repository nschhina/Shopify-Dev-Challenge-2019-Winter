#!/usr/bin/python

from django.contrib import admin
from django.urls import path, include
from .views import LineItemList
from django.conf.urls import url

urlpatterns = [
    path('', LineItemList.as_view(), name= "lineitemview"),
]
