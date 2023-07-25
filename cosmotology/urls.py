from django.urls import path
from . import views

urlpatterns = [

    path('',views.cosmotology, name = 'cosmotology'),
]