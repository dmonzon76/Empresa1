from rest_framework.routers import DefaultRouter
from apps.purchases.api.views import PurchaseOrderViewSet

app_name = "purchases_api"

router = DefaultRouter()
router.register("purchase-orders", PurchaseOrderViewSet,
                basename="purchase-order")

urlpatterns = router.urls
