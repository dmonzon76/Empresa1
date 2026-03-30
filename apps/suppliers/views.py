from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Supplier
from .forms import SupplierForm


class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers/suppliers_list.html"
    context_object_name = "suppliers"


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "suppliers/suppliers_detail.html"
    context_object_name = "supplier"


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/suppliers_form.html"
    success_url = reverse_lazy("suppliers:list")


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/suppliers_form.html"
    success_url = reverse_lazy("suppliers:list")


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "suppliers/suppliers_confirm_delete.html"
    context_object_name = "supplier"
    success_url = reverse_lazy("suppliers:list")
