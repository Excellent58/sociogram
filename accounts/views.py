from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse
from .models import Profile, FollowersCount
from core.models import Post


# render user profile
@login_required(login_url='accounts:login')
def profile(request, username):
    pk = User.objects.get(username=username).id
    user_object = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.filter(user=user_object)   

    number_of_posts = len(posts)

    follower = request.user.username
    user = username

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'unfollow'
    else:
        button_text = 'follow'

    print(f"user_followers: {len(FollowersCount.objects.filter(user=user))}")
    print(f"user_following: {len(FollowersCount.objects.filter(follower=user))}")
    user_followers = len(FollowersCount.objects.filter(user=user))
    user_following = len(FollowersCount.objects.filter(follower=user))
    print(f'button: {button_text}')

    context = {
        "user_object": user_object,
        "user_profile": user_profile,
        "user_posts": posts,
        "number_of_posts": number_of_posts,
        'button_text': button_text,
        "user_followers": user_followers,
        "user_following": user_following,
    }

    return render(request, 'profile.html', context)

@login_required(login_url='accounts:signin')
def EditProfile():
    pass

@login_required(login_url='accounts:login')
def follow(request):
    if request.method == "POST":
        follower = request.POST['follower']
        user = request.POST['user']

        print(f"follower: {follower}, User: {user}")

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            print(f"unfollow: {delete_follower}")
            delete_follower.delete()
            return redirect(reverse("accounts:profile", args=[user]))
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            print(f"follow: {new_follower}")
            new_follower.save()
            return redirect(reverse('accounts:profile', args=[user]))
    else:
        return redirect('/')

# allow user to setup his/her profile after registering
# @login_required(login_url='signin')
# def settings(request):
#     pass
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('accounts:login')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect("accounts:signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect("accounts:signup")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id
                )
                new_profile.save()
                return redirect("core:index")
        else:
            messages.info(request, 'passwords did not match')
            return redirect('accounts:signup')

    return render(request, "signup.html")


@login_required(login_url="accounts:login")
def logout(request):
    auth.logout(request)
    return redirect("accounts:login")
