from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfilesViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="alain", password="x")
        cls.profile = Profile.objects.create(user=user, favorite_city="Strasbourg")

    def test_index_status_ok_and_template(self):
        url = reverse("profiles:index")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "profiles/index.html")
        self.assertContains(resp, "Profiles")
        self.assertContains(resp, "alain")

    def test_detail_status_ok_and_content(self):
        url = reverse("profiles:detail", kwargs={"username": "alain"})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "profiles/detail.html")
        self.assertContains(resp, "alain")
        self.assertContains(resp, "Strasbourg")

    def test_str_profile(self):
        self.assertEqual(str(self.profile), "alain")
