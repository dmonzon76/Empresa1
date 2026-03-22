from django.views.generic import TemplateView
from apps.dashboard.services.dashboard_service import DashboardService


class DashboardHomeView(TemplateView):
    template_name = "dashboard/dashboard_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(DashboardService.get_all_kpis())
        return context
