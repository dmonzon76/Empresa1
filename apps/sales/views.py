from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from apps.sales.models import SalesOrder, SalesOrderItem
from apps.sales.forms import SalesOrderForm, SalesOrderItemForm


# ORDER LIST
class SalesOrderListView(View):
    template_name = "sales/sales_order_list.html"

    def get(self, request):
        orders = SalesOrder.objects.all().order_by("-created_at")
        return render(request, self.template_name, {"orders": orders})


# ORDER DETAILS
class SalesOrderDetailView(View):
    template_name = "sales/sales_order_detail.html"

    def get(self, request, pk):
        order = get_object_or_404(SalesOrder, pk=pk)
        return render(request, self.template_name, {"order": order})


# CREATE ORDER
class SalesOrderCreateView(View):
    template_name = "sales/sales_order_form.html"

    def get(self, request):
        form = SalesOrderForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect("sales:order_detail", order.id)
        return render(request, self.template_name, {"form": form})


# EDIT ORDER
class SalesOrderUpdateView(View):
    template_name = "sales/sales_order_form.html"

    def get(self, request, pk):
        order = get_object_or_404(SalesOrder, pk=pk)
        form = SalesOrderForm(instance=order)
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        order = get_object_or_404(SalesOrder, pk=pk)
        form = SalesOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("sales:order_detail", order.id)
        return render(request, self.template_name, {"form": form})


# CONFIRM ORDER
class SalesOrderConfirmView(View):
    template_name = "sales/sales_order_confirm.html"

    def get(self, request, pk):
        return render(request, self.template_name, {"pk": pk})

    def post(self, request, pk):
        order = get_object_or_404(SalesOrder, pk=pk)
        order.status = "CONFIRMED"
        order.save()
        return redirect("sales:order_detail", order.id)


# ADD ITEM
class SalesOrderItemCreateView(View):
    template_name = "sales/sales_item_form.html"

    def get(self, request, pk):
        form = SalesOrderItemForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, pk):
        order = get_object_or_404(SalesOrder, pk=pk)
        form = SalesOrderItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.order = order
            item.save()
            return redirect("sales:order_detail", order.id)
        return render(request, self.template_name, {"form": form})


# DELETE ITEM
class SalesOrderItemDeleteView(View):
    template_name = "sales/item_confirm_delete.html"

    def get(self, request, pk):
        item = get_object_or_404(SalesOrderItem, pk=pk)
        return render(request, self.template_name, {"item": item})

    def post(self, request, pk):
        item = get_object_or_404(SalesOrderItem, pk=pk)
        order_id = item.order.id
        item.delete()
        return redirect("sales:order_detail", order_id)


# DASHBOARD
def dashboard(request):
    return render(request, "placeholders/module_placeholder.html", {
        "module_name": "Sales",
        "description": "Orders, quotations, and customer transactions."
    })
