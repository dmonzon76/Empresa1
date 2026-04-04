from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import AddressAssignment
from ..forms.assignment import AddressAssignmentForm

class AssignmentListView(ListView):
    model = AddressAssignment
    template_name = "addresses/assignment_list.html"
    context_object_name = "object_list"
    ordering = ["-created_at"]

    def get_queryset(self):
        return (
            AddressAssignment.objects
            .select_related("address", "address_type")
            .order_by("-created_at")
        )

class AssignmentCreateView(CreateView):
    model = AddressAssignment
    form_class = AddressAssignmentForm
    template_name = "addresses/assignment_form.html"
    success_url = reverse_lazy("addresses:assignment_list")

class AssignmentUpdateView(UpdateView):
    model = AddressAssignment
    form_class = AddressAssignmentForm
    template_name = "addresses/assignment_form.html"
    success_url = reverse_lazy("addresses:assignment_list")

class AssignmentDeleteView(DeleteView):
    model = AddressAssignment
    template_name = "addresses/assignment_confirm_delete.html"
    success_url = reverse_lazy("addresses:assignment_list")
