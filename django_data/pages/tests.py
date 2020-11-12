from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "pages/_base.html")
        self.assertTemplateUsed(self.response, "pages/home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "wymco")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, "No content")

    def test_homepag_view_class(self):
        view = resolve(reverse("home"))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
