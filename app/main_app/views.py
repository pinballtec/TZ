# from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm, UpdateProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(LoginView):
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')


class Register(FormView):
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super(Register, self).get(*args, **kwargs)


class Update_user(LoginRequiredMixin, FormView):
    template_name = 'main_app/update_user.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('main')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'instance': self.request.user
        })
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


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
