from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContentCreater,StaffTable,NitacagraUsers


class CreateUser(UserCreationForm):
   
    first_name = forms.CharField(required=True , label='Enter First Name',
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }
                              ))
    last_name = forms.CharField(required=True , label='Enter last Name',
                                 widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    username = forms.CharField(required=True , label='Enter Username',
                                widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    email = forms.EmailField(required=True , label='Enter Email',
                              widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                     
                                  }))
   
   
    #location = first_name = forms.CharField(required=True , label='Enter Location')

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username','email','password1','password2'] 
        
        
        
class GeneralUserForm(ModelForm):
    Gender = [('male','Male'),('female','Female')]
    city = forms.CharField(required=True , label='Enter City',
                            widget=forms.TextInput(
                                  attrs={
                                      
                                      'class':'form-control input',
                                       'spellcheck':"true",
                                       'type':'text'
                                  }))
    phoneNumber=forms.IntegerField( label='Enter Phone Number', required=True,                                )
    gender = forms.ChoiceField(label='Select Gender',choices= Gender, required=False,widget=forms.RadioSelect())
    profilePicture = forms.ImageField(label='Upload Profile Picture', required=False)
    address = forms.CharField(label='Enter Address', required=False)
    
    class Meta:
        model =NitacagraUsers 
        fields = ['city','profilePicture','phoneNumber','gender']
   
   
    
    
# class CreateUser(UserCreationForm):
#     first_name = forms.CharField(required=True , label='Enter First Name')
#     last_name = forms.CharField(required=True , label='Enter last Name')
#     username = forms.CharField(required=True , label='Enter Username')
#     email = forms.EmailField(required=True , label='Enter Email')
#     city = forms.CharField(required=True , label='Enter City')
#     phonenumber = forms.CharField(required=True , label='Enter Phone Number')
   
    
#     class Meta:
#         model = User
#         fields = ['first_name','last_name', 'username','email','password1','password2','city','phonenumber'] 