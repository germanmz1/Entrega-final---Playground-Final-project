from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegisterForm


def signup_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:home")
    else:
        form = UserRegisterForm()

    return render(request, "accounts/signup.html", {"form": form})



class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


@login_required
def logout_view(request):
    logout(request)
    return redirect("core:home")


@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, "accounts/profile.html", {"profile": profile})


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        profile.avatar = request.FILES.get("avatar", profile.avatar)
        profile.bio = request.POST.get("bio", profile.bio)
        profile.fecha_nacimiento = request.POST.get(
            "fecha_nacimiento",
            profile.fecha_nacimiento
        )
        profile.save()
        return redirect("accounts:profile")

    return render(request, "accounts/edit_profile.html", {"profile": profile})