from django.contrib import admin
from .models import PurchaseOrder
# Register your models here.



@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ("number", "date", "supplier", "total_amount")
    search_fields = ("number",)
    list_filter = ("date", "supplier")
