from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.contenttypes.models import ContentType

from .models import Supplier
from .forms import SupplierForm

from apps.addresses.forms.assignment import AddressAssignmentFormSet
from apps.addresses.models import AddressAssignment


# ---------------------------------------------------------
# LIST VIEW — Optimizada con prefetch para domicilios
# ---------------------------------------------------------
class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers/suppliers_list.html"
    context_object_name = "suppliers"

    def get_queryset(self):
        return (
            Supplier.objects.all()
            .prefetch_related(
                "address_assignments__address",
                "address_assignments__address_type",
            )
        )


# ---------------------------------------------------------
# DETAIL VIEW
# ---------------------------------------------------------
class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "suppliers/suppliers_detail.html"
    context_object_name = "supplier"

    def get_queryset(self):
        return (
            Supplier.objects.all()
            .prefetch_related(
                "address_assignments__address",
                "address_assignments__address_type",
            )
        )



# ---------------------------------------------------------
# CREATE VIEW — Con formset de direcciones
# ---------------------------------------------------------
class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/suppliers_form.html"
    success_url = reverse_lazy("suppliers:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.method == "GET":
            context["formset"] = AddressAssignmentFormSet()
        else:
            context["formset"] = AddressAssignmentFormSet(self.request.POST)

        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        formset = AddressAssignmentFormSet(self.request.POST)

        if formset.is_valid():
            for f in formset:
                if f.cleaned_data and not f.cleaned_data.get("DELETE"):
                    assignment = f.save(commit=False)
                    assignment.content_type = ContentType.objects.get_for_model(Supplier)
                    assignment.object_id = self.object.id
                    assignment.save()

        return response


# ---------------------------------------------------------
# UPDATE VIEW — Con formset de direcciones
# ---------------------------------------------------------
class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/suppliers_form.html"
    success_url = reverse_lazy("suppliers:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        supplier = self.object

        if self.request.method == "POST":
            context["formset"] = AddressAssignmentFormSet(self.request.POST)
        else:
            initial_data = [
                {
                    "address_type": a.address_type,
                    "address": a.address,
                    "is_primary": a.is_primary,
                    "DELETE": False,
                }
                for a in supplier.address_assignments.all()
            ]
            context["formset"] = AddressAssignmentFormSet(initial=initial_data)

        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        supplier = self.object
        formset = AddressAssignmentFormSet(self.request.POST)

        if formset.is_valid():
            supplier.address_assignments.all().delete()

            for f in formset:
                if f.cleaned_data and not f.cleaned_data.get("DELETE"):
                    assignment = f.save(commit=False)
                    assignment.content_type = ContentType.objects.get_for_model(Supplier)
                    assignment.object_id = supplier.id
                    assignment.save()

        return response


# ---------------------------------------------------------
# DELETE VIEW
# ---------------------------------------------------------
class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "suppliers/suppliers_confirm_delete.html"
    context_object_name = "supplier"
    success_url = reverse_lazy("suppliers:list")


# ---------------------------------------------------------
# DASHBOARD PLACEHOLDER
# ---------------------------------------------------------
def dashboard(request):
    return render(request, "placeholders/module_placeholder.html", {
        "module_name": "Suppliers",
        "description": "Vendor management, contracts, and purchasing."
    })
