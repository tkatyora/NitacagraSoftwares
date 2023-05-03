from django.urls import path
from . import views

urlpatterns = [
    path('', views.trialProject, name = 'trialProjects'),
    path('blog',views.blog, name ='blog'),
    path('tutorials',views.tutorials,name='tutorials')
    
]
