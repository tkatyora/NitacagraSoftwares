from django.shortcuts import render
from .models import advertisment,aboutUs

# Create your views here.
advertismentdata = advertisment.objects.all()
about_us = aboutUs.objects.all()


def home(request):
    content ={}
    content ={
        'advert' : advertismentdata
    }
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request , 'portal/admin-dashboard.html')
    if request.user.is_authenticated and request.user.is_staff:
         return render(request,'MurimiVangu/portal/Maindashboard.html')
    return render(request , 'Nitacagra/index.html' , content)
def about(request):
    content ={}
    content ={
        'data' : about_us
    }
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request , 'portal/admin-dashboard.html')
    if request.user.is_authenticated and request.user.is_staff:
         return render(request,'MurimiVangu/portal/Maindashboard.html')
    return render(request , 'Nitacagra/about.html',content)
def newProjects(request):
    return render(request , 'Nitacagra/newProjects.html')


# testing code 
def hometest(request):
    content ={}
    content ={
        'advert' : advertismentdata
    }
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request , 'portal/admin-dashboard.html')
    if request.user.is_authenticated and request.user.is_staff:
         return render(request,'MurimiVangu/portal/Maindashboard.html')
    return render(request , 'Nitacagra/index.html' , content)