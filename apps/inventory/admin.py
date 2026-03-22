from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import InventoryItem, InventoryMovement, InventoryRule


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "min_stock", "is_below_min_display")
    list_filter = ("product__category",)
    search_fields = ("product__name", "product__sku")
    ordering = ("product__name",)

    @admin.display(description="Stock bajo", boolean=True)
    def is_below_min_display(self, obj):
        return obj.is_below_min()


@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    list_display = ("product", "movement_type", "quantity", "date", "note")
    list_filter = ("movement_type", "date", "product__category")
    search_fields = ("product__name", "note")
    ordering = ("-date",)
    date_hierarchy = "date"


@admin.register(InventoryRule)
class InventoryRuleAdmin(admin.ModelAdmin):
    list_display = ("product", "min_stock", "max_stock")
    search_fields = ("product__name",)
    ordering = ("product__name",)
