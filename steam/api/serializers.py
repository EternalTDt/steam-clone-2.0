from rest_framework import serializers
from mainpage.models import Product, Category, Company


class ProductCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    category = ProductCategorySerializer()
    company = ProductCompanySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'
