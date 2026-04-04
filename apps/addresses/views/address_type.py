from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from ..models import AddressType
from ..forms.address_type import AddressTypeForm

class AddressTypeListView(ListView):
    model = AddressType
    template_name = "addresses/address_type_list.html"
    context_object_name = "object_list"
    ordering = ["name"]

class AddressTypeCreateView(CreateView):
    model = AddressType
    form_class = AddressTypeForm
    template_name = "addresses/address_type_form.html"
    success_url = reverse_lazy("addresses:type_list")

class AddressTypeUpdateView(UpdateView):
    model = AddressType
    form_class = AddressTypeForm
    template_name = "addresses/address_type_form.html"
    success_url = reverse_lazy("addresses:type_list")

class AddressTypeDeleteView(DeleteView):
    model = AddressType
    template_name = "addresses/address_type_confirm_delete.html"
    success_url = reverse_lazy("addresses:type_list")
