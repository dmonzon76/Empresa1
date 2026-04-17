from django.db import models

# Create your models here.
from django.db import models


class PurchaseOrder(models.Model):
    number = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    supplier = models.ForeignKey(
        "suppliers.Supplier", on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        ordering = ["-date", "-id"]

    def __str__(self) -> str:
        return self.number
