from django.db import models
from django.db.models import Model
from django.urls import reverse
from django.utils.text import slugify


class Post(Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(null=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug_from_request':self.slug})

    class Meta:
        ordering = ['-date_published']

class Tag(Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    posts = models.ManyToManyField(Post, related_name='tag')

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Comment(Model):
    body = models.TextField()
    likes = models.IntegerField(default=0, blank=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')

    def __str__(self):
        return self.body
