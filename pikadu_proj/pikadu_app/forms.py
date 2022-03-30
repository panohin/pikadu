from django import forms
from .models import Post, Tag, Comment

class CreatePostForm(forms.Form):
    model = Post
    title = forms.CharField()
    body = forms.Field()

class CreateTagForm(forms.Form):
    name = forms.CharField()

class EnterNameForm(forms.Form):
    name = forms.CharField()

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
