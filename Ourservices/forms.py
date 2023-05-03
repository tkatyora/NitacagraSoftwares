from django import forms
from django.forms import ModelForm 
from .models import servicesTable , order ,customers
from datetime import datetime
class addServiceForm(ModelForm):
    name =forms.CharField(label='Name Of The Service', max_length=20, required=True)
    pic =forms.ImageField(label='Select Picture(optinal)', required=False)
    briefDisc=forms.CharField(label='Maximum Words 80',max_length=90, required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':5,
                                      'cols':5,
                                      'placeholder':'Enter A brief Discription Of The Service'
                                  }
                              ))
    FullDisc=forms.CharField(label='Maximum Words 150 ',max_length=160, required=True,
                              widget=forms.Textarea(
                                  attrs={
                                      'rows':10,
                                      'cols':5,
                                      'placeholder':'Enter A Full Discription Of The Service'
                                  }
                              ))
    oldPrice =forms.DecimalField(label='Current Price', required=True,initial=30.00,max_digits=7,decimal_places=2)
    newPrice =forms.DecimalField(label='Reduced Price', required=False,initial=00.00,max_digits=7,decimal_places=2)
    class Meta:
        model = servicesTable
        fields =['name','section','pic','briefDisc','FullDisc','newPrice','oldPrice','specialOffer']

class BuyserviceForm(ModelForm):
    account =[('Yes','Create an Account'),
              ('No','Do Not Create an Account')]
    FullName =forms.CharField(label='Enter Your Name', max_length=50, required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    Email=forms.EmailField(label='Enter Email', required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    PhoneNumber =forms.CharField(label='Enter Phonenumber', max_length=15, required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    Location =forms.CharField(label='Enter Location', max_length=50, required=True , widget=forms.TextInput(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    Account =forms.ChoiceField( choices=account, label='Customer Account', required=True , widget=forms.RadioSelect(
                                  attrs={
                                       'class':'form-control input',}
                              ))
    class Meta:
        model = customers
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

    
