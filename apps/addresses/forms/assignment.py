from django import forms
from django.forms import formset_factory
from apps.addresses.models import AddressAssignment


class AddressAssignmentForm(forms.ModelForm):
    class Meta:
        model = AddressAssignment
        fields = ["address_type", "address", "is_primary"]
        widgets = {
            "address": forms.Select(attrs={"class": "form-control"}),
            "address_type": forms.Select(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned = super().clean()

        address_type = cleaned.get("address_type")
        address = cleaned.get("address")
        is_primary = cleaned.get("is_primary")

        # If it is not yet associated with an entity, we do not validate it.
        if not self.instance.content_type_id or not self.instance.object_id:
            return cleaned

        qs = AddressAssignment.objects.filter(
            content_type=self.instance.content_type,
            object_id=self.instance.object_id,
            address_type=address_type,
        )

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if address and qs.filter(address=address).exists():
            raise forms.ValidationError(
                f"This entity already has this address assigned to the type {address_type.name}."
            )

        if address_type.is_unique_per_entity and qs.exists():
            raise forms.ValidationError(
                f"There can only be one address of type {address_type.name} for this entity."
            )

        if is_primary and qs.filter(is_primary=True).exists():
            raise forms.ValidationError(
                f"There is already a primary address for the type {address_type.name}."
            )

        return cleaned


# FormSet normal (NO inline)
AddressAssignmentFormSet = formset_factory(
    AddressAssignmentForm,
    extra=1,
    can_delete=True
)
