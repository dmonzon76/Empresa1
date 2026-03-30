from django.contrib import admin
from ..models import AddressType


@admin.register(AddressType)
class AddressTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "is_active", "is_unique_per_entity")
    list_filter = ("is_active", "is_unique_per_entity")
    search_fields = ("name", "code")
    ordering = ("name",)
