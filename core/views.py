from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def index(request):
    return render(request, "index.html")


# upload an image
@login_required(login_url='signin')
def upload(request):
    pass

# search for users through usernames
@login_required(login_url='signin')
def search(request):
    pass

@login_required(login_url='signin')
def like_unlike_post(request):
    pass


# run tailwind - npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch