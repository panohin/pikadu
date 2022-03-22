from django.db import models
from django.db.models import Model
from django.utils.text import slugify


class Post(Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)
    date_published = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_published']



