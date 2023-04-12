from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from ..forms import TaskForm, UpdateProfileForm


class TaskFormTestCase(TestCase):
    def test_task_form_valid_data(self):
        form = TaskForm(data={
            'title': 'Test Task',
            'description': 'This is a test task.',
            'completed': False,
            'created': timezone.now(),
            'user': User.objects.create_user(
                username='testuser', password='testpassword')
        })
        self.assertTrue(form.is_valid())

    def test_task_form_empty_data(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_task_form_valid_user(self):
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        form = TaskForm(data={
            'title': 'Test Task',
            'description': 'This is a test task.',
            'completed': False,
            'created': timezone.now(),
            'user': user
        })
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_user(self):
        form = TaskForm(data={
            'title': 'Test Task',
            'description': 'This is a test task.',
            'completed': False,
            'created': timezone.now(),
            'user': 'invalid_user'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('user', form.errors)


class UpdateProfileFormTestCase(TestCase):
    def test_update_profile_form_valid_data(self):
        form = UpdateProfileForm(data={
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        self.assertTrue(form.is_valid())

    def test_update_profile_form_empty_data(self):
        form = UpdateProfileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_update_profile_form_max_length(self):
        form = UpdateProfileForm(data={
            'username': 'A' * 151,
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_update_profile_form_valid_password(self):
        form = UpdateProfileForm(data={
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        self.assertTrue(form.is_valid())

    def test_update_profile_form_invalid_email(self):
        form = UpdateProfileForm(data={
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalid_email',
            'password': 'testpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
