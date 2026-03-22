from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from .models import Customer
from .serializers.customer_serializer import CustomerSerializer


class CustomerListAPI(ListAPIView):
    queryset = Customer.objects.all().order_by("id")
    serializer_class = CustomerSerializer


class CustomerDetailAPI(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = "id"


class CustomerCreateAPI(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateAPI(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = "id"


class CustomerDeleteAPI(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = "id"