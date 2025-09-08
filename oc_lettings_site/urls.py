"""Chemins d'URL pour oc_lettings_site."""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("boom/", views.boom),  # pour tester la page 500
]

# Pour personnaliser la gestion des erreurs 404 et 500
handler404 = "oc_lettings_site.views.error_404"
handler500 = "oc_lettings_site.views.error_500"
