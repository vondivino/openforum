from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Forum(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(null=False, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum-detail', kwargs={'slug':self.slug})

class Discussion(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    forum = models.ForeignKey(
        Forum,
        on_delete=models.CASCADE
    )
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discussion-detail', kwargs={'slug':self.slug})

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    discussion = models.ForeignKey(
        Discussion,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.body[:50]

    def get_absolute_url(self):
        return reverse('discussion-detail', kwargs={'slug': self.discussion.slug})