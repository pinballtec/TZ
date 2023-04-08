from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Task
import datetime


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.task = Task.objects.create(user=self.user,
                                        title='Test Task',
                                        description='Test Description',
                                        completed=False,
                                        created=datetime.datetime.now())

    def test_task_creation(self):
        self.assertIsInstance(self.task, Task)
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.completed, False)

    def test_task_string_representation(self):
        self.assertEqual(str(self.task), 'Test Task')
