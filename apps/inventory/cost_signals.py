from apps.products.models import Product
from apps.inventory.models import InventoryMovement, InventoryItem
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=InventoryMovement)
def update_average_cost(sender, instance, created, **kwargs):
    """
    Recalcula el costo promedio cuando entra stock.
    Solo aplica para movimientos tipo IN.
    """
    if not created:
        return

    if instance.movement_type != InventoryMovement.IN:
        return

    product = instance.product
    item, _ = InventoryItem.objects.get_or_create(product=product)

    previous_stock = item.quantity - instance.quantity
    previous_cost = product.average_cost or 0
    incoming_cost = instance.unit_cost

    # Primera compra o stock previo cero
    if previous_stock <= 0:
        product.average_cost = incoming_cost
    else:
        product.average_cost = (
            (previous_stock * previous_cost) +
            (instance.quantity * incoming_cost)
        ) / (previous_stock + instance.quantity)

    product.save()
