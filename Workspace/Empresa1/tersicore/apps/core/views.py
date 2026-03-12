
from django.shortcuts import render
from django.db.models import Sum
from apps.customers.models import Customer
from apps.products.models import Product


def dashboard(request):
    # Últimos clientes
    customers = Customer.objects.filter(is_active=True).order_by("-id")[:5]

    # KPI básicos
    total_customers = Customer.objects.filter(is_active=True).count()
    total_products = Product.objects.count()

    # INVENTARIO

    # Umbral de bajo stock (ajustalo a tu criterio)
    LOW_STOCK_THRESHOLD = 5

    # Cantidad de productos con bajo stock
    low_stock_count = Product.objects.filter(
        is_inventoried=True,
        stock__lt=LOW_STOCK_THRESHOLD,
    ).count()

    # Stock total (suma de stock de todos los productos)
    total_stock = (
        Product.objects.aggregate(total_stock=Sum("stock"))["total_stock"] or 0
    )

    # Stock agrupado por unidad de medida
    stock_by_unit = (
        Product.objects
        .values("quantity_type")
        .annotate(total_stock=Sum("stock"))
        .order_by("quantity_type")
    )

    # Stock agrupado por categoría
    stock_by_category = (
        Product.objects
        .values("category__name")
        .annotate(total_stock=Sum("stock"))
        .order_by("category__name")
    )

    context = {
        "total_customers": total_customers,
        "total_products": total_products,
        "customers": customers,

        "low_stock_count": low_stock_count,
        "total_stock": total_stock,
        "stock_by_unit": stock_by_unit,
        "stock_by_category": stock_by_category,

        # Si ya tenés estos datos para el gráfico de clientes por categoría:
        # "categories_labels": categories_labels,
        # "categories_counts": categories_counts,
    }
    return render(request, "starting/index.html", context)
