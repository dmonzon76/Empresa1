from rest_framework import serializers


class DashboardKpiSerializer(serializers.Serializer):
    total_sales = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_purchases = serializers.DecimalField(max_digits=12, decimal_places=2)
    stock_value = serializers.DecimalField(max_digits=12, decimal_places=2)
