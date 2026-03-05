
from django.db import models
from apps.customers.models import Customer

app_name = "apps/addresses"

class CustomerAddress(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="addresses"
    )

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    is_primary = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Customer Address"
        verbose_name_plural = "Customer Addresses"
        ordering = ["-is_primary", "customer"]

    def __str__(self):
        return f"{self.address} ({self.customer})"