from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.inventory.models import InventoryMovement, InventoryItem


@receiver(post_save, sender=InventoryMovement)
def apply_movement_on_create(sender, instance, created, **kwargs):
    if not created:
        return

    item, _ = InventoryItem.objects.get_or_create(product=instance.product)

    if instance.movement_type == InventoryMovement.IN:
        item.quantity += instance.quantity

    elif instance.movement_type == InventoryMovement.OUT:
        item.quantity -= instance.quantity

    elif instance.movement_type == InventoryMovement.ADJUST:
        item.quantity = instance.quantity

    item.save()


@receiver(post_delete, sender=InventoryMovement)
def reverse_movement_on_delete(sender, instance, **kwargs):
    item, _ = InventoryItem.objects.get_or_create(product=instance.product)

    if instance.movement_type == InventoryMovement.IN:
        item.quantity -= instance.quantity

    elif instance.movement_type == InventoryMovement.OUT:
        item.quantity += instance.quantity

    elif instance.movement_type == InventoryMovement.ADJUST:
        return  # No revertimos ajuste
