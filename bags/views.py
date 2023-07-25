from django.shortcuts import render

# Create your views here.

def bags(request):
    return render(request, 'bags/bags.html')