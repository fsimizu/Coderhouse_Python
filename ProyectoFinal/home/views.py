from django.shortcuts import render, redirect
from posts.models import Post
from .forms import SearchForm

# Create your views here.

def home(request):

    if request.method == "POST":
        # searched_posts = Post.objects.all()  
        searched_posts = {}
        searched_string = SearchForm(request.POST)

        if searched_string.is_valid():
            data = searched_string.cleaned_data
            searched_posts = Post.objects.filter(title__contains=data["title"])  
            print(searched_posts)
        return render(request, "home/index.html", {"posts": searched_posts})
    
    else:
        posts = Post.objects.all()  
        form = SearchForm()
        return render(request, "home/index.html", {"nav_form": form, "posts": posts})
