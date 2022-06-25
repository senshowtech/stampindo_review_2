
# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ProductSerializer, AuthorSerializer, BookSerializer
from .models import Product, Book, Author


class ProductList(APIView):
    def get(self, request, id=None):
        queryset = Product.objects.all()
        read_serializer = ProductSerializer(queryset, many=True)
        return Response(read_serializer.data)


class AuthorList(APIView):
    def get(self, request):
        queryset = Author.objects.all()
        read_serializer = AuthorSerializer(queryset, many=True)
        return Response(read_serializer.data)


class BookList(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        read_serializer = BookSerializer(queryset, many=True)
        return Response(read_serializer.data)
