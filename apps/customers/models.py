from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from apps.addresses.models import AddressAssignment
from .utils import generate_customer_number

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    category = models.ForeignKey(
        "categories.CustomerCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="customers"
    )

    customer_number = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    address_assignments = GenericRelation(
        AddressAssignment,
        related_query_name="customer"
    )

    def save(self, *args, **kwargs):
        if not self.customer_number:
            self.customer_number = generate_customer_number(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_number} - {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def addresses(self):
        return self.address_assignments.select_related("address", "address_type")

    def primary_address(self, type_code=None):
        qs = self.addresses
        if type_code:
            qs = qs.filter(address_type__code=type_code)
        return qs.filter(is_primary=True).first()
