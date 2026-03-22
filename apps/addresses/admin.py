from django.contrib import admin
from .models import CustomerAddress


@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "address",
        "city",
        "country",
        "is_primary",
        "created_at",
    )

    list_filter = ("country", "is_primary", "created_at")
    search_fields = (
        "customer__first_name",
        "customer__last_name",
        "address",
        "city",
        "postal_code",
    )

    ordering = ("-is_primary", "customer")