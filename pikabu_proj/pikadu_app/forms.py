from django import forms
from .models import Post, Tag

class CreatePostForm(forms.Form):
    title = forms.CharField()
    body = forms.Field()

class CreateTagForm(forms.Form):
    name = forms.CharField()
