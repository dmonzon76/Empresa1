# accounts/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

def accounts_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard:index")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def accounts_logout(request):
    logout(request)
    return render(request, "accounts/logout.html")

def accounts_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard:index")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def accounts_profile(request):
    return render(request, "accounts/profile.html")