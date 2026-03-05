from django.db import models
from django.utils import timezone
# Create your models here.


class SalesOrder(models.Model):
    # Possible states of the order
    DRAFT = "DRAFT"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

    STATUS_CHOICES = [
        (DRAFT, "Borrador"),
        (CONFIRMED, "Confirmada"),
        (CANCELLED, "Cancelada"),
    ]

    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.PROTECT,
        related_name="sales_orders"
    )

    date = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=DRAFT
    )

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-id"]
        verbose_name = "Sales Order"
        verbose_name_plural = "Sales Orders"

    def __str__(self):
        return f"Orden #{self.id} - {self.customer}"

    @property
    def total_amount(self):
        return sum(item.subtotal for item in self.items.all())

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    def confirm(self):
        """Confirm the order (Billing will then convert it into an invoice)."""
        self.status = self.CONFIRMED
        self.save()

    def cancel(self):
        """Cancel the order (if it has not yet been invoiced)."""
        self.status = self.CANCELLED
        self.save()


class SalesOrderItem(models.Model):
    order = models.ForeignKey(
        SalesOrder,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.PROTECT
    )

    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.product} x {self.quantity}"

    @property
    def subtotal(self):
        return self.quantity * self.price
