# inventory/api_views.py
from django.http import JsonResponse
from django.db.models import Sum, F
from .models import InventoryItem, InventoryMovement
from django.db.models.functions import TruncMonth

def inventory_kpis(request):
    items = InventoryItem.objects.all()

    low_stock = items.filter(quantity__lt=F("min_stock")).count()
    total_products = items.count()
    total_stock = items.aggregate(total=Sum("quantity"))["total"] or 0

    return JsonResponse({
        "low_stock": low_stock,
        "total_products": total_products,
        "total_stock": float(total_stock),
    })

    

def inventory_monthly_chart(request):
    movements = (
        InventoryMovement.objects
        .annotate(month=TruncMonth("date"))
        .values("month", "movement_type")
        .annotate(total=Sum("quantity"))
        .order_by("month")
    )

    data = {}

    for m in movements:
        month = m["month"].strftime("%Y-%m")
        if month not in data:
            data[month] = {"IN": 0, "OUT": 0}

        data[month][m["movement_type"]] = float(m["total"])

    return JsonResponse(data)