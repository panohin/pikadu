from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_post', views.create_post, name='create_post_url'),
    path('create_tag', views.create_tag, name='create_tag_url'),
    path('tags', views.TagList.as_view(), name='tag_list_url'),
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<str:slug_from_request>', views.post_detail, name='post_detail_url'),
]
