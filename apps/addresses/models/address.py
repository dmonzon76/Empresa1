from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["country", "city", "street"]

        def __str__(self):
            return self.full_address



    @property
    def full_address(self):
        parts = [
            self.street,
            self.city,
            self.state,
            self.country,
            self.postal_code,
        ]
        # Filtra None o strings vacíos
        parts = [p for p in parts if p]
        return ", ".join(parts)
