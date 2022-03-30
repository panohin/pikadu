from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Post, Tag, Comment
from django.forms import modelform_factory
from .forms import CreatePostForm, CreateTagForm, EnterNameForm
from django.http import HttpResponse
from .utils import ObjectListMixin



class PostList(ObjectListMixin, View):
    object_model = Post
    title = "Последние посты"
    template = 'pikadu_app/object_list.html'

class TagList(ObjectListMixin, View):
    object_model = Tag
    title = "Список тэгов"
    template = 'pikadu_app/object_list.html'


def post_detail(request, slug_from_request):
    post = Post.objects.get(slug=slug_from_request)
    return render(request, 'pikadu_app/post_detail.html',
                  context={'post': post}
                  )


def create_post(request):
    model = Post
    form = CreatePostForm
    title = 'Создание поста'
    form_template = 'pikadu_app/create_post_form.html'

    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            Post(title=form['title'].value(), body=form['body'].value()).save()
            return redirect('post_list')
        return HttpResponse('createpostform not valid')
    else:
        form = CreatePostForm
        title = 'Создание поста'
        return render(request, 'pikadu_app/create_post_form.html', context={'form': form,
                                                                            'title': title})

def create_tag(request):
    if request.POST:
        form = CreateTagForm(request.POST)
        if form.is_valid():
            Tag(name=form['name'].value()).save()
            return redirect('tag_list_url')
        else:
            return HttpResponse('createtagform not valid')
    else:
        form = CreateTagForm()
        return render(request, 'pikadu_app/create_tag_form.html',
                      context={'form': form, 'title': 'Создание тега'})

def enter_name(request):
    if request.POST:
        form = EnterNameForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data.name)
    else:
        title = 'Введите имя'
        current_name = 'Pavel'
        form = EnterNameForm()
        return render(request, 'pikadu_app/enter_name.html', context={'title':title,
                                                                      'current_name':current_name,
                                                                      'form':form})
