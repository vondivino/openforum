from django.db import models

from django.contrib.auth.models import User

class Forum(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.title

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