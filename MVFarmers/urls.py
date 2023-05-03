from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.ViewProblems , name='viewProblems'),
    path('create', views.CreateProblem , name='CreateProblem'),
    path('delete/<int:pk>', views.DeleteProblem , name='DeleteProblem'),
    path('update/<int:pk>' ,views.UpdateProblem , name='UpdateProblem'),
   
]

#Urls for Api
# urlpatterns = [
#     path('' ,views.ViewProblemsApi ),
#     # path('delete', views.DeleteProblemApi ),
#     # path('update' ,views.UpdateProblemApi ),
#     # path('create', views.CreateProblemApi ),
# ]
