from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoryModel, ProductModel
from .serializers import CategoryRecursiveSerializer, ProductSerializer



class CategoryView(APIView):
    """ Категории """

    def get(self, request, ct=None):
        if ct:
            categories = CategoryModel.objects.filter(parent__id=ct).filter(activated=True)
            serializer = CategoryRecursiveSerializer(categories, many=True, context={'request': request})
        else:
            categories = CategoryModel.objects.filter(level=0).filter(activated=True)
            serializer = CategoryRecursiveSerializer(categories, many=True, context={'request': request})

        return Response(serializer.data)
        


class ProductsView(APIView):
    """ Продукты """

    def get(self, request, ct):
        products = ProductModel.objects.filter(activated=True).filter(category__id__in=CategoryModel.objects.get(id=ct).get_descendants(include_self=True))
        serializer = ProductSerializer(products, many=True, context={'request': request})

        return Response(serializer.data)



class ProductView(APIView):
    """ Продукт """

    def get(self, request, id):
        product = ProductModel.objects.get(id=id)
        serializer = ProductSerializer(product, context={'request': request})

        return Response(serializer.data)