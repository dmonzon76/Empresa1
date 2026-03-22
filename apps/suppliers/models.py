from django.db import models


class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    activity = models.CharField(max_length=255, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["company_name"]

        def __str__(self):
            return self.company_name
