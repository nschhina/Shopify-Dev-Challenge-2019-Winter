# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView

class ProductList(APIView):
    def get(self,request):
        prodlist = Product.objects.all()
        serializer = ProductSerializer(prodlist,many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, product_name):
        try:
            return Product.objects.get(product_name=product_name)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_name):
        snippet = self.get_object(product_name)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, product_name):
        snippet = self.get_object(product_name)
        serializer = ProductSerializer(snippet, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_name):
        snippet = self.get_object(product_name)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
