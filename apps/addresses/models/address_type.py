from django.db import models

class AddressType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_unique_per_entity = models.BooleanField(default=False)

    def __str__(self):
        return self.name
