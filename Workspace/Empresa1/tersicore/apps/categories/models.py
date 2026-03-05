from django.db import models
from django.utils import timezone

class CustomerCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    prefix = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="Optional prefix to generate customer_number (ej: VIP-, CORP-, etc.)"
    )

    sequence = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Customer Category"
        verbose_name_plural = "Customer Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def next_sequence(self):
        self.sequence += 1
        self.save(update_fields=["sequence"])
        return self.sequence



class ProductCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.name