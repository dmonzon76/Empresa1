from django.urls import path
from .views_api import (
    CustomerListAPI,
    CustomerDetailAPI,
    CustomerCreateAPI,
    CustomerUpdateAPI,
    CustomerDeleteAPI,
)

app_name = "customers_api"

urlpatterns = [
    path("", CustomerListAPI.as_view(), name="list"),
    path("<int:id>/", CustomerDetailAPI.as_view(), name="detail"),
    path("create/", CustomerCreateAPI.as_view(), name="create"),
    path("<int:id>/update/", CustomerUpdateAPI.as_view(), name="update"),
    path("<int:id>/delete/", CustomerDeleteAPI.as_view(), name="delete"),
]