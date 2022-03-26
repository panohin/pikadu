from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tags', views.tag_list, name='tag_list_url'),
    path('<str:slug_from_request>', views.post_detail, name='post_detail_url'),
    path('', views.post_list, name='post_list'),
]
