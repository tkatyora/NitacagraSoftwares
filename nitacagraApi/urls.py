from django.urls import path
from . import views


urlpatterns = [
    path('',views.viewServiceApi),
    path('create',views.createServiceApi)

]
