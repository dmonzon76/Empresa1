from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "stock", "pvp", "is_inventoried")
    list_filter = ("is_inventoried", "category")
    search_fields = ("name",)
    ordering = ("id",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "category")
        }),
        ("Inventory", {
            "fields": ("is_inventoried", "stock")
        }),
        ("Price", {
            "fields": ("pvp",)
        }),
        ("Presentation", {
            "fields": ("image", "quantity_type", "quantity_value", "color")
        }),
        ("Time", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )