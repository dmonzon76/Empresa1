from rest_framework import serializers
from apps.categories.models import CustomerCategory


class CustomerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = [
            "id",
            "name",
            "prefix",
            "sequence",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["sequence", "created_at", "updated_at"]