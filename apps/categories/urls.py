# apps/categories/urls.py

from django.urls import path
from .views import (
    CustomerCategoryListView,
    CustomerCategoryCreateView,
    CustomerCategoryUpdateView,
    CustomerCategoryDeleteView,
    ProductCategoryListView,
    ProductCategoryCreateView,
    ProductCategoryUpdateView,
    ProductCategoryDeleteView,
)

app_name = "categories"

urlpatterns = [
    # Customer categories
    path("customers/", CustomerCategoryListView.as_view(), name="customers_list"),
    path("customers/create/", CustomerCategoryCreateView.as_view(), name="customers_create"),
    path("customers/<int:pk>/update/", CustomerCategoryUpdateView.as_view(), name="customers_update"),
    path("customers/<int:pk>/delete/", CustomerCategoryDeleteView.as_view(), name="customers_delete"),

    # Product categories
    path("products/", ProductCategoryListView.as_view(), name="products_list"),
    path("products/create/", ProductCategoryCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/update/", ProductCategoryUpdateView.as_view(), name="products_update"),
    path("products/<int:pk>/delete/", ProductCategoryDeleteView.as_view(), name="products_delete"),
]
