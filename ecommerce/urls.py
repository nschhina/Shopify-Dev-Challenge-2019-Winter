
from django.contrib import admin
from django.urls import path, include
from .views import ListShoppingCartView

urlpatterns = [
    path('shop/', ListShoppingCartView.as_view(), name= "shopcart"),
]
