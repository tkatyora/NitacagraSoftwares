from django.shortcuts import render
from .models import *
# Create your views here.
# importing all objects in my models 


# code for blogs
def blog(request):
   
    content={}
  
    return render(request , 'undeveloped.html',content)
def tutorials(request):
    return render(request,'home.html')
