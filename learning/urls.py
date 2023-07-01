from django.urls import path
from . import views

urlpatterns = [
    path('blog',views.blog, name ='blog'),
    path('tutorials',views.tutorials,name='tutorials')
    
]
