from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer
from .forms import CustomerForm
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect

from apps.addresses.forms.assignment import AddressAssignmentFormSet
from apps.addresses.models import AddressAssignment
from django.contrib.contenttypes.models import ContentType
from django.views.generic import UpdateView


class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"

    def get_queryset(self):
        return (
            Customer.objects.all()
            .prefetch_related(
                "address_assignments__address",
                "address_assignments__address_type",
            )
        )




class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customers:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Si es GET → formset vacío
        if self.request.method == "GET":
            context["formset"] = AddressAssignmentFormSet()
        else:
            # Si es POST → formset con datos enviados
            context["formset"] = AddressAssignmentFormSet(self.request.POST)

        return context

    def form_valid(self, form):
        """
        1. Guarda el Customer
        2. Procesa el formset
        3. Asigna content_type y object_id
        4. Guarda las direcciones
        """
        response = super().form_valid(form)

        formset = AddressAssignmentFormSet(self.request.POST)

        if formset.is_valid():
            for f in formset:
                if f.cleaned_data and not f.cleaned_data.get("DELETE"):
                    assignment = f.save(commit=False)
                    assignment.content_type = ContentType.objects.get_for_model(Customer)
                    assignment.object_id = self.object.id
                    assignment.save()

        return response


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
        context = super().get_context_data(**kwargs)
        customer = self.object

        if self.request.method == "POST":
            context["formset"] = AddressAssignmentFormSet(self.request.POST)
        else:
            # Cargar datos iniciales del formset
            initial_data = [
                {
                    "address_type": a.address_type,
                    "address": a.address,
                    "is_primary": a.is_primary,
                    "DELETE": False,
                }
                for a in customer.address_assignments.all()
            ]
            context["formset"] = AddressAssignmentFormSet(initial=initial_data)

        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        customer = self.object
        formset = AddressAssignmentFormSet(self.request.POST)

        if formset.is_valid():
            # Borrar asignaciones anteriores
            customer.address_assignments.all().delete()

            # Crear nuevas asignaciones
            for f in formset:
                if f.cleaned_data and not f.cleaned_data.get("DELETE"):
                    assignment = f.save(commit=False)
                    assignment.content_type = ContentType.objects.get_for_model(Customer)
                    assignment.object_id = customer.id
                    assignment.save()

        return response




class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "customers/customer_confirm_delete.html"
    context_object_name = "customer"
    success_url = reverse_lazy("customers:list")


