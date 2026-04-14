from django.shortcuts import render
from django.db.models import Count
from datetime import date, timedelta

from apps.customers.models import Customer


def crm_dashboard(request):
    today = date.today()
    month = today.month
    year = today.year

    # New clients this month
    new_clients_month = Customer.objects.filter(
        created_at__year=year,
        created_at__month=month
    ).count()

    # Active / inactive clients
    active_clients = Customer.objects.filter(is_active=True).count()
    inactive_clients = Customer.objects.filter(is_active=False).count()

    # Churn (clients who became inactive in the last 60 days)
    last_60 = today - timedelta(days=60)
    churn = Customer.objects.filter(
        is_active=False,
        updated_at__gte=last_60
    ).count() if hasattr(Customer, "updated_at") else 0

    # Clients by category
    clients_by_category = (
        Customer.objects.values("category__name")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

    labels_category = [c["category__name"] for c in clients_by_category]
    values_category = [c["total"] for c in clients_by_category]

    # New clients in the last 12 months
    labels_12 = []
    values_12 = []
    for i in range(12):
        m = (today.month - i - 1) % 12 + 1
        y = today.year if today.month - i > 0 else today.year - 1
        labels_12.append(f"{m}/{y}")
        values_12.append(
            Customer.objects.filter(
                created_at__year=y, created_at__month=m).count()
        )
    labels_12.reverse()
    values_12.reverse()

    # Latest clients
    latest_clients = Customer.objects.order_by("-created_at")[:10]

    context = {
        "new_clients_month": new_clients_month,
        "active_clients": active_clients,
        "inactive_clients": inactive_clients,
        "churn": churn,
        "labels_category": labels_category,
        "values_category": values_category,
        "labels_12": labels_12,
        "values_12": values_12,
        "latest_clients": latest_clients,
    }

    return render(request, "reports/crm_dashboard.html", context)
