from django.test import TestCase
from django.urls import reverse
from lettings.models import Address, Letting


class LettingsViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        addr = Address.objects.create(
            number=1,
            street="Main St",
            city="Los Angeles",
            state="CA",
            zip_code=90001,
            country_iso_code="USA",
        )
        cls.letting = Letting.objects.create(title="Test Letting", address=addr)

    def test_index_status_ok_and_template(self):
        url = reverse("lettings:index")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "lettings/index.html")
        self.assertContains(resp, "Lettings")
        self.assertContains(resp, "Test Letting")

    def test_detail_status_ok_and_content(self):
        url = reverse("lettings:detail", kwargs={"letting_id": self.letting.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "lettings/detail.html")
        self.assertContains(resp, "Test Letting")

    def test_str_letting(self):
        self.assertEqual(str(self.letting), "Test Letting")
