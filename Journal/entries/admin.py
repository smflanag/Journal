from django.contrib import admin
from entries.models import Post,User

# Register your models here.
admin.site.register(User)
admin.site.register(Post)