from django.contrib import admin

# Register your models here.
from . models import Post, LikePost, Comment


admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(Comment)
