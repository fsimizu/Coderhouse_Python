from django.shortcuts import render, redirect
from .models import Post
from users.models import Avatar 
from .forms import SearchForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

def about(req):
    avatar = ""
    if req.user.is_authenticated:
        avatar = Avatar.objects.filter(user=req.user).last()
    return render(req, "home/about.html", {"avatar": avatar})


class PostList(ListView):
    model = Post
    template_name = "home/index.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            avatar = Avatar.objects.filter(user=self.request.user).last()
            context['avatar'] = avatar
        return context
    

class FilteredPostList(ListView):
    model = Post
    template_name = "home/index.html"
    context_object_name = "posts"    
    # Para filtrar
    def get_queryset(self):
        queryset = super(FilteredPostList, self).get_queryset()
        search_term = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search_term) | queryset.filter(content__icontains=search_term)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            avatar = Avatar.objects.filter(user=self.request.user).last()
            context['avatar'] = avatar
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "home/post-detail.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            avatar = Avatar.objects.filter(user=self.request.user).last()
            context['avatar'] = avatar
        return context


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "home/confirm-delete.html"
    success_url = reverse_lazy("home:index")     
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            avatar = Avatar.objects.filter(user=self.request.user).last()
            context['avatar'] = avatar
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "home/post-new.html"
    fields=["title", "subtitle", "content", "imageUrl"]
    success_url = reverse_lazy("home:index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            avatar = Avatar.objects.filter(user=self.request.user).last()
            context['avatar'] = avatar
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "home/post-edit.html"
    fields=["title", "subtitle", "content", "imageUrl"]
    # success_url = reverse_lazy("home:index")
        
    def get_success_url(self):
        # Redirect to the detail view of the updated post
        return reverse_lazy('home:post-detail', kwargs={'pk': self.object.pk}) # type: ignore
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            avatar = Avatar.objects.filter(user=self.request.user).last()
            context['avatar'] = avatar
        return context