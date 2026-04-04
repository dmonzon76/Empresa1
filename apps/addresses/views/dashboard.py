from django.shortcuts import render
from ..models import Address, AddressType, AddressAssignment

def dashboard(request):
    return render(
        request,
        "addresses/dashboard.html",
        {
            "address_count": Address.objects.count(),
            "type_count": AddressType.objects.count(),
            "assignment_count": AddressAssignment.objects.count(),
            "recent_addresses": Address.objects.order_by("-id")[:5],
            "recent_assignments": AddressAssignment.objects.select_related("address", "address_type")[:5],
        },
    )

