from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_post', views.create_post, name='create_post_url'),
    path('create_tag', views.create_tag, name='create_tag_url'),
    path('tags', views.tag_list, name='tag_list_url'),
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<slug:url>', views.PostDetail.as_view(), name='post_detail_url'),
]
