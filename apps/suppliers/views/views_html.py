from django.views.generic import ListView, DetailView
from apps.suppliers.models import Supplier


class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers/suppliers_list.html"
    context_object_name = "suppliers"


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "suppliers/suppliers_detail.html"
    context_object_name = "supplier"
