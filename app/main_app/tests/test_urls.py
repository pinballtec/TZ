from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..views import PlansList, PlanDetail
from ..models import Task


class URLPatternTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Task Description',
            created='2022-01-01'
        )

    def test_main_url_pattern(self):
        self.client.login(username='testuser',
                          password='testpassword')
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__,
                         PlansList.as_view().__name__)
        self.assertTemplateUsed(response, 'main_app/index.html')

    def test_plan_detail_url_pattern(self):
        self.client.login(username='testuser',
                          password='testpassword')
        url = reverse('record', args=[str(self.task.pk)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__,
                         PlanDetail.as_view().__name__)
        self.assertTemplateUsed(response, 'main_app/index_detail.html')

    def test_plan_create_view(self):
        self.client.login(username='testuser',
                          password='testpassword')
        url = reverse('record-record')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'main_app/index_create.html')


class UpdateRecordTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')

    def test_update_record_view_status_code(self):
        self.client.login(username='testuser',
                          password='testpassword')
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('update-record', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_update_record_view_template_used(self):
        self.client.login(username='testuser', password='testpassword')
        task = Task.objects.create(title='Test Task',
                                   description='Test Description')
        response = self.client.get(reverse('update-record', args=[task.pk]))
        self.assertTemplateUsed(response, 'main_app/index_update.html')

    def test_update_record_view_form_submission(self):
        self.client.login(username='testuser', password='testpassword')
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
    def setUp(self):
        self.task = Task.objects.create(title='Test Task',
                                        description='Test Description')
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')

    def test_delete_record_view_status_code(self):
        self.client.login(username='testuser',
                          password='testpassword')
        response = self.client.get(reverse('delete-record',
                                           args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_delete_record_view_template_used(self):
        self.client.login(username='testuser',
                          password='testpassword')


class RegisterViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')

    def test_register_view_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'main_app/register.html')

    def test_register_view_form_submission(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser1234',
            'password1': 'zUV62Dt&d6G921231314',
            'password2': 'zUV62Dt&d6G921231314'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main'))

    def test_register_view_form_submission_with_existing_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'newpassword',
            'password2': 'newpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,
                            'A user with that username already exists.')

    def test_register_view_form_submission_with_mismatched_passwords(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'password1',
            'password2': 'password2'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,
                            'The two password fields didn’t match.')


class UpdateUserViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')

    def test_update_user_view_accessible(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('update_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/update_user.html')

    def test_update_user_view_unauthenticated_redirect(self):
        self.client.logout()
        response = self.client.get(reverse('update_user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse('login') + '?next=' + reverse('update_user'))


class PasswordChangeViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_password_change_view_accessible(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('password_change'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/password_change.html')

    def test_password_change_view_unauthenticated_redirect(self):
        self.client.logout()
        response = self.client.get(reverse('password_change'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse('login') + '?next=' + reverse('password_change'))

    def test_password_change_view_valid_form_submission(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('password_change'), data={
            'old_password': 'testpassword',
            'new_password1': 'new_password',
            'new_password2': 'new_password',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('password_change_done'))

    def test_password_change_view_invalid_form_submission(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('password_change'), data={
            'old_password': 'incorrect_password',
            'new_password1': 'new_password',
            'new_password2': 'incorrect_new_password',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/password_change.html')
        self.assertContains(response,
                            'Your old password was entered incorrectly.')
