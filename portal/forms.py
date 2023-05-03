from django import forms
from django.forms import ModelForm 
from main.models import aboutUs ,  advertisment


class CreateHomeForm(forms.ModelForm):
    
    class Meta:
        model = advertisment
        fields = '__all__'

class CreateAboutForm(forms.ModelForm):
    takudzwa =forms.ImageField(label='Add Picture For Takudzwa', required=False)
    gracious =forms.ImageField(label='Add Picture For Gracious', required=False)
    nicole =forms.ImageField(label='Add Picture For Nicole', required=False)
    carey =forms.ImageField(label='Add Picture For Carey', required=False)
    history=forms.CharField(label="Enter Company's History",max_length=800, required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':5,
                                      'cols':5,
                                      'class':'form-control input',  
                                  }
                              ))
    history=forms.CharField(label="Enter Company's Core Values",max_length=800, required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':5,
                                      'cols':5,
                                      'class':'form-control input',  
                                  }
                              ))
    coreValues=forms.CharField(label="Enter Company's Vision And Mission",max_length=800, required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':5,
                                      'cols':5,
                                      'class':'form-control input',  
                                  }
                              ))
    
    class Meta:
        model = aboutUs
        fields = '__all__'
