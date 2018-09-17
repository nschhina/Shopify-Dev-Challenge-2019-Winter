# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import LineItem
from order.models import Order
from .serializers import LineItemSerializer
from rest_framework.views import APIView

class LineItemList(APIView):
    def get(self,request):
        lineitemlist = LineItem.objects.all()
        serializer = LineItemSerializer(lineitemlist,many = True)
        return Response(serializer.data)
#     def post(self, request):
#         serializer = LineItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class LineItemDetail(APIView):
#     def get_object(self, order_name):
#         try:
#             return LineItem.objects.get(order_name=order_name)
#         except LineItem.DoesNotExist:
#             raise Http404
#
#     def get(self, request, order_name):
#         snippet = LineItem.get_object(order_name)
#         serializer = LineItemSerializer(snippet)
#         return Response(serializer.data)
#     #
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
