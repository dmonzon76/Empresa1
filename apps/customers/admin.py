from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Customer
from apps.addresses.models import AddressAssignment


class AddressAssignmentInline(GenericTabularInline):
    model = AddressAssignment
    extra = 0
    readonly_fields = ("address", "address_type", "is_primary", "created_at")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_number",
        "full_name",
        "email",
        "phone",
        "category",
        "is_active",
        "created_at",
    )

    list_filter = ("category", "is_active", "created_at")
    search_fields = ("first_name", "last_name", "email", "customer_number")
    ordering = ("-created_at",)
    readonly_fields = ("customer_number", "created_at", "updated_at")

    fieldsets = (
        ("Identity", {"fields": ("first_name", "last_name", "email", "phone")}),
        ("Category", {"fields": ("category",)}),
        ("Internal Info", {"fields": ("customer_number",)}),
        ("Status", {"fields": ("is_active",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    inlines = [AddressAssignmentInline]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = "Name"
