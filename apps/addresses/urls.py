from django.urls import path
from .views.dashboard import address_dashboard

app_name = "apps.addresses"

urlpatterns = [
    path("dashboard/", address_dashboard, name="dashboard"),
]
