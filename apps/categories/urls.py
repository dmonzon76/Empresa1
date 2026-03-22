# categories/urls.py

from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    # Customer Categories
    path("customers/", views.CustomerCategoryListView.as_view(), name="customers_list"),
    path("customers/create/", views.CustomerCategoryCreateView.as_view(), name="customers_create"),
    path("customers/<int:pk>/edit/", views.CustomerCategoryUpdateView.as_view(), name="customers_edit"),
    path("customers/<int:pk>/delete/", views.CustomerCategoryDeleteView.as_view(), name="customers_delete"),

    # Product Categories
    path("products/", views.ProductCategoryListView.as_view(), name="products_list"),
    path("products/create/", views.ProductCategoryCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/edit/", views.ProductCategoryUpdateView.as_view(), name="products_edit"),
    path("products/<int:pk>/delete/", views.ProductCategoryDeleteView.as_view(), name="products_delete"),
]