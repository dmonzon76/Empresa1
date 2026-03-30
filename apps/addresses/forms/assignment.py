from django import forms
from django.contrib.contenttypes.models import ContentType
from ..models import AddressAssignment


class AddressAssignmentForm(forms.ModelForm):
    class Meta:
        model = AddressAssignment
        fields = "__all__"

    def clean(self):
        cleaned = super().clean()

        entity_ct = cleaned.get("content_type")
        entity_id = cleaned.get("object_id")
        address = cleaned.get("address")
        address_type = cleaned.get("address_type")
        is_primary = cleaned.get("is_primary")

        if not entity_ct or not entity_id or not address_type:
            return cleaned

        qs = AddressAssignment.objects.filter(
            content_type=entity_ct,
            object_id=entity_id,
            address_type=address_type,
        )

        # Avoid duplicating the same address for the same entity
        if address and qs.filter(address=address).exists():
            raise forms.ValidationError(
                    f"This entity already has this address assigned to the type {address_type.name}")

        # If the type is unique per entity
        if address_type.is_unique_per_entity and qs.exists():
            raise forms.ValidationError(
                f"There can only be one address of type {address_type.name} for this entity."
            )

        # Only one primary per type
        if is_primary:
            if qs.filter(is_primary=True).exists():
                raise forms.ValidationError(
                    f"Already exists a primary address for the type {address_type.name}."
                )

        return cleaned
