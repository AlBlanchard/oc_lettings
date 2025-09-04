from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    profiles_list = Profile.objects.select_related("user").all()
    return render(request, "profiles/index.html", {"profiles_list": profiles_list})


def detail(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile.objects.select_related("user"), user=user)
    return render(request, "profiles/detail.html", {"profile": profile})
