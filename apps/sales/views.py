# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from apps.sales.models import SalesOrder, SalesOrderItem
from apps.sales.forms import SalesOrderForm, SalesOrderItemForm


# ============================
# LIST OF ORDERS
# ============================
class SalesOrderListView(ListView):
    model = SalesOrder
    template_name = "sales/order_list.html"
    context_object_name = "orders"
    paginate_by = 20


# ============================
# ORDER DETAILS
# ============================
class SalesOrderDetailView(DetailView):
    model = SalesOrder
    template_name = "sales/order_detail.html"
    context_object_name = "order"


# ============================
# CREATE ORDER
# ============================
class SalesOrderCreateView(CreateView):
    model = SalesOrder
    form_class = SalesOrderForm
    template_name = "sales/order_form.html"

    def get_success_url(self):
        return reverse_lazy("sales:order_detail", args=[self.object.id])


# ============================
# EDIT ORDER
# ============================
class SalesOrderUpdateView(UpdateView):
    model = SalesOrder
    form_class = SalesOrderForm
    template_name = "sales/order_form.html"

    def get_success_url(self):
        return reverse_lazy("sales:order_detail", args=[self.object.id])


# ============================
# ADD ITEM TO ORDER
# ============================
class SalesOrderItemCreateView(CreateView):
    model = SalesOrderItem
    form_class = SalesOrderItemForm
    template_name = "sales/item_form.html"

    def form_valid(self, form):
        order = get_object_or_404(SalesOrder, pk=self.kwargs["order_id"])

        # 🔒 Seguridad: solo permitir agregar ítems si la orden está en borrador
        if order.status != SalesOrder.DRAFT:
            return redirect("sales:order_detail", order.id)

        form.instance.order = order
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("sales:order_detail", args=[self.kwargs["order_id"]])


# ============================
# DELETE ITEM
# ============================
class SalesOrderItemDeleteView(DeleteView):
    model = SalesOrderItem
    template_name = "sales/item_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("sales:order_detail", args=[self.object.order.id])

    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()

        # 🔒 Seguridad: solo permitir eliminar ítems si la orden está en borrador
        if item.order.status != SalesOrder.DRAFT:
            return redirect("sales:order_detail", item.order.id)

        return super().dispatch(request, *args, **kwargs)


# ============================
# CONFIRM ORDER
# ============================
class SalesOrderConfirmView(TemplateView):
    template_name = "sales/order_confirm.html"

    def post(self, request, *args, **kwargs):
        order = get_object_or_404(SalesOrder, pk=kwargs["pk"])

        # 🔒 Seguridad: solo confirmar si está en borrador
        if order.status == SalesOrder.DRAFT:
            order.confirm()

        return redirect("sales:order_detail", pk=order.id)