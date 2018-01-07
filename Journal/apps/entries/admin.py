from django.contrib import admin

from Journal.apps.entries.models import User, Post

admin.site.register(User)
admin.site.register(Post)