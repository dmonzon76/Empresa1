from django.urls import path
from .views import (
    dashboard,
    AccountListView,
    AccountLedgerView,
    JournalEntryListView,
    JournalEntryDetailView,
    journal_create,   # ✔️ ESTA ES LA CORRECTA
)

app_name = "accounting"

urlpatterns = [
    path("", dashboard, name="dashboard"),

    path("accounts/", AccountListView.as_view(), name="accounts_list"),
    path("accounts/<int:pk>/ledger/", AccountLedgerView.as_view(), name="account_ledger"),

    path("journal/", JournalEntryListView.as_view(), name="journal_list"),
    path("journal/new/", journal_create, name="journal_create"),  # ✔️ OK
    path("journal/<int:pk>/", JournalEntryDetailView.as_view(), name="journal_detail"),
]
