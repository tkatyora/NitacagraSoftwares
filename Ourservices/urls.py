from django.urls import path
from . import views

urlpatterns = [

    path('',views.services, name = 'services'),
    path('add',views.addservices, name = 'addservices'),
    path('update/<int:pk>',views.updateservices, name = 'updateservice'),
    path('delete/<int:pk>',views.deleteservice, name = 'deleteservice'),
    path('buyservice',views.buyservice, name = 'buyservice'),
     path('moreinformation/<int:pk>',views. moreInformation, name = 'moreinformation'),
    path('products',views.products, name = 'products'),
    path('projectsGuides',views.projectsGuides, name = 'projectsGuides'),
   
]