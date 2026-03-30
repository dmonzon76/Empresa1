from django.urls import path
from .views import (
    PurchaseOrderListView,
    PurchaseOrderDetailView,
    PurchaseOrderDeleteView,
)

app_name = "purchases"

urlpatterns = [
    path("purchase-orders/", PurchaseOrderListView.as_view(), name="list"),
    path("purchase-orders/<int:pk>/", PurchaseOrderDetailView.as_view(), name="detail"),
    path("purchase-orders/<int:pk>/delete/", PurchaseOrderDeleteView.as_view(), name="delete"),
]
