from django.db import models
from apps.customers.models import Customer
from apps.products.models import Product


class SalesOrder(models.Model):
    DRAFT = "DRAFT"
    CONFIRMED = "CONFIRMED"

    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (CONFIRMED, "Confirmed"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True, null=True)

    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT)

    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Order #{self.id}"

    def recalculate_total(self):
        total = sum(item.subtotal() for item in self.items.all())
        self.total = total
        self.save()


class SalesOrderItem(models.Model):
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.product} x {self.quantity}"
