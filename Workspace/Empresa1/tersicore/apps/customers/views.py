from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Customer
from .forms import CustomerForm
from .serializers.customer_serializer import CustomerSerializer, CustomerCategorySerializer

class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customers:list")

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"
    context_object_name = "customer"


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customers:list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Edit Customer"
        return data


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "customers/customer_confirm_delete.html"
    context_object_name = "customer"
    success_url = reverse_lazy("customers:list")


# API ViewSets
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerCategoryViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerCategorySerializer