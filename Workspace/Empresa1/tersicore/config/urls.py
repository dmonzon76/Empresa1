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
    # Django Admin SIEMPRE primero
    path("admin/", admin.site.urls),

    # Apps principales
   
  
    path("", include("apps.core.urls")),
    path("customers/", include("apps.customers.urls_html")),   # HTML
    path("api/customers/", include("apps.customers.urls_api")),  # API
    path("products/", include("apps.products.urls")),
    path("categories/", include("apps.categories.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("sales/", include("apps.sales.urls")),
    path("inventory/", include("apps.inventory.urls")),
    


    # APIs
    path("api/categories/", include("apps.categories.urls_api")),
    path("api/customers/", include("apps.customers.urls_api")),
    path("api/products/", include("apps.products.urls_api")),
    path("api/accounts/", include("apps.accounts.urls_api")),

    # Core (dashboard)
    path("", include("apps.core.urls")),

    # Redirección opcional
    # path("", RedirectView.as_view(url='dashboard/', permanent=False), name='root'),
    ]

