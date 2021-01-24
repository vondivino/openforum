from django.contrib import admin

from forums.models import Forum, Discussion, Comment 

admin.site.register(Forum)
admin.site.register(Discussion)
admin.site.register(Comment)
