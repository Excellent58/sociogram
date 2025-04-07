from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.create_post, name='post'),
    path("like-post/", views.like_post, name='like-post'),
]
