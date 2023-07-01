from django.urls import path
from . import views


# creating urls ofr the portal
urlpatterns = [
    #portal for nitacagra
    path('',views.dashboard , name='dashboard'),
    path('View',views.Viewservices , name='PortalServices'),
    path('users', views.viewUsers , name= 'viewUsers'),
    path('CreateAboutUs', views.CreateAboutUs , name= 'createAbout'),
    path('UpdateAboutUs/<int:pk>', views.UpdateAboutUs , name= 'updateAbout'),
    path('CreateHome', views.CreateHome , name= 'createHome'),
    path('UpdateHome/<int:pk>', views.UpdateHome , name= 'updateHome'),
    #commom url
    path('profile',views.Profile,name='profile'),

]
