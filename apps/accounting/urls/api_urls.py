from rest_framework.routers import DefaultRouter
from apps.accounting.api.views import JournalEntryViewSet

app_name = "accounting_api"

router = DefaultRouter()
router.register("journal-entries", JournalEntryViewSet,
                basename="journal-entry")

urlpatterns = router.urls
