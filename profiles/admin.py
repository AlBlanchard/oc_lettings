"""Configuration de l'admin pour l'application profiles."""

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Configuration de l'admin pour le modèle Profile."""

    list_display = ("user", "favorite_city")
    search_fields = ("user__username", "favorite_city")
