from django.contrib import admin
from .models import Account, JournalEntry, JournalEntryLine
from django.apps import AppConfig
# Register your models here.

class JournalEntryLineInline(admin.TabularInline):
    model = JournalEntryLine
    extra = 1

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "parent", "is_postable")
    list_filter = ("is_postable",)


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "description")
    inlines = [JournalEntryLineInline]




class AccountingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounting"
    verbose_name = "Accounting"


    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Chart of Accounts"
