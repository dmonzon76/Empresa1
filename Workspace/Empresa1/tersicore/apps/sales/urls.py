from django.urls import path
from . import views
from . import api_views

app_name = "sales"

urlpatterns = [
    path("orders/", views.SalesOrderListView.as_view(), name="order_list"),
    path("orders/create/", views.SalesOrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/", views.SalesOrderDetailView.as_view(), name="order_detail"),
    path("orders/<int:pk>/edit/", views.SalesOrderUpdateView.as_view(), name="order_edit"),
    path("orders/<int:pk>/confirm/", views.SalesOrderConfirmView.as_view(), name="order_confirm"),

    # Items
    path("orders/<int:order_id>/items/add/", views.SalesOrderItemCreateView.as_view(), name="item_add"),
    path("items/<int:pk>/delete/", views.SalesOrderItemDeleteView.as_view(), name="item_delete"),
    path("api/kpis/", api_views.sales_kpis, name="api_kpis"),

]
