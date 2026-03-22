
from django.contrib import admin
from .models import Customer
from apps.addresses.models import CustomerAddress


class CustomerAddressInline(admin.TabularInline):
    model = CustomerAddress
    extra = 1
    fields = (
        "address",
        "city",
        "state",
        "postal_code",
        "country",
        "is_primary",
    )
    ordering = ("-is_primary",)
    show_change_link = True


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

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "customer_number",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "customer_number",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Identity", {
            "fields": ("first_name", "last_name", "email", "phone")
        }),
        ("Category", {
            "fields": ("category",)
        }),
        ("Internal Info", {
            "fields": ("customer_number",)
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )

    inlines = [CustomerAddressInline]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = "Name"