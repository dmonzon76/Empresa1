from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "display_name",
        "supplier_type",
        "tax_id",
        "email",
        "phone",
        "is_active",
    )

    search_fields = (
        "company_name",
        "first_name",
        "last_name",
        "contact_name",
        "tax_id",
    )

    list_filter = ("is_active",)
    ordering = ("company_name", "last_name", "first_name")

    def supplier_type(self, obj):
        return "Company" if obj.company_name else "Person"
    supplier_type.short_description = "Type"
