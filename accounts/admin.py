from django.contrib import admin

# Register your models here.
from . models import Profile, FollowersCount


admin.site.register(Profile)
admin.site.register(FollowersCount)
