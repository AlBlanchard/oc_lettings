"""Vues pour oc_lettings_site."""

from django.shortcuts import render
from .utils.audit_decorator import audit_command


@audit_command(category="base_app", action="view_index")
def index(request):
    """
    Page d'accueil.
    param request: La requête HTTP
    return: La page d'accueil
    """
    return render(request, "index.html")


# --- Personnalisation des pages d'erreurs 404 et 500 ---


def _render_error(request, code: int, title: str, message: str):
    """
    Affiche une page d'erreur personnalisée.
    param request: La requête HTTP
    param code: Le code d'erreur HTTP
    param title: Le titre de l'erreur
    param message: Le message d'erreur
    return: La page d'erreur
    """
    ctx = {"code": code, "title": title, "message": message}
    return render(request, "error.html", ctx, status=code)


def error_404(request, exception):
    """
    Page d'erreur 404.
    param request: La requête HTTP
    param exception: L'exception levée
    return: La page d'erreur 404
    """
    return _render_error(
        request,
        404,
        "Page introuvable",
        f"La page demandée n'existe pas : {request.get_full_path()}",
    )


def error_500(request):
    """
    Page d'erreur 500.
    param request: La requête HTTP
    return: La page d'erreur 500
    """
    return _render_error(
        request, 500, "Erreur serveur", "Un problème est survenu de notre côté."
    )


def boom(request):
    """
    Fonction de test pour provoquer une erreur 500.
    param request: La requête HTTP
    return: La page d'accueil
    """
    raise ZeroDivisionError("boom")
