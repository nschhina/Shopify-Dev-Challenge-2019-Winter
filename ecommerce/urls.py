
from django.contrib import admin
from django.urls import path, include
from .views import ListShoppingCartAView,ListShoppingCartBView

urlpatterns = [
    path('shopA/', ListShoppingCartAView.as_view(), name= "shopAcart"),
    path('shopB/', ListShoppingCartBView.as_view(), name= "shopBcart")
]
