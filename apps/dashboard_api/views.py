from rest_framework.views import APIView
from rest_framework.response import Response
from apps.dashboard.services.dashboard_service import DashboardService


class DashboardStatsView(APIView):
    def get(self, request):
        return Response(DashboardService.get_all_kpis())
