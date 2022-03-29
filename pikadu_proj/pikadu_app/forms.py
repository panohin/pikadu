from django import forms
from .models import Post, Tag, Comment

class CreatePostForm(forms.Form):
    model = Post
    title = forms.CharField()
    body = forms.Field()

class CreateTagForm(forms.Form):
    name = forms.CharField()
