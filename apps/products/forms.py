from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "image",
            "pvp",
            "stock",
            "quantity_type",
            "quantity_value",
            "color",
            "is_inventoried",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "pvp": forms.NumberInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "quantity_type": forms.Select(attrs={"class": "form-select"}),
            "quantity_value": forms.NumberInput(attrs={"class": "form-control"}),
            "color": forms.Select(attrs={"class": "form-select"}),
            "is_inventoried": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }