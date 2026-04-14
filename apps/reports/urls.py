from django.urls import path
from .views.dashboard import reports_dashboard
from .views.finance import finance_dashboard
from .views.sales import sales_dashboard
from .views.inventory import inventory_dashboard
from .views.crm import crm_dashboard
from .views.purchases import purchases_dashboard

app_name = "reports"

urlpatterns = [
    path('', reports_dashboard, name='dashboard'),
    path('finance/', finance_dashboard, name='finance_dashboard'),
    path('sales/', sales_dashboard, name='sales_dashboard'),
    path('inventory/', inventory_dashboard, name='inventory_dashboard'),
    path('crm/', crm_dashboard, name='crm_dashboard'),
    path('purchases/', purchases_dashboard, name='purchases_dashboard'),
]
