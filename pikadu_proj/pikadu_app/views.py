from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from .models import Post, Tag, Comment
from django.forms import modelform_factory
from .forms import CreatePostForm, CreateTagForm, EnterNameForm, AddComment, UpdateComment
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
        form = CreatePostForm()
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

def update_post(request, slug):
    if request.POST:
        form = CreatePostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post.objects.get(slug=slug)
            post.title = data['title']
            post.body = data['body']
            post.save()
            return render(request, 'pikadu_app/post_detail.html', context={'post':post})
    else:
        post = Post.objects.get(slug=slug)
        data = {
            'title': post.title,
            'body': post.body
        }
        form = CreatePostForm(data)
        title = 'Редактирование поста'
        return render(request, 'pikadu_app/update_post.html', context={'form': form,
                                                                        'title': title,
                                                                       'post':post})

def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    return redirect('post_list')

def add_comment(request, slug):
    post = Post.objects.get(slug=slug)
    if request.POST:
        form = AddComment(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(post_id=post.id, body=data['body'])
            return redirect('post_list')
        else:
            return HttpResponse('form AddComment is not valid')
    else:
        form = AddComment()
        title = 'Добавить комментарий'
        return render(request, 'pikadu_app/add_comment.html', context={'post':post,
                                                                       'form':form,
                                                                       'title':title})

def update_comment(request, slug, comment_id):
    post = Post.objects.get(slug=slug)
    comment = Comment.objects.get(id=comment_id)
    if request.POST:
        form = UpdateComment(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment.body = data['body']
            comment.save()
            return redirect('post_detail_url', slug)
    else:
        form = AddComment({'body':comment.body})
        title = 'Редактировать комментарий'
        return render(request, 'pikadu_app/update_comment.html', context={'post':post,
                                                                       'form':form,
                                                                       'title':title})

def delete_comment(request, slug, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect('post_detail_url', slug)

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
