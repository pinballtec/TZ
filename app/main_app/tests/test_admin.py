from django.test import TestCase
from django.contrib.admin.sites import site
from ..models import Task


class TaskAdminTest(TestCase):
    def test_task_admin_registered(self):
        # Ensure that Task model is registered with the admin site
        self.assertIn(Task, site._registry)
