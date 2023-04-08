from django.urls import path
from .views import PlansList, PlanDetail

urlpatterns = [
    path('main/',
         PlansList.as_view(template_name="main_app/index.html"),
         name='main'),
    path('main/<int:pk>/',
         PlanDetail.as_view(template_name="main_app/index_detail.html"),
         name='record'),

]
