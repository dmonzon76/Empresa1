from django.apps import AppConfig
import importlib


class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.inventory'

    def ready(self):
        importlib.import_module('apps.inventory.stock_signals')
        importlib.import_module('apps.inventory.cost_signals')
