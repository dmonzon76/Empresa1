from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, "placeholders/module_placeholder.html", {
        "module_name": "Reports",
        "description": "Analytics, KPIs, and business intelligence."
    })
