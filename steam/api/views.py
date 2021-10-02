from rest_framework.response import Response
from rest_framework import viewsets
from mainpage.models import Product
from .serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer