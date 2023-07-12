from django import forms
from django.forms import ModelForm 
from .models import * 
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class addServiceForm(ModelForm):
    name = forms.ChoiceField(label=' Select Name Of The Service',choices=servicesTable().Name,required=True)
    #name =forms.CharField(, required=False,choices = servicesTable().Name)
    picture =forms.ImageField(label='Select Picture Of service', required= False ,help_text='Picture Should be of size 3000 x 2143' ,error_messages={
        'required':'The Image is required',
    })
    Discription=forms.CharField(label='Service Discription', required=True, help_text='Discription Should Be 150 words ',
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':5,
                                      'cols':5, 
                                  }
                              ))
    specialOffer= forms.BooleanField(label='On Promotion', required=False, help_text='select if the Product is on Promotion')
    
    class Meta: 
        model = servicesTable
        fields = ['name' ,'picture','Discription','specialOffer']
        
        
        
             
class AddDetailedForm(ModelForm):
    #type = [('standard','Standard'),('premium',"Premium"),('ecomerce','E-commerce'),('custom','Custom')]
    type =forms.CharField(label='Enter Type of Service', required=True)
    Price= forms.DecimalField(label='Price' ,required=True,decimal_places=2)
    class Meta: 
        model = Detailed
        fields = ['type' ,'Price','service','specialOffer']
        
        
class FunctionalityForm(ModelForm):
    
    Pages =forms.CharField(label='Enter Pages Details',  required=True , widget=forms.TextInput(
                                  attrs={
                                       'placeholder':'example Maximun of 20 pages',
                                       'class':'form-control input',}
                              ))
    Host =forms.CharField(label='Enter Your Name', required=True , widget=forms.TextInput(
                                  attrs={
                                       'placeholder':'example Hosted on render.com',
                                       'class':'form-control input',}
                              ))
    HostDays =forms.CharField(label='Number oF Hosted Days', max_length=50, required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    Responsive =forms.CharField(label='Enter Detaild On Responsvive Device', max_length=50, required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    SocialMedia =forms.CharField(label='Enter Details on Social Media', max_length=50, required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    seo= forms.BooleanField(label='SEO', required=True,)
    class Meta: 
        model = Functionality
        fields = ['Pages' ,'Host', 'HostDays','Responsive','SocialMedia']




class BuyserviceForm(ModelForm):
    name =forms.CharField(label='Enter Your Name', max_length=50, required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    email=forms.EmailField(label='Enter Email', required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    PhoneNumber =forms.CharField(label='Enter Phonenumber', max_length=15, required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    class Meta:
        model = CustomerWithoutAccount()
        fields = '__all__'

class CreateorderForm(ModelForm):
    ReceivedDate= forms.DateField(label=' Enter Date To Receive Service', required=False,
                                  widget=forms.DateInput(
                                  attrs={
                                       'class':'form-control input',
                                       'type':'date',
                                       'min':datetime.now().date()
                                       
                                       }
                              ))
    class Meta:
        model = order
        fields = ['ReceivedDate']

    
