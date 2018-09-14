#!/usr/bin/python

from django.contrib import admin
from django.urls import path, include
from .views import ListProductView

urlpatterns = [
    path('', ListProductView.as_view(), name= "productview"),
]
