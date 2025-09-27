"""Modèles pour l'application lettings."""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse.
    param number: Le numéro de la rue (1-9999).
    param street: Le nom de la rue (max 64 caractères).
    param city: La ville (max 64 caractères).
    param state: L'état (2 lettres).
    param zip_code: Le code postal (5 chiffres).
    param country_iso_code: Le code ISO du pays (3 lettres).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Modèle représentant une location.
    param title: Le titre de la location (max 256 caractères).
    param address: La relation OneToOne avec le modèle Address.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Letting"
        verbose_name_plural = "Lettings"

    def __str__(self):
        return self.title
