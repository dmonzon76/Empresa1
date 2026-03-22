# inventory/urls.py
from django.urls import path
from .views import (
    InventoryListView,
    InventoryDetailView,
    InventoryMovementCreateView,
)
from . import api_views

app_name = "inventory"

urlpatterns = [
    path("", InventoryListView.as_view(), name="stock_list"),
    path("<int:pk>/", InventoryDetailView.as_view(), name="stock_detail"),
    path("movement/add/", InventoryMovementCreateView.as_view(), name="movement_add"),

    # API
    path("api/kpis/", api_views.inventory_kpis, name="api_kpis"),
    path("api/chart/monthly/", api_views.inventory_monthly_chart, name="api_monthly_chart"),
]