"""Vues pour l'application lettings."""

from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """
    Vue pour l'index des locations.
    param request: La requête HTTP.
    return: La page index avec la liste des locations.
    """
    lettings = Letting.objects.select_related("address").all()
    return render(request, "lettings/index.html", {"lettings": lettings})


def detail(request, letting_id: int):
    """
    Vue pour le détail d'une location spécifique.
    param request: La requête HTTP.
    param letting_id: L'ID de la location à afficher.
    return: La page detail avec les informations de la location."""
    letting = get_object_or_404(
        Letting.objects.select_related("address"), id=letting_id
    )
    return render(request, "lettings/detail.html", {"letting": letting})
