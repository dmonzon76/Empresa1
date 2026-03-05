from django import forms
from .models import SalesOrder, SalesOrderItem
from apps.products.models import Product


# ============================
# SALES ORDER FORM
# ============================
class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ["customer", "notes"]

        widgets = {
        "customer": forms.Select(attrs={"class": "form-control"}),
        "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
}


# ============================
# ORDER ITEM FORM
# ============================
class SalesOrderItemForm(forms.ModelForm):
    class Meta:
        model = SalesOrderItem
        fields = ["product", "quantity", "price"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ordenar productos alfabéticamente
        self.fields["product"].queryset = Product.objects.all().order_by("name")

        # Si el producto viene del POST, sugerir precio
        if "product" in self.data:
            try:
                product_id = int(self.data.get("product"))
                product = Product.objects.get(id=product_id)
                self.fields["price"].initial = product.price
            except (ValueError, Product.DoesNotExist):
                pass

        # Si estamos editando un item existente
        elif self.instance.pk:
            self.fields["price"].initial = self.instance.price