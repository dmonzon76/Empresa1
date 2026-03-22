# categories/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomerCategory, ProductCategory
from .forms import CustomerCategoryForm, ProductCategoryForm

# -------------------------
# CUSTOMER CATEGORIES
# -------------------------

class CustomerCategoryListView(ListView):
    model = CustomerCategory
    template_name = "categories/customers_list.html"
    context_object_name = "categories"


class CustomerCategoryCreateView(CreateView):
    model = CustomerCategory
    form_class = CustomerCategoryForm
    template_name = "categories/form.html"
    success_url = reverse_lazy("categories:customers_list")


class CustomerCategoryUpdateView(UpdateView):
    model = CustomerCategory
    form_class = CustomerCategoryForm
    template_name = "categories/form.html"
    success_url = reverse_lazy("categories:customers_list")


class CustomerCategoryDeleteView(DeleteView):
    model = CustomerCategory
    template_name = "categories/confirm_delete.html"
    success_url = reverse_lazy("categories:customers_list")


    
# -------------------------
# PRODUCT CATEGORIES
# -------------------------

class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = "categories/products_list.html"
    context_object_name = "categories"


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = "categories/form.html"
    success_url = reverse_lazy("categories:products_list")


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = "categories/form.html"
    success_url = reverse_lazy("categories:products_list")
    extra_context = {"title": "Edit Product Category"}

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = "categories/confirm_delete.html"
    success_url = reverse_lazy("categories:products_list")


    