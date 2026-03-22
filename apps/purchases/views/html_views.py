from apps.purchases.models import PurchaseOrder
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View


class PurchaseOrderListView(View):
    template_name = "purchases/purchases_list.html"

    def get(self, request):
        purchase_orders = PurchaseOrder.objects.all().order_by("-created_at")
        return render(request, self.template_name, {"purchase_orders": purchase_orders})


class PurchaseOrderDetailView(View):
    template_name = "purchases/purchases_detail.html"

    def get(self, request, pk):
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
        return render(request, self.template_name, {"purchase_order": purchase_order})
