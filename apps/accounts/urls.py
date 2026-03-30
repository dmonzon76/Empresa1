from django.urls import path
from .views import (
    accounts_login,
    accounts_logout,
    accounts_register,
    accounts_profile,
)

app_name = "accounts"

urlpatterns = [
    path("login/", accounts_login, name="login"),
    path("logout/", accounts_logout, name="logout"),
    path("register/", accounts_register, name="register"),
    path("profile/", accounts_profile, name="profile"),
]
