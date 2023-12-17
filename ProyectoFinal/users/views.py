from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Avatar
from .forms import UserAvatar

# Create your views here.

class UserList(UserPassesTestMixin, ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"

    def test_func(self):
        return self.request.user.is_superuser # type: ignore


class UserDetail(DetailView):
    model = User
    template_name = "users/user-details.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['user']
        avatar = Avatar.objects.filter(user=user).last()
        context['avatar'] = avatar
        return context


class UserUpdate(UpdateView):
    model = User
    template_name = "users/user-edit.html"
    fields=["username", "first_name", "last_name", "email"]
    success_url = reverse_lazy("users:index")


class UserDelete(DeleteView):
    model = User
    template_name = "users/user-delete.html"
    success_url = reverse_lazy("users:index")


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            session = authenticate(username=username, password=password)
            login(request, session)
            return redirect('home:index')
        else:
            return render(request, "users/login.html", {"form": form})
            # return redirect('home:index')
        
    else:
        form = AuthenticationForm()
        return render(request, "users/login.html", {"form": form})
    

def register(request):

    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password1"]
            
            form.save()
            return redirect('home:index')
        
        else:
            print("invalid form")
            return render(request, "users/register.html", {"form": form})
    else:
        form = RegisterUserForm()

    return render(request, "users/register.html", {"form": form})



def upload_avatar(request):
    user = request.user
    avatar = ""
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user).last()

    if request.method == "GET":
        form = UserAvatar()
        return render(
            request, "users/user-avatar.html",
            context={"form": form, "user": user, "avatar": avatar}
        )
    
    else:
        form = UserAvatar(request.POST, request.FILES)
        if form.is_valid():
            modelo = Avatar(user=user, image=form.cleaned_data["image"])
            modelo.save()
            return redirect("home:index")
        



from django.contrib.auth.views import LogoutView
from django.views import View

class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            from django.contrib.auth import logout
            logout(request)
        return redirect('home:index')
    

