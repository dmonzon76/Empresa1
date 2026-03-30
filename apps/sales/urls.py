from django.urls import path
from .views import (
    SalesOrderListView,
    SalesOrderDetailView,
)

app_name = "sales"

urlpatterns = [
    path("orders/", SalesOrderListView.as_view(), name="list"),
    path("orders/<int:pk>/", SalesOrderDetailView.as_view(), name="detail"),
]

