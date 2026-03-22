from django.urls import path
from apps.purchases.views.html_views import (
    PurchaseOrderListView,
    PurchaseOrderDetailView,
)

app_name = "purchases_html"

urlpatterns = [
    path("purchase-orders/", PurchaseOrderListView.as_view(), name="list"),
    path("purchase-orders/<int:pk>/",
         PurchaseOrderDetailView.as_view(), name="detail"),
]
