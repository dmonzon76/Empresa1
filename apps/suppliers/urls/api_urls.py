from django.urls import path, include
from apps.suppliers.api.urls import router as suppliers_router

app_name = "suppliers_api"

urlpatterns = [
    path("", include(suppliers_router.urls)),
]
