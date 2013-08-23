from django.conf import settings
from django.core.files import storage
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    subject = models.CharField(max_length=300)
    body = models.TextField()
    icon = models.ImageField(upload_to="icon/%Y/%m/%d/",
                             storage=storage.FileSystemStorage(),
                             blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
