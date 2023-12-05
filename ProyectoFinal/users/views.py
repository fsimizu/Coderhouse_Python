from django.shortcuts import render, redirect
from . import models, forms
from .models import User, Role

# Create your views here.

def users(request):
    # # llamada BBDD
    users = models.User.objects.all()
    context = {"users": users}

    return render(request, "users/index.html", context)


def login(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            print(request.POST)
            return redirect("users:login")
    else:
        form = forms.UserForm()

    return render(request, "users/login.html", {"form": form})



def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            role_name = "User"
            role, created = Role.objects.get_or_create(name=role_name)

            model = models.User(
                first_name=data["first_name"], 
                last_name=data["last_name"],
                email=data["email"],
                password=data["password"],
                role = role
                )
            
            print(request.POST)
            model.save()
            return redirect("/")
    else:
        form = forms.RegisterForm()

    return render(request, "users/register.html", {"form": form})