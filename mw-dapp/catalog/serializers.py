from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import CategoryModel, ProductModel, ProductImageModel


class CategoryRecursiveSerializer(serializers.ModelSerializer):
    """MPTT категории с потомками"""

    name = serializers.CharField()
    inserted = serializers.ListField(child=RecursiveField(), source='get_children')

    class Meta:
        model = CategoryModel
        fields = ('id','name', 'level', 'inserted',)


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImageModel
        fields = ('id', 'image', )


class ProductSerializer(serializers.ModelSerializer):
    """ Продукты """

    images = ProductImageSerializer(many=True)

    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'category', 'preview', 'description', 'category', 'images')