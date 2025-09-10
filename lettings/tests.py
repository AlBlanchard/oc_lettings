"""Tests pour l'application lettings."""

from django.test import TestCase
from django.urls import reverse
from lettings.models import Address, Letting


class LettingsViewsTests(TestCase):
    """Tests des vues pour l'application lettings."""

    @classmethod
    def setUpTestData(cls):
        addr = Address.objects.create(
            number=1,
            street="Lil Wayne St",
            city="Brumath City",
            state="CA",
            zip_code=90001,
            country_iso_code="USA",
        )
        cls.letting = Letting.objects.create(title="Test Letting", address=addr)

    def test_index_status_ok_and_template(self):
        """
        Test de la vue index : statut 200, bon template, contenu attendu.
        """
        url = reverse("lettings:index")
        resp = self.client.get(url)

        assert resp.status_code == 200
        assert "lettings/index.html" in [t.name for t in resp.templates]
        assert b"Lettings" in resp.content
        assert b"Test Letting" in resp.content

    def test_detail_status_ok_and_content(self):
        """
        Test de la vue detail : statut 200, bon template, contenu attendu.
        """
        url = reverse("lettings:detail", kwargs={"letting_id": self.letting.pk})
        resp = self.client.get(url)

        assert resp.status_code == 200
        assert "lettings/detail.html" in [t.name for t in resp.templates]
        assert b"Test Letting" in resp.content

    def test_str_letting(self):
        """Test de la méthode __str__ du modèle Letting."""
        assert str(self.letting) == "Test Letting"
