from django.test import TestCase
from django.urls import reverse
from ..views import PlansList, PlanDetail
from ..models import Task


class URLPatternTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Task Description',
            created='2022-01-01'
        )

    def test_main_url_pattern(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__,
                         PlansList.as_view().__name__)
        self.assertTemplateUsed(response, 'main_app/index.html')

    def test_plan_detail_url_pattern(self):
        url = reverse('record', args=[str(self.task.pk)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__, PlanDetail.as_view().__name__)
        self.assertTemplateUsed(response, 'main_app/index_detail.html')
