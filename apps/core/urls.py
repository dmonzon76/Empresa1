from django.urls import path
from django.views.generic import RedirectView

app_name = "core"

urlpatterns = [
    #Redirects the system root to the dashboard
    path("", RedirectView.as_view(url="/dashboard/", permanent=False), name="root"),
]
