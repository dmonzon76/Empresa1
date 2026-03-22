from rest_framework import serializers
from apps.categories.models import CustomerCategory


class CustomerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = "__all__"