from django import forms
from .models import Post, Tag, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

class CreateTagForm(forms.Form):
    name = forms.CharField()

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class EnterNameForm(forms.Form):
    name = forms.CharField()

class UpdateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
