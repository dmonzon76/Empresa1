# apps/inventory/views.py
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import InventoryItem, InventoryMovement
from .inventory_forms import InventoryMovementForm


class InventoryListView(ListView):
    model = InventoryItem
    template_name = "inventory/stock_list.html"
    context_object_name = "items"
    paginate_by = 20


class InventoryDetailView(DetailView):
    model = InventoryItem
    template_name = "inventory/stock_detail.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movements"] = InventoryMovement.objects.filter(
            product=self.object.product
        ).order_by("-date")
        return context


class InventoryMovementCreateView(CreateView):
    model = InventoryMovement
    form_class = InventoryMovementForm
    template_name = "inventory/movement_form.html"

    def form_valid(self, form):
        movement = form.save()
        movement.apply()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "inventory:stock_detail",
            args=[self.object.product.inventoryitem.id]
        )
from django.shortcuts import render

def dashboard(request):
    return render(request, "placeholders/module_placeholder.html", {
        "module_name": "Inventory",
        "description": "Stock levels, warehouses, and product tracking."
    })
