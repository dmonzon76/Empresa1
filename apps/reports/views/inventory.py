from django.shortcuts import render
from django.db.models import Sum, F
from datetime import date, timedelta

from apps.products.models import Product
from apps.inventory.models import InventoryItem, InventoryMovement


def inventory_dashboard(request):
    today = date.today()
    month = today.month
    year = today.year

    total_stock = InventoryItem.objects.aggregate(
        total=Sum("quantity")
    )["total"] or 0

    stock_value = (
        InventoryItem.objects
        .annotate(value=F("quantity") * F("product__cost"))
        .aggregate(total=Sum("value"))
    )["total"] or 0

    low_stock = InventoryItem.objects.filter(
        quantity__lt=F("min_stock")
    ).count()

    last_60 = today - timedelta(days=60)
    no_movement = (
        InventoryItem.objects
        .exclude(movements__date__gte=last_60)
        .count()
    )

    rotation = (
        InventoryMovement.objects.filter(movement_type="OUT")
        .values("product__category__name")
        .annotate(total=Sum("quantity"))
        .order_by("-total")
    )

    labels_rotation = [r["product__category__name"] for r in rotation]
    values_rotation = [float(r["total"]) for r in rotation]

    stock_category = (
        InventoryItem.objects
        .values("product__category__name")
        .annotate(total=Sum("quantity"))
        .order_by("-total")
    )

    labels_category = [c["product__category__name"] for c in stock_category]
    values_category = [float(c["total"]) for c in stock_category]

    movements = (
        InventoryMovement.objects.filter(date__year=year)
        .values("date__month")
        .annotate(total=Sum("quantity"))
        .order_by("date__month")
    )

    labels_movements = [m["date__month"] for m in movements]
    values_movements = [float(m["total"]) for m in movements]

    context = {
        "total_stock": total_stock,
        "stock_value": stock_value,
        "low_stock": low_stock,
        "no_movement": no_movement,
        "labels_rotation": labels_rotation,
        "values_rotation": values_rotation,
        "labels_category": labels_category,
        "values_category": values_category,
        "labels_movements": labels_movements,
        "values_movements": values_movements,
    }

    return render(request, "reports/inventory_dashboard.html", context)
