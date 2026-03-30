from django.contrib import admin
from ..models import AddressAssignment
from ..forms.assignment import AddressAssignmentForm




@admin.register(AddressAssignment)
class AddressAssignmentAdmin(admin.ModelAdmin):
    form = AddressAssignmentForm

    list_display = (
        "id",
        "entity",
        "address",
        "address_type",
        "is_primary",
        "created_at",
    )

    list_filter = ("address_type", "is_primary")
    search_fields = ("address__street", "entity__id")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
