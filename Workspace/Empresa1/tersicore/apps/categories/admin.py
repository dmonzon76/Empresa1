# categories/admin.py

from django.contrib import admin
from .models import CustomerCategory, ProductCategory

@admin.register(CustomerCategory)
class CustomerCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "prefix", "sequence", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "prefix")
    readonly_fields = ("sequence", "created_at", "updated_at")


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "is_active", "created_at")
    list_filter = ("is_active", "parent")
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")