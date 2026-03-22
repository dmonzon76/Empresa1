from django.urls import path
import apps.dashboard.views.html_views as html_views

app_name = "dashboard_html"

urlpatterns = [
    path("", html_views.DashboardHomeView.as_view(), name="home"),
]
