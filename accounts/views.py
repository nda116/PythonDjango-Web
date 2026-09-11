from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegisterForm, UserUpdateForm

def register(request):
    if request.user.is_authenticated:
        return redirect("library:book-list")

    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Registration completed successfully.")
        return redirect("library:book-list")

    return render(request, "accounts/register.html", {"form":form})

@login_required
def profile(request):
    form = UserUpdateForm(request.POST or None, instance=request.user)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("accounts:profile") 

    return render(request, "accounts/profile.html", {"form": form})