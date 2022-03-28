from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_post', views.create_post, name='create_post_url'),
    path('create_tag', views.create_tag, name='create_tag_url'),
    path('enter_name', views.enter_name, name='enter_name_url'),
    path('tags', views.tag_list, name='tag_list_url'),
    path('', views.post_list, name='post_list'),
    path('post/<str:slug_from_request>', views.post_detail, name='post_detail_url'),
]
