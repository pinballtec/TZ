# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


class PlansList(ListView):
    model = Task


class PlanDetail(DetailView):
    model = Task
