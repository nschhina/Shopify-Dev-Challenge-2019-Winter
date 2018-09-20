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
    def put(self, request):
        snippet = LineItem.objects.all()
        serializer = LineItemSerializer(snippet, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, order_name):
        snippet = self.get_object(order_name)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
