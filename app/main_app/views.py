# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


class PlansList(ListView):
    model = Task
