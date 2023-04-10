# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin


class Login(LoginView):
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')


class PlansList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset2 = queryset.filter(user=self.request.user)
        return queryset2


class PlanDetail(LoginRequiredMixin, DetailView):
    model = Task


class PlanCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    print(form_class)
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdatePlan(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('main')


class DeletePlan(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('main')
