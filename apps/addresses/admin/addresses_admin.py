from django.contrib import admin
from ..models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "street",
        "city",
        "state",
        "country",
        "postal_code",
        "created_at",
    )

    search_fields = ("street", "city", "state", "country", "postal_code")
    list_filter = ("country", "city", "state")
    ordering = ("country", "city", "street")
    readonly_fields = ("created_at", "updated_at")
