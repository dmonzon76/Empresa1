from django.contrib import admin
from ..models import AddressAssignment
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from apps.addresses.models import AddressAssignment


@admin.register(AddressAssignment)
class AddressAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "entity",
        "address",
        "address_type",
        "is_primary",
        "created_at",
    )

    list_filter = (
        "address_type",
        "is_primary",
    )

    search_fields = (
        "address__street",
        "address__city",
        "address__state",
        "address__country",
        "object_id",
    )

    ordering = ("-created_at",)

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (None, {"fields": ("content_type", "object_id", "address", "address_type", "is_primary")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

class AddressAssignmentInline(GenericTabularInline):
    model = AddressAssignment
    extra = 1
    autocomplete_fields = ["address", "address_type"]
    fields = ["address_type", "address", "is_primary"]
    verbose_name = "Address"
    verbose_name_plural = "Addresses"
