from django.urls import path
from . import views
from .views import (
    SupplierListView, SupplierDetailView, SupplierCreateView,   SupplierUpdateView, SupplierDeleteView)


app_name = "suppliers"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", SupplierListView.as_view(), name="list"),
    path("create/", SupplierCreateView.as_view(), name="create"),
    path("<int:pk>/", SupplierDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", SupplierUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", SupplierDeleteView.as_view(), name="delete"),
]
