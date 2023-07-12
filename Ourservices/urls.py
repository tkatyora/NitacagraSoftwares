from django.urls import path
from . import views

urlpatterns = [

    path('',views.services, name = 'services'),
    path('View',views.Viewservices , name='PortalServices'),
    path('add',views.addservices, name = 'addservices'),
    path('add_Detailed_Discription',views.addDetailedDisc, name = 'detailed'),
    path('add_Functionality/<int:ID>',views.addFunctionality, name = 'addfunc'),
    path('update/<int:pk>',views.updateservices, name = 'updateservice'),
    path('delete/<int:pk>',views.deleteservice, name = 'deleteservice'),
    path('buyservice',views.buyservice, name = 'buyservice'),
     path('moreinformation/<int:pk>',views. moreInformation, name = 'moreinformation'),
    path('products',views.products, name = 'products'),
    path('moreDetails',views.details, name = 'detail'),
    path('projectsGuides',views.projectsGuides, name = 'projectsGuides'),
   
]