from django.contrib import admin
from .models import Account, JournalEntry, JournalEntryLine

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "type", "parent", "is_postable", "icon", "color")
    list_filter = ("type", "is_postable")
    search_fields = ("code", "name")
    list_editable = ("is_postable",)


class JournalEntryLineInline(admin.TabularInline):
    model = JournalEntryLine
    extra = 1


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "description")
    inlines = [JournalEntryLineInline]
    search_fields = ("description",)
    list_filter = ("date",)
