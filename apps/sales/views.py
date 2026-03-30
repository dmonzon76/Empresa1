from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from apps.sales.models import SalesOrder


class SalesOrderListView(View):
    template_name = "sales/sales_list.html"

    def get(self, request):
        orders = SalesOrder.objects.all().order_by("-created_at")
        return render(request, self.template_name, {"orders": orders})


class SalesOrderDetailView(View):
    template_name = "sales/sales_detail.html"

    def get(self, request, pk):
        order = get_object_or_404(SalesOrder, pk=pk)
        return render(request, self.template_name, {"order": order})
