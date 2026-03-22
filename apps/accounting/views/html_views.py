from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from apps.accounting.models import Account, JournalEntry
from django.views.generic import DetailView


class AccountListView(ListView):
    model = Account
    template_name = "accounting/accounts_list.html"
    context_object_name = "accounts"


class JournalEntryListView(ListView):
    model = JournalEntry
    template_name = "accounting/journal_list.html"
    context_object_name = "journal_entries"


class JournalEntryCreateView(CreateView):
    model = JournalEntry
    template_name = "accounting/journal_form.html"
    fields = ["date", "description"]  # Ajustalo según tu modelo
    success_url = reverse_lazy("accounting:journal_list")

class LedgerView(DetailView):
    model = Account
    template_name = "accounting/ledger.html"
    context_object_name = "account"
