from django.urls import path
from .views import PlansList

urlpatterns = [
    path('main/',
         PlansList.as_view(template_name="main_app/index.html"),
         name='main'),
]
