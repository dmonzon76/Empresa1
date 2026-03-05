from django.db import models
from django.utils import timezone
from .utils import generate_customer_number


class Customer(models.Model):
    # Basic identity
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    # Dynamic category
    category = models.ForeignKey(
        # the category model lives in the categories app, not customers
        "categories.CustomerCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="customers"
    )

    # Internal identifier
    customer_number = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    # Metadata
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # State
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.customer_number:
            self.customer_number = generate_customer_number(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_number} - {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"