from django.db import models
from django.contrib.auth.models import User
from apps.customers.models import Customer

# Create your models here




class Account(models.Model):
    user = models.OneToOneField (User,on_delete=models.CASCADE,related_name="account")
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True,related_name="system_accounts")
    role = models.CharField(max_length=50,choices=[
            ("admin", "Administrador"),
            ("operator", "Operador"),
            ("viewer", "Solo lectura"),
        ],
        default="viewer"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} ({self.role})"