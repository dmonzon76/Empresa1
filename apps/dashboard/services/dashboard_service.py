from django.db.models import Count, Sum, Avg
from django.utils.timezone import now
from apps.customers.models import Customer
from apps.categories.models import CustomerCategory
from apps.inventory.models import Product, InventoryMovement
from apps.sales.models import SalesOrder


class DashboardService:

    @staticmethod
    def get_customer_kpis():
        total_customers = Customer.objects.count()
        active_customers = Customer.objects.filter(is_active=True).count()

        customers = Customer.objects.order_by("-created_at")[:5]

        categories = CustomerCategory.objects.annotate(
            total=Count("customers"))
        categories_labels = [c.name for c in categories]
        categories_counts = [c.total for c in categories]

        return {
            "total_customers": total_customers,
            "active_customers": active_customers,
            "customers": customers,
            "categories_labels": categories_labels,
            "categories_counts": categories_counts,
        }

    @staticmethod
    def get_inventory_kpis():
        total_products = Product.objects.count()
        low_stock_count = Product.objects.filter(stock__lt=10).count()
        total_stock = Product.objects.aggregate(
            total=Sum("stock"))["total"] or 0

        stock_by_unit = (
            Product.objects.values("quantity_type")
            .annotate(total_stock=Sum("stock"))
            .order_by("quantity_type")
        )

        stock_by_category = (
            Product.objects.values("category__name")
            .annotate(total_stock=Sum("stock"))
            .order_by("category__name")
        )

        current_year = now().year
        monthly_movements = (
            InventoryMovement.objects.filter(date__year=current_year)
            .values("date__month")
            .annotate(total=Sum("quantity"))
            .order_by("date__month")
        )

        return {
            "total_products": total_products,
            "low_stock_count": low_stock_count,
            "total_stock": total_stock,
            "stock_by_unit": stock_by_unit,
            "stock_by_category": stock_by_category,
            "inventory_monthly": list(monthly_movements),
        }

    @staticmethod
    def get_sales_kpis():
        today = now().date()
        month_start = today.replace(day=1)

        sales_today = SalesOrder.objects.filter(
            date=today,
            status=SalesOrder.CONFIRMED
        ).count()

        sales_month = SalesOrder.objects.filter(
            date__gte=month_start,
            status=SalesOrder.CONFIRMED
        ).count()

        sales_count = SalesOrder.objects.filter(
            status=SalesOrder.CONFIRMED
        ).count()

        ticket_avg = SalesOrder.objects.filter(
            status=SalesOrder.CONFIRMED
        ).aggregate(
            avg=Avg("total")
        )["avg"] or 0

        return {
            "sales_today": sales_today,
            "sales_month": sales_month,
            "sales_count": sales_count,
            "ticket_avg": round(ticket_avg, 2),
        }

    @staticmethod
    def get_all_kpis():
        data = {}
        data.update(DashboardService.get_customer_kpis())
        data.update(DashboardService.get_inventory_kpis())
        data.update(DashboardService.get_sales_kpis())
        return data
