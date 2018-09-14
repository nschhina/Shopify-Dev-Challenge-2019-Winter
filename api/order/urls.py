#!/usr/bin/python

from django.contrib import admin
from django.urls import path, include
from .views import ListOrderView

urlpatterns = [
    path('', ListOrderView.as_view(), name= "orderview"),
]
