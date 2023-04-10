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
        self.assertEqual(response.resolver_match.func.__name__,
                         PlanDetail.as_view().__name__)
        self.assertTemplateUsed(response, 'main_app/index_detail.html')

    def test_plan_create_view(self):
        url = reverse('record-record')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'main_app/index_create.html')


class UpdateRecordTestCase(TestCase):
    def test_update_record_view_status_code(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('update-record', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_update_record_view_template_used(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('update-record', args=[task.pk]))
        self.assertTemplateUsed(response, 'main_app/index_update.html')

    def test_update_record_view_form_submission(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        data = {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'completed': True,
            'created': '2022-01-01 12:00:00',
        }
        response = self.client.post(reverse('update-record',
                                            args=[task.pk]), data=data)
        self.assertEqual(response.status_code, 302)
        updated_task = Task.objects.get(pk=task.pk)
        self.assertEqual(updated_task.title, 'Updated Task')
        self.assertEqual(updated_task.description, 'Updated Description')
        self.assertEqual(updated_task.completed, True)


class DeleteRecordTestCase(TestCase):
    def test_delete_record_view_status_code(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('delete-record', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_delete_record_view_template_used(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('delete-record', args=[task.pk]))
        self.assertTemplateUsed(response, 'main_app/index_delete.html')

    def test_delete_record_view_deletes_task(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.post(reverse('delete-record', args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
