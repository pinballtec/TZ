# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm


class PlansList(ListView):
    model = Task


class PlanDetail(DetailView):
    model = Task


class PlanCreate(CreateView):
    model = Task

    form_class = TaskForm
    success_url = reverse_lazy('main')
