from django.contrib import admin
from .models import Account, JournalEntry, JournalEntryLine

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
