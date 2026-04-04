from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .address import Address
from .address_type import AddressType

class AddressAssignment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    entity = GenericForeignKey("content_type", "object_id")

    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="assignments")
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE, related_name="assignments")

    is_primary = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Address Assignment"
        verbose_name_plural = "Address Assignments"
        unique_together = ("content_type", "object_id", "address", "address_type")

    def __str__(self):
        return f"{self.entity} → {self.address} ({self.address_type})"
