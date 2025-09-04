from django.test import TestCase, override_settings
from django.urls import path, include
from django.http import HttpResponse


def boom(_):
    raise RuntimeError("boom")


def home(_):
    return HttpResponse("home")


def profiles_index(_):
    return HttpResponse("profiles index")


def lettings_index(_):
    return HttpResponse("lettings index")


# on fabrique un mini "include" namespacé 'profiles'
profiles_patterns = (
    [path("", profiles_index, name="index")],  # /profiles/ -> 'profiles:index'
    "profiles",
)

lettings_patterns = (
    [path("", lettings_index, name="index")],  # /lettings/ -> 'lettings:index'
    "lettings",
)

urlpatterns = [
    path("profiles/", include(profiles_patterns)),  # namespace 'profiles'
    path("boom/", boom),
    path("", home, name="home"),
    path("lettings/", include(lettings_patterns)),
]

handler404 = "oc_lettings_site.views.error_404"
handler500 = "oc_lettings_site.views.error_500"


@override_settings(
    DEBUG=False,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
)
class ErrorPagesTests(TestCase):
    def setUp(self):
        # Ne pas repropager les exceptions : renvoie bien une 500 avec le template
        self.client.raise_request_exception = False

    def test_404_page(self):
        r = self.client.get("/does-not-exist-xyz/")
        assert r.status_code == 404
        assert b"Page introuvable" in r.content

    def test_500_page(self):
        r = self.client.get("/boom/")
        assert r.status_code == 500
        assert b"Erreur serveur" in r.content
