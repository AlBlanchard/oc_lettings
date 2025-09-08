import pytest
from django.test import TestCase, override_settings


@override_settings(
    DEBUG=False,
    ALLOWED_HOSTS=["*"],
)
class ErrorPagesTests(TestCase):
    def test_404_page(self):
        r = self.client.get("/does-not-exist-xyz/")
        assert r.status_code == 404
        assert b"Page introuvable" in r.content

    def test_500_page(self):
        with pytest.raises(ZeroDivisionError):
            r = self.client.get("/boom/")
            assert r.status_code == 500
            assert b"Erreur serveur" in r.content
