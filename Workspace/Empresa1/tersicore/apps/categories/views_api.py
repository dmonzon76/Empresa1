from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from .models import CustomerCategory
from .serializers.category_serializer import CustomerCategorySerializer


class CustomerCategoryListAPI(ListAPIView):
    queryset = CustomerCategory.objects.all().order_by("id")
    serializer_class = CustomerCategorySerializer


class CustomerCategoryDetailAPI(RetrieveAPIView):
    queryset = CustomerCategory.objects.all()
    serializer_class = CustomerCategorySerializer
    lookup_field = "id"


class CustomerCategoryCreateAPI(CreateAPIView):
    queryset = CustomerCategory.objects.all()
    serializer_class = CustomerCategorySerializer


class CustomerCategoryUpdateAPI(UpdateAPIView):
    queryset = CustomerCategory.objects.all()
    serializer_class = CustomerCategorySerializer
    lookup_field = "id"


class CustomerCategoryDeleteAPI(DestroyAPIView):
    queryset = CustomerCategory.objects.all()
    serializer_class = CustomerCategorySerializer
    lookup_field = "id"