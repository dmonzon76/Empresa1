from django.urls import path, include
from django.views.generic import RedirectView

app_name = "core"

urlpatterns = [
    path("", RedirectView.as_view(url="/dashboard/", permanent=False), name="root"),

    # 👉 Registrar la app accounting con namespace
    path("accounting/", include("apps.accounting.urls", namespace="accounting")),
]
