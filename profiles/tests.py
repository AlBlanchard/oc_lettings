"""Tests pour l'application profiles."""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfilesViewsTests(TestCase):
    """Tests des vues de l'application profiles."""

    @classmethod
    def setUpTestData(cls):
        """Créer un utilisateur et un profil pour les tests."""
        user = User.objects.create_user(username="alain", password="x")
        cls.profile = Profile.objects.create(user=user, favorite_city="Strasbourg")

    def test_index_status_ok_and_template(self):
        """Tester que la page index renvoie un statut 200 et utilise le bon template."""
        url = reverse("profiles:index")
        resp = self.client.get(url)

        assert resp.status_code == 200
        assert "profiles/index.html" in [t.name for t in resp.templates]
        assert b"Profiles" in resp.content
        assert b"alain" in resp.content

    def test_detail_status_ok_and_content(self):
        """
        Tester que la page detail renvoie un statut 200
        , utilise le bon template et affiche les bonnes infos.
        """
        url = reverse("profiles:detail", kwargs={"username": "alain"})
        resp = self.client.get(url)

        assert resp.status_code == 200
        assert "profiles/detail.html" in [t.name for t in resp.templates]
        assert b"alain" in resp.content
        assert b"Strasbourg" in resp.content

    def test_str_profile(self):
        """Tester la méthode __str__ du modèle Profile."""
        assert str(self.profile) == "alain"
