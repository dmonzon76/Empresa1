from django.db import models

ACCOUNT_TYPES = [
    ("ASSET", "Asset"),
    ("LIABILITY", "Liability"),
    ("EQUITY", "Equity"),
    ("INCOME", "Income"),
    ("EXPENSE", "Expense"),
]

ACCOUNT_STYLE = {
    "ASSET":     {"icon": "fa-solid fa-box",               "color": "#0d6efd"},
    "LIABILITY": {"icon": "fa-solid fa-scale-balanced",    "color": "#6f42c1"},
    "EQUITY":    {"icon": "fa-solid fa-building-columns",  "color": "#198754"},
    "INCOME":    {"icon": "fa-solid fa-arrow-trend-up",    "color": "#fd7e14"},
    "EXPENSE":   {"icon": "fa-solid fa-money-bill",        "color": "#dc3545"},
}

class Account(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="children"
    )

    is_postable = models.BooleanField(default=True)

    icon = models.CharField(max_length=50, default="fa-regular fa-circle")
    color = models.CharField(max_length=20, default="#6c757d")

    def save(self, *args, **kwargs):
        if self.type in ACCOUNT_STYLE:
            self.icon = ACCOUNT_STYLE[self.type]["icon"]
            self.color = ACCOUNT_STYLE[self.type]["color"]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} — {self.name}"


class JournalEntry(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return f"Entry {self.pk} — {self.date}"


class JournalEntryLine(models.Model):
    entry = models.ForeignKey(JournalEntry, related_name="lines", on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.account.code} — D:{self.debit} C:{self.credit}"
