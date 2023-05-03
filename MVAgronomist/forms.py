from django import forms
from django.forms import ModelForm
from .models import Solutions

class CreateSolutionForm(ModelForm):
    class Meta:
        model = Solutions
        fields ="__all__"
