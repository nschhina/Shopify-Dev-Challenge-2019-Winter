# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from lineitem.models import LineItem
from .serializers import OrderSerializer
from rest_framework.views import APIView

class OrderList(APIView):
    def get(self,request):
        orderlist = Order.objects.all()
        serializer = OrderSerializer(orderlist,many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):

    def get_object(self, order):
        try:
            return Order.objects.get(order_name=order_name)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, order_name):
        snippet = Order.objects.get(order_name=order_name)
        snippet=snippet.lineitem_set.all()
        serializer = OrderSerializer(snippet)
        return Response(serializer.data)

    # def put(self, request, order_name):
    #     snippet = self.get_object(order_name)
    #     serializer = OrderSerializer(snippet, data=request.data, partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, order_name):
    #     snippet = self.get_object(order_name)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
