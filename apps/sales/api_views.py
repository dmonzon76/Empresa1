from django.http import JsonResponse
from django.utils.timezone import now
from django.db.models import Sum, Count, F
from .models import SalesOrder


def sales_kpis(request):
    today = now().date()
    month = today.month
    year = today.year

    orders = SalesOrder.objects.filter(status=SalesOrder.CONFIRMED)

    # Sales of the day
    sales_today = orders.filter(date=today).aggregate(
        total=Sum("total"))["total"] or 0

    # Sales of the month
    sales_month = orders.filter(
        date__year=year,
        date__month=month
    ).aggregate(total=Sum("total"))["total"] or 0

    # Order quantity
    count_orders = orders.count()

    # Average ticket
    ticket_avg = orders.aggregate(avg=Sum("total") / Count("id"))["avg"] or 0

    return JsonResponse({
        "sales_today": float(sales_today),
        "sales_month": float(sales_month),
        "count_orders": count_orders,
        "ticket_avg": float(ticket_avg),
    })
