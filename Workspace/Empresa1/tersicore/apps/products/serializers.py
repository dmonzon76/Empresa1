from rest_framework import serializers
from .models import Product
from apps.categories.models import ProductCategory
from apps.categories.serializers.product_category_serializer import ProductCategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(),
        source="category",
        write_only=True
    )

    class Meta:
        model = Product
        fields = "__all__"
        