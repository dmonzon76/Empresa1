from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from apps.accounting.models import Account, JournalEntry
from django.db.models import Sum
from django.views.generic import DetailView
from apps.accounting.models import Account, JournalEntryLine

def index(request):
    return render(request, "accounting/index.html")


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
    fields = ["date", "description"]
    success_url = reverse_lazy("accounting:journal_list")



class LedgerView(DetailView):
    model = JournalEntry
    template_name = "accounting/ledger.html"
    context_object_name = "entry"



class AccountLedgerView(DetailView):
    model = Account
    template_name = "accounting/account_ledger.html"
    context_object_name = "account"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Todas las líneas asociadas a esta cuenta
        lines = JournalEntryLine.objects.filter(
            account=self.object
        ).select_related("entry").order_by("entry__date", "entry__id")

        # Saldos acumulados
        running_balance = 0
        ledger_rows = []

        for line in lines:
            running_balance += float(line.debit) - float(line.credit)
            ledger_rows.append({
                "date": line.entry.date,
                "description": line.entry.description,
                "debit": line.debit,
                "credit": line.credit,
                "balance": running_balance,
            })

        context["ledger_rows"] = ledger_rows
        context["total_debit"] = lines.aggregate(Sum("debit"))["debit__sum"] or 0
        context["total_credit"] = lines.aggregate(Sum("credit"))["credit__sum"] or 0
        context["final_balance"] = context["total_debit"] - context["total_credit"]

        return context
    
def dashboard(request):
    return render(request, "placeholders/module_placeholder.html", {
        "module_name": "Accounting",
        "description": "Financial operations, ledgers, invoices, and more."
    })
