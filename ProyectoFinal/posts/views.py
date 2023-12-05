from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post, User
from django.utils import timezone

# Create your views here.

def posts(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user_email = "fersimizu@gmail.com"
            user, created = User.objects.get_or_create(email=user_email)

            model = Post(
                title=data["title"], 
                imageUrl=data["imageUrl"],
                content=data["content"],
                user = user
                )
            
            print(request.POST)
            model.save()
            return redirect("/")
        else:
            print("form not valid")
    else:
        form = PostForm()
    return render(request, "posts/index.html", {"form": form})

# def register(request):
#     if request.method == "POST":
#         form = forms.RegisterForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data

#             role_name = "User"
#             role, created = Role.objects.get_or_create(name=role_name)

#             model = models.User(
#                 first_name=data["first_name"], 
#                 last_name=data["last_name"],
#                 email=data["email"],
#                 password=data["password"],
#                 role_id = role
#                 )
            
#             print(request.POST)
#             model.save()
#             return redirect("/")
#     else:
#         form = forms.RegisterForm()

#     return render(request, "users/register.html", {"form": form})