from django.contrib import admin
from .models import SalesOrder, SalesOrderItem


class SalesOrderItemInline(admin.TabularInline):
    model = SalesOrderItem
    extra = 1
    fields = ("product", "quantity", "price", "subtotal")
    readonly_fields = ("subtotal",)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status != SalesOrder.DRAFT:
            return False
        return True

    def has_add_permission(self, request, obj):
        if obj and obj.status != SalesOrder.DRAFT:
            return False
        return True


@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "date", "status", "total_amount_display")
    list_filter = ("status", "date")
    search_fields = ("customer__first_name", "customer__last_name")
    readonly_fields = ("created_at", "total_amount_display")
    inlines = [SalesOrderItemInline]

    fieldsets = (
        ("Order Information", {
            "fields": ("customer", "date", "status", "notes")
        }),
        ("Totals", {
            "fields": ("total_amount_display",),
        }),
        ("Traceability", {
            "fields": ("created_at",),
        }),
    )

    def total_amount_display(self, obj):
        return f"${obj.total}"
    total_amount_display.short_description = "Total"


@admin.register(SalesOrderItem)
class SalesOrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity",
                    "price", "subtotal_display")
    search_fields = ("order__id", "product__name")

    def subtotal_display(self, obj):
        return f"${obj.subtotal}"
    subtotal_display.short_description = "Subtotal"
