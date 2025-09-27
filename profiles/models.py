"""Modèles pour l'application profiles."""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Modèle Profile pour étendre le modèle User.
    param user: La relation OneToOne avec le modèle User.
    param favorite_city: La ville préférée de l'utilisateur (max 64 caractères, optionnelle).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        """Meta pour le modèle Profile."""

        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username
