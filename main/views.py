from django.shortcuts import render
from .models import advertisment, didYouKnow ,aboutUs
from .decorators import unathenicated_user

# Create your views here.
# collecting The Data from Database
advertismentdata = advertisment.objects.all()
about_us = aboutUs.objects.all()
second_slide = advertisment.objects.get(slide='2')
first_slide = advertisment.objects.get(slide='1')
last_slide = advertisment.objects.get(slide='3')
#latest = didYouKnow.objects.latest('date')


#print(latest)
@unathenicated_user
def home(request):
    content ={}
    content ={
        'advert' : advertismentdata,
        'first_slide': first_slide,
        'last_slide': last_slide,
        'second_slide': second_slide,
        'know':know
    }
    return render(request , 'Nitacagra/index.html' , content)

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