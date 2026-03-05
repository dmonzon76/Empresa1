# accounts/urls.py
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.accounts_login, name="accounts-login"),
    path("logout/", views.accounts_logout, name="accounts-logout"),
    path("register/", views.accounts_register, name="accounts-register"),
    path("profile/", views.accounts_profile, name="accounts-profile"),
]