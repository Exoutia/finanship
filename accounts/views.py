from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    print(request)
    user = User.objects.get(username=request.user)
    return render(request, "profile.html", {"user": user})


@login_required
def index(request):
    return HttpResponse(b"Hello, world. You're at the accounts index.")
