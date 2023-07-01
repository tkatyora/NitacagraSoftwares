from django.shortcuts import render
from .models import advertisment,aboutUs
from .decorators import unathenicated_user

# Create your views here.
advertismentdata = advertisment.objects.all()
about_us = aboutUs.objects.all()

@unathenicated_user
def home(request):
    content ={}
    content ={
        'advert' : advertismentdata
    }
    return render(request , 'Nitacagra/home.html' , content)

@unathenicated_user
def about(request):
    content ={}
    content ={
        'data' : about_us
    }
    return render(request , 'Nitacagra/about.html',content)

@unathenicated_user
def WhatsNew(request):
    return render(request , 'undeveloped.html')



# testing code 
@unathenicated_user
def hometest(request):
    content ={}
    content ={
        'advert' : advertismentdata
    }
    return render(request , 'Nitacagra/index.html' , content)