from django import forms
from django.forms import ModelForm
from .models import Problems

class CreateProblemForm(ModelForm):
    class Meta:
        model = Problems
        fields = ['body']
