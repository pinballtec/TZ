from django.urls import reverse
from django.test import TestCase
from ..models import Task


class PlansListTestCase(TestCase):
    def test_plans_list_view_status_code(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_plans_list_view_template_used(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'main_app/index.html')

    def test_plans_list_view_model_data_displayed(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('main'))
        self.assertContains(response, task.title)
        self.assertContains(response, task.description)


class PlanDetailTestCase(TestCase):
    def test_plan_detail_view_status_code(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('record', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_plan_detail_view_template_used(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('record', args=[task.pk]))
        self.assertTemplateUsed(response, 'main_app/index_detail.html')

    def test_plan_detail_view_model_data_displayed(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('record', args=[task.pk]))
        self.assertContains(response, task.title)
        self.assertContains(response, task.description)


class PlanCreateTestCase(TestCase):
    def test_plan_create_view_status_code(self):
        response = self.client.get(reverse('record-record'))
        self.assertEqual(response.status_code, 200)

    def test_plan_create_view_template_used(self):
        response = self.client.get(reverse('record-record'))
        self.assertTemplateUsed(response, 'main_app/index_create.html')

    def test_plan_create_view_form_submission(self):
        data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'completed': False,
            'created': '2022-01-01 12:00:00',
        }
        response = self.client.post(reverse('record-record'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(
            title='Test Task',
            description='Test Description').exists())
