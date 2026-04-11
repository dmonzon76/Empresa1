from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet
from .models import JournalEntry, JournalEntryLine

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ["date", "description"]


class JournalEntryLineBaseFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        total_debit = 0
        total_credit = 0

        for form in self.forms:
            if form.cleaned_data.get("DELETE"):
                continue

            debit = form.cleaned_data.get("debit") or 0
            credit = form.cleaned_data.get("credit") or 0

            total_debit += debit
            total_credit += credit

        if total_debit != total_credit:
            raise forms.ValidationError(
                f"El asiento no está balanceado. Débito total = {total_debit}, Crédito total = {total_credit}."
            )


JournalEntryLineFormSet = inlineformset_factory(
    JournalEntry,
    JournalEntryLine,
    formset=JournalEntryLineBaseFormSet,  # ← ahora sí existe
    fields=["account", "debit", "credit"],
    extra=2,
    can_delete=True
)
class JournalEntryLineBaseFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        total_debit = 0
        total_credit = 0
        has_valid_line = False

        for form in self.forms:
            if form.cleaned_data.get("DELETE"):
                continue

            account = form.cleaned_data.get("account")
            debit = form.cleaned_data.get("debit") or 0
            credit = form.cleaned_data.get("credit") or 0

            # Línea completamente vacía → ignorar
            if not account and debit == 0 and credit == 0:
                continue

            # Si hay datos, la línea debe ser válida
            has_valid_line = True

            # Validación: cuenta obligatoria
            if not account:
                raise forms.ValidationError("Hay líneas con valores pero sin cuenta asignada.")

            # Validación: no permitir débito y crédito simultáneos
            if debit > 0 and credit > 0:
                raise forms.ValidationError("Una línea no puede tener débito y crédito al mismo tiempo.")

            # Validación: al menos uno debe tener valor
            if debit == 0 and credit == 0:
                raise forms.ValidationError("Hay líneas sin débito ni crédito.")

            total_debit += debit
            total_credit += credit

        if not has_valid_line:
            raise forms.ValidationError("Debe ingresar al menos una línea contable.")

        if total_debit != total_credit:
            raise forms.ValidationError(
                f"El asiento no está balanceado. Débito total = {total_debit}, Crédito total = {total_credit}."
            )
