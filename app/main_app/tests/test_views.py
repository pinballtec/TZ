from django.urls import reverse
from django.test import TestCase
from ..models import Task
from django.contrib.auth.models import User


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


class UpdatePlanTestCase(TestCase):
    def test_update_plan_view_status_code(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('update-record', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_update_plan_view_template_used(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('update-record', args=[task.pk]))
        self.assertTemplateUsed(response, 'main_app/index_update.html')

    def test_update_plan_view_form_submission(self):
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


class DeletePlanTestCase(TestCase):
    def test_delete_plan_view_status_code(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('delete-record', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_delete_plan_view_template_used(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('delete-record', args=[task.pk]))
        self.assertTemplateUsed(response, 'main_app/index_delete.html')

    def test_delete_plan_view_deletes_task(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.post(reverse('delete-record', args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())


class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_view_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_template_used(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'main_app/login.html')

    def test_login_view_login_form_submission(self):
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main'))

    def test_login_view_redirect_authenticated_user(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main'))
