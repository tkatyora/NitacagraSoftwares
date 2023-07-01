from django.urls import path
from . import views
from Accounts import views as view


urlpatterns = [

    path('',views.home, name = 'home'),
    path('testhome',views.hometest, name = 'hometest'),
    path('about',views.about, name = 'about'),
    path('WhatsNew',views.WhatsNew, name = 'newProjects'),
    path('signIn',view.signin , name='sign_in'),
    path('signUp',view.signup , name='sign_up'),
    path('logout',view.signout , name ='logout'),  
]


