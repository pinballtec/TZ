# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib.auth.views import LoginView


class Login(LoginView):
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')


class PlansList(ListView):
    model = Task


class PlanDetail(DetailView):
    model = Task


class PlanCreate(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('main')


class UpdatePlan(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('main')


class DeletePlan(DeleteView):
    model = Task
    success_url = reverse_lazy('main')
