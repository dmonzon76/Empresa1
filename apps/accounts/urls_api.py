from django.urls import path
from .views_api import AccountListAPI, AccountDetailAPI

urlpatterns = [
    path("", AccountListAPI.as_view(), name="api-account-list"),
    path("<int:pk>/", AccountDetailAPI.as_view(), name="api-account-detail"),
]