from django import forms
from django.utils import timezone
from .models import Task


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
