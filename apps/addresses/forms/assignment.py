from django import forms
from django.contrib.contenttypes.models import ContentType
from ..models import AddressAssignment

class AddressAssignmentForm(forms.ModelForm):
    class Meta:
        model = AddressAssignment
        fields = [
            "content_type",
            "object_id",
            "address",
            "address_type",
            "is_primary",
        ]

    def clean(self):
        cleaned = super().clean()

        content_type = cleaned.get("content_type")
        object_id = cleaned.get("object_id")
        address = cleaned.get("address")
        address_type = cleaned.get("address_type")
        is_primary = cleaned.get("is_primary")

        if not content_type or not object_id or not address_type:
            return cleaned

        qs = AddressAssignment.objects.filter(
            content_type=content_type,
            object_id=object_id,
            address_type=address_type,
        )

        # Exclude your own record from editing

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        # 1) Avoid duplicating the same address for the same entity + type

        if address and qs.filter(address=address).exists():
            raise forms.ValidationError(
                f"This entity already has this address assigned to the type {address_type.name}."
            )

        # 2) If the type is unique per entity, ensure there is only one address of that type for the entity
        if address_type.is_unique_per_entity and qs.exists():
            raise forms.ValidationError(
                f"There can only be one address of type {address_type.name} for this entity."
            )

        # 3) Only one primary per type
        if is_primary and qs.filter(is_primary=True).exists():
            raise forms.ValidationError(
                f"There is already a primary address for the type {address_type.name}."
            )

        return cleaned
