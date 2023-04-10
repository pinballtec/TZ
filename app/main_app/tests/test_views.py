from django.urls import reverse
from django.test import TestCase
from ..models import Task
from django.contrib.auth.models import User


class PlansListTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_plans_list_view_status_code(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_plans_list_view_template_used(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'main_app/index.html')

    def test_plans_list_view_model_data_displayed(self):
        self.client.login(username='testuser', password='testpassword')
        task = Task.objects.create(title='Test Task',
                                   description='Test Description',
                                   user=self.user)
        response = self.client.get(reverse('main'))
        self.assertContains(response, task.title)
        self.assertContains(response, task.description)


class PlanDetailTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_plan_detail_view_status_code(self):
        self.client.login(username='testuser', password='testpassword')
        task = Task.objects.create(title='Test Task',
                                   description='Test Description',
                                   user=self.user)
        response = self.client.get(reverse('record', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_plan_detail_view_template_used(self):
        self.client.login(username='testuser', password='testpassword')
        task = Task.objects.create(title='Test Task',
                                   description='Test Description',
                                   user=self.user)
        response = self.client.get(reverse('record', args=[task.pk]))
        self.assertTemplateUsed(response, 'main_app/index_detail.html')

    def test_plan_detail_view_model_data_displayed(self):
        self.client.login(username='testuser', password='testpassword')
        task = Task.objects.create(title='Test Task',
                                   description='Test Description',
                                   user=self.user)
        response = self.client.get(reverse('record', args=[task.pk]))
        self.assertContains(response, task.title)
        self.assertContains(response, task.description)


class PlanCreateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_plan_create_view_status_code(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('record-record'))
        self.assertEqual(response.status_code, 200)

    def test_plan_create_view_template_used(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('record-record'))
        self.assertTemplateUsed(response, 'main_app/index_create.html')

    def test_plan_create_view_form_submission(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'completed': False,
            'created': '2022-01-01 12:00:00',
        }
        response = self.client.post(reverse('record-record'), data=data)
        self.assertEqual(response.status_code, 302)

        task = Task.objects.get(title='Test Task')
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Test Description')
        self.assertEqual(task.user, self.user)


class UpdatePlanTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')

    def test_update_plan_view_status_code(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('update-record', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_update_plan_view_template_used(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('update-record', args=[task.pk]))
        self.assertTemplateUsed(response, 'main_app/index_update.html')

    def test_update_plan_view_form_submission(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        self.client.login(username='testuser', password='testpassword')
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
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')

    def test_delete_plan_view_status_code(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete-record', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_delete_plan_view_template_used(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete-record', args=[task.pk]))
        self.assertTemplateUsed(response, 'main_app/index_delete.html')

    def test_delete_plan_view_deletes_task(self):
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete-record', args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
