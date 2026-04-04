from django.apps import AppConfig

class AddressesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.addresses"
    verbose_name = "Addresses"

    # Uncomment if you add signals in the future
    # def ready(self):
    #     import tersicore.apps.addresses.signals
