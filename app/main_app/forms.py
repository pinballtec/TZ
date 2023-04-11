from django import forms
from django.utils import timezone
from .models import Task
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Custom Title Label',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'custom-class',
                                      'placeholder': 'Enter title'}),
    )
    description = forms.CharField(
        label='Custom Description Label',
        max_length=150,
        widget=forms.Textarea(attrs={'rows': 5,
                                     'placeholder': 'Enter description'}),
    )
    completed = forms.BooleanField(
        label='Custom Completed Label',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-class'}),
    )
    created = forms.DateTimeField(
        label='Custom Created Label',
        initial=timezone.now(),
        widget=forms.TextInput(attrs={'class': 'custom-class',
                                      'readonly': True}),
    )

    class Meta:
        model = Task
        fields = ['user', 'title', 'description',
                  'completed', 'created']


class UpdateProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
