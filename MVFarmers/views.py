from django.shortcuts import render,redirect
from .forms import CreateProblemForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required ,permission_required

# Create your views here.
# VIEWS FOR INTERGRATED APPLICATIONS
def ViewProblems(request):
    content ={}
    
    
    return render(request, 'CreateProblem.html',content)  
@login_required( login_url = 'sign_in') 
#@permission_required('Farmers.add_Problems',raise_exception = True ) 
def CreateProblem(request):
        form = CreateProblemForm(request.POST)
        if request.method == 'POST':
            if form.is_valid:
                Problem= form.save(commit ='false')
                Problem.creater =request.user
                Problem.save()
                messages.success(request, 'Problem Successfully Created')
                return redirect('dashboard')
            else:
                messages.success(request, 'Problem Not Created')
        else:
           form = CreateProblemForm()  
        content = {}
        content ={
            'form':form
        }
        return render(request, 'Farmer/CreateProblem.html',content)         
    



def DeleteProblem(request , pk):
    pk = Problem.object.get('id')
    pass
def UpdateProblem(request):
    
    pass


# VIEWS FOR EXTERNAL APLICATIONS
def ViewProblemsApi(request):
    pass

