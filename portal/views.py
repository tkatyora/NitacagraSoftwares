from django.shortcuts import render ,redirect
from Ourservices.models import *
from Accounts.models import *
from django.contrib.auth.decorators import login_required ,permission_required
from Accounts.models import NitacagraUsers
from .forms import  CreateAboutForm ,CreateHomeForm
from django.contrib import messages
from main.models import aboutUs ,advertisment

# Create your views here.


# Create your views here.
#PORTAL FOR NITACAGRA
orderInfo = order.objects.all()
customer = customers.objects.all()
customerWithAccount = ContentCreater.objects.all()
PortalServices = servicesTable.objects.all() 
AllUsers = NitacagraUsers.objects.all()
about_us = aboutUs.objects.all()
homepage = advertisment.objects.all()

# Dashboard for admins only
@login_required(login_url='sign_in') 
#@permission_required('Farmers.add_Problems',raise_exception = True ) 
def dashboard(request):
    content ={}
    content={
        'customer': customer,
        'order':orderInfo,
        'accountCustomer': customerWithAccount,
        'data':about_us
    }
    return render(request,'portal/admin-dashboard.html',content)
def viewUsers(request):
    content ={}
    content={
        'AllUsers':AllUsers
    }
    return render(request,'portal/users.html',content)

#DASHBOARD FOR CUSTOMERS THE FIRST DASHBOARD THAT IS REACHED BY EVERYONE

#VIEWING SERVICES IF A ADMIN PERSON IS LOGGED IN
@login_required(login_url='sign_in') 
def Viewservices(request):
    content ={}
    content ={
    'PortalServices' : PortalServices
   }    
    
    return render(request,'portal/PortalServices.html',content)

@login_required(login_url='sign_in')
def Profile(request):
    content ={}
    content ={
   'AllUsers': AllUsers
   }    
    
    return render(request,'portal/profile.html',content)
#ABOUT PAGE
@login_required(login_url='sign_in')
def CreateAboutUs(request):
    if request.method == 'POST':
        form = CreateAboutForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully Created the About Page')
            return redirect('dashboard')
        else:
            messages.warning(request,'Failed to Create The About Page')
            return redirect('CreateAbout')
    else:
        form = CreateAboutForm()
    content ={}
    content ={
    'form':form
   }    
    
    return render(request,'portal/CreateAbout.html',content)
@login_required(login_url='sign_in')
def UpdateAboutUs(request ,pk ):
    update = aboutUs.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateAboutForm(request.POST,instance=update) 
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully Updated the About Page')
            return redirect('dashboard')
        else:
            messages.warning(request,'Failed to Update The About Page')
            return redirect('updateAbout')
    else:
        form = CreateAboutForm(instance=update)
    content ={}
    content ={
    'form':form,
    'data':about_us,
   }    
 
    return render(request,'portal/UpdateAbout.html',content)
#HOME PAGE
    
@login_required(login_url='sign_in')
def CreateHome(request):
    if request.method == 'POST':
        form = CreateHomeForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully Created the Home Page')
            return redirect('dashboard')
        else:
            messages.warning(request,'Failed to Create The Home Page')
            return redirect('CreateAbout')
    else:
        form =CreateHomeForm()
    content ={}
    content ={
    'form':form
   }    
    
    return render(request,'portal/homePage/CreateHome.html',content)
@login_required(login_url='sign_in')
def UpdateHome(request ,pk ):
    update = advertisment.objects.get(id=pk)
    if request.method == 'POST':
        form = CreateAboutForm(request.POST,instance=update) 
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully Updated the Home Page')
            return redirect('dashboard')
        else:
            messages.warning(request,'Failed to Update The Home Page')
            return redirect('updateAbout')
    else:
        form = CreateAboutForm(instance=update)
    content ={}
    content ={
    'form':form,
    'data':homepage,
   }

#END OF NITACAGRA PORTAL

#START OF PORTAL FOR MURIMIWANKU
maindashboard = True
@login_required(login_url='sign_in') 
def mainDashBoard(request):
    content ={}
    content ={
        'maindashboard':maindashboard
   
   }    
    
    return render(request,'MurimiVangu/portal/Maindashboard.html',content)
