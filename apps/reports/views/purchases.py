from django.shortcuts import render
from django.db.models import Sum
from datetime import date, timedelta

from apps.purchases.models import PurchaseOrder
from apps.suppliers.models import Supplier


def purchases_dashboard(request):
    today = date.today()
    month = today.month
    year = today.year

    # Purchases of the day
    purchases_day = PurchaseOrder.objects.filter(date=today).aggregate(
        total=Sum("total_amount")
    )["total"] or 0

    # Purchases of the month
    purchases_month = PurchaseOrder.objects.filter(
        date__year=year, date__month=month
    ).aggregate(total=Sum("total_amount"))["total"] or 0

    # Total orders
    total_orders = PurchaseOrder.objects.filter(
        date__year=year, date__month=month
    ).count()

    # Average cost per order
    average_cost = purchases_month / total_orders if total_orders > 0 else 0

    # Pending orders (only if your model has a status field)
    pending_orders = (
        PurchaseOrder.objects.filter(status="PENDING").count()
        if hasattr(PurchaseOrder, "status")
        else 0
    )

    # Purchases by supplier
    purchases_supplier = (
        PurchaseOrder.objects.values("supplier__name")
        .annotate(total=Sum("total_amount"))
        .order_by("-total")
    )

    labels_suppliers = [p["supplier__name"] for p in purchases_supplier]
    values_suppliers = [float(p["total"]) for p in purchases_supplier]

    # Top supplier
    top_supplier = labels_suppliers[0] if labels_suppliers else "N/A"

    # Purchases in the last 12 months
    labels_12 = []
    values_12 = []

    for i in range(12):
        m = (today.month - i - 1) % 12 + 1
        y = today.year if today.month - i > 0 else today.year - 1

        labels_12.append(f"{m}/{y}")
        values_12.append(
            PurchaseOrder.objects.filter(
                date__year=y, date__month=m
            ).aggregate(total=Sum("total_amount"))["total"]
            or 0
        )

    labels_12.reverse()
    values_12.reverse()

    context = {
        "purchases_day": purchases_day,
        "purchases_month": purchases_month,
        "total_orders": total_orders,
        "average_cost": average_cost,
        "pending_orders": pending_orders,
        "top_supplier": top_supplier,
        "labels_suppliers": labels_suppliers,
        "values_suppliers": values_suppliers,
        "labels_12": labels_12,
        "values_12": values_12,
    }

    return render(request, "reports/purchases_dashboard.html", context)
