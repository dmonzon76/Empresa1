from django.urls import path
from .views import (
    InventoryListView,
    InventoryDetailView,
    InventoryMovementCreateView,
)

app_name = "inventory"

urlpatterns = [
    path("stock/", InventoryListView.as_view(), name="stock_list"),
    path("stock/<int:pk>/", InventoryDetailView.as_view(), name="stock_detail"),
    path("movement/new/", InventoryMovementCreateView.as_view(), name="movement_create"),
]
