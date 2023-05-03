# from django.shortcuts import render
# from Farmers.models import Problems
# from .forms import CreateSolutionForm
# from django.contrib import messages

# from django.contrib.auth.decorators import permission_required,login_required

# # VIEWS FOR THE INTERGRATED APPLICATION
# @login_required(login_url='sign_in')
# #@permission_required('Farmers.view_Problems',raise_exception=True)
# def ViewSolutions(request):
#     AllProblems = Problems.objects.all()
#     if request.method == 'POST':
#         form = CreateSolutionForm(request.POST)
#         if form.is_valid():
#             Solutions = form.save(commit=False)
#             Solutions.creater = request.user
#             Solutions.save()
#             messages.success(request,'Solution Created')
#         else:
#              messages.success(request,'Solution not Created')
#     else:
#        form = CreateSolutionForm() 
#     content ={
#         'Problems':AllProblems,
#         'form':form
#     }
#     return render(request, 'Agro/ViewProblems.html',content)
# def DeleteSolution(request):
#     pass
# def UpdateSolution(request):
#     pass
# def CreateSolution(request):
# #     if request.method == 'POST':
# #         form = CreateSolutionForm(request.POST)
# #         if form.is_valid():
# #             Solutions = form.save(commit=False)
# #             Solutions.creater = request.user
# #             Solutions.save()
# #             messages.success('Solution Created')
# #         else:
# #              messages.success('Solution not Created')
# #     else:
# #        form = CreateSolutionForm()    
# #     content ={}
# #     content ={
# #         'form':form
# #     }
#     return render(request, 'Agro/ViewProblems.html',content)
    