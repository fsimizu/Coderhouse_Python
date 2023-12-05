from django import forms
from posts.models import Post

class SearchForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title"]

