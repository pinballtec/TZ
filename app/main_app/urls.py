from django.urls import path
from .views import PlansList, PlanDetail, PlanCreate, UpdatePlan, DeletePlan

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

]
