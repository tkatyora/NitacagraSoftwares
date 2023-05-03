from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required



# Create your views here.
@login_required(login_url='sign_in') 
def dashboard(request):
    return render(request,  'portal/dashboard.html')
    
