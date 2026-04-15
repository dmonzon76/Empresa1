from django.shortcuts import render
from django.db.models import Sum
from datetime import date
from apps.accounting.models import JournalEntryLine


def finance_dashboard(request):
    today = date.today()
    month = today.month
    year = today.year

    # Income (accounts starting with 4)
    income_month = JournalEntryLine.objects.filter(
        account__code__startswith="4",
        entry__date__year=year,
        entry__date__month=month
    ).aggregate(total=Sum("credit") - Sum("debit"))["total"] or 0

    # Expenses (accounts starting with 5)
    expenses_month = JournalEntryLine.objects.filter(
        account__code__startswith="5",
        entry__date__year=year,
        entry__date__month=month
    ).aggregate(total=Sum("debit") - Sum("credit"))["total"] or 0

    # Operating result
    operating_result = income_month - expenses_month

    # Cash available (cash + banks)
    cash_available = JournalEntryLine.objects.filter(
        account__code__startswith="1.1.1"
    ).aggregate(total=Sum("debit") - Sum("credit"))["total"] or 0

    # Accounts receivable (customers)
    accounts_receivable = JournalEntryLine.objects.filter(
        account__code__startswith="1.1.3"
    ).aggregate(total=Sum("debit") - Sum("credit"))["total"] or 0

    # Accounts payable (suppliers)
    accounts_payable = JournalEntryLine.objects.filter(
        account__code__startswith="2.1.1"
    ).aggregate(total=Sum("credit") - Sum("debit"))["total"] or 0

    context = {
        "income_month": income_month,
        "expenses_month": expenses_month,
        "operating_result": operating_result,
        "cash_available": cash_available,
        "accounts_receivable": accounts_receivable,
        "accounts_payable": accounts_payable,
    }

    return render(request, "reports/finance_dashboard.html", context)
