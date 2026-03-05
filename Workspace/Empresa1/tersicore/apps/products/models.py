from django.db import models
from django.conf import settings
from decimal import Decimal
from django.utils import timezone
from apps.categories.models import ProductCategory


class Product(models.Model):

    UNIT_CHOICES = [
        ('unit', 'Unit'),
        ('kg', 'Kilograms'),
        ('g', 'Grams'),
        ('lt', 'Liters'),
        ('ml', 'Milliliters'),
    ]

    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('white', 'White'),
    ]

    name = models.CharField(max_length=150, verbose_name='Name', unique=True)

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products"
    )

    image = models.ImageField(
        upload_to='product/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='Image'
    )

    is_inventoried = models.BooleanField(default=True, verbose_name='¿Is inventoried?')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    pvp = models.DecimalField(default=Decimal("0.00"), max_digits=9, decimal_places=2, verbose_name='Sale price')

    quantity_type = models.CharField(max_length=10, choices=UNIT_CHOICES, default='unit', verbose_name='Quantity type')
    quantity_value = models.DecimalField(max_digits=10, decimal_places=2, default=1, verbose_name='Quantity value')

    color = models.CharField(max_length=20, choices=COLOR_CHOICES, blank=True, null=True, verbose_name='Color')
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)


    def __str__(self):
        category_name = self.category.name if self.category else "No category"
        return f"{self.name} ({category_name})"

    def get_image(self):
        if self.image:
            return f'{settings.MEDIA_URL}{self.image}'
        return f'{settings.STATIC_URL}img/empty.png'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']

        