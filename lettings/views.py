from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    lettings = Letting.objects.select_related("address").all()
    return render(request, "lettings/index.html", {"lettings": lettings})


def detail(request, letting_id: int):
    letting = get_object_or_404(
        Letting.objects.select_related("address"), id=letting_id
    )
    return render(request, "lettings/detail.html", {"letting": letting})
