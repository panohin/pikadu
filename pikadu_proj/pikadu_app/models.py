from django.db import models
from django.db.models import Model
from django.urls import reverse
from django.utils.text import slugify


class Post(Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
<<<<<<< HEAD
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True,
        allow_unicode=True
        )
    date_published = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(null=True, blank=True)
=======
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(null=True)
    tags = models.ManyToManyField('Tag', related_name='post', blank=True)

>>>>>>> 52a8c5cbf912c7458ac4ee7acdcd84e0bd1e96d7

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug_from_request':self.slug})

    def get_update_url(self):
        return reverse('update_post_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('delete_post_url', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-date_published']

class Tag(Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Comment(Model):
    body = models.TextField()
    likes = models.IntegerField(default=0, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True)

    def __str__(self):
        return self.body

    def get_update_url(self):
        return reverse('update_comment_url', kwargs={'slug':self.slug,
                                                     'comment_id':self.id})
