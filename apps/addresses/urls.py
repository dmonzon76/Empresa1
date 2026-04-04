from django.urls import path
from .views.dashboard import dashboard
from .views.addresses import (
    AddressListView,
    AddressCreateView,
    AddressUpdateView,
    AddressDeleteView,
    AddressDetailView,
)
from .views.address_type import (
    AddressTypeListView,
    AddressTypeCreateView,
    AddressTypeUpdateView,
    AddressTypeDeleteView,
)
from .views.assignment import (
    AssignmentListView,
    AssignmentCreateView,
    AssignmentUpdateView,
    AssignmentDeleteView,
)

app_name = "addresses"

urlpatterns = [
    # Dashboard
    path("dashboard/", dashboard, name="dashboard"),

    # Addresses
    path("list/", AddressListView.as_view(), name="address_list"),
    path("create/", AddressCreateView.as_view(), name="address_create"),
    path("<int:pk>/", AddressDetailView.as_view(), name="address_detail"),
    path("<int:pk>/edit/", AddressUpdateView.as_view(), name="address_edit"),
    path("<int:pk>/delete/", AddressDeleteView.as_view(), name="address_delete"),

    # Address Types
    path("types/", AddressTypeListView.as_view(), name="type_list"),
    path("types/create/", AddressTypeCreateView.as_view(), name="type_create"),
    path("types/<int:pk>/edit/", AddressTypeUpdateView.as_view(), name="type_edit"),
    path("types/<int:pk>/delete/", AddressTypeDeleteView.as_view(), name="type_delete"),

    # Assignments
    path("assignments/", AssignmentListView.as_view(), name="assignment_list"),
    path("assignments/create/", AssignmentCreateView.as_view(), name="assignment_create"),
    path("assignments/<int:pk>/edit/", AssignmentUpdateView.as_view(), name="assignment_edit"),
    path("assignments/<int:pk>/delete/", AssignmentDeleteView.as_view(), name="assignment_delete"),
]
