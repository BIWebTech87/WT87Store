from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from products.models import Product
from products.serializaers import ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get(self):
        return self.queryset

