# categories/forms.py

from django import forms
from .models import CustomerCategory, ProductCategory

class CustomerCategoryForm(forms.ModelForm):
    class Meta:
        model = CustomerCategory
        fields = ["name", "prefix", "description", "is_active"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ["name", "description", "parent", "is_active"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }