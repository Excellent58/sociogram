from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages

from itertools import chain

from accounts.models import Profile, FollowersCount
from .models import Post
import random


@login_required(login_url="accounts:login")
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = []
    username = request.user.username

    try:
        user_profile = Profile.objects.get(user=user_object)
    except:
        print("profile does not exist")

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)

    for username in user_following_list:
        feed_list = Post.objects.filter(user=username)
        feed.append(feed_list)

    feed_list = list(chain(*feed))

    # get user that the current user is not following
    # that he/she might want to follow
    users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestions_list = [x for x in list(users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    # return user profile details
    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))
    print(user_profile)
    print(feed_list)
    print(suggestions_username_profile_list)

    return render(
        request,
        "index.html",
        {
            "username": username,
            "user_profile": user_profile,
            "posts": feed_list,
            "users_to_follow": suggestions_username_profile_list,
        },
    )


# upload an image
@login_required(login_url='accounts:signin')
def create_post(request):
    if request.method == "POST":
        current_user = request.user.username
        image = request.FILES.get('post_image')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=current_user, image=image, text=caption)
        new_post.save()
        messages.success(request, 'Post created successfully')

        return redirect('core:index')
    else:
        messages.error(request, 'Post not created')
        return redirect('core:index')

# search for users through usernames
@login_required(login_url='accounts:signin')
def search(request):
    # use advanced sql queries to search for user names
    pass

@login_required(login_url='accounts:signin')
def like_unlike_post(request):
    pass


# run tailwind - npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
