from rest_framework import serializers
from ..models import Customer

class CustomerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name"]

class CustomerSerializer(serializers.ModelSerializer):
    category_detail = CustomerCategorySerializer(source="category", read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "category",
            "category_detail",
            "customer_number",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["customer_number", "created_at", "updated_at"]