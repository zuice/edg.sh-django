from django.contrib.auth import login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect

from authentication.forms import CustomAuthenticationForm, CustomUserCreationForm


def login_view(request: HttpRequest):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")  # Redirect to home page after login

        print(form.errors)
    else:
        form = CustomAuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("/")


def register_view(request: HttpRequest):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")  # Redirect to home page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
