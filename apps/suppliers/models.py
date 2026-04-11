from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from apps.addresses.models import AddressAssignment


class Supplier(models.Model):
    # Company fields
    company_name = models.CharField(max_length=255, blank=True, null=True)

    # Human person fields
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    # Optional: contact person for companies
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    address_assignments = GenericRelation(
        AddressAssignment,
        related_query_name="supplier"
    )
    activity = models.CharField(max_length=255, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["company_name", "last_name", "first_name"]

    def __str__(self):
        return self.display_name

    @property
    def display_name(self):
        """
        Returns the best possible name for the supplier:
        - Company name if available
        - Otherwise: First + Last name
        """
        if self.company_name:
            return self.company_name

        if self.first_name or self.last_name:
            return f"{self.first_name or ''} {self.last_name or ''}".strip()

        return "Unnamed Supplier"
