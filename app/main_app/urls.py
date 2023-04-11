from django.urls import path
from .views import PlansList, PlanDetail, PlanCreate
from .views import UpdatePlan, DeletePlan, Login, Register
from django.contrib.auth.views import LogoutView

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
]
