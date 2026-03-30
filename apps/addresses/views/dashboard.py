from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType
from ..models import AddressAssignment, AddressType


def address_dashboard(request):
    assignments = AddressAssignment.objects.select_related(
        "address", "address_type"
    ).all()

    # -------------------------
  #  GET FILTERS
    # -------------------------
    type_code = request.GET.get("type")
    country = request.GET.get("country")
    entity = request.GET.get("entity")
    primary = request.GET.get("primary")

    if type_code:
        assignments = assignments.filter(address_type__code=type_code)

    if country:
        assignments = assignments.filter(address__country__icontains=country)

    if entity:
        assignments = assignments.filter(content_type__model=entity.lower())

    if primary == "1":
        assignments = assignments.filter(is_primary=True)

    # -------------------------
    # ORDERING
    # -------------------------
    order = request.GET.get("order", "-created_at")
    assignments = assignments.order_by(order)

    # -------------------------
    # PAGINATION
    # -------------------------
    paginator = Paginator(assignments, 20)
    page = request.GET.get("page")
    assignments_page = paginator.get_page(page)

    # Types and entities available for filters
    types = AddressType.objects.all()
    entities = ContentType.objects.filter(
        model__in=["customer", "supplier"]
    )

    return render(
        request,
        "addresses/dashboard.html",
        {
            "assignments": assignments_page,
            "types": types,
            "entities": entities,
            "order": order,
        },
    )
