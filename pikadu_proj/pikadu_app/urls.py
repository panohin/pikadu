from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/<str:slug_from_request>', views.post_detail, name='post_detail_url'),
    path('post/<str:slug>/update', views.update_post, name='update_post_url'),
    path('post/<str:slug>/add_comment', views.add_comment, name='add_comment_url'),
    path('post/<str:slug>/<int:comment_id>', views.update_comment, name='update_comment_url'),
    path('post/<str:slug>/<int:comment_id>/delete', views.delete_comment, name='delete_comment_url'),
    path('post/<str:slug>/delete', views.delete_post, name='delete_post_url'),
    path('enter_name', views.enter_name, name='enter_name_url'),
    path('create_post', views.create_post, name='create_post_url'),
    path('create_tag', views.create_tag, name='create_tag_url'),
<<<<<<< HEAD
    path('tags', views.tag_list, name='tag_list_url'),
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<slug:url>', views.PostDetail.as_view(), name='post_detail_url'),
=======
    path('tags', views.TagList.as_view(), name='tag_list_url'),
    path('', views.PostList.as_view(), name='post_list'),
>>>>>>> 52a8c5cbf912c7458ac4ee7acdcd84e0bd1e96d7
]
