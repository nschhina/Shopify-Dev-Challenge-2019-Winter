
from django.contrib import admin
from django.urls import path, include
from .views import ListShoppingCartView

urlpatterns = [
    path('cart/', ListShoppingCartView.as_view(), name="cartview")
]
