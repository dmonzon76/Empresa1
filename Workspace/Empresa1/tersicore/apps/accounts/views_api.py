# apps/accounts/views_api.py

from rest_framework.generics import RetrieveAPIView, ListAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer


class AccountListAPI(ListAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


class AccountDetailAPI(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"