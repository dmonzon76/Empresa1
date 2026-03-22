from django.urls import path
from apps.suppliers.views.views_html import SupplierListView, SupplierDetailView

app_name = "suppliers_html"

urlpatterns = [
    path("", SupplierListView.as_view(), name="list"),
    path("<int:pk>/", SupplierDetailView.as_view(), name="detail"),
]
