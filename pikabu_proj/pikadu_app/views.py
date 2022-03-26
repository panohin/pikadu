from django.shortcuts import render
from .models import Post, Tag

def post_list(request):
    posts = Post.objects.all()
    title = "Последние посты"
    return render(request, 'pikadu_app/object_list.html',
                  context={'objects':posts,
                           'title':title}
                  )

def post_detail(request, slug_from_request):
    post = Post.objects.get(slug=slug_from_request)
    return render(request, 'pikadu_app/post_detail.html',
                  context={'post':post}
                  )

def tag_list(request):
    tags = Tag.objects.all()
    title = "Список тэгов"
    return render(request, 'pikadu_app/object_list.html',
                  context={'objects':tags,
                           'title':title}
                  )
