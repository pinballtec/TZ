from django.test import TestCase
from django.urls import reverse
from ..views import PlansList


class URLPatternTest(TestCase):
    def test_main_url_pattern(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__,
                         PlansList.as_view().__name__)
        self.assertTemplateUsed(response, 'main_app/index.html')
