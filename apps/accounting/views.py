from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Sum
from django.utils.timezone import now

from django.views.generic import ListView, CreateView, DetailView

from apps.accounting.models import (
    Account,
    JournalEntry,
    JournalEntryLine,
)
from django.shortcuts import render, redirect
from .forms import JournalEntryForm, JournalEntryLineFormSet

# -----------------------------
# Dashboard
# -----------------------------
def dashboard(request):
    today = now()

    month_lines = JournalEntryLine.objects.filter(
        entry__date__year=today.year,
        entry__date__month=today.month
    )

    context = {
        "total_accounts": Account.objects.count(),
        "total_entries": JournalEntry.objects.count(),
        "month_debit": month_lines.aggregate(Sum("debit"))["debit__sum"] or 0,
        "month_credit": month_lines.aggregate(Sum("credit"))["credit__sum"] or 0,
        "recent_entries": JournalEntry.objects.order_by("-date")[:5],
        "recent_lines": JournalEntryLine.objects.select_related("account", "entry")
            .order_by("-entry__date")[:10],
    }

    return render(request, "accounting/dashboard.html", context)


# -----------------------------
# Accounts
# -----------------------------
class AccountListView(ListView):
    model = Account
    template_name = "accounting/accounts_list.html"
    context_object_name = "accounts"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.annotate(
            total_debit=Sum("journalentryline__debit"),
            total_credit=Sum("journalentryline__credit")
        )


class AccountLedgerView(DetailView):
    model = Account
    template_name = "accounting/account_ledger.html"
    context_object_name = "account"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        lines = (
            JournalEntryLine.objects
            .filter(account=self.object)
            .select_related("entry")
            .order_by("entry__date", "entry__id")
        )

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
            "entry_id": line.entry.id,   # ← agregado
})



        context["ledger_rows"] = ledger_rows
        context["total_debit"] = lines.aggregate(Sum("debit"))["debit__sum"] or 0
        context["total_credit"] = lines.aggregate(Sum("credit"))["credit__sum"] or 0
        context["final_balance"] = context["total_debit"] - context["total_credit"]

        return context


# -----------------------------
# Journal Entries
# -----------------------------
class JournalEntryListView(ListView):
    model = JournalEntry
    template_name = "accounting/journal_list.html"
    context_object_name = "journal_entries"
    ordering = ["-date"]


class JournalEntryDetailView(DetailView):
    model = JournalEntry
    template_name = "accounting/journal_detail.html"
    context_object_name = "entry"


def journal_create(request):
    if request.method == "POST":
        form = JournalEntryForm(request.POST)
        formset = JournalEntryLineFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            entry = form.save()
            lines = formset.save(commit=False)
            for line in lines:
                line.entry = entry
                line.save()
            return redirect("accounting:journal_detail", pk=entry.pk)

    else:
        form = JournalEntryForm()
        formset = JournalEntryLineFormSet()

    return render(request, "accounting/journal_form.html", {
        "form": form,
        "formset": formset,
    })
