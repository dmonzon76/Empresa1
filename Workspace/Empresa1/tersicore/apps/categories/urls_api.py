# apps/categories/urls_api.py

from django.urls import path
from .views_api import (
    CustomerCategoryListAPI,
    CustomerCategoryDetailAPI,
    CustomerCategoryCreateAPI,
    CustomerCategoryUpdateAPI,
    CustomerCategoryDeleteAPI,
)

app_name = "categories_api"

urlpatterns = [
    path("", CustomerCategoryListAPI.as_view(), name="list"),
    path("<int:id>/", CustomerCategoryDetailAPI.as_view(), name="detail"),
    path("create/", CustomerCategoryCreateAPI.as_view(), name="create"),
    path("<int:id>/update/", CustomerCategoryUpdateAPI.as_view(), name="update"),
    path("<int:id>/delete/", CustomerCategoryDeleteAPI.as_view(), name="delete"),
]