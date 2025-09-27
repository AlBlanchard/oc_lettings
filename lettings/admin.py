"""Configuration de l'interface d'administration pour l'application lettings."""

from django.contrib import admin
from .models import Letting, Address


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """Configuration de l'interface d'administration pour le modèle Letting."""

    list_display = ("title", "address")
    search_fields = ("title", "address__city", "address__street")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Configuration de l'interface d'administration pour le modèle Address."""

    list_display = ("number", "street", "city", "state", "zip_code")
    search_fields = ("street", "city", "state", "zip_code")
