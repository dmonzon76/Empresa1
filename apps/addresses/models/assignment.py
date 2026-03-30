from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .address import Address
from .address_type import AddressType


class AddressAssignment(models.Model):
    # Generic relation to ANY entity (Supplier, Customer, etc.)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    entity = GenericForeignKey("content_type", "object_id")

    # Assigned address
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE)

    # Flags
    is_primary = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Address Assignment"
        verbose_name_plural = "Address Assignments"

    def __str__(self):
        return f"{self.entity} → {self.address} ({self.address_type})"
