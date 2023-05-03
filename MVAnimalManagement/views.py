# from django.shortcuts import render
# from .models import fowlRunConditions
# from django.contrib.auth.decorators import login_required , permission_required

# # Create your views here.
# # sellecting all the condtions in the database
# @login_required(login_url='sign_in') 
# def MurimiVanguDashboard(request):
   
#     content={}
#     content={
       
#     }
#     return render(request,'MurimiVangu/fowlrun/MvSeconddashboard.html', content)
# @login_required(login_url='sign_in') 
# def Conditions(request):
#     conditions = fowlRunConditions.objects.all()
#     content={}
#     content={
#         'conditions':conditions
#     }
#     return render(request,'MurimiVangu/fowlrun/conditions.html', content)