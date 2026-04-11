# inventory/forms.py
from django import forms
from .models import InventoryMovement



class InventoryMovementForm(forms.ModelForm):
    class Meta:
        model = InventoryMovement
        fields = ["movement_type", "quantity", "note"]
        widgets = {
            "movement_type": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "note": forms.TextInput(attrs={"class": "form-control"}),
        }
