from django.urls import path
from . import views

app_name = "accounting"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),  # ← NUEVA
    path("accounts/", views.AccountListView.as_view(), name="accounts_list"),
    path("journal/", views.JournalEntryListView.as_view(), name="journal_list"),
    path("journal/create/", views.JournalEntryCreateView.as_view(), name="journal_create"),
    path("ledger/<int:pk>/", views.LedgerView.as_view(), name="ledger"),
    path("account/<int:pk>/ledger/", views.AccountLedgerView.as_view(), name="account_ledger"),
]
