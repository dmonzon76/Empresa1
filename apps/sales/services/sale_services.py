from django.db import transaction
from django.core.exceptions import ValidationError
from apps.sales.models import SalesOrder, SalesOrderItem
from apps.inventory.services.stock_service import StockService  # futuro módulo
from apps.products.models import Product


class SalesService:

    # ============================
    # CREATE ORDER
    # ============================
    @staticmethod
    def create_order(customer, notes=""):
        return SalesOrder.objects.create(
            customer=customer,
            notes=notes
        )

    # ============================
    # ADD ITEM TO ORDER
    # ============================
    @staticmethod
    def add_item(order: SalesOrder, product: Product, quantity, price=None):
        if order.status != SalesOrder.DRAFT:
            raise ValidationError("Only draft items can be added.")

        if price is None:
            price = product.price

        return SalesOrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price
        )

    # ============================
    # DELETE ITEM
    # ============================
    @staticmethod
    def delete_item(item: SalesOrderItem):
        if item.order.status != SalesOrder.DRAFT:
            raise ValidationError("Items cannot be removed from a confirmed order.")
        item.delete()

    # ============================
    # CHECK STOCK (before confirming)
    # ============================
    @staticmethod
    def validate_stock(order: SalesOrder):
        """
        Verify that there is sufficient stock for each product.
        It does not deduct stock, it only validates it.
        """
        for item in order.items.all():
            stock = StockService.get_stock(item.product)
            if stock < item.quantity:
                raise ValidationError(
                    f"Insufficient stock for {item.product.name}. "
                    f"Available: {stock}, requested: {item.quantity}"
                )
        return True

    # ============================
    # CONFIRM ORDER
    # ============================
    @staticmethod
    @transaction.atomic
    def confirm_order(order: SalesOrder):
        if order.status != SalesOrder.DRAFT:
            raise ValidationError("The order has already been confirmed or cancelled..")

        # Check stock before confirming
        SalesService.validate_stock(order)

        # Confirm order
        order.status = SalesOrder.CONFIRMED
        order.save()

        return order

    # ============================
    # PREPARE ORDER FOR BILLING
    # ============================
    @staticmethod
    def prepare_for_invoicing(order: SalesOrder):
        """
        It returns a dictionary ready to create an invoice. 
        Billing then converts it to an invoice.
        """
        if order.status != SalesOrder.CONFIRMED:
            raise ValidationError("Only confirmed orders can be invoiced..")

        return {
            "customer": order.customer,
            "items": [
                {
                    "product": item.product,
                    "quantity": item.quantity,
                    "price": item.price,
                    "subtotal": item.subtotal,
                }
                for item in order.items.all()
            ],
            "total": order.total_amount,
            "order_id": order.id,
        }