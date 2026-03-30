"""
URL configuration for tersicore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # CORE
    path("", include(("apps.core.urls", "core"), namespace="core")),

    # HTML
    path("dashboard/", include(("apps.dashboard.urls", "dashboard"), namespace="dashboard")),
    path("products/", include(("apps.products.urls", "products"), namespace="products")),
    path("categories/", include(("apps.categories.urls", "categories"), namespace="categories")),
    path("accounts/", include(("apps.accounts.urls", "accounts"), namespace="accounts")),
    path("sales/", include(("apps.sales.urls", "sales"), namespace="sales")),
    path("inventory/", include(("apps.inventory.urls", "inventory"), namespace="inventory")),
    path("purchases/", include(("apps.purchases.urls", "purchases"), namespace="purchases")),
    path("suppliers/", include(("apps.suppliers.urls", "suppliers"), namespace="suppliers")),
    path("accounting/", include(("apps.accounting.urls", "accounting"), namespace="accounting")),
    path("customers/", include(("apps.customers.urls", "customers"), namespace="customers")),
    path("reports/", include(("apps.reports.urls", "reports"), namespace="reports")),
    path("addresses/", include(("apps.addresses.urls", "addresses"), namespace="addresses")),

]



