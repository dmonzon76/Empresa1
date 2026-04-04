from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from ..models import Address

class AddressListView(ListView):
    model = Address
    template_name = "addresses/address_list.html"
    context_object_name = "object_list"
    ordering = ["-id"]

class AddressDetailView(DetailView):
    model = Address
    template_name = "addresses/address_detail.html"
    context_object_name = "address"

class AddressCreateView(CreateView):
    model = Address
    fields = ["street", "city", "state", "country", "postal_code", "notes"]
    template_name = "addresses/address_form.html"
    success_url = reverse_lazy("addresses:address_list")

class AddressUpdateView(UpdateView):
    model = Address
    fields = ["street", "city", "state", "country", "postal_code", "notes"]
    template_name = "addresses/address_form.html"
    success_url = reverse_lazy("addresses:address_list")

class AddressDeleteView(DeleteView):
    model = Address
    template_name = "addresses/address_confirm_delete.html"
    success_url = reverse_lazy("addresses:address_list")
