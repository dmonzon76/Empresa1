from django.shortcuts import render
from .models import CustomerAddress


def address_list(request):
    addresses = CustomerAddress.objects.select_related("customer").all()

    return render(
        request,
        "addresses/list.html",
        {"addresses": addresses},
    )
