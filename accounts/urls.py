from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("profile/<str:username>/", views.profile, name='profile'),
    path("edit/", views.EditProfile, name="edit"),
    path("follow/", views.follow, name='follow')
]
