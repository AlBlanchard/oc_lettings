from django.shortcuts import render
from profiles.models import Profile
from lettings.models import Letting


def index(request):
    return render(request, "index.html")
