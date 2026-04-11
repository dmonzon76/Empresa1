from django.db import models


class AddressType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_unique_per_entity = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "Address Type"
        verbose_name_plural = "Address Types"

        def __str__(self):
            return str(self.name)

    # ---------------------------------------------------------
    # CONS BY TYPE (Bootstrap Icons)
    # Compatible with your numeric codes and real names
    # ---------------------------------------------------------
    @property
    def icon(self):
        code = str(self.code or "").strip()
        name = str(self.name or "").strip().upper()

        # --- Fiscal (code=1) ---
        if code == "1" or "FISCAL" in name:
            return "bi bi-receipt"

        # --- Company Supplier (code=2) ---
        if code == "2" or "COMPANY" in name:
            return "bi bi-building"

        # --- Customer Supplier (code=3) ---
        if code == "3" or "CUSTOMER" in name:
            return "bi bi-people"

        # --- Natural Person (code=5) ---
        if code == "5" or "PERSON" in name:
            return "bi bi-person"

        # --- Supplier (code=6) ---
        if code == "6" or "SUPPLIER" in name:
            return "bi bi-briefcase"

        # --- Factory (code=8) ---
        if code == "8" or "FACTORY" in name or "PLANT" in name:
            return "bi bi-gear-wide-connected"

        # Default
        return "bi bi-geo-alt"

    # ---------------------------------------------------------
    # COLORS BY TYPE (Bootstrap text colors)
    # ---------------------------------------------------------
    @property
    def color(self):
        code = str(self.code or "").strip()
        name = str(self.name or "").strip().upper()

        if code == "1" or "FISCAL" in name:
            return "text-success"      # Green
        if code == "2" or "COMPANY" in name:
            return "text-primary"      # Blue
        if code == "3" or "CUSTOMER" in name:
            return "text-info"         # Cyan
        if code == "5" or "PERSON" in name:
            return "text-danger"       # Red
        if code == "6" or "SUPPLIER" in name:
            return "text-dark"         # Dark
        if code == "8" or "FACTORY" in name or "PLANT" in name:
            return "text-secondary"    # Secondary

        return "text-muted"            # Default
