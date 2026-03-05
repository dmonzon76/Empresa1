
from django.shortcuts import render
from apps.customers.models import Customer
from apps.products.models import Product

def dashboard(request):
    context = {
        "total_customers": Customer.objects.filter(is_active=True).count(),
        "total_products": Product.objects.count(),
        # más KPIs cuando tengas ventas / facturación / cuenta corriente
    }
    return render(request, "starting/index.html", context)




