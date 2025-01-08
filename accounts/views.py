from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile


# follow and unfollow a user
@login_required(login_url="signin")
def follow_unfollow(request):
    pass

# render user profile
@login_required(login_url='login')
def profile(request):#include pk
    return render(request, 'profile.html')

@login_required(login_url='signin')
def EditProfile():
    pass

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
            return redirect('login')
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
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect("signup")
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
                return redirect("login")
        else:
            messages.info(request, 'passwords did not match')
            return redirect('signup')

    return render(request, "signup.html")


@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    return redirect("login")
