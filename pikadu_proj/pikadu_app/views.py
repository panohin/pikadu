from django.shortcuts import render, redirect
from .models import Post, Tag
from django.forms import modelform_factory
from .forms import CreatePostForm, CreateTagForm
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.all()
    title = "Последние посты"
    return render(request, 'pikadu_app/object_list.html',
                  context={'objects':posts,
                           'title':title}
                  )
def tag_list(request):
    tags = Tag.objects.all()
    title = "Список тэгов"
    return render(request, 'pikadu_app/object_list.html',
                  context={'objects':tags,
                           'title':title}
                  )

def post_detail(request, slug_from_request):
    post = Post.objects.get(slug=slug_from_request)
    return render(request, 'pikadu_app/post_detail.html',
                  context={'post':post}
                  )

def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            Post(title=form['title'].value(), body=form['body'].value()).save()
            return redirect('post_list')
        return HttpResponse('createpostform not valid')
    else:
        form = modelform_factory(Post, fields={'title':'Заголовок',
                                           'body': 'Текст поста',
                                           })
        title = 'Создание поста'
        return render(request, 'pikadu_app/create_post_form.html', context={'form':form,
                                                                        'title':title})

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
                      context={'form':form, 'title':'Создание тега'})
