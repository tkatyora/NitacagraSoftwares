from django.shortcuts import render
from .models import *
# Create your views here.
# importing all objects in my models 

def trialProject(request):
    return render(request, 'projetcts.html')

# code for blogs
def blog(request):
   
    content={}
  
    return render(request , 'Nitacagra/blog.html',content)
def tutorials(request):
    return render(request,'home.html')
