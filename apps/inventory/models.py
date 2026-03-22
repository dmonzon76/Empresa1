from django.db import models
from apps.products.models import Product


class InventoryItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    min_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory Items"

    def __str__(self):
        return f"{self.product.name} — {self.quantity}"

    def is_below_min(self):
        return self.quantity < self.min_stock


class InventoryMovement(models.Model):
    IN = "IN"
    OUT = "OUT"
    ADJUST = "ADJUST"

    MOVEMENT_TYPES = [
        (IN, "entry"),
        (OUT, "exit"),
        (ADJUST, "balance"),
    ]

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Unit cost"
    )
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Inventory Movement"
        verbose_name_plural = "Inventory Movements"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.movement_type} — {self.product.name} — {self.quantity}"

    def apply(self):
        item, created = InventoryItem.objects.get_or_create(product=self.product)

        if self.movement_type == self.IN:
            item.quantity += self.quantity

        elif self.movement_type == self.OUT:
            item.quantity -= self.quantity

        elif self.movement_type == self.ADJUST:
            item.quantity = self.quantity

        item.save()


class InventoryRule(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    min_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Inventory Rule"
        verbose_name_plural = "Inventory Rules"

    def __str__(self):
        return f"Rules for {self.product.name}"
