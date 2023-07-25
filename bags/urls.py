from django.urls import path
from . import views

urlpatterns = [

    path('',views.bags, name = 'bags'),
]