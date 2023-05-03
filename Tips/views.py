# from django.shortcuts import render,redirect
# from .models import *
# from diseases.models import Diseases
# from chirembavangu.forms import Createtip
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required , permission_required

# # Create your views here.

# AllTips = Tips.objects.all()
# AllTips.reverse()
# FiveLastTips = AllTips[:8]




# AllTips.reverse()
# def tips(request):
#     Admin = 'False'
#     content={}
#     content={
#         'tips':AllTips,
#         'admin':Admin
#     }
#     return render(request, 'tips.html' , content )

# #The following functions are for when the user is logged in
# @login_required(login_url='sign_in')

# @permission_required('Tips.add_Tips') 
# def createTip(request):
#     if request.method == 'POST':
#         form = Createtip(request.POST)
#         if form.is_valid():
#             tip = form.save(commit= False)
#             tip.Creater = request.user
#             tip.save()
#             messages.success(request,'Tip Created Successfully')
#             return redirect('dashboard')
#         else:
#              return redirect('admin')
           
#     else:
#        form = Createtip() 
#     content={}
#     content={
#         'form':form,
#         'tips':FiveLastTips
#     }
  
#     return render(request, 'newtip.html' ,content )
# @login_required(login_url='sign_in') 
# def updateTip(request,pk):
#     updatetip = Tips.objects.get(id =pk)
#     form = Createtip(instance= updatetip)
#     if request.method == 'POST':
#         form = Createtip(request.POST,instance= updatetip)
#         if form.is_valid():
#             form.save()
#         return redirect('viewtips')
#     content={}
#     content={
   
#         'form':form,
#         'tips':FiveLastTips
#     }
#     return render(request, 'newtip.html' , content )
# @login_required(login_url='sign_in') 
# def deleteTip(request,pk):
#     deletetip = Tips.objects.get(id=pk)
#     content={}
#     content={
#         'tip':deletetip
#     }
#     if request.method == 'POST':
#          deletetip.delete()
#          return redirect('viewtips')
#     return render(request, 'deteletip.html' , content )
# @login_required(login_url='login') 
# def ViewTips(request):
#     Admin = 'True'
#     content={}
#     content={
#         'tips':AllTips,
#         'admin':Admin
#     }
#     return render(request, 'adminalltips.html' , content )
#  #The functions for someone logged in ended hear
