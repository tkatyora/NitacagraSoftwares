from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from Accounts.models import ContentCreater
from django.core.mail import send_mail
from .forms import addServiceForm ,BuyserviceForm , CreateorderForm
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth import login
# Create your views here.
serviceinfo = servicesTable.objects.all()

# function for services

#view for viewing all the services using the intergrated
def services(request):
    content = {}
    content = {
        'service': serviceinfo
    }

    return render(request, 'Ourservices/offerredServices.html', content)

    
 #VIEWA FOR ADDING SERVICES   
@login_required(login_url='sign_in') 
def addservices(request):
    if request.method == 'POST':
        form = addServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'servive added succesfully')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Sorry servive not updated succesfully')
    else:
        form = addServiceForm()
    content = {}
    content = {
        'form': form,

    }
    return render(request, 'Ourservices/AddService.html', content)

@login_required(login_url='sign_in') 
def updateservices(request, pk):
    # Querry out the Services which much be updated
    Service_to_update = servicesTable.objects.get(id=pk)
    if request.method == 'POST':
        form = addServiceForm(request.POST, instance=Service_to_update)
        if form.is_valid():
            form.save()
            messages.success(request, 'servive updated succesfully')
            return redirect('PortalServices')
        else:
            messages.warning(request, 'Sorry service not updated ')
    else:
        form = addServiceForm(instance=Service_to_update)
    content = {}
    content = {
        'form':  form,
        'services': Service_to_update

    }
    return render(request, 'Ourservices/updateService.html', content)

@login_required(login_url='sign_in') 
def deleteservice(request, pk):
    service_to_delete = servicesTable.objects.get(id=pk)
    if request.method == 'POST':
        service_to_delete.delete()
        messages.success(request, 'servive Succesfully Deleted')
        return redirect('PortalServices')
    content = {}
    content = {
        'service_to_delete': service_to_delete,
        'services': serviceinfo
    }
    return render(request, 'Ourservices/delete.html', content)

def moreInformation(request,pk):
    service = servicesTable.objects.get(id=pk)
   
    content = {}
    content = {
        'moreInfo': service,
        'service': serviceinfo
    }
    return render(request, 'Ourservices/detailed.html',content)


def buyservice(request):
    form2 = CreateorderForm(request.POST)
    if request.method == 'POST':
        form = BuyserviceForm(request.POST)
        account = form.data.get('Account') 
        date = form.data.get('ReceiveDate') 
        name =form.data.get('FullName')
        number = random.randrange(100,200)
        username = f'{name}@nitacagra'
        password = f'nita{number}'
        if account == 'Yes':
            if form.is_valid():
                customer = form.save()
                print('username' + username)
                print('password' + password)
                message = 'Order is Created Succefully\nAccount created You Can Chane The below password and Username'
                messages.success(request, message)
                #login (request,customer)
                return redirect('dashboard')
            else:
                 messages.success(request, 'Order not success created Correct Errors Below')
        elif account == 'No':
           message = 'Order is Created Succefully Thanks for choosing us'
           messages.success(request, message)
           return redirect('dashboard')
        # Creating a order query
        orders = order(
            orderNumber=23, ReceiveDate=Date)
        order.save(self=orders)
    else:
        form =BuyserviceForm()
    content ={}
    content={
        'form':form,
        'form2':form2
    }
    return render(request, 'Ourservices/buy.html',content)
        # # information from buy.html page
        # FullName = request.POST['fullname']
        # Account = request.POST['Account']
        # Email = request.POST['email']
        # Phone = request.POST.get('phone')
        # Location = request.POST.get('location')
        # DeliveredDate = request.POST.get('datereceive')
        # password = 'takudzwa2000'
        # role = 'customer'

        # if Account == 'True':
        #     # creating a customer account
        #     users = User.objects.create(username=FullName, first_name=FullName, email=Email, password=password)
        #     customer = ContentCreater.objects.create(phoneNumber=Phone, location=Location, user=users, roles=role)
        #     customer.save()
        # else:
        #     # Saving a customer in the database
        #     customer = customers(FullName=FullName, Email=Email, PhoneNumber=Phone, Location=Location)
        #     customer.save()

        # # Creating a order query
        # orders = order(
        #     orderNumber=23, ReceiveDate=DeliveredDate)

        # order.save(self=orders)

        # # sending email code
        # # send_mail(
        # #     'service delivred',
        # #     FullName,
        # #     Email,
        # #     ['tkatyora7@gmail,tkatyora6@gmail.com'],
        # #     fail_silently=False,
        # # )
        # return redirect('services')






# functions for produts
def products(request):
    return render(request, 'products.html')
# functions for projectsguides


def projectsGuides(request):
    return render(request, 'project-guides.html')
