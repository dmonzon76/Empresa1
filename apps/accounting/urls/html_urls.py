from django.urls import path
import apps.accounting.views.html_views as html_views

app_name = "accounting_html"


urlpatterns = [
    path("accounts/", html_views.AccountListView.as_view(), name="accounts_list"),
    path("journal/", html_views.JournalEntryListView.as_view(), name="journal_list"),
    path("journal/new/", html_views.JournalEntryCreateView.as_view(), name="journal_create"),
    path("ledger/<int:pk>/", html_views.LedgerView.as_view(), name="ledger"),
    path("journal/new/", html_views.JournalEntryCreateView.as_view(), name="journal_create"),

]
