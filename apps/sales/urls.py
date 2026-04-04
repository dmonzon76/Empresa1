from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),

    # ORDERS
    path("orders/", views.SalesOrderListView.as_view(), name="order_list"),
    path("orders/create/", views.SalesOrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/", views.SalesOrderDetailView.as_view(), name="order_detail"),
    path("orders/<int:pk>/edit/", views.SalesOrderUpdateView.as_view(), name="order_edit"),
    path("orders/<int:pk>/confirm/", views.SalesOrderConfirmView.as_view(), name="order_confirm"),

    # ITEMS
    path("orders/<int:pk>/items/add/", views.SalesOrderItemCreateView.as_view(), name="item_add"),
    path("items/<int:pk>/delete/", views.SalesOrderItemDeleteView.as_view(), name="item_delete"),
]
