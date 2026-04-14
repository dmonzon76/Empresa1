from django.shortcuts import render
from django.db.models import Sum, F
from datetime import date, timedelta

from apps.sales.models import SalesOrder, SalesOrderItem
from apps.products.models import Product


def sales_dashboard(request):
    today = date.today()
    month = today.month
    year = today.year

    sales_day = SalesOrder.objects.filter(date=today).aggregate(
        total=Sum("total")
    )["total"] or 0

    sales_month = SalesOrder.objects.filter(
        date__year=year,
        date__month=month
    ).aggregate(total=Sum("total"))["total"] or 0

    total_orders = SalesOrder.objects.filter(
        date__year=year,
        date__month=month
    ).count()

    average_ticket = sales_month / total_orders if total_orders > 0 else 0

    last_30 = today - timedelta(days=30)
    sales_by_day = (
        SalesOrder.objects.filter(date__gte=last_30)
        .values("date")
        .annotate(total=Sum("total"))
        .order_by("date")
    )

    labels_day = [v["date"].strftime("%d-%m") for v in sales_by_day]
    values_day = [float(v["total"]) for v in sales_by_day]

    # SALES BY CATEGORY (CORRECTO)
    sales_category = (
        Product.objects.values("category__name")
        .annotate(
            total=Sum(F("salesorderitem__quantity") * F("salesorderitem__price"))
        )
        .order_by("-total")
    )

    labels_category = [v["category__name"] for v in sales_category]
    values_category = [float(v["total"] or 0) for v in sales_category]

    # TOP 10 PRODUCTS (CORRECTO)
    top_products = (
        Product.objects.annotate(
            total=Sum(F("salesorderitem__quantity") * F("salesorderitem__price"))
        )
        .order_by("-total")[:10]
    )

    labels_top = [p.name for p in top_products]
    values_top = [float(p.total or 0) for p in top_products]

    context = {
        "sales_day": sales_day,
        "sales_month": sales_month,
        "total_orders": total_orders,
        "average_ticket": average_ticket,
        "labels_day": labels_day,
        "values_day": values_day,
        "labels_category": labels_category,
        "values_category": values_category,
        "labels_top": labels_top,
        "values_top": values_top,
    }

    return render(request, "reports/sales_dashboard.html", context)
