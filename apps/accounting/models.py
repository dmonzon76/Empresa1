from django.db import models

class Account(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )
    is_postable = models.BooleanField(default=True)

    class Meta:
        ordering = ["code"]
        verbose_name = "Account"
        verbose_name_plural = "Chart of Accounts"

    def __str__(self):
        return f"{self.code} - {self.name}"


class JournalEntry(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["-date", "-id"]

    def __str__(self):
        return f"JE {self.id} - {self.date}"


class JournalEntryLine(models.Model):
    entry = models.ForeignKey(
        JournalEntry,
        related_name="lines",
        on_delete=models.CASCADE
    )
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.entry_id} - {self.account} ({self.debit}/{self.credit})"
