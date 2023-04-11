from django.urls import path
from .views import PlansList, PlanDetail, PlanCreate, Update_user
from .views import UpdatePlan, DeletePlan, Login, Register
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('main/',
         PlansList.as_view(template_name="main_app/index.html"),
         name='main'),
    path('main/<int:pk>/',
         PlanDetail.as_view(template_name="main_app/index_detail.html"),
         name='record'),
    path('create-record/',
         PlanCreate.as_view(template_name="main_app/index_create.html"),
         name='record-record'),
    path('update-record/<int:pk>/',
         UpdatePlan.as_view(template_name="main_app/index_update.html"),
         name='update-record'),
    path('delete-record/<int:pk>/',
         DeletePlan.as_view(template_name="main_app/index_delete.html"),
         name='delete-record'),
    path('login/',
         Login.as_view(template_name='main_app/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(next_page='main'),
         name='logout'),
    path('register/',
         Register.as_view(template_name='main_app/register.html'),
         name='register'),
    path('update_user/',
         Update_user.as_view(template_name='main_app/update_user.html'),
         name='update_user'),
    path('password/',
         PasswordChangeView.as_view(
             template_name='main_app/password_change.html'),
         name='password_change'),
    path('password/change/done/',
         PasswordChangeDoneView.as_view(
             template_name='main_app/password_change_done.html'),
         name='password_change_done'),
]
