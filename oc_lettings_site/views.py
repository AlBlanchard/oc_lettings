from django.shortcuts import render


def index(request):
    return render(request, "index.html")


# --- Personnalisation des pages d'erreurs 404 et 500 ---


def _render_error(request, code: int, title: str, message: str):
    ctx = {"code": code, "title": title, "message": message}
    return render(request, "error.html", ctx, status=code)


def error_404(request, exception):
    return _render_error(
        request, 404, "Page introuvable", "La page demandée n'existe pas."
    )


def error_500(request):
    return _render_error(
        request, 500, "Erreur serveur", "Un problème est survenu de notre côté."
    )
