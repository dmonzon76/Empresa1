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
from django.views.generic import RedirectView

urlpatterns = [
    # Django Admin ALWAYS first
    path("admin/", admin.site.urls),

    # Main apps
    path("", include("apps.core.urls")),
    path("customers/", include("apps.customers.urls_html")),   # HTML
    path("products/", include("apps.products.urls")),
    path("categories/", include("apps.categories.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("sales/", include("apps.sales.urls")),
    path("inventory/", include("apps.inventory.urls")),

    # HTML namespaces
    path(
        "purchases/",
        include(("apps.purchases.urls.html_urls", "purchases_html"), namespace="purchases_html")
    ),
    path(
        "suppliers/",
        include(("apps.suppliers.urls.html_urls", "suppliers_html"), namespace="suppliers_html")
    ),
    path(
        "accounting/",
        include(("apps.accounting.urls.html_urls", "accounting_html"), namespace="accounting_html")
    ),
    path(
        "reports/",
        include(("apps.reports.urls.html_urls", "reports_html"), namespace="reports_html")
    ),

    path("dashboard/", include("apps.dashboard.urls.html_urls")),


    # APIs
    path("api/categories/", include("apps.categories.urls_api")),
    path("api/products/", include("apps.products.urls_api")),
    path("api/accounts/", include("apps.accounts.urls_api")),
    path("api/customers/", include("apps.customers.urls_api")),
    path(
        "purchases/api/",
        include(("apps.purchases.urls.api_urls", "purchases_api"), namespace="purchases_api")
    ),
    path(
        "suppliers/api/",
        include(("apps.suppliers.urls.api_urls", "suppliers_api"), namespace="suppliers_api")
    ),
    path(
        "accounting/api/",
        include(("apps.accounting.urls.api_urls", "accounting_api"), namespace="accounting_api")
    ),
    path(
        "reports/api/",
        include(("apps.reports.urls.api_urls", "reports_api"), namespace="reports_api")
    ),
    path("api/dashboard/", include("apps.dashboard_api.urls")),

]
