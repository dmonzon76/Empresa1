# apps/products/urls_api.py

from django.urls import path
from .views_api import (
    ProductListAPI,
    ProductDetailAPI,
    ProductCreateAPI,
    ProductUpdateAPI,
    ProductDeleteAPI,
)

app_name = "products_api"

urlpatterns = [
    path("", ProductListAPI.as_view(), name="list"),
    path("<int:id>/", ProductDetailAPI.as_view(), name="detail"),
    path("create/", ProductCreateAPI.as_view(), name="create"),
    path("<int:id>/update/", ProductUpdateAPI.as_view(), name="update"),
    path("<int:id>/delete/", ProductDeleteAPI.as_view(), name="delete"),
]