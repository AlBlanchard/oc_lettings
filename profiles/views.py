"""Vues pour l'application profiles."""

from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.models import User


def index(request):
    """Vue index pour afficher la liste des profils.
    param request: La requête HTTP.
    return: La page index avec la liste des profils.
    """
    profiles_list = Profile.objects.select_related("user").all()
    return render(request, "profiles/index.html", {"profiles_list": profiles_list})


def detail(request, username):
    """Vue detail pour afficher un profil spécifique.
    param request: La requête HTTP.
    param username: Le nom d'utilisateur du profil à afficher.
    return: La page detail avec les informations du profil.
    """
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile.objects.select_related("user"), user=user)
    return render(request, "profiles/detail.html", {"profile": profile})
