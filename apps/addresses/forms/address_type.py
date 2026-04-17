from django import forms
from apps.addresses.models import AddressType

class AddressTypeForm(forms.ModelForm):
    class Meta:
        model = AddressType
        fields = ["name", "code", "is_active", "is_unique_per_entity"]

    def clean_code(self):
        code = self.cleaned_data["code"].strip()
        if not code:
            raise forms.ValidationError("The code cannot be empty.")
        return code
