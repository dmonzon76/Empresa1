# inventory/forms.py
from django import forms
from .models import InventoryMovement

class InventoryMovementForm(forms.ModelForm):
    class Meta:
        model = InventoryMovement
        fields = ["product", "movement_type", "quantity", "note"]