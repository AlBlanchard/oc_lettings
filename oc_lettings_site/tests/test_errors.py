"""Tests pour les pages d'erreurs 404 et 500 personnalisées."""

import pytest
from django.test import TestCase, override_settings


@override_settings(
    DEBUG=False,
    ALLOWED_HOSTS=["*"],
)
class ErrorPagesTests(TestCase):
    """Tests des pages d'erreurs 404 et 500 personnalisées."""

    def test_404_page(self):
        """
        Test de la page 404 personnalisée.
        """
        r = self.client.get("/does-not-exist-xyz/")
        assert r.status_code == 404
        assert b"Page introuvable" in r.content

    def test_500_page(self):
        """
        Test de la page 500 personnalisée.
        """
        with pytest.raises(ZeroDivisionError):
            r = self.client.get("/boom/")
            assert r.status_code == 500
            assert b"Erreur serveur" in r.content
